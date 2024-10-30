# SimplifAI

## 👋 Introduction
In the healthcare sector, existing bureaucracy negatively impacts the time dedicated to clinical activities and harms the doctor-patient relationship. With this project, we aim to simplify some bureaucratic processes performed by doctors, such as (i) the creation of discharge notes from hospitalizations and (ii) the writing of clinical consultation diaries. We intend to use techniques for summarization, speech-to-text, and topic analysis, among others, related to technologies associated with LLMs.

This project is a proof of concept (PoC) that aims to address the issues explained above. It is understood that this goes against the rules of the AI Act, but as a PoC, it should demonstrate that it is possible and that AI has the capability to effectively assist doctors in making their work easier.

## 🏥 Motivation and Background

Evidence-based medicine relies heavily on the collection and processing of extensive data. However, patients often perceive excessive bureaucracy as diverting clinicians' attention away from personalized care. The significant time dedicated to these administrative tasks can be attributed to inefficient information systems, with the actual costs of data collection and processing exceeding initial estimates. Notably, 70% of clinicians have reported that, in the past five years, the time required for data entry and documentation has increased considerably.
 
This project aims to address these inefficiencies by reducing redundant documentation and focusing on essential information only. Additionally, it seeks to standardize data entry formats, making documentation more uniform and accessible.

## 🎯 Project Scope and Goals
Our project targets two primary bureaucratic processes:
1. The creation of discharge notes from hospitalizations.
2. The writing of clinical consultation diaries.

We use various advanced techniques such as text summarization, speech-to-text, and topic analysis to achieve these goals.

## ⚙️ Proof of Concept (PoC)

This project is a proof of concept (PoC) that demonstrates the feasibility of using AI to assist in healthcare documentation. It is understood that this PoC might contravene the rules of the AI Act, but it aims to show that AI has the potential to significantly ease the workload of doctors.

## ⚠️ Challenges and Considerations

### Ethical and Legal Considerations
- Addressing potential conflicts with the AI Act and ensuring ethical use of AI in healthcare.

### Technical Challenges
- Accurate voice capture and transcription.

## 🌟 Conclusion and Impact 

This proof of concept demonstrates the potential of AI to alleviate the bureaucratic burden on doctors, thereby enhancing their efficiency and improving the doctor-patient relationship. By automating routine documentation tasks, we can significantly impact the healthcare sector, allowing doctors to focus more on patient care.

## ❓ How to install 

### Requirements:

Python 3.12 or later
Node

To run our frontend as it is you should start by installing the dependencies with:

    cd frontend
    npm install

Next just run the frontend in developer mode:

    npm run dev

In order to use all the application features is recommended to also run our backend. Again, start by creating a python environment and installing the packages:

    cd backend
    pip install -r requirements.txt

Before start the application it's mandatory to have an .env file configured in order to the application use the desired API keys. The structure of that file must be:

DB_CONNECTION_STRING={MONGO_DB_KEY}

GPT_API_KEY={GPT_KEY}

GROQ_API_KEY={GROK_KEY}

LANGFUSE_SECRET_KEY={LANGFUSE_SECRET_KEY}

LANGFUSE_PUBLIC_KEY_KEY={LANGFUSE_PUBLIC_KEY}


We don't give our keys for security reasons, so you must use yours to actually use the application. The .env file must be in the backend folder.

Now you are able to actually start the application with

    python -m uvicorn start:app --reload --port 8000