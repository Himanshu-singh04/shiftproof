# B01: SDK/version selection evidence

Status: research in progress for [issue #9](https://github.com/Himanshu-singh04/shiftproof/issues/9).
The product's supported pair remains **UNSELECTED**. Coordinator review and
separate founder approval are pending; this spike does not resolve runtime or
isolation ADRs.

## Original request and bounded scope

Original founder instruction: “ok proceed”, responding to assigning the first
bounded decision tasks, including SDK-version selection for ShiftProof.

Compare at most three packages within two working days. Recommend one exact pair
only after actual pinned artifacts reproduce a documented semantic difference,
an unchanged control and a failure/unsupported scenario without service access.
Preserve synthetic inputs, raw observations, lockfile and exact rerun commands.
No product adapter, CLI, analyzer or report implementation is authorized.

Acceptance follows issue #9 A1–A6: candidate identity/licensing/citations;
actual offline differential evidence; reproducible provisioning and provenance;
narrow capture seam with honest isolation gaps; recommendation with remaining
gates and current provisioning status; issue-linked, attributed and verified PR.

## Initial shortlist

Two packages are being compared; no third candidate is needed yet:

- `stripe` 12.18.0 → 13.0.0: official v13 changelog documents a default change
  from zero to one retry. Investigate its injectable HTTP client with synthetic
  500/200 responses, a 200 control and a non-retryable error.
- `@aws-sdk/client-s3` 3.726.1 → 3.729.0: release notes document new default
  integrity protections. Registry marks the target deprecated for checksum
  validation problems; its wider dependency/transport surface is a trade-off.

These are service SDKs for TypeScript consumers, not general-purpose utilities.
No compatibility or market-validation claim has been established at this checkpoint.
