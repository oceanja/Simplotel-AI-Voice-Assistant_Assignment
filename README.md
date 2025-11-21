# 🎙️ QueryBot — Simplotel AI Voice Assistant

An AI-powered, voice-enabled assistant built for **Simplotel** as part of the **Software Engineer Internship Assignment**.

QueryBot allows users to speak queries related to Simplotel’s services, products and company information, and instantly receive both **text and voice responses** — all inside an interactive, futuristic UI.

This project demonstrates core backend engineering skills, AI integration, and real-world application design for the **hospitality & hotel technology industry**.

---

## 🚀 What This Project Does

QueryBot follows this complete pipeline:

1. User **speaks a question**
2. Speech is converted to **text using OpenAI Whisper**
3. The text is matched with Simplotel-related FAQs using **NLP logic**
4. A relevant answer is generated
5. The answer is converted into **speech using gTTS**
6. The response is:
   - Displayed on screen
   - Played automatically (no Play button required)

All of this happens inside a **responsive web interface** built with Streamlit.

---

## 🏨 Why this is relevant for Simplotel

Simplotel serves 3,000+ hotels across 26 countries and provides:

- Hotel websites
- Booking engines
- E-commerce solutions
- Digital marketing tools

This assistant can be directly used as:
✅ Hotel support bot  
✅ Customer service AI  
✅ Sales / onboarding demo bot  
✅ Internal knowledge assistant  

It is tailored to answer Simplotel-specific questions and can easily be extended for hotel-specific use cases.

---

## 🛠️ Tech Stack

**Frontend**
- Streamlit
- HTML / CSS (Glassmorphism UI)
- Responsive design (Mobile + Desktop)

**Backend / AI**
- Python
- OpenAI Whisper — Speech to Text
- gTTS — Text to Speech
- Custom NLP Intent Matching Logic

**Data Handling**
- JSON knowledge base (`faq.json`)
- Chat memory using Streamlit state

**Supporting Libraries**
- `sounddevice`
- `numpy`
- `json`
- `base64`
- `datetime`

---

## 📂 Project Structure
```

AI_VOICE_BOT/
│
├── app.py → Main UI & app controller
├── voicebot.py → Core bot logic
├── requirements.txt → Dependencies
├── README.md → Documentation
│
├── data/
│ └── faq.json → Simplotel questions & answers
│
├── utils/
│ ├── speech_to_text.py → Voice input (Whisper)
│ ├── text_to_speech.py → Audio output (gTTS)
│ └── nlp.py → NLP matching logic
│
└── audio/
├── input.wav
└── output.mp3

```


---

## 💬 Supported Questions

QueryBot is trained to answer the following types of Simplotel-specific questions (from `faq.json`):

You can ask things like:

### 🔹 Company Information
- “What is Simplotel?”
- “Where is Simplotel located?”
- “Who founded Simplotel?”
- “When was Simplotel founded?”

### 🔹 Product & Services
- “What services does Simplotel offer?”
- “What is Simplotel’s booking engine?”
- “How does Simplotel help hotels?”
- “Does Simplotel build hotel websites?”

### 🔹 Scale & Reach
- “How many hotels does Simplotel work with?”
- “In how many countries is Simplotel present?”

### 🔹 Technology Stack
- “What technologies does Simplotel use?”
- “Is Simplotel built using Python?”
- “What backend does Simplotel use?”

### 🔹 Careers / Internship
- “What is the Intern – Backend Engineer role?”
- “What skills are required for Simplotel internship?”
- “What is the stipend for internship at Simplotel?”
- “Where is the internship located?”


No code change is required.

---

## ⚙️ How To Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/oceanja/Simplotel-AI-Voice-Assistant_Assignment.git

```
### 🔹 Create & Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 🔹 Install dependencies
```bash
pip install -r requirements.txt
```

