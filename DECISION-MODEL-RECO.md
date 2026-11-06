# Decision-model recommendation: indicator-source review

Date: 2026-10-11. Public-source proposal; no model evaluation.
Reviewed [README](https://github.com/Ethical-Tech-CoLab/forced-labor-structural-risk-index/blob/9436ebf93743a90cc2206b558b4aba15aa86364b/README.md).
This is a README-led assessment, not a validation of the scoring pipeline.

## Recommendation

Keep all published normalization, weighting, coverage floors, aggregation,
seeded uncertainty and tier/rank semantics deterministic. The index describes
structural conditions, not prevalence or individual culpability.

Test an offline assistant for matching source documentation to indicator
definitions and checking claim/source support. Input: indicator definition,
source excerpt, country/period and provenance. Output: supports / contradicts /
not established, with an explicit insufficient-information path.

Do not produce country risk scores with Jev, turn confidence into prevalence,
rank firms or people by inferred guilt, fill missing indicators with model
guesses, or upgrade unscored countries to scored.

## Evaluation and alternatives

Compare manual codebook review and exact country/date/unit checks with a local
classifier, Jev's [citation-checking pattern](https://docs.typesafe.ai/cookbooks/citation_check.md),
Microsoft-Decision-1 and Sage on approved public source material.
Exact proprietary model weights are not available for local inference.

Split by indicator/source family and period. Include definition drift,
incompatible denominators, missing countries, delayed observations and
correlated sources. Measure unsupported-support acceptance, relevant-source
recall, calibration and review time. Preserve disagreement for human adjudication.
The same source repeated by different outlets is not independent corroboration.

## Gate and impact

Only derived annotations may change. The original index and uncertainty
outputs must remain byte-for-byte unchanged in a no-write pilot. Keep source
coverage and all limitations visible. No operational screening or enforcement
decision is in scope.

There is no established LLM spend to remove; justify added processing by
measured reviewer benefit and total accepted-record cost. Stop if the assistant
conceals missingness or encourages unjustified precision in country rankings.
