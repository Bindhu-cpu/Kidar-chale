# 🌍 Kidar Chale — AI-Powered Travel Planner

**Kidar Chale** is an AI-powered travel planning application built using Retrieval-Augmented Generation (RAG) and a Multi-Agent AI architecture. It helps users discover destinations, plan trips, and find travel experiences based on their budget, duration, and interests.

## ✨ Key Features

### 🔎 1. Find a Destination
Not sure where to travel? Enter your budget and trip requirements to discover destinations that match your needs.

### 🗺️ 2. Plan My Trip
Already know your destination? Get sightseeing recommendations, suggested itineraries, and estimated expenses tailored to your budget and trip duration.

### 🎨 3. My Vibe
Choose your preferred travel style, such as mountains, beaches, nature, or adventure. Discover destinations and travel plans that match your interests and budget.

## 🤖 AI Architecture

Kidar Chale uses a Multi-Agent AI workflow with specialized agents for:

- **Requirement Agent:** Collects user travel preferences and requirements.
- **Destination Agent:** Recommends suitable travel destinations.
- **Itinerary Agent:** Organizes sightseeing places and trip schedules.
- **Budget Agent:** Estimates trip expenses based on user requirements.
- **Final Agent:** Combines the results into a personalized travel plan.

## 📚 Retrieval-Augmented Generation (RAG)

The RAG component retrieves relevant information from a travel knowledge base containing destination details, itinerary guidance, and budget information.

The project uses FAISS and Sentence Transformers for semantic search and relevant knowledge retrieval.

## 🛠️ Tech Stack

- Python
- Streamlit
- Retrieval-Augmented Generation (RAG)
- Multi-Agent AI
- FAISS
- Sentence Transformers

## 📁 Project Structure

- `app.py` — Main Streamlit application
- `agents/` — Specialized travel-planning agents
- `rag/` — RAG engine and semantic search index
- `knowledge/` — Travel destination, budget, and itinerary information
- `assets/` — Application images
- `requirements.txt` — Python dependencies

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Bindhu-cpu/Kidar-chale.git
cd Kidar-chale
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

## 🎯 Project Goal

To make travel planning easier by combining destination discovery, personalized itineraries, budget estimation, and interest-based recommendations in one application.

## 👩‍💻 Developer

**Bindhu Madhavi**

---

*Built with Python, RAG, and Multi-Agent AI.*
