---
title: "ThreadNavigatorAI2.0"
emoji: "🧵"
colorFrom: "red"
colorTo: "green"
sdk: streamlit
sdk_version: "1.33.0"
app_file: app.py
pinned: true
---

# 🧵 ThreadNavigatorAI 2.0 — Multi-Agent Reddit Thread Analyzer with LLM-as-a-Judge

[![Built with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red?logo=streamlit)](https://streamlit.io)  
[![Multi-Agent LLMs](https://img.shields.io/badge/LLM%20Stack-Multi--Agent-blueviolet?logo=python)]()  
[![Deployed on Hugging Face](https://img.shields.io/badge/Hosted%20on-HuggingFace-orange?logo=huggingface)](https://huggingface.co/spaces/rajesh1804/ThreadNavigatorAI2.0)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 🔍 **ThreadNavigatorAI 2.0** is a modular, multi-agent Reddit analyzer that summarizes threads, verifies claims, and scores insights using LLM-as-a-Judge. Built for high-scale moderation and discourse comprehension under real-world latency and token constraints.

🎯 Designed for folks evaluating **top-tier AI engineering talent**.

---

## 🚀 What’s New in 2.0

ThreadNavigatorAI 2.0 builds directly on [v1.0](https://github.com/rajesh1804/ThreadNavigatorAI) by introducing:

| Feature                    | 1.0                        | 🚀 2.0 Upgrade                          |
|---------------------------|----------------------------|----------------------------------------|
| Agent Orchestration       | LangGraph (Reply, Mod)     | Modular pipeline (Summarizer, FC, Eval) |
| Summarization             | Prompt + RAG               | Semantic + config-driven transformer   |
| Moderation                | Rule-based + LLM           | 🔍 Fact Checker Agent (tool-augmented) |
| Evaluation                | Manual                     | 🧠 LLM-as-a-Judge (rubric-based)       |
| UI                        | Basic Streamlit            | ✨ Tabbed layout, latency toggle, download |
| Scalability               | Single-thread only         | 100 threads (real + mock hybrid)       |

---

## 📊 Architecture Overview

<p align="center">
  <img src="https://github.com/rajesh1804/threadnavigatorai2.0/raw/main/assets/threadnavigator_flow.png" alt="ThreadNavigatorAI Multi-Agent Flow" width="720"/>
</p>

```text
Thread JSON → [Multi-Agent Orchestration]
              ├── 🔍 Summarizer Agent → Extracts core insights
              ├── 🧪 Fact Checker Agent → Verifies claims via tools
              └── 🧠 Evaluator Agent → LLM-as-a-Judge on rubric (Relevance, Factuality...)

              ↳ Config-driven model orchestration (via config.yaml)
              ↳ Latency + model tracking in UI
              ↳ Deployed on Hugging Face Spaces (Streamlit + Docker)
```

---

## 🌟 Key Features

✅ **Multi-Agent Stack** (Summarizer, Fact Checker, Evaluator)  
✅ **Semantic Summarization + Retrieval**  
✅ **LLM-as-a-Judge** via rubric-based evaluation (like RAGAS)  
✅ **Hybrid Simulation Mode** (10 real + 90 mock = 100 total threads)  
✅ **Live Latency Display + Model Attribution**  
✅ **Streamlit UX** with onboarding, source links, toggles, download  
✅ **Free-tier Deployable** (OpenRouter APIs, Streamlit, Hugging Face)

---

## 🧠 Agent Stack (Config-Driven)

> Modular multi-agent architecture modeled after real-world Reddit analysis workflows.

| Agent            | Role                                           | Model Used (Free-tier)                         |
|------------------|------------------------------------------------|------------------------------------------------|
| 🧠 Summarizer     | Extracts semantic insights from messy Reddit posts using transformer-based compression        | `moonshotai/kimi-k2:free`                      |
| 🧪 Fact Checker   |Verifies factuality using retrieval tools          | `deepseek/deepseek-r1:free`                    |
| 📊 Evaluator      | Scores output on Relevance, Coherence, and Factuality (LLM-as-a-Judge) | `openrouter/mistralai/mistral-7b-instruct:free` |
| 🔧 Tools          | External retrieval & KB (Serper, Wikipedia)    | —                                              |

All agents use individual OpenRouter models, with latency tracked per call.

---

## 🔎 How It Works

Select a Reddit-style thread from 100 examples.

Agents are triggered in sequence:

- **🧠 Summarizer** → condenses the entire thread  
- **🧪 Fact Checker** → verifies major claims with external data  
- **📊 Evaluator** → scores the summary based on LLM rubrics  

Output is displayed in a polished tabbed UI with latency + model trace.  
Optionally download the result as JSON.  

All agents are modular — swap-in / swap-out via `config.yaml`.

---

## 🖼️ UI Preview

<p align="center">
  <img src="https://github.com/rajesh1804/threadnavigatorai2.0/raw/main/assets/threadnavigator_demo.png" width="750"/>
</p>

**Tabbed layout includes:**

- 🧠 **Summary** (with model and source)  
- 🔎 **Fact Checks** (claim + judgment)  
- ⚡ **Latency** (per agent)  
- 📊 **Evaluation** (scored by LLM)

#### 🚢 Live Demo

📌 Try the fully working UI on Hugging Face:  
👉 [ThreadNavigatorAI 2.0 – Live Space](https://huggingface.co/spaces/rajesh1804/ThreadNavigatorAI2.0)

No login, no billing — real inference with OpenRouter free-tier models.

---

## 🧪 Sample Output (Thread ID: `threadid_011`)

- **🧠 Summary**: Debate around GPT-4 vs Gemini, with user opinions and factual misunderstandings  
- **🔎 Claim**: “Gemini was trained on YouTube comments” → 🔴 Incorrect  

**📊 Eval Score:**
- Relevance: 🟢 5 — Very relevant  
- Coherence: 🟡 3 — Some redundancy  
- Factuality: 🟢 4 — Mostly accurate  

**⏱️ Latency**:
- Summarizer: 2.1s
- FactChecker: 3.4s
- Evaluator: 1.9s

---

## 📁 Project Structure
```bash
ThreadNavigatorAI2.0/                      
├── ui/                        
│   └── app.py                     # Streamlit frontend
├── cli/ 
│   └── batch_run.py               # Multi-thread processor
├── config/                        # Models and tool settings
│   └── config.yaml
├── agents/
│   ├── summarizer_agent.py
│   ├── factchecker_agent.py
│   └── evaluator_agent.py
├── utils/
│   ├── llm_utils.py
├── data/
│   ├── batch_output.json          # 10 threads real inference and 90 threads simulated inference
│   └── threads_100.json           # 100 simulated threads
├── assets/
│   ├── threadnavigator_flow.png   # Architecture Diagram
│   └── threadnavigator-demo.gif   # UI Demo
└── requirements.txt

```

---

## 💼 Why This Project Stands Out
- ✅ Represents real-world pipeline for Reddit moderation/analysis
- ✅ Dynamic toggles: latency, evaluation, download
- ✅ Hybrid inference simulates scale under free-tier
- ✅ LLM-as-a-Judge with model attribution & traceability
- ✅ Fully local, frictionless UI with onboarding
- ✅ Built like an internal debugging tool for social platforms

---

## 🧰 Run Locally (for Devs)

```bash
git clone https://github.com/rajesh1804/ThreadNavigatorAI2.0
cd ThreadNavigatorAI2.0
pip install -r requirements.txt
```

Create `.env`:

```bash
OPENROUTER_API_KEY=sk-
SERPER_API_KEY=
```

Then run:
```bash
streamlit run app.py
```

---

## 🧠 Linked Projects

| Project              | Description                                                              | Link |
|----------------------|---------------------------------------------------------------------------|------|
| 🧵 ThreadNavigatorAI 1.0 | RAG-based summarizer + moderator + reply agent using LangGraph            | [🔗 View](https://github.com/rajesh1804/ThreadNavigatorAI) |
| 🚕 RideCastAI           | Real-time ride fare/ETA prediction with spatial heatmaps                  | [🔗 View](https://github.com/rajesh1804/RideCastAI) |
| 🛒 GroceryGPT+          | Vector search + reranking grocery assistant with fuzzy recall             | [🔗 View](https://github.com/rajesh1804/GroceryGPT) |
| 🎬 StreamWiseAI         | Netflix-style movie recommender with Retention Coach Agent                | [🔗 View](https://github.com/rajesh1804/StreamWiseAI) |

---

## ⚠️ Known Challenges

- 🧪 `gemma-3-4b-it` rejected evaluation due to instruction tuning being disabled — switched to `mistralai-7b:free`
- 📉 Reddit data volume limited to 10 threads (real) due to OpenRouter limits — mock data generated for scalability tests
- ⏱️ Tool-based fact-checking adds ~2–3 seconds latency — handled with async retries + optional toggle
- 🧵 No full LangGraph orchestration in this version (ThreadNavigator 1.0 had it) — but this version enables more precise per-agent control

---

## 🧑‍💼 About Me

**Rajesh Marudhachalam** — AI/ML Engineer with a focus on building LLM-native applications.  
📍 [GitHub](https://github.com/rajesh1804) | [LinkedIn](https://www.linkedin.com/in/rajesh1804/)

Projects: [RideCastAI](https://github.com/rajesh1804/RideCastAI), [StreamWiseAI](https://github.com/rajesh1804/StreamWiseAI), [GroceryGPT+](https://github.com/rajesh1804/GroceryGPT)

---

## 🙌 Acknowledgments

- [OpenRouter](https://openrouter.ai) — Free-tier LLM APIs  
- [Streamlit](https://streamlit.io) — UI framework  
- [Serper.dev](https://serper.dev) — Web search API  
- [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page) — Factual KB  
- [Hugging Face Spaces](https://huggingface.co/spaces) — App Hosting  

---

## 📜 License

MIT License

⭐️ *Star this repo if it impressed you. Follow for more elite-level ML + LLM builds.*
