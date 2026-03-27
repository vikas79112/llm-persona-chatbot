# 🎤 LLM Persona Chatbot

A persona-based AI chatbot that mimics different personalities of Indian stand-up comedians using LLMs.
Built with **LangChain**, **Mistral LLM**, and **Streamlit** with dynamic persona switching and conversation memory.

---
## Demo
https://llm-persona-chatbot-669omxqeonjgsweku8up5m.streamlit.app/

## 🚀 Features

* Multiple AI personas (Samay Raina, Akash Gupta, Calm Comedian, Roast Mode)
* Real-time chat interface
* Conversation memory
* Persona switching
* Streamlit chat UI
* LLM integration using LangChain
* Environment variable support using dotenv

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Mistral LLM
* python-dotenv

---

## 📂 Project Structure

```
llm-persona-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/llm-persona-chatbot
cd llm-persona-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` file and add your API key

```
MISTRAL_API_KEY=your_api_key_here
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🧠 How It Works

* User selects a comedian persona from the dropdown.
* The system sets a **System Prompt** based on the selected persona.
* Conversation history is stored using **LangChain message objects**.
* The chatbot generates responses in the selected comedian’s style using **Mistral LLM**.
* Streamlit provides the chat interface.

---

## 🔮 Future Improvements

* Add voice input
* Add text-to-speech responses
* Save chat history
* Add more personas (teacher, interviewer, motivational coach)
* Deploy the app online

---
