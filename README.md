# Groq Chatbot

A conversational chatbot built with **LangChain** and **Groq** open-source models, featuring a clean Streamlit UI.

## Features

- Multiple open-source models: Llama 3.3 70B, Llama 3.1 8B, Mixtral 8x7B, Gemma2 9B
- Conversation memory (context-aware responses)
- Adjustable temperature
- Clear conversation button

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/KonulJ/groq-chatbot.git
cd groq-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Groq API key
Get a free API key at https://console.groq.com, then create a `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the app
```bash
streamlit run app.py
```

## Project Structure

```
├── app.py           # Streamlit UI
├── chatbot.py       # LangChain + Groq logic
├── requirements.txt # Dependencies
├── .env             # API key (not committed)
└── README.md
```

## Tech Stack

- [LangChain](https://www.langchain.com/)
- [Groq](https://groq.com/)
- [Streamlit](https://streamlit.io/)
