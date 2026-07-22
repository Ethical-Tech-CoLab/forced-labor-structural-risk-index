"""Composite: phase scores -> Product-1 risk score, then rank. LOCKED rule 7.

Replaces the STUB. Product-1 composite = equal-weight GEOMETRIC mean of the
Recruitment (R) and Exploitation (E) phase scores -- the soft-conjunctive
spine. Monetization is Product-2 ONLY and never enters here.

Missing-data handling (rule 9): if EITHER R or E is not-scored for a country,
the composite is NOT-SCORED (None) -- no zero-substitution, no annihilation.
No baseline floor in v1 (locked rule 7: add an annihilation guard only if the
data shows a phase zeroing otherwise-informative scores).
"""
import math


def geometric_mean(values):
    """Equal-weight geometric mean of a list of non-None values in [0,1].

    Returns None if any value is missing (conjunctive spine: both phases are
    separately necessary, so a missing phase -> not-scored, not zero).

    Inputs are VALIDATED, not clamped. A phase score outside [0,1] (or NaN)
    means an upstream aggregation bug; silently coercing a negative to 0.0
    used to annihilate the whole product and then rank that country as LOWEST
    risk, with no trace. Raise instead so the bug surfaces at build time.

    Note: a phase score of exactly 0.0 still annihilates the product by
    design -- locked rule 7 keeps the soft-conjunctive spine with no baseline
    floor, and run.py reports composite == 0.0 as a build anomaly. That is an
    index-math decision and is deliberately unchanged here."""
    vals = [v for v in values if v is not None]
    if len(vals) != len(values) or not vals:
        return None
    prod = 1.0
    for v in vals:
        if not isinstance(v, (int, float)) or math.isnan(v) or not (0.0 <= v <= 1.0):
            raise ValueError(
                f"phase score {v!r} is not a finite value in [0,1]; "
                "phase scores are 0-1 anchored by construction, so this is an "
                "upstream aggregation bug (do not clamp -- fix the source)"
            )
        prod *= v
    return prod ** (1.0 / len(vals))


def composite_scores(aggregated):
    """{iso3: composite|None} -- geometric_mean(R_score, E_score)."""
    out = {}
    for iso3, obj in aggregated.items():
        r = obj["phases"].get("recruitment", {}).get("score")
        e = obj["phases"].get("exploitation", {}).get("score")
        out[iso3] = geometric_mean([r, e])
    return out


def rank(composite):
    """Return [(rank, iso3, score)] sorted by descending risk. Drops None."""
    ordered = sorted(
        ((c, s) for c, s in composite.items() if s is not None),
        key=lambda kv: kv[1],
        reverse=True,
    )
    return [(i + 1, c, s) for i, (c, s) in enumerate(ordered)]
