<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img alt="Tayab Ahamed, AI Research and Engineering Lab. A plot of twelve repositories: the horizontal axis is the month each was created from March to August 2026, the four rows are the research divisions, and the lines between points mark technology or design decisions that two repositories share." src="assets/hero.svg" width="100%">
</picture>

</div>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/registry-dark.svg">
  <img alt="Experiment registry. Twelve numbered experiments, 001 to 012, each listed with its division, state, primary language and month opened. State is derived from evidence: deployed means a public URL exists, open means an OSI licence is declared, prototype means neither." src="assets/registry.svg" width="100%">
</picture>

</div>

<div align="center">

### Building AI systems that assume the model can be wrong.

Twelve experiments. Every one of them is the same question in a different domain.

</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img alt="" src="assets/divider.svg" width="100%">
</picture>

## The lab

Four divisions. Grouped by the question the work asks, not the language it happens to be written in.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/lab-map-dark.svg">
  <img alt="Lab map. Four research divisions with three experiments each. Division 01 autonomous agents: FaultSeeker, RepoMedic-Agent, neuroops. Division 02 grounded retrieval: StudyMind, AI-Sakhi, vetaid-rag-assistant. Division 03 perception and vision: Pothole-Detection, ecosentinel, ReloopAI. Division 04 systems and simulation: Deploy-Platform, LifeSim-AI, SETRS-Trajectory-Preemption." src="assets/lab-map.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img alt="" src="assets/divider.svg" width="100%">
</picture>

## What I am solving

Every card is a real repository. Open the notebook under it for the objective, the failure it guards against, the architecture and the stack.

### Division 01 &nbsp;&middot;&nbsp; Autonomous Agents

> Can a system diagnose a fault and act on it without a human in the loop?

<a href="https://github.com/Tayab-Ahamed/FaultSeeker-"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/cards/card-FaultSeeker--dark.svg">
  <img alt="EXP-01 FaultSeeker. Blockchain transaction forensics. Division: Autonomous Agents. Language: Python. Pipeline: Trace then Replay then Detect then Calibrate then Verdict." src="assets/cards/card-FaultSeeker-.svg" width="100%">
</picture></a>

<details>
<summary><b>Open the notebook</b> &mdash; EXP-01 FaultSeeker</summary>

**Objective.** Locate the vulnerability behind an on-chain exploit by replaying the transaction that caused it.

**The problem.** After a smart contract is drained, the evidence is a raw trace. Reading it by hand is slow, and a wrong conclusion is worse than none.

**Architecture.** Trace ingestion across EVM chains, a reentrancy detection engine, and a confidence calibrator that reports how much the verdict should be trusted.

```mermaid
flowchart LR
    S0("Trace")
    S1("Replay")
    S2("Detect")
    S3("Calibrate")
    S4("Verdict")
    S0 --> S1 --> S2 --> S3 --> S4
```

| | |
|---|---|
| **Stack** | Python &middot; EVM traces &middot; Ollama &middot; OpenAI &middot; Gemini &middot; Claude &middot; Qwen &middot; LaTeX |
| **Language** | Python |
| **Licence** | Apache-2.0 |
| **Created** | 13 March 2026 |
| **Repository** | [FaultSeeker-](https://github.com/Tayab-Ahamed/FaultSeeker-) |
| **Status** | Open source, no public deployment |

> Carries a LaTeX survey paper alongside the code. The only repo of the twelve with an outside fork.

</details>

<a href="https://github.com/Tayab-Ahamed/RepoMedic-Agent"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/cards/card-RepoMedic-Agent-dark.svg">
  <img alt="EXP-05 RepoMedic-Agent. Repository health agent. Division: Autonomous Agents. Language: JavaScript. Pipeline: Clone then Six skills then Score then Rank then Report." src="assets/cards/card-RepoMedic-Agent.svg" width="100%">
</picture></a>

<details>
<summary><b>Open the notebook</b> &mdash; EXP-05 RepoMedic-Agent</summary>

**Objective.** Audit any GitHub repository or local codebase and return one health report.

**The problem.** Code review catches the diff. Nobody reviews the repository itself -- its secrets, its missing tests, its stale dependencies.

**Architecture.** Six skills run in sequence -- repo analysis, security scan, doc analysis, test analysis, dependency analysis, scoring -- producing a weighted score, ranked issues and quick wins as structured JSON.

```mermaid
flowchart LR
    S0("Clone")
    S1("Six skills")
    S2("Score")
    S3("Rank")
    S4("Report")
    S0 --> S1 --> S2 --> S3 --> S4
```

| | |
|---|---|
| **Stack** | Node.js 18+ &middot; gitagent &middot; GitHub API &middot; npm registry |
| **Language** | JavaScript |
| **Licence** | MIT |
| **Created** | 3 April 2026 |
| **Topics** | `ai-agent` &middot; `code-quality` &middot; `dev-tools` &middot; `gitagent` &middot; `gitclaw` &middot; `hackathon` &middot; `nodejs` &middot; `security` |
| **Repository** | [RepoMedic-Agent](https://github.com/Tayab-Ahamed/RepoMedic-Agent) |
| **Status** | Open source, no public deployment |

> Audits itself in CI. Secrets are masked in every finding.

</details>

<a href="https://github.com/Tayab-Ahamed/neuroops"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/cards/card-neuroops-dark.svg">
  <img alt="EXP-10 neuroops. Autonomous SRE for Kubernetes. Division: Autonomous Agents. Language: Python. Pipeline: Detect then Diagnose then Plan then Remediate then Verify." src="assets/cards/card-neuroops.svg" width="100%">
</picture></a>

<details>
<summary><b>Open the notebook</b> &mdash; EXP-10 neuroops</summary>

**Objective.** Detect a cluster incident, find the root cause, and remediate it without paging a human.

**The problem.** On-call exists because the diagnosis step is human. An agent that guesses the cause and acts on it is more dangerous than the outage.

**Architecture.** A LangGraph multi-agent root-cause pipeline over Kubernetes, instrumented with OpenTelemetry so the agent's own reasoning is observable, and benchmarked against deliberately injected chaos experiments.

```mermaid
flowchart LR
    S0("Detect")
    S1("Diagnose")
    S2("Plan")
    S3("Remediate")
    S4("Verify")
    S0 --> S1 --> S2 --> S3 --> S4
```

| | |
|---|---|
| **Stack** | Python &middot; LangGraph &middot; Kubernetes &middot; OpenTelemetry &middot; Chaos engineering |
| **Language** | Python |
| **Licence** | MIT |
| **Created** | 22 May 2026 |
| **Repository** | [neuroops](https://github.com/Tayab-Ahamed/neuroops) |
| **Status** | Open source, no public deployment |

> Self-observability is the point -- the agent is measured the way it measures the cluster.

</details>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img alt="" src="assets/divider.svg" width="100%">
</picture>

### Division 02 &nbsp;&middot;&nbsp; Grounded Retrieval

> Can a model answer only from evidence it is able to cite?

<a href="https://github.com/Tayab-Ahamed/StudyMind"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/cards/card-StudyMind-dark.svg">
  <img alt="EXP-02 StudyMind. Study assistant over your own PDFs. Division: Grounded Retrieval. Language: JavaScript. Pipeline: PDF then Index then Retrieve then Summarise then Chat." src="assets/cards/card-StudyMind.svg" width="100%">
</picture></a>

<details>
<summary><b>Open the notebook</b> &mdash; EXP-02 StudyMind</summary>

**Objective.** Upload PDFs, get summaries, and hold a conversation with your own notes.

**The problem.** A general chatbot will answer confidently about a document it has never read.

**Architecture.** React client, Node service, MongoDB store, JWT auth, Claude for summarisation and chat.

```mermaid
flowchart LR
    S0("PDF")
    S1("Index")
    S2("Retrieve")
    S3("Summarise")
    S4("Chat")
    S0 --> S1 --> S2 --> S3 --> S4
```

| | |
|---|---|
| **Stack** | React &middot; Node.js &middot; MongoDB &middot; JWT &middot; Claude |
| **Language** | JavaScript |
| **Licence** | none declared |
| **Created** | March 2026 |
| **Repository** | [StudyMind](https://github.com/Tayab-Ahamed/StudyMind) |
| **Status** | Prototype, no public deployment |

> The earliest retrieval experiment. Everything in Division 02 is a stricter answer to the same question.

</details>

<a href="https://github.com/Tayab-Ahamed/AI-Sakhi"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/cards/card-AI-Sakhi-dark.svg">
  <img alt="EXP-09 AI-Sakhi. Adaptive tutoring system. Division: Grounded Retrieval. Language: TypeScript. Pipeline: Diagnose then Teach then Practise then Measure then Adapt." src="assets/cards/card-AI-Sakhi.svg" width="100%">
</picture></a>

<details>
<summary><b>Open the notebook</b> &mdash; EXP-09 AI-Sakhi</summary>

**Objective.** Teach, then measure whether the teaching worked, then adapt -- with every claim traceable to a source page.

**The problem.** A tutor that hallucinates does not merely fail to teach. It installs a misconception that has to be removed later.

**Architecture.** Next.js 16 standalone and FastAPI. Retrieval uses all-MiniLM-L6-v2 embeddings in ChromaDB with page-level attribution and a distance threshold that refuses to answer rather than guess. SM-2 spaced repetition schedules review; a mastery score combines accuracy, difficulty, recency and hint penalty; a deterministic, auditable classifier labels misconceptions. JWT, role-based access and tenant isolation across student, teacher, guardian and admin roles.

```mermaid
flowchart LR
    S0("Diagnose")
    S1("Teach")
    S2("Practise")
    S3("Measure")
    S4("Adapt")
    S0 --> S1 --> S2 --> S3 --> S4
```

| | |
|---|---|
| **Stack** | Next.js 16 &middot; FastAPI &middot; Python 3.11 &middot; Groq &middot; Llama &middot; ChromaDB &middot; all-MiniLM-L6-v2 &middot; SQLite WAL &middot; JWT &middot; Docker |
| **Language** | TypeScript |
| **Licence** | none declared |
| **Created** | 12 May 2026 |
| **Repository** | [AI-Sakhi](https://github.com/Tayab-Ahamed/AI-Sakhi) |
| **Status** | Prototype, no public deployment |

> The retrieval threshold is a refusal mechanism: below it, the system declines to answer.

</details>

<a href="https://github.com/Tayab-Ahamed/vetaid-rag-assistant"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/cards/card-vetaid-rag-assistant-dark.svg">
  <img alt="EXP-11 VetAid. Veterinary first-aid assistant. Division: Grounded Retrieval. Language: Python. Pipeline: Symptom then Filter then Retrieve then Cite then Guide." src="assets/cards/card-vetaid-rag-assistant.svg" width="100%">
</picture></a>

<details>
<summary><b>Open the notebook</b> &mdash; EXP-11 VetAid</summary>

**Objective.** Give a pet owner calm, step-by-step first aid during an emergency, with every step cited.

**The problem.** An owner searching during an emergency gets contradictory advice from strangers. A hallucinated instruction here can kill the animal.

**Architecture.** Streamlit interface over a LangChain and ChromaDB retrieval pipeline into Groq-hosted Llama 3.1. Species-aware filters for dog, cat and other; inline citations with expandable source evidence; conversational memory across follow-ups; indexes both the bundled manuals and user-uploaded PDFs.

```mermaid
flowchart LR
    S0("Symptom")
    S1("Filter")
    S2("Retrieve")
    S3("Cite")
    S4("Guide")
    S0 --> S1 --> S2 --> S3 --> S4
```

| | |
|---|---|
| **Stack** | Python &middot; Streamlit &middot; LangChain &middot; ChromaDB &middot; Groq &middot; Llama 3.1 |
| **Language** | Python |
| **Licence** | none declared |
| **Created** | 2 July 2026 |
| **Topics** | `ai-assistant` &middot; `chatbot` &middot; `chromadb` &middot; `groq` &middot; `langchain` &middot; `llama3` &middot; `rag` &middot; `semantic-search` &middot; `streamlit` |
| **Repository** | [vetaid-rag-assistant](https://github.com/Tayab-Ahamed/vetaid-rag-assistant) |
| **Status** | Prototype, no public deployment |

> Ships a warning that it is not a substitute for a veterinarian. Knowing the limit is part of the design.

</details>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img alt="" src="assets/divider.svg" width="100%">
</picture>

### Division 03 &nbsp;&middot;&nbsp; Perception and Vision

> Can a single camera frame become a decision?

<a href="https://github.com/Tayab-Ahamed/Pothole-Detection"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/cards/card-Pothole-Detection-dark.svg">
  <img alt="EXP-03 Pothole-Detection. Real-time road defect detection. Division: Perception and Vision. Language: Python. Pipeline: Frame then YOLOv8 then Detect then Log then CSV." src="assets/cards/card-Pothole-Detection.svg" width="100%">
</picture></a>

<details>
<summary><b>Open the notebook</b> &mdash; EXP-03 Pothole-Detection</summary>

**Objective.** Detect potholes in a live camera feed, a video file, or a still image, and log every detection.

**The problem.** Road defect surveys are manual. A detector is only useful if it runs on the hardware a survey team already has.

**Architecture.** YOLOv8 inference behind both a Flask dashboard and a CLI, with webcam, video and image inputs and CSV export.

```mermaid
flowchart LR
    S0("Frame")
    S1("YOLOv8")
    S2("Detect")
    S3("Log")
    S4("CSV")
    S0 --> S1 --> S2 --> S3 --> S4
```

| | |
|---|---|
| **Stack** | Python &middot; YOLOv8 &middot; Flask &middot; OpenCV &middot; CSV export |
| **Language** | Python |
| **Licence** | none declared |
| **Created** | March 2026 |
| **Repository** | [Pothole-Detection](https://github.com/Tayab-Ahamed/Pothole-Detection) |
| **Status** | Prototype, no public deployment |

> First perception experiment. Two interfaces over one model -- a pattern that repeats later.

</details>

<a href="https://github.com/Tayab-Ahamed/ecosentinel"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/cards/card-ecosentinel-dark.svg">
  <img alt="EXP-07 ecosentinel. Environmental monitoring station. Division: Perception and Vision. Language: TypeScript. Pipeline: Feeds then Ingest then Prophet then Map then Forecast." src="assets/cards/card-ecosentinel.svg" width="100%">
</picture></a>

<details>
<summary><b>Open the notebook</b> &mdash; EXP-07 ecosentinel</summary>

**Objective.** Watch air quality and wildfire risk on one map, and forecast where the readings are heading.

**The problem.** Environmental data arrives from separate feeds at separate cadences, and none of them tell you what happens next.

**Architecture.** Next.js 16 and React 19 front end with Three.js, Leaflet and Recharts; FastAPI backend on SQLModel and Alembic over PostgreSQL; Gemini Vision for imagery, Prophet for PM2.5, CO2 and NO2 forecasting, Whisper for speech input, NASA FIRMS for wildfire coordinates.

```mermaid
flowchart LR
    S0("Feeds")
    S1("Ingest")
    S2("Prophet")
    S3("Map")
    S4("Forecast")
    S0 --> S1 --> S2 --> S3 --> S4
```

| | |
|---|---|
| **Stack** | Next.js 16 &middot; React 19 &middot; Tailwind v4 &middot; Three.js &middot; Leaflet &middot; FastAPI &middot; SQLModel &middot; Alembic &middot; PostgreSQL &middot; Gemini Vision &middot; Prophet &middot; Whisper &middot; NASA FIRMS |
| **Language** | TypeScript |
| **Licence** | MIT |
| **Created** | 19 April 2026 |
| **Topics** | `air-quality` &middot; `climate` &middot; `computer-vision` &middot; `docker` &middot; `environmental-monitoring` &middot; `fastapi` &middot; `full-stack` &middot; `machine-learning` &middot; `nextjs` &middot; `react` &middot; `typescript` &middot; `wildfire-detection` |
| **Repository** | [ecosentinel](https://github.com/Tayab-Ahamed/ecosentinel) |
| **Status** | Open source, no public deployment |

> Ships its own design system rather than a component library.

</details>

<a href="https://github.com/Tayab-Ahamed/ReloopAI"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/cards/card-ReloopAI-dark.svg">
  <img alt="EXP-12 ReloopAI. Circular resource exchange. Division: Perception and Vision. Language: TypeScript. Pipeline: Photo then Vision + OCR then Match then Dispatch then Receipt." src="assets/cards/card-ReloopAI.svg" width="100%">
</picture></a>

<details>
<summary><b>Open the notebook</b> &mdash; EXP-12 ReloopAI</summary>

**Objective.** Turn one photo of surplus into a matched, routed, tracked and impact-reported pickup.

**The problem.** Surplus is redistributed by phone calls and spreadsheets, so it expires before it reaches anyone.

**Architecture.** Vision, OCR and an LLM run in parallel on the uploaded photo to draft the listing. A weighted scorer ranks recipients on distance 30, urgency 25, category fit 20, storage 15 and availability 10. Three n8n workflows then orchestrate approval, dispatch and the post-pickup impact receipt. The AI layer is provider-agnostic and boots with no keys at all on a mock provider.

```mermaid
flowchart LR
    S0("Photo")
    S1("Vision + OCR")
    S2("Match")
    S3("Dispatch")
    S4("Receipt")
    S0 --> S1 --> S2 --> S3 --> S4
```

| | |
|---|---|
| **Stack** | React 18 &middot; TypeScript 5.6 &middot; Vite 6 &middot; Three.js r169 &middot; Framer Motion &middot; Node 20 &middot; Express &middot; MongoDB &middot; Groq &middot; Llama 3.2 Vision &middot; n8n &middot; SendGrid &middot; Twilio &middot; S3 |
| **Language** | TypeScript |
| **Licence** | MIT |
| **Created** | 13 July 2026 |
| **Repository** | [ReloopAI](https://github.com/Tayab-Ahamed/ReloopAI) |
| **Status** | **Live** &mdash; deployed and reachable |
| **Live** | [reloop-ai-liart.vercel.app](https://reloop-ai-liart.vercel.app) |

> The only experiment with a public deployment, and the most committed-to of the twelve.

</details>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img alt="" src="assets/divider.svg" width="100%">
</picture>

### Division 04 &nbsp;&middot;&nbsp; Systems and Simulation

> Can we test the consequence before it reaches the world?

<a href="https://github.com/Tayab-Ahamed/Deploy-Platform"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/cards/card-Deploy-Platform-dark.svg">
  <img alt="EXP-04 Deploy-Platform. Self-hosted deployment platform. Division: Systems and Simulation. Language: Go. Pipeline: Push then Build then Registry then k3s then URL." src="assets/cards/card-Deploy-Platform.svg" width="100%">
</picture></a>

<details>
<summary><b>Open the notebook</b> &mdash; EXP-04 Deploy-Platform</summary>

**Objective.** Give a single machine the deploy-a-container-and-get-a-URL workflow of a hosted PaaS.

**The problem.** Managed platforms are the fastest way to ship and the fastest way to lose control of your own infrastructure.

**Architecture.** Go 1.22 API on the standard library with zero external dependencies, React and Vite dashboard, k3s for scheduling, a local Docker Registry v2, Nginx wildcard routing, and a JSON file as the database.

```mermaid
flowchart LR
    S0("Push")
    S1("Build")
    S2("Registry")
    S3("k3s")
    S4("URL")
    S0 --> S1 --> S2 --> S3 --> S4
```

| | |
|---|---|
| **Stack** | Go 1.22 &middot; React 18 &middot; Vite &middot; k3s &middot; Docker Registry v2 &middot; Nginx |
| **Language** | Go |
| **Licence** | MIT |
| **Created** | 30 March 2026 |
| **Topics** | `container-registry` &middot; `deployment` &middot; `devops` &middot; `docker` &middot; `docker-compose` &middot; `golang` &middot; `heroku-alternative` &middot; `k3s` &middot; `kubernetes` &middot; `nginx` &middot; `paas` &middot; `platform-engineering` &middot; `react` &middot; `self-hosted` &middot; `vite` &middot; `wsl2` |
| **Repository** | [Deploy-Platform](https://github.com/Tayab-Ahamed/Deploy-Platform) |
| **Status** | Open source, no public deployment |

> Zero external Go dependencies. The whole API is standard library.

</details>

<a href="https://github.com/Tayab-Ahamed/LifeSim-AI"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/cards/card-LifeSim-AI-dark.svg">
  <img alt="EXP-06 LifeSim-AI. Financial decision simulator. Division: Systems and Simulation. Language: TypeScript. Pipeline: Choice then Rules then Clamp then Compound then Outcome." src="assets/cards/card-LifeSim-AI.svg" width="100%">
</picture></a>

<details>
<summary><b>Open the notebook</b> &mdash; EXP-06 LifeSim-AI</summary>

**Objective.** Play out a sequence of financial life decisions and see the compounded consequence.

**The problem.** Financial advice is abstract until you watch a choice compound against you.

**Architecture.** A deterministic rules engine with clamped effects and hidden traits runs the simulation locally; an optional AI mode narrates it. The rules engine is authoritative either way.

```mermaid
flowchart LR
    S0("Choice")
    S1("Rules")
    S2("Clamp")
    S3("Compound")
    S4("Outcome")
    S0 --> S1 --> S2 --> S3 --> S4
```

| | |
|---|---|
| **Stack** | TypeScript &middot; React &middot; OpenAI &middot; Gemini &middot; Qwen |
| **Language** | TypeScript |
| **Licence** | none declared |
| **Created** | 9 April 2026 |
| **Repository** | [LifeSim-AI](https://github.com/Tayab-Ahamed/LifeSim-AI) |
| **Status** | Prototype, no public deployment |

> Clearest statement of the fallback pattern -- the model narrates, the rules engine decides.

</details>

<a href="https://github.com/Tayab-Ahamed/SETRS-Trajectory-Preemption"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/cards/card-SETRS-Trajectory-Preemption-dark.svg">
  <img alt="EXP-08 SETRS. Emergency corridor orchestration. Division: Systems and Simulation. Language: Python. Pipeline: Trajectory then Predict then Preempt then SUMO then Corridor." src="assets/cards/card-SETRS-Trajectory-Preemption.svg" width="100%">
</picture></a>

<details>
<summary><b>Open the notebook</b> &mdash; EXP-08 SETRS</summary>

**Objective.** Hold a green corridor ahead of a moving ambulance by predicting its trajectory and preempting the signals on its path.

**The problem.** An ambulance loses minutes at intersections it was always going to reach. The signals only react once it arrives.

**Architecture.** SUMO traffic simulation driven through TraCI, a FastAPI control service, and a React operations view -- the corridor is proven in simulation before any real intersection is touched.

```mermaid
flowchart LR
    S0("Trajectory")
    S1("Predict")
    S2("Preempt")
    S3("SUMO")
    S4("Corridor")
    S0 --> S1 --> S2 --> S3 --> S4
```

| | |
|---|---|
| **Stack** | Python &middot; SUMO &middot; TraCI &middot; FastAPI &middot; React |
| **Language** | Python |
| **Licence** | none declared |
| **Created** | 26 April 2026 |
| **Topics** | `ambulance-routing` &middot; `emergency-response` &middot; `fastapi` &middot; `intelligent-transportation-systems` &middot; `react` &middot; `smart-city` &middot; `sumo-simulation` &middot; `traci` &middot; `traffic-signal-preemption` |
| **Repository** | [SETRS-Trajectory-Preemption](https://github.com/Tayab-Ahamed/SETRS-Trajectory-Preemption) |
| **Status** | Prototype, no public deployment |

> The strongest case for simulating first -- the failure mode here is measured in lives.

</details>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img alt="" src="assets/divider.svg" width="100%">
</picture>

## How the systems connect

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/atlas-dark.svg">
  <img alt="Technology atlas. A knowledge graph of the whole laboratory: twelve repositories on an outer ring grouped into four divisions, and every technology used by two or more of them floating in the centre, joined to each repository that uses it." src="assets/atlas.svg" width="100%">
</picture>

These repositories were not planned as an ecosystem. The connections are there anyway, because the same conclusions kept getting reached. Read across a row to see who shares a decision; read down a column to see what a system is made of.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/substrate-dark.svg">
  <img alt="Repository relationship matrix. Ten shared layers plotted against the twelve repositories, with a filled cell where a repository uses that layer. The layers are model routing, deterministic fallback, grounding and citation, weighted scoring, vector retrieval, vision inference, FastAPI services, React front ends, container and cluster, and simulate before shipping." src="assets/substrate.svg" width="100%">
</picture>

<details>
<summary><b>The same graph, as a graph</b></summary>

```mermaid
flowchart TB
    subgraph SHARED ["Shared decisions"]
        ROUTE("Multi-provider routing")
        FALL("Deterministic fallback")
        CITE("Grounding and citation")
        SCORE("Weighted scoring")
        SIM("Simulate before shipping")
    end
    ROUTE --> FaultSeeker & ReloopAI & LifeSim
    FALL --> ReloopAI & LifeSim & AISakhi & FaultSeeker
    CITE --> AISakhi & VetAid & StudyMind
    SCORE --> ReloopAI & AISakhi & RepoMedic
    SIM --> SETRS & neuroops & LifeSim
    FaultSeeker("FaultSeeker")
    ReloopAI("ReloopAI")
    LifeSim("LifeSim-AI")
    AISakhi("AI-Sakhi")
    VetAid("vetaid-rag-assistant")
    StudyMind("StudyMind")
    RepoMedic("RepoMedic-Agent")
    SETRS("SETRS-Trajectory-Preemption")
    neuroops("neuroops")
```

</details>

### Three conclusions I keep reaching

**01 &nbsp; Never depend on one model**

Four repositories put two or more providers behind a single interface. ReloopAI goes furthest: it boots and stays browsable with no API key at all.

<sub>[FaultSeeker](https://github.com/Tayab-Ahamed/FaultSeeker-) &middot; [ReloopAI](https://github.com/Tayab-Ahamed/ReloopAI) &middot; [LifeSim-AI](https://github.com/Tayab-Ahamed/LifeSim-AI) &middot; [AI-Sakhi](https://github.com/Tayab-Ahamed/AI-Sakhi)</sub>

**02 &nbsp; Make the answer show its evidence**

AI-Sakhi attributes to the page and refuses below a distance threshold. VetAid puts citations inline and lets you expand the source. FaultSeeker reports a calibrated confidence with its verdict.

<sub>[AI-Sakhi](https://github.com/Tayab-Ahamed/AI-Sakhi) &middot; [VetAid](https://github.com/Tayab-Ahamed/vetaid-rag-assistant) &middot; [FaultSeeker](https://github.com/Tayab-Ahamed/FaultSeeker-) &middot; [StudyMind](https://github.com/Tayab-Ahamed/StudyMind)</sub>

**03 &nbsp; Simulate before it reaches the world**

SETRS proves an ambulance corridor in SUMO before touching an intersection. neuroops benchmarks its own agent against injected chaos. LifeSim keeps a deterministic engine authoritative over the narration.

<sub>[SETRS](https://github.com/Tayab-Ahamed/SETRS-Trajectory-Preemption) &middot; [neuroops](https://github.com/Tayab-Ahamed/neuroops) &middot; [LifeSim-AI](https://github.com/Tayab-Ahamed/LifeSim-AI)</sub>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img alt="" src="assets/divider.svg" width="100%">
</picture>

## Method

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/workflow-dark.svg">
  <img alt="Development workflow in five steps: frame the failure, model the world first, route never bind, make it cite, and gate the release. Each step names the repositories that demonstrate it." src="assets/workflow.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img alt="" src="assets/divider.svg" width="100%">
</picture>

## Research log

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/timeline-dark.svg">
  <img alt="Research log from March to August 2026 in four phases: tools first in March, applied systems in April, rigour in May, and grounded and shipped in July. Twelve repositories are plotted on a spine in creation order." src="assets/timeline.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img alt="" src="assets/divider.svg" width="100%">
</picture>

## Instruments

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg">
  <img alt="Instrument inventory. Technologies grouped by role: languages, models, retrieval, services, interface, data and runtime. Language entries show how many of the twelve repositories use that language as their primary language." src="assets/stack.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img alt="" src="assets/divider.svg" width="100%">
</picture>

## Where this goes

The next step is the one the log is already pointing at. The twelve experiments taught me how to make a single system behave; what they have not yet taught me is how to prove it. `AI-Sakhi` has release gates, `neuroops` benchmarks itself against injected chaos, `FaultSeeker` reports a calibrated confidence, `RepoMedic` audits its own repository in CI. Four separate attempts at the same missing discipline: **evaluation**.

So that is where I am going. AI engineering where the evaluation harness is built before the feature, where refusal is a designed behaviour rather than an edge case, and where a system that cannot show its evidence is not considered finished.

I am looking for AI or ML engineering work where that is the standard.

<div align="center">

[**All repositories**](https://github.com/Tayab-Ahamed?tab=repositories) &nbsp;&middot;&nbsp; [**ReLoop AI, live**](https://reloop-ai-liart.vercel.app)

&nbsp;&middot;&nbsp; [**LinkedIn**](https://www.linkedin.com/in/tayab-ahamed-822575308/)

</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/divider-dark.svg">
  <img alt="" src="assets/divider.svg" width="100%">
</picture>

## Colophon

<details>
<summary><b>How this page is built</b></summary>

Every image on this page is an SVG generated by a Python script in [`scripts/`](scripts). Nothing is hand-drawn, nothing is stock, nothing was downloaded. The facts all live in one file, [`scripts/repos.py`](scripts/repos.py), which is also where this README's prose comes from &mdash; so the words and the pictures cannot disagree.

```
python3 scripts/build_all.py      # regenerates every asset and this README
```

| | |
|---|---|
| **Assets** | 38 SVG files, light and dark pairs, roughly 3&ndash;20&nbsp;KB each |
| **Dependencies** | none &mdash; the standard library draws the SVG by hand |
| **Dark mode** | `<picture>` with `prefers-color-scheme`, honoured natively by GitHub |
| **Accessibility** | every SVG carries `<title>` and `<desc>`; every `<img>` carries alt text; all body copy is real Markdown |
| **JavaScript** | none |

A word on honesty. This page shows no star counts, no follower counts and no streak graphics, because those numbers are currently zero and dressing them up would undermine everything else here. The counts that do appear &mdash; twelve repositories, four divisions, five months, one live deployment &mdash; are all verifiable from the repository list. One repository, [`foundry`](https://github.com/Tayab-Ahamed/foundry), is a fork of the Ethereum toolchain and is deliberately excluded from the twelve.

</details>
