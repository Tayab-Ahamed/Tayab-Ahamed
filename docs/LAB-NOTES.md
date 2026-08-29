# Lab notes

Where every claim on the profile comes from, and what was deliberately left out.

The brief for this profile said: only use information that exists in the
repositories, never fabricate accomplishments, do not exaggerate. This file is
the audit trail for that.

---

## Sources

Everything was read from the public GitHub API and from the repositories' own
READMEs:

- `https://api.github.com/users/Tayab-Ahamed` &mdash; account metadata
- `https://api.github.com/users/Tayab-Ahamed/repos` &mdash; all 13 repositories,
  paginated
- The README of each repository, read in full where one exists

No other source was used. Nothing was inferred from the account holder's name,
location, or anything outside the repositories.

---

## The count

The account has **13 public repositories**. The profile presents **12**.

The excluded one is [`foundry`](https://github.com/Tayab-Ahamed/foundry), a fork
of the Ethereum development toolchain. It is a fork, not original work, and
counting it as a thirteenth experiment would inflate the number. It is still
named in the README colophon rather than hidden, and it is recorded in
`repos.py` as `FORK` with its upstream URL, because it is genuine context &mdash;
it was forked while FaultSeeker was being built.

---

## Numbers that appear, and why they are safe

| Claim | Basis |
|---|---|
| 12 experiments | 13 public repositories minus 1 fork |
| 4 divisions | an editorial grouping, described as such |
| 5 months | 13 March 2026 to 4 August 2026, from `created_at` and `updated_at` |
| 1 live deployment | ReloopAI's `homepage` field |
| Python 5, TypeScript 4, JavaScript 2, Go 1 | the `language` field of each of the 12 |
| Per-repository licences | the `license` field |
| Topic lists | the `topics` field |

---

## Numbers that were deliberately omitted

**Total commits.** Contribution counts are known for only 7 of the 12
repositories (FaultSeeker 13, AI-Sakhi 17, ReloopAI 34, Deploy-Platform 2,
ecosentinel 13, VetAid 2, RepoMedic 10). Summing a partial set and presenting it
as a total would be a fabricated statistic. The one place a commit count is used
is the timeline's Phase 04 note that ReloopAI is the most committed-to of the
twelve, which holds across every value that is known.

**Repository sizes.** Available for some repositories, not all. Not used.

**Stars, forks, followers.** All effectively zero. Omitted entirely rather than
displayed as zeroes or disguised behind streak widgets.

**Node sizing on the hero.** Every node in the hero plot is the same size. The
obvious temptation was to scale each by commits or repository size, but with
that data incomplete the sizes would encode noise while looking like
information. Meaning is carried by the edges instead, which come from verifiable
technology choices.

---

## Two approximations, both marked

`StudyMind` and `Pothole-Detection` report a creation month but no day. Their
GitHub repository ids place both between `FaultSeeker-` (13 March) and
`Deploy-Platform` (30 March), so on the hero and the timeline they are plotted at
24 and 27 March respectively.

- Their **ordering** is certain, since repository ids increase monotonically.
- Their **exact position** is not, and is never displayed as a precise date. Both
  cards show only "March 2026".
- The timeline carries a visible footnote saying so.
- `repos.py` keeps these values in a separate `PLOT_DATE` dict, apart from the
  real `created` field, with a comment explaining why.

---

## Attribution

Two repositories are team projects. The README does not imply otherwise, and
the contributor list on each repository is the authoritative record.

If you want teammates credited by name on the profile, add them to that
experiment's `note` field in `repos.py` and rebuild.

---

## The four divisions

The divisions are an **editorial device**, not a label GitHub provides. Three
experiments landed in each, which is a coincidence of the grouping, not a
planned symmetry.

They are derived from what each system does:

| Division | Basis |
|---|---|
| D1 Autonomous Agents | systems that decide and then act &mdash; RepoMedic's six sequential skills, neuroops' LangGraph multi-agent RCA, FaultSeeker's automated verdicts |
| D2 Grounded Retrieval | systems built on retrieval with attribution &mdash; all three use a vector store and cite sources |
| D3 Perception and Vision | systems whose input is an image &mdash; YOLOv8, Gemini Vision, Llama 3.2 Vision |
| D4 Systems and Simulation | systems that model consequence before acting &mdash; SUMO traffic simulation, LifeSim's rules engine, k3s orchestration |

---

## The substrate matrix

The ten shared layers are cross-repository facts, each verifiable in the source
READMEs. A cell is filled only where the technology is named in that
repository's own documentation.

The strongest rows are the interesting ones:

- **React front ends, 7 of 12** &mdash; the most common single choice
- **Container and cluster, 5 of 12** &mdash; Docker throughout, k3s where
  scheduling is genuinely needed
- **Deterministic fallback, 4 of 12** &mdash; the one that matters most, and the
  basis of the first conviction in the README

---

## The three convictions

The README states three conclusions. Each is a pattern observed across multiple
repositories, not a statement of belief invented for the page:

1. **Never depend on one model.** ReloopAI routes across Groq, OpenAI, Hugging
   Face and a mock, and boots with zero API keys configured. LifeSim-AI runs a
   local rules engine when no provider is available. FaultSeeker calibrates
   rather than trusting a single verdict.
2. **Make the answer show its evidence.** AI-Sakhi attributes to the NCERT page
   and refuses beyond a retrieval distance threshold. VetAid renders inline
   citations with expandable source evidence. FaultSeeker reports tiered
   confidence with ECE and Brier scores.
3. **Simulate before it reaches the world.** SETRS proves corridor preemption in
   SUMO before touching a signal. neuroops benchmarks itself against injected
   chaos. LifeSim-AI clamps every model-suggested effect through deterministic
   rules.

---

## Still unverified

- The ReloopAI demo URL is taken from the repository's `homepage` field. Worth
  confirming it still resolves before pushing.
- Four READMEs were not read in full: `Pothole-Detection`, `neuroops`, `SETRS`
  and `StudyMind`. Their cards are built from their API descriptions and topics,
  which are detailed enough to be accurate but thinner than the other eight. If
  you want those cards deeper, that is the place to look.
- An earlier draft of this profile listed PyTorch, Whisper, scikit-learn and RAG
  as part of the stack based on inference. Whisper survived because ecosentinel
  names it explicitly. The others were removed because no repository names them.
