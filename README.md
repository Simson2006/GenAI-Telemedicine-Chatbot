# Generative AI Telemedicine WhatsApp Chatbot
An intelligent Gen AI-based telemedicine assistant that provides instant and context-aware medical insights via WhatsApp,powered by Llama 3.3-70B Versatile and a RAG pipeline trained on real-world disease data. 

# Overview
1.This project integrates Large Language Model (LLM) capabilities with Twilio, Flask, and SQLite to deliver accurate, real-time medical responses through WhatsApp.
2.It solves the problem of limited access to quick and reliable health guidance, especially in areas where medical experts are not readily available.

# Key Features
🤖 LLM-Powered Chatbot: Uses Llama 3.3-70B Versatile to generate human-like, medically relevant responses.

📚 RAG Integration: Trained with a curated dataset of 200+ diseases sourced from the Mayo Clinic website for enhanced factual accuracy.

💬 Context-Aware Chat: Maintains user–bot message history in SQLite, allowing the bot to understand past conversations.

🌐 WhatsApp Integration: Uses Twilio API and Ngrok to connect Flask backend with WhatsApp in real time.

⚡ Advantages: Offers 24/7 accessibility, instant guidance, and requires no separate app installation.

# System Architecture
 [User on WhatsApp]
        ↓
   [Twilio API]
        ↓
[Flask Server via Ngrok]
        ↓
[RAG + Llama 3.3-70B Model]
        ↓
[SQLite (Chat History)]
        ↓
[Response sent back to WhatsApp]

# How It Works
1.User sends a medical query via WhatsApp.

2.Twilio forwards the message to the Flask backend through an Ngrok tunnel.

3.The backend retrieves chat history and system context, and passes it to the Llama model along with the user query.

4.The LLM generates a response using RAG-based retrieval from the medical dataset.

5.The response is sent back to the user via WhatsApp, maintaining conversation continuity.

# Problem Solved
This chatbot solves the challenge of immediate and accessible healthcare guidance, especially in regions with limited medical infrastructure.
By combining WhatsApp’s accessibility with LLM reasoning, it delivers real-time, intelligent medical support to anyone, anywhere.
