# Peer Review — The Forced Labor Structural Risk Index (FLSRI): A Research Report on a Country-Level Measure of the Conditions Under Which Forced Labour Becomes More Likely

**Reviewer role:** External academic referee (methods and measurement), reviewing at the bar of a peer-reviewed policy-methods venue.
**Recommendation:** Major revisions
**Date:** 22 July 2026

---

## Summary of the submission

The paper documents FLSRI, a country-level composite that scores the *structural conditions* under which forced labour becomes more likely, for 184 of ~195 countries on a 0–1 scale (§1.1). Its organising idea, borrowed from criminology, is deliberately conjunctive: exploitation becomes likely only where an exposed population (Recruitment, R) coincides with an environment in which exploiting them runs unchecked (Exploitation, E), so the two phases are combined by a geometric mean rather than an average, and a country can score high only when *both* halves are high (§1.3–§1.4, §5.4). Forty-three indicators across eleven domains, each traceable to a named public dataset, feed the score (§1.6, §6). A Monetization phase is computed but excluded from the headline as a "disruptor" rather than a "driver" (§1.5, §6.3).

The genuine contribution is conceptual and procedural rather than numerical, and the paper says so (§14.2). It is unusually disciplined against the two failure modes that sink most composite indices: circularity (predicting forced labour from a measure of forced labour, §7.1) and governance-laundering (a rule-of-law ranking under a new label, §7.2–§7.5). It refuses imputation (missing is never zero, §5.7), publishes uncertainty bands wide enough to embarrass its own ranking (§8.3–§8.4), pre-registers its validation criteria and reports the one that failed (§10.1–§10.3), and states its most damaging limitation — that it under-reads destination-side sponsorship systems, so the UAE ranks 146th of 184 (§11.2) — on the face of the site. Taken as a whole it is one of the more honest measurement writeups I have reviewed. My objections are not to that honesty; they are that in three places the paper *lists* a problem where it needs to *confront the consequence* of that problem for its own central claim.

---

## Major issues

### 1. The flagship geometric-mean design is only as valid as its weakest multiplicand — and the paper concedes that multiplicand (the Exploitation phase) does not measure its construct

**Location:** §6.2.1, §5.6.3, §11.4, §14.2 (claim), against §6.2.1, §6.2.3, §11.4 (concession).

The paper's proudest contribution is that the conjunctive structure is "encoded in the arithmetic rather than asserted in prose" (§14.2): score = √(R × E). The whole normative appeal of the geometric mean is that a low E *drags the product down* regardless of R. But that property cuts both ways: it hands the E half enormous leverage over every country's headline score. And the paper concedes that the E half is not validly measured. The Foreclosed-exit domain "does not measure what it was designed to measure" and is "explicitly labelled a stand-in" built from protective-factor *absence* (§6.2.1); State-production-of-unfreedom sources only two of five designed drivers and "is where the index comes closest to being a corruption measure" (§6.2.3). Because E holds only three domains to R's eight, each E domain carries ~2.7× the marginal weight of an R domain (§5.6.3, §11.4).

**Why it matters:** the celebrated conjunctive logic is therefore multiplying a reasonably-grounded R by an E that is, on the paper's own account, largely labour-institution weakness plus corruption. The claim "a country scores high only where *both* an exposed population and an unchecked environment are present" (§14.2) cannot hold if "unchecked environment" is operationally a governance proxy — because then the conjunction reduces to "exposed population × weak governance," which is close to the very thing §7 tries to escape. This is not a limitation to note; it partly undermines the contribution the paper rests its case on.

**Path forward:** confront the implication head-on in the methods and conclusion. Concretely: (a) report the score both with and without the geometric mean (the simulation page already allows the swap, §12.2) and show how much of the conjunctive "drag" is actually being driven by the un-validated E domains; (b) run the sensitivity of the ranking to *dropping Foreclosed-exit entirely* (the paper floats this as an open question at §6.2.1 — resolve it, don't leave it open); (c) if E survives, defend the claim that it measures "unchecked exploitation" rather than "weak institutions," or soften §14.2 to match.

### 2. The evidence that the index carries forced-labour-specific signal — as opposed to generic development/governance signal — is thinner than the paper's framing implies, and in one place the paper's prose is more favourable than its own code

**Location:** §7.4, §10.2, §10.3–§10.5, against `docs/validation/validation_results_v2_*.json`.

Everything rests on one load-bearing claim: that the ~37% of composite variation *not* shared with rule of law (§7.4, "roughly a third of the variation is not governance") is genuinely about forced labour rather than about poverty, demographics, conflict, or noise. The paper offers essentially one piece of positive evidence for this: §10.2, "A forced-labour-specific signal, child labour prevalence drawn from an independent source, remains significantly associated with the composite once governance is held constant on both sides." Three problems compound here:

- **The one external prevalence test failed.** Against Walk Free's Global Slavery Index, net of governance, "no significant association was demonstrated" (§10.3). The paper reads this as "uninformative rather than disconfirming" because the benchmark is itself governance-entangled — a defensible reading, but it means the index has *no* passing external check (§10.4, §11.12).
- **The surviving positive signal is a coherence check the project itself says cannot validate the index.** I checked the repository. The child-labour signal is an IPUMS-derived layer (so genuinely independent of the WDI `SL.TLF.0714.ZS` series used as a scoring input — good), but the validation JSON labels this exact test **"COHERENCE CHECK — not an independent validation criterion; cannot pass/fail the index"** (`docs/validation/validation_results_v2_v04spu_w05.json`, line 205). The paper's §10.2 presents it, in a list of "reported outcomes," as though it were a validation pass. That is a gap between the paper's framing and the project's own more careful self-labelling.
- **"A third is not governance" is asserted, not shown to be forced-labour signal.** The de-biasing stress test (§7.5) demonstrates the *ranking is robust* to how governance is netted out (Kendall's τ ≥ 0.96) — an admirable check — but robustness of the ranking is not evidence that the residual variance is forced-labour-specific rather than, say, residual poverty or conflict.

**Why it matters:** the paper's central defence against "this is just governance re-labelled" (§7, §14.3) depends on the residual carrying real forced-labour content. As written, that defence leans on a test the code says is non-dispositive while the only dispositive external test returned null.

**Path forward:** (a) bring §10.2's prose into line with the code — call the child-labour test a coherence check, not a validation outcome, and report the internal-migration FL-proximate signal alongside it as the JSON does; (b) strengthen the positive case with at least one FL-proximate benchmark that is *not* itself an index input and *not* governance-laden (e.g., an independent domestic-worker or recruitment-corridor indicator), residualized on both sides; (c) reframe §7.4 to say the residual is *consistent with* forced-labour structure, not demonstrated to be it, until (b) is done.

### 3. The uncertainty structure quietly undercuts the stated use case: the index is stable where it is merely confirmatory and unreadable where it would add value

**Location:** §8.1, §8.4, §11.11, §13.2.

The paper is admirably candid that the median rank band is 45 ranks wide and only ~2% of countries have bands narrower than 10 ranks (§8.4), so "a difference of a few places in the middle of the table is not a finding" (§8.6, §11.11). What stays stable are the extremes: the top decile retains ~79% of members across simulations (§8.4). But §8.1 already tells us the extremes are Yemen, Chad, Afghanistan, South Sudan, Sudan at the top and the Nordics at the bottom — and the paper itself calls this ordering "a face-validity check, not a discovery." So the reliable part of the index reproduces what is already known, and the novel part — discriminating among the middle 120-odd countries where a triage user would actually need guidance — is by the paper's own account not supportable.

**Why it matters:** §13.2 sells the index as "a triage instrument" that "points to where vulnerability and unchecked exploitation hold together." If mid-table order is meaningless and only the obvious extremes are stable, the practical decision-value for a procurement or labour-inspectorate user is unclear, and the paper never squares this. This is a contribution-level tension, not a caveat.

**Path forward:** state plainly what decision the index *does* support given its uncertainty — most likely tier membership rather than rank (which the paper already leans toward, §8.2, §13.4), and specifically the identification of countries that are high on *both* phases but *not* already obvious from a governance ranking. Add an analysis showing where FLSRI's tiers *diverge* from a plain rule-of-law tiering: those divergences are the paper's real evidentiary payload and would directly answer both this issue and Issue 2.

### 4. Positioning: the paper does not situate itself against comparator measures or the composite-indicator methodology literature, and its "review of a project" voice obscures its own contribution

**Location:** §2.2, §4.4, §10.3, Attribution; absence throughout.

The paper is written in the third person about "the project" and "the documentation" — a plain-language *review of* a prototype rather than a paper *making* a methodological argument (Attribution; e.g. §5.6.3 "The project's own interactive material states this plainly"). This blurs authorship (the Attribution reveals it is the author's own masters research) and, more importantly, leaves the paper-level contribution unstated: what does *this document* add beyond the repository it describes? Relatedly, the claimed gap — that existing vulnerability measures are "built partly from the same governance material" (§2.2) — is asserted against *unnamed* competitors. The Walk Free GSI is invoked only as an alignment reference (§4.4) and a failed benchmark (§10.3); its methodology is never engaged. There is no engagement at all with the standard methodology for composite indicators (weighting, aggregation, and sensitivity analysis are exactly the paper's core moves), e.g. the OECD/JRC *Handbook on Constructing Composite Indicators* [1].

**Why it matters:** at a peer-reviewed venue this is the difference between "a well-documented system" and "a paper." Reviewers in this space will want to know how FLSRI's conjunctive structure and de-biasing compare to the GSI Vulnerability model and to established composite-index practice, and whether the gap it claims is real once named alternatives are on the table.

**Path forward:** add a positioning section that (a) names the two or three closest comparators (GSI Vulnerability model; any trafficking/forced-labour risk indices) and states concretely where FLSRI differs; (b) cites the composite-indicator methods literature [1] to locate its equal-weighting, geometric-aggregation, and sensitivity choices within known practice; (c) states the paper's own contribution in the first person, distinct from the software's.

---

## Minor issues

- **m1.** §10.2 — "drawn from an independent source" is load-bearing but unexplained in the paper; name the source (the IPUMS FL-proximate layer, per the repo) so the reader can see it is *not* the WDI input series, and report the paired internal-migration signal the validation actually uses.
- **m2.** §7.1.1 — the paper honestly flags that a derived UNODC detected-victim *share* enters scoring while detection *counts* are refused as a benchmark, but the reconciliation ("share ≠ count, less a function of state capacity") is asserted without evidence. Show the empirical correlation between that share and a state-capacity proxy, or drop the input.
- **m3.** §11.10 — three inputs entering the published scorer (UNODC victim composition; DEMSCORE 29-country tied-status; kafala 8-country) are absent from the auto-generated codebook, and the narrower coverage of two is not reflected in domain confidence flags. This is disclosed, but it is a reproducibility defect: the codebook's claim that it "cannot drift from the pipeline" (§12.4) is technically false for the published build. Align them.
- **m4.** §6.1.7 — the child-marriage → forced-labour mechanism is "under review rather than settled," yet the indicator is included and averaged at equal weight. Including an indicator whose mechanism you flag as unsettled sits uneasily with the no-fabrication rigor elsewhere; either defend inclusion or hold it out pending the review.
- **m5.** §6.1.1 vs §6.2.2 — the same underlying series (employment in agriculture) is anchored 0–80% in Recruitment and 0–60% in Exploitation *and* enters both phases. Beyond the double-count already flagged (§11.5), the inconsistent anchoring of one series across phases needs a stated rationale.
- **m6.** §8.2 — the tier cuts (0.281/0.402) were "fixed at the registration stage." State whether those registered cuts were themselves derived from an earlier build; otherwise "pre-registration" does not fully rule out output-informed thresholds.
- **m7.** §11.5 — the collinearity/double-count screen is flagged as "not been run and reported" in multiple places (§5.6.4, §6.1.8, §11.5). This is a small analysis that would resolve several open items at once (agriculture, informality, refugee outflow); running it should be a priority, not a future note.
- **m8.** Citation form — datasets, legal instruments, and comparators are named in prose only. For an academic venue add formal references (a `## References` section) so each source and its vintage is citable. (This review uses inline `[n]` markers per the same constraint; see References below.)
- **m9.** §9 — the sub-national layer rests on non-redistributable IPUMS data (§9.4) and is carried by a single statistic ("~17% of variance within countries," §9.2). Either develop it as a contribution or mark it explicitly as preliminary illustration so it is not read as validated.

---

## Things the report gets right

- **Limitations stated as self-description, not concession (§11, §14.4).** The paper publishes the fact that the UAE ranks 146th *and* explains why that is a blind spot rather than a finding (§11.2). Reporting your most damaging result in the same breath as the result itself is rare and should be protected.
- **The no-imputation rule (§3.4, §5.7).** Refusing to convert missing data to zero, applying an explicit coverage floor, and leaving 11 countries unscored rather than inventing values is exactly right and unusually well enforced.
- **Circularity discipline, including where it is imperfect (§7.1, §7.1.1).** Excluding the US TIP report, organised-crime outcomes, the Basel AML composite, and the V-Dem freedom-from-forced-labour item is disciplined; flagging the one input (UNODC share) where the rule is applied less strictly is the mark of a careful author.
- **The de-biasing stress test (§7.5).** Re-running the governance correction across scopes and reference measures and reporting τ ≥ 0.96 is more than most composite indices attempt.
- **Pre-registered validation with a reported failure (§10.1–§10.3).** Registering fail thresholds in advance and then reporting the criterion that did not pass (§10.3) is the single most credibility-earning move in the paper.
- **Uncertainty bands wide enough to embarrass the ranking (§8.3–§8.4).** Building the presentation and the arithmetic from one rule so they cannot drift (§8.5), and recording that an earlier version of that rule was wrong and when it was fixed (§8.5), is exemplary.
- **The conjunctive idea itself (§1.4, §14.2).** Even given Issue 1, encoding "both halves must be present" in a geometric mean rather than asserting it in prose is a genuine, transferable conceptual contribution.

---

## Verdict

**Major revisions.** This is a strong, honest prototype writeup whose problems are almost all fixable through argument and a few targeted analyses rather than a rebuild — but they are validity- and contribution-level problems (the flagship conjunctive claim leans on an admittedly-invalid E phase; the "not just governance" defence rests on a test the code labels non-dispositive), which is why it is not a minor-revisions call.

**The single highest-value revision:** run and report a validation that isolates *forced-labour-specific* signal in the non-governance residual using a benchmark that is neither an index input nor governance-laden — and, as its most persuasive form, show precisely where FLSRI's tiers diverge from a plain rule-of-law tiering (Issue 3's suggestion). That one analysis is the linchpin: it would substantiate the "roughly a third is not governance" claim (Issue 2), demonstrate what the index adds beyond confirming the obvious extremes (Issue 3), and give the geometric-mean structure something to stand on beyond the E phase (Issue 1).

---

## References

[1] Nardo, Michela, Michaela Saisana, Andrea Saltelli, Stefano Tarantola, Anders Hoffman, and Enrico Giovannini. *Handbook on Constructing Composite Indicators: Methodology and User Guide.* OECD Publishing and Joint Research Centre, European Commission, 2008.

*Note on format: per the Claude Code rendering constraint, references appear in this section with inline `[n]` markers rather than as Word footnotes.*
