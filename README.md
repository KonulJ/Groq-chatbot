# Groq Chatbot

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.3-yellowgreen?logo=chainlink&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LPU%20Inference-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A conversational AI chatbot powered by **Groq's ultra-fast LPU inference** and **LangChain**, with a clean **Streamlit** interface. Supports multiple open-source LLMs with real-time model switching, session memory, and configurable generation parameters.

---

## Features

- **4 open-source models** — switch between Llama 3.3 70B, Llama 3.1 8B, Mixtral 8x7B, and Gemma2 9B at runtime
- **Conversation memory** — full session context retained via `ConversationBufferMemory`
- **Adjustable temperature** — tune response creativity from 0.0 to 1.0
- **Ultra-fast inference** — Groq LPU delivers significantly faster responses than standard GPU APIs
- **Secure API key handling** — credentials loaded from `.env`, never hardcoded
- **Clear conversation** — reset session with one click

---

## Supported Models

| Model | Parameters | Best For |
| --- | --- | --- |
| `llama-3.3-70b-versatile` | 70B | Complex reasoning, detailed answers |
| `llama-3.1-8b-instant` | 8B | Speed, lightweight tasks |
| `mixtral-8x7b-32768` | 8x7B MoE | Long context (32K tokens), coding |
| `gemma2-9b-it` | 9B | Instruction following, concise replies |

---

## Project Structure

```
groq-chatbot/
├── app.py            # Streamlit UI — chat interface, sidebar, session state
├── chatbot.py        # LangChain logic — LLM init, memory, chain
├── requirements.txt  # Python dependencies
├── .env              # API key (git-ignored)
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- Free Groq API key from [console.groq.com](https://console.groq.com)

### 1. Clone the repository

```bash
git clone https://github.com/KonulJ/groq-chatbot.git
cd groq-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API key

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the app

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## How It Works

1. The user sends a message via the Streamlit chat input.
2. `ConversationChain` prepends the full session history from `ConversationBufferMemory` to maintain context.
3. `ChatGroq` sends the enriched prompt to the selected model via the Groq API.
4. The response is displayed in the chat window and saved to session memory.
5. Switching models reinitializes the chain while keeping the displayed history intact.

---

## Tech Stack

| Tool | Role |
| --- | --- |
| [LangChain](https://www.langchain.com/) | LLM orchestration, memory, chains |
| [Groq](https://groq.com/) | LPU-accelerated inference for open-source LLMs |
| [Streamlit](https://streamlit.io/) | Interactive web UI |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Secure environment variable loading |

---

## Roadmap

- [ ] Streaming token output
- [ ] Customizable system prompt via sidebar
- [ ] Export chat history to `.txt` / `.json`
- [ ] RAG integration for document-aware Q&A
- [ ] Docker support for deployment

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

*Built by [Konul Jafarova](https://github.com/KonulJ)*
