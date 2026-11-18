# Evidence contract

Status: proposed contract revision `0.1`; not an implemented schema or validated adapter.
It supports [SP-01–SP-13](product.md) and the [solution design](specs/001-mvp/solution-design.md).
Normative words below specify intended implementation behavior, not current functionality.

## Envelope and conventions

A `RunRecord` contains `schemaVersion`, `runId`, `state`, `createdAt`, `identity`,
`scope`, `capabilities`, `callsites`, `scenarios`, `observations`, `citations`,
`normalizations`, `gaps`, `findings`, `coverage`, `status`, and `semanticDigest`.
`state` is `pending | running | complete | failed | cancelled`.
`status` is `compatible-within-tested-scope | incompatible | unknown`.
Only a complete record can be compatible. A failed/cancelled record may retain
an already validated incompatibility, with its incomplete-run banner and gaps.

- IDs are unique within a bundle; references must resolve and types must match.
- Strings are UTF-8; timestamps are UTC ISO-8601; byte counts are nonnegative integers.
- Paths are repository-relative POSIX paths; absolute paths and `..` escapes are rejected.
- Source positions are one-based lines and columns, with exclusive end positions.
- Required lists are present even when empty. Unknown values use `null` plus a gap;
  absent required fields make the record invalid, not equivalent to an empty value.
- Enum values are closed for a schema revision. Unknown revisions fail validation.
- Ordering is stable by ID unless an observation explicitly represents ordered data.
- Hash references have `algorithm: sha256`, lowercase hex `digest`, and byte `size`.
  Hashes detect content changes relative to a reference; they do not authenticate
  an author, remote server, package publisher or observation. No signing is proposed.
- Schema validation rejects duplicate IDs, dangling links and contradictory scope.
  Invalid input yields a diagnostic unknown report where enough identity is available.

## Identity, scope and citations

`identity` contains:

| Field | Proposed contract |
| --- | --- |
| `packageName`, `sourceVersion`, `targetVersion` | Exact package name and resolved versions, never ranges; initially unselected |
| `sourceLock`, `targetLock` | Content hash, lockfile format/revision, selected workspace and package resolution path |
| `sourceArtifact`, `targetArtifact` | Resolved artifact identity, available registry integrity metadata and actual artifact hash |
| `repository` | Optional commit SHA, dirty flag and sorted file-content manifest hash; SHA alone cannot identify dirty inputs |
| `tool`, `adapter`, `runtime` | Exact version/build hash; runtime includes platform/architecture |
| `fixtures`, `normalizationPolicy`, `scopePolicy` | Revision and content hash for each |

Different lockfile formats, multiple resolutions of the selected SDK, absent
artifacts or inconsistent installed versions are unsupported until explicitly
handled. Require a unique workspace/resolution path; do not silently pick one.
Artifact hashes and registry metadata are provenance, not an authenticity guarantee.

`scope` records include/exclude globs, explicit user exclusions with reasons,
supported syntax, capability subset, scenario assignment policy, observation
dimensions and `evidenceMode: offline-synthetic | offline-mocked` for MVP.
An intentional pre-run exclusion narrows scope and is always displayed; a parse
failure or unexpected unresolved call within scope is a gap, not an exclusion.
Freeze scope before comparison; changing it creates a new run and scope hash.
Future `trusted-local-harness` and `remote-service` modes require separate ADRs
and contracts and cannot be asserted by an MVP record.

A `Citation` has `id`, `kind` (`primary-doc | release-note | source | fixture`),
`urlOrPath`, `title`, `publisher`, `retrievedAt`, `contentHash`, `locator`,
`applicableVersions`, `claim`, and `versionMatch: exact | uncertain | mismatch`.
Retain an allowable excerpt or local snapshot reference for reproducibility;
record licensing/retention restrictions. A URL alone is insufficient for a claim.
Documentation may explain an expectation; it cannot substitute for an observation.
Primary-doc claims need exact applicability; uncertainty creates a gap for that claim.
No selected SDK documentation or external API behavior is claimed in this plan.

## Call-site and capability records

A `Callsite` has `id`, `file`, `fileHash`, `range`, `importSpecifier`,
`resolvedSymbol` (nullable), `resolutionPath` (nullable), `syntaxKind`,
`discovery: resolved | unresolved`, `capabilityIds`, `scenarioIds`,
`mapping: covered | partial | unsupported | unmapped`, and `gapIds`.
Stable IDs derive from file hash, range and symbol descriptor, not line number alone.
Record only minimal source excerpts; redact before persisting sensitive literals.

Discovery supports an explicitly tested syntax subset. SDK aliases passed to
unknown functions, computed property calls, runtime imports, wrappers with lost
provenance and parse/config-resolution failures become unresolved candidates or
scope-level gaps. There is no sound claim to enumerate all runtime calls.
Coverage reports distinguish scanned files, unscanned exclusions and failed files.

A `Capability` has `id`, `name`, `pairIdentity`, `support: supported | partial | unsupported`,
`supportedForms`, `unsupportedForms`, `requiredScenarioIds`, `requiredCitationIds`,
`observationDimensions`, `limitations`, and `gapIds`.
Examples of dimensions to investigate are request serialization, response mapping,
error representation, pagination and retry scheduling; none is claimed supported yet.
The selected adapter must specify which dimensions it can intercept offline.

Scenario assignment is frozen before replay. Each resolved in-scope call requires
every scenario in its capability's required set and any call-specific scenarios
declared by the reviewer. A supported capability cannot have an empty required set.
Unmapped argument behavior produces a gap; method-name matching is not sufficient
evidence that a fixture represents a call site's usage.

## Scenarios and observations

A `Scenario` has `id`, `capabilityId`, `callsiteIds`, `fixtureHash`, `inputHash`,
`harnessHash`, `expectedSourceAssertions`, `comparisonDimensions`, `citationIds`,
`normalizationRuleIds`, `seed`, `clockPolicy`, `limits`, and `evidenceMode`.
One immutable scenario descriptor is passed to both versions; adapter translations
must preserve intended input semantics and be declared and tested.
If equivalent inputs cannot be constructed, the scenario is unknown.

An `Observation` has `id`, `scenarioId`, `side: source | target`, `packageIdentity`,
`attempt`, `execution: completed | timeout | crash | blocked | not-run`,
`rawHash`, `redactedArtifact`, `normalizedHash`, `assertionResults`,
`events`, `durationMs`, `limitsApplied`, and `gapIds`.
Events have monotonically increasing sequence numbers and typed payloads for
request, response, return, throw, retry and clock advance when supported.
SDK-thrown errors captured as expected scenario behavior are completed observations;
harness/process crashes are execution failures, never semantic differences.

Capture preserves omitted vs present fields, null, undefined, numeric values,
binary bytes, ordered arrays and structured exceptions using explicit tagged values
where JSON cannot represent the native value. Unsupported values, cycles or
truncated output create gaps; they must not be silently stringified.
Raw artifacts are redacted before persistence. If redaction removes a required
comparison dimension, report unknown; hashes of secrets must not be published.

Each side gets a fresh working directory, SDK dependency tree, fixture state,
clock and deterministic seed. Customer repository code is parsed, never imported.
Only reviewed product-owned harness code and pinned SDK code execute; dependency
provisioning must not execute arbitrary install scripts. A child process alone is
not a sandbox. Network denial, filesystem limits and environment filtering need
a tested enforcement mechanism before replay can be enabled.
If enforcement is unavailable, support discovery/reporting only and mark replay blocked.
Mock transport exercises the adapter's declared boundary, not a remote API server.

## Normalization rules

A `NormalizationRule` has `id`, `revision`, `pathSelector`, `operation`,
`parameters`, `reason`, `citationIds`, and positive/negative test references.
Operations are a closed, reviewed set; no arbitrary scripts or downloaded functions.
Default is no normalization. Rules run in listed order and record changed paths.

Allowed examples, only after justification: replace a fixture-generated timestamp
with a declared clock token; canonicalize object-key order for serialization.
Array order, omitted/null differences, error type/code, retry count, pagination
boundaries and request fields remain material unless explicitly scoped otherwise.
Never use broad field deletion to turn a known difference into equivalence.
Retain redacted raw and normalized views so reviewers can inspect every change.
Rule or fixture changes require a new digest and run; do not reinterpret old results.

## Exact status calculation

A scenario outcome is `equivalent | different | unknown` with reason codes.
Evaluate in this order:

1. Validate pair identity, scenario equality, source expectation assertions,
   required citations, capture completeness, enforced isolation and comparison rules.
   If any prerequisite fails, outcome is unknown even if raw outputs look different.
2. Require one completed, unambiguous observation for each side and no unresolved
   nondeterminism. A missing side, crash, timeout, truncation or failed source
   baseline assertion makes the outcome unknown.
3. Apply the declared normalization; compare all required typed dimensions exactly.
   Any material unequal dimension yields different; otherwise equivalent.
4. Retries do not erase failed attempts. Conflicting repeated observations create
   a nondeterminism gap and unknown until a new controlled run explains them.

Create a required obligation for every callsite/scenario mapping and scope-level
gap. An obligation passes only when its mapping is covered, capability supported,
all required citations are exact, and all assigned scenarios are equivalent.
Partial or unsupported capability, unresolved call, parse failure, missing mapping,
missing scenario or missing evidence makes the obligation unknown.

Aggregate a structurally valid record in this exact order:

1. If any valid in-scope required scenario is different: **incompatible**.
2. Else, if state is not complete, no resolved calls or no required scenarios exist,
   any obligation is unknown, or any blocking run gap exists: **unknown**.
3. Else: **compatible-within-tested-scope**.

Do not count unmapped demonstration scenarios toward compatibility or incompatibility;
show them as supplemental evidence. A known incompatibility outranks unknown gaps,
but the report still displays every gap. A known difference establishes a behavioral
change under the fixture, not necessarily that the target SDK is defective.
Approval of an intentional behavior change does not rewrite historical evidence.
Malformed records receive unknown diagnostics; they cannot establish incompatibility.

## Coverage and report lifecycle

`coverage` contains counts of files scanned/excluded/failed; calls resolved/unresolved;
calls covered/partial/unsupported/unmapped; required scenarios equivalent/different/unknown;
and lists of scope-level gaps and limitations. These are corpus counts, not a
percentage of all runtime behavior. Zero denominators display `N/A`, not 100%.
Do not combine file coverage, call coverage and fixture coverage into one score.

A `Gap` has `id`, `code`, `scopeRef`, `detail`, `blocking`, `requiredEvidence`,
and `nextAction`. Core codes include `PAIR_UNRESOLVED`, `PARSE_FAILED`,
`DYNAMIC_CALL`, `CAPABILITY_UNSUPPORTED`, `SCENARIO_MISSING`, `CITATION_MISSING`,
`VERSION_MISMATCH`, `ISOLATION_UNAVAILABLE`, `TIMEOUT`, `NONDETERMINISTIC`,
`CAPTURE_INCOMPLETE`, `REDACTION_LOSS`, and `IO_FAILURE`.
Blocking is determined by the frozen scope/policy, not an LLM or post-hoc override.

A `Finding` has `id`, `status`, `callsiteIds`, `scenarioIds`, `observationIds`,
`citationIds`, `gapIds`, `changedPaths`, `explanation`, and `nextActions`.
Initial explanations use deterministic templates, never invented causal diagnoses.
Markdown is rendered only from validated JSON; escape source/doc text as data.
Write artifacts into a new run directory, then publish a completion manifest last.
An interrupted directory without that manifest is partial and cannot be consumed
as a completed report. Readers verify hashes and referenced files before display.

The semantic digest covers canonical JSON of identity, scope, typed observations,
rules, outcomes and gaps. Exclude run ID, wall-clock timestamps, elapsed durations,
absolute local paths and diagnostic log ordering; list those separately as metadata.
No cross-run merging of observations unless a future contract defines comparability.
User-owned retention and deletion are described in [operations](operations.md).

## Deferred extensions

Compilation evidence is a separate static check with tool/version/diagnostics;
it cannot satisfy a scenario obligation. A trusted local harness must explicitly
authorize customer code execution and document its privileges and evidence mode.
Actual service tests need credentials, endpoint/version identity, request controls,
and a separate risk/coverage contract; offline outcomes cannot be relabeled.

Future explanations receive only a bounded validated evidence bundle. They must
cite IDs, distinguish observations from hypotheses and abstain on unknowns.
A future `PatchProposal` contains a textual diff, target file hashes, evidence IDs,
assumptions and required checks. It is inert report content; no apply/merge endpoint
exists. Automated transformation generation is deferred beyond MVP.
