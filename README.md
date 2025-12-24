# 🕉️ Maitra (मैत्र) 
### *Empowering Maharashtra through Intelligent Voice-First Governance*

**Maitra** is a state-of-the-art AI Voice Assistant designed to bridge the gap between complex government bureaucracy and the common citizen. Built specifically for the Maharashtra state context, it leverages **Hybrid RAG**, **Agentic Reasoning**, and **Real-time Voice AI** to provide instant, accurate, and empathetic guidance in Marathi.

---

## 📺 Demo Experience
- **Primary Language:** Marathi (`mr-IN`)
- **Interaction:** Ultra-low latency Voice-to-Voice
- **Intelligence:** Eligibility logic, monthly-to-annual income conversion, and real-time web verification.

---

## 🛠️ Implementation Details

Our architecture is built on four pillars of modern AI engineering:

### 1. The Voice Core (LiveKit + Sarvam AI)
We utilized **LiveKit** for its robust WebRTC transport layer, ensuring near-zero latency. For a localized experience, we integrated **Sarvam AI**, utilizing their `bulbul:v2` model for high-fidelity Marathi Text-to-Speech (TTS) and highly accurate Speech-to-Text (STT).

### 2. Hybrid RAG Strategy
Unlike static bots, Maitra uses a dual-search approach to ensure accuracy:
- **Verified Layer:** The agent first queries a local **CSV database** (`schemes.csv`) for official, verified government records.
- **Dynamic Layer:** If information is missing or the user asks for "latest news/dates," the agent triggers the **Tavily Web Search** tool to fetch real-time 2024-2025 updates.

### 3. Agentic Reasoning (Llama 3.3 70B via Groq)
Using **Groq’s** high-speed LPU inference, the agent performs "Chain of Thought" reasoning:
- **Financial Calculation:** If a user mentions a monthly income, the agent internally calculates the annual income before performing an eligibility check.
- **Contextual Memory:** It maintains conversational state, remembering user attributes like age and gender to refine search results.

### 4. Safety & Marathi Localization
The agent is governed by a strict **System Prompt** that prevents "Technical Leaks" (JSON/Tags). It is designed to be polite ("आपण"), using formal Marathi to respect the cultural context of government-citizen interaction.



---

## 🚀 Getting Started (For Judges)

### 1. Prerequisites
- Python 3.10+
- A LiveKit Cloud Project
- API Keys: **Groq, Sarvam AI, Tavily,** and **LiveKit**.

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/maitra-voice-agent.git](https://github.com/YOUR_USERNAME/maitra-voice-agent.git)
cd maitra-voice-agent

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
3. Environment Setup
Create a .env file in the root directory:

```bash

LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your_key
LIVEKIT_API_SECRET=your_secret
GROQ_API_KEY=your_groq_key
SARVAM_API_KEY=your_sarvam_key
TAVILY_API_KEY=your_tavily_key
```
4. Running the Agent
```Bash
python main.py dev
```
