"""Single source of truth for the profile overview.

Every fact here is taken from the public GitHub repository list
(https://api.github.com/users/Tayab-Ahamed/repos). The fork `foundry`
is deliberately excluded.
"""

# Divisions, in order. index -> (key, name, question)
DIVISIONS = [
    ("agents", "Autonomous Agents",
     ["Can a system diagnose a fault and act on it", "without a human in the loop?"]),
    ("retrieval", "Grounded Retrieval",
     ["Can a model answer only from evidence", "it is able to cite?"]),
    ("vision", "Perception and Vision",
     ["Can a machine read the physical world", "well enough to act on it?"]),
    ("systems", "Systems and Simulation",
     ["Can we test the consequence before", "it reaches the world?"]),
    ("assurance", "Security and Assurance",
     ["Can a pipeline prove it was not", "tampered with?"]),
]

DIVISION_INDEX = {k: i for i, (k, _n, _q) in enumerate(DIVISIONS)}

# exp number is creation order across the 17 original repositories.
REPOS = [
    dict(n=1, name="FaultSeeker-", label="FaultSeeker", div="agents",
         blurb="Blockchain transaction forensics", lang="Python", licence="Apache-2.0",
         created="2026-03-13", month="Mar", home="",
         pipeline=["Trace", "Replay", "Detect", "Calibrate", "Verdict"],
         tech=["Python", "LLM routing", "EVM", "LaTeX"],
         layers=["routing", "scoring", "simulate"]),
    dict(n=2, name="StudyMind", label="StudyMind", div="retrieval",
         blurb="Study assistant over your own PDFs", lang="JavaScript", licence="",
         created="2026-03-28", month="Mar", home="",
         pipeline=["PDF", "Index", "Retrieve", "Summarise", "Chat"],
         tech=["JavaScript", "React", "Node.js", "MongoDB", "Claude"],
         layers=["grounding", "vector", "react"]),
    dict(n=3, name="Pothole-Detection", label="Pothole-Detection", div="vision",
         blurb="Real-time road defect detection", lang="Python", licence="MIT",
         created="2026-03-29", month="Mar", home="",
         pipeline=["Frame", "Infer", "Track", "Log", "Dashboard"],
         tech=["Python", "YOLOv8", "Flask", "OpenCV"],
         layers=["vision"]),
    dict(n=4, name="Deploy-Platform", label="Deploy-Platform", div="systems",
         blurb="Push a zip, get a live URL", lang="JavaScript", licence="MIT",
         created="2026-03-30", month="Mar", home="",
         pipeline=["Upload", "Build", "Registry", "Deploy", "Route"],
         tech=["Go", "React", "Docker", "Kubernetes", "Nginx"],
         layers=["container", "react"]),
    dict(n=5, name="RepoMedic-Agent", label="RepoMedic-Agent", div="agents",
         blurb="Repository health agent", lang="JavaScript", licence="MIT",
         created="2026-04-03", month="Apr", home="",
         pipeline=["Clone", "Six skills", "Score", "Rank", "Report"],
         tech=["Node.js", "GitHub API", "JavaScript"],
         layers=["scoring"]),
    dict(n=6, name="LifeSim-AI", label="LifeSim-AI", div="systems",
         blurb="Deterministic life simulation, narrated", lang="TypeScript", licence="",
         created="2026-04-09", month="Apr", home="",
         pipeline=["State", "Tick", "Resolve", "Narrate", "Persist"],
         tech=["TypeScript", "React", "LLM routing"],
         layers=["routing", "fallback", "simulate", "react"]),
    dict(n=7, name="ecosentinel", label="ecosentinel", div="vision",
         blurb="Environmental intelligence platform", lang="TypeScript", licence="MIT",
         created="2026-04-19", month="Apr", home="",
         pipeline=["Sense", "Fuse", "Forecast", "Scan", "Alert"],
         tech=["TypeScript", "Next.js", "React", "FastAPI", "Docker", "Computer vision"],
         layers=["vision", "fastapi", "react", "container"]),
    dict(n=8, name="SETRS-Trajectory-Preemption", label="SETRS", div="systems",
         blurb="Emergency corridor orchestration", lang="Python", licence="",
         created="2026-04-26", month="Apr", home="",
         pipeline=["Track", "Predict", "Reserve", "Preempt", "Release"],
         tech=["Python", "SUMO", "FastAPI", "React", "TraCI"],
         layers=["simulate", "fastapi", "react"]),
    dict(n=9, name="AI-Sakhi", label="AI-Sakhi", div="retrieval",
         blurb="Multilingual study companion", lang="TypeScript", licence="MIT",
         created="2026-05-12", month="May", home="",
         pipeline=["Ask", "Retrieve", "Attribute", "Answer", "Refuse"],
         tech=["TypeScript", "React", "Vector search", "LLM routing"],
         layers=["routing", "grounding", "vector", "scoring", "react"]),
    dict(n=10, name="neuroops", label="neuroops", div="agents",
         blurb="Autonomous SRE for Kubernetes", lang="Python", licence="MIT",
         created="2026-05-22", month="May", home="",
         pipeline=["Detect", "Diagnose", "Plan", "Remediate", "Verify"],
         tech=["Python", "LangGraph", "Kubernetes", "OpenTelemetry", "FastAPI"],
         layers=["simulate", "container", "fastapi"]),
    dict(n=11, name="vetaid-rag-assistant", label="VetAid", div="retrieval",
         blurb="First-aid RAG for pet emergencies", lang="Python", licence="",
         created="2026-07-02", month="Jul", home="",
         pipeline=["Question", "Embed", "Retrieve", "Cite", "Answer"],
         tech=["Python", "LangChain", "ChromaDB", "Streamlit", "Groq"],
         layers=["grounding", "vector"]),
    dict(n=12, name="Sentinel-FL", label="Sentinel-FL", div="assurance",
         blurb="Backdoor immune system for federated learning", lang="Python", licence="MIT",
         created="2026-07-08", month="Jul", home="",
         pipeline=["Aggregate", "Detect", "Explain", "Repair", "Attest"],
         tech=["Python", "Flower", "PyTorch", "Cryptographic attestation"],
         layers=["scoring", "attest", "simulate"]),
    dict(n=13, name="Actionguard-Autoaudit", label="Actionguard Autoaudit", div="assurance",
         blurb="Auditing and remediation for CI pipelines", lang="Python", licence="MIT",
         created="2026-07-08", month="Jul", home="",
         pipeline=["Scan", "Audit", "Triage", "Patch", "Pull request"],
         tech=["Python", "zizmor", "GitHub Actions", "SAST", "LLM routing"],
         layers=["routing", "scoring", "attest"]),
    dict(n=14, name="Actionguard-CI", label="Actionguard CI", div="assurance",
         blurb="Workflow security auditor with reports", lang="Python", licence="MIT",
         created="2026-07-08", month="Jul", home="",
         pipeline=["Ingest", "Analyse", "Score", "Report", "Gate"],
         tech=["Python", "zizmor", "GitHub Actions", "SAST"],
         layers=["scoring", "attest"]),
    dict(n=15, name="ReloopAI", label="ReloopAI", div="vision",
         blurb="Circular resource exchange, matched by AI", lang="TypeScript", licence="MIT",
         created="2026-07-13", month="Jul", home="https://reloop-ai-liart.vercel.app",
         pipeline=["Photo", "Classify", "Match", "Dispatch", "Notify"],
         tech=["TypeScript", "React", "Llama 3.2 Vision", "n8n", "Computer vision"],
         layers=["routing", "fallback", "vision", "scoring", "react"]),
    dict(n=16, name="Airgap-noc-Copilot", label="Airgap NOC Copilot", div="agents",
         blurb="Offline NOC copilot for MPLS and SD-WAN", lang="Python", licence="",
         created="2026-08-13", month="Aug", home="",
         pipeline=["Telemetry", "Risk score", "Retrieve", "Diagnose", "Runbook"],
         tech=["Python", "FAISS", "Containerlab", "FRRouting", "Local LLM"],
         layers=["grounding", "vector", "scoring", "simulate", "container"]),
    dict(n=17, name="RecoverOS", label="RecoverOS", div="agents",
         blurb="Policy-governed revenue recovery", lang="Python", licence="MIT",
         created="2026-08-22", month="Aug", home="",
         pipeline=["Detect", "Decide", "Bound", "Execute", "Prove"],
         tech=["Python", "Policy engine", "LLM routing", "Audit trail"],
         layers=["routing", "scoring", "attest"]),
]

# Shared layers used by the relationship matrix, in display order.
LAYERS = [
    ("routing", "Model routing"),
    ("fallback", "Deterministic fallback"),
    ("grounding", "Grounding and citation"),
    ("scoring", "Weighted scoring"),
    ("vector", "Vector retrieval"),
    ("vision", "Vision inference"),
    ("attest", "Audit trail and attestation"),
    ("fastapi", "FastAPI services"),
    ("react", "React front ends"),
    ("container", "Container and cluster"),
    ("simulate", "Simulate before shipping"),
]

# Instrument inventory, grouped by role.
STACK = [
    ("LANGUAGES", ["Python \u00b710", "TypeScript \u00b74", "JavaScript \u00b73", "Go"]),
    ("MODELS", ["Claude", "GPT", "Gemini", "Llama 3.2 Vision", "Qwen", "Groq", "Ollama", "Local LLM"]),
    ("RETRIEVAL", ["LangChain", "LangGraph", "ChromaDB", "FAISS", "Vector search"]),
    ("SERVICES", ["FastAPI", "Flask", "Node.js", "Streamlit", "n8n", "Nginx"]),
    ("INTERFACE", ["React", "Next.js", "Vite", "Tailwind"]),
    ("PERCEPTION", ["YOLOv8", "OpenCV", "PyTorch", "Flower"]),
    ("ASSURANCE", ["zizmor", "SAST", "GitHub Actions", "OpenTelemetry", "LitmusChaos"]),
    ("DATA AND RUNTIME", ["Docker", "Kubernetes", "k3s", "MongoDB", "SUMO", "Containerlab"]),
]


def state(repo):
    if repo["home"]:
        return "deployed"
    if repo["licence"]:
        return "open"
    return "prototype"


def by_division():
    out = []
    for key, name, question in DIVISIONS:
        out.append((key, name, question, [r for r in REPOS if r["div"] == key]))
    return out
