# Evidence contract

Status: proposed contract revision `0.1`; not an implemented schema or validated adapter.
It supports [SP-01–SP-13](product.md) and the [solution design](specs/001-mvp/solution-design.md).
Normative words below specify intended implementation behavior, not current functionality.

## Envelope and conventions

A `RunRecord` contains `schemaVersion`, `runId`, `state`, `createdAt`, `identity`,
`scope`, `capabilities`, `callsites`, `scenarios`, `observations`, `citations`,
`normalizations`, `gaps`, `scenarioOutcomes`, `obligations`, `findings`, `coverage`,
`status`, and `semanticDigest`.
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
- Top-level record collections are unordered sets keyed by unique ID; canonical
  serialization sorts them by ID. Reference lists are duplicate-free unordered
  sets sorted by ID, except the ordered `Scenario.normalizationRuleIds` sequence.
  `reasonCodes` and `changedPaths` are unordered sets sorted lexically.
- Ordered arrays preserve their supplied order in storage and the semantic digest:
  normalization rule sequences, fixture steps/inputs, captured payload arrays and
  observation events (in sequence-number order). Other arrays preserve order unless
  their schema explicitly declares set semantics. Never recursively sort arrays.
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
Default is no normalization. Rules execute in each scenario's `normalizationRuleIds`
order and record changed paths; the top-level `normalizations` collection is only
an ID-keyed lookup, not an execution sequence. Reordering rule references changes
the scenario and its digest even when a particular fixture happens to compare equally.

Allowed examples, only after justification: replace a fixture-generated timestamp
with a declared clock token; canonicalize object-key order for serialization.
Array order, omitted/null differences, error type/code, retry count, pagination
boundaries and request fields remain material unless explicitly scoped otherwise.
Never use broad field deletion to turn a known difference into equivalence.
Retain redacted raw and normalized views so reviewers can inspect every change.
Rule or fixture changes require a new digest and run; do not reinterpret old results.

## Persisted comparison results

`scenarioOutcomes` contains exactly one `ScenarioOutcome` per declared Scenario,
including supplemental and not-yet-run scenarios. Its required fields are `id`,
`scenarioId`, `outcome: equivalent | different | unknown`, `observationIds`,
`sourceObservationId`, `targetObservationId`, `reasonCodes`, `gapIds`, and `changedPaths`.
`scenarioId` resolves to exactly one Scenario. `observationIds` references every
Observation for that scenario, including failed attempts, and no other scenario's
observations. Observation `(scenarioId, side, attempt)` tuples are unique; attempts
are positive integers. Empty observation lists represent missing execution evidence.

For equivalent/different, both selected observation IDs are non-null, belong to
`observationIds`, and match their named sides and the run's package identities.
Select the lowest completed attempt on each side only after all recorded attempts
are completed, prerequisite-valid and mutually consistent within that side;
otherwise outcome is unknown. For unknown, both selected IDs are null; retain
available attempts in `observationIds` for diagnosis rather than selecting favorable data.

- Equivalent: `reasonCodes` is exactly `["EQUIVALENT"]`; `gapIds` and `changedPaths`
  are empty; all scenario prerequisites and compared dimensions passed.
- Different: `reasonCodes` is exactly `["MATERIAL_DIFFERENCE"]`; `gapIds` is empty;
  `changedPaths` is nonempty and names differing paths within declared comparison
  dimensions. Both observations passed prerequisites before comparison.
- Unknown: `gapIds` is nonempty and references the precise missing/invalid evidence;
  `reasonCodes` is exactly the distinct referenced Gap codes; `changedPaths` is empty
  because no valid material comparison is asserted. Not-yet-run scenarios use a
  `NOT_RUN` gap; failed source expectations use `BASELINE_FAILED`.

`obligations` contains `Obligation` records with required fields `id`,
`kind: mapping | callsite-gap | scope-gap`, `callsiteId`, `scenarioOutcomeId`,
`state: pass | fail | unknown`, `reasonCodes`, and `gapIds`. Reference/cardinality rules:

- `mapping`: exactly one per frozen required `(callsite, scenario)` pair;
  `callsiteId` and `scenarioOutcomeId` are non-null and resolve to those records.
  The outcome's Scenario must reciprocally list the call in `callsiteIds`, and
  the Callsite must list that scenario in `scenarioIds` and its `capabilityId` in
  `capabilityIds`. The mapping includes every capability-required and call-specific
  scenario; a missing definition is a gap, never a dangling reference.
- `callsite-gap`: exactly one per in-scope call with unresolved discovery, incomplete
  mapping, unsupported/partial capability, or missing required scenario definition.
  `callsiteId` is non-null, `scenarioOutcomeId` is null, and `gapIds` lists all its
  blocking coverage gaps. It may coexist with mapping obligations for that call.
- `scope-gap`: exactly one per blocking scope-level Gap; both nullable references
  are null and `gapIds` contains exactly that Gap ID. Nonblocking informational
  gaps remain displayed but do not create required obligations.

Mapping state is unknown if mapping/capability/citation prerequisites fail or its
scenario outcome is unknown; otherwise equivalent yields pass and different yields
fail. Pass uses exactly `["EVIDENCE_COMPLETE"]`, fail exactly `["MATERIAL_DIFFERENCE"]`,
both with empty `gapIds`. Unknown requires nonempty `gapIds` and exactly their
distinct codes as `reasonCodes`. Both gap kinds are always unknown. Missing mapping
evidence uses `MAPPING_INCOMPLETE`; other gaps use the applicable contract code.
All gap references resolve to Gap records and identify the affected scenario,
callsite or run scope. Duplicate obligations for the same kind/key are invalid.
Supplemental scenarios have outcomes but no mapping obligations; a scenario is
required precisely when at least one mapping obligation references its outcome.

Comparison is the sole owner of outcomes, obligation states, findings, coverage and
aggregate status. `Comparison.evaluate` returns these persisted RunRecord fields;
Report validates structure/references and renders them without recomputation.
Pending or incomplete snapshots use explicit unknown outcomes/obligations rather
than omitting required results. A structurally malformed input is a diagnostic,
not a completed evidence record whose missing derived fields Report may invent.

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

Create the required mapping, callsite-gap and scope-gap obligations defined above.
A mapping obligation passes only when its mapping is covered, capability supported,
all required citations are exact, and its scenario is equivalent; a valid different
outcome with those prerequisites yields fail.
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
`CAPTURE_INCOMPLETE`, `REDACTION_LOSS`, `IO_FAILURE`, `NOT_RUN`, `BASELINE_FAILED`,
and `MAPPING_INCOMPLETE`.
Blocking is determined by the frozen scope/policy, not an LLM or post-hoc override.

A `Finding` has `id`, `status`, `callsiteIds`, `scenarioIds`, `scenarioOutcomeIds`,
`obligationIds`, `observationIds`, `citationIds`, `gapIds`, `changedPaths`,
`explanation`, and `nextActions`. Outcome/obligation references resolve to the
persisted collections; at least one of these two reference lists is nonempty.
Comparison assigns finding status from that referenced evidence using the same
precedence as aggregation; Report displays the persisted value, never re-derives it.
Initial explanations use deterministic templates, never invented causal diagnoses.
Markdown is rendered only from validated JSON; escape source/doc text as data.
Write artifacts into a new run directory, then publish a completion manifest last.
An interrupted directory without that manifest is partial and cannot be consumed
as a completed report. Readers verify hashes and referenced files before display.

The semantic digest covers canonical JSON of identity, scope, complete scenario
descriptors (including ordered `normalizationRuleIds`), typed observations,
rules, `scenarioOutcomes`, `obligations`, aggregate status and gaps, preserving the
ordered/unordered distinctions above. Exclude run ID, wall-clock timestamps, elapsed durations,
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
