# 🚀 NLP Log Classification System

<p align="center">

# Intelligent Hybrid Log Classification using NLP, Machine Learning & LLMs

</p>

---

## 👩‍💻 Developed By

# **Muskan Sondhiya**

B.Tech Computer Science (Data Science)

Artificial Intelligence • Machine Learning • NLP • Generative AI

GitHub: https://github.com/Muskan136

---

# 📌 Project Overview

The NLP Log Classification System is an intelligent log analysis application that automatically classifies system logs using a hybrid Natural Language Processing framework.

The application combines Rule-Based Processing, Machine Learning, and Large Language Models to classify structured, semi-structured, and unseen log messages with improved accuracy.

This project demonstrates practical applications of NLP, Machine Learning, FastAPI, and LLMs for enterprise log analysis.

---

# ✨ Features

- Hybrid NLP Classification
- Regex-based Log Classification
- Sentence Transformer Embeddings
- Logistic Regression Model
- LLM-powered Classification
- REST API using FastAPI
- Batch CSV Processing
- Automatic Log Categorization
- High Accuracy Classification
- Modular Architecture

---

# 🏗 Architecture

```
                    Input Log File
                           │
                           ▼
                  Log Preprocessing
                           │
                           ▼
               Hybrid Classification Engine
      ┌────────────────┬─────────────────┬────────────────┐
      │                │                 │
      ▼                ▼                 ▼
 Regex Processor   ML Classifier      LLM Processor
      │                │                 │
      └────────────────┴─────────────────┘
                     │
                     ▼
          Final Log Classification
```

---

# 🛠 Tech Stack

### Programming Language

- Python

### Backend

- FastAPI

### Machine Learning

- Scikit-Learn
- Sentence Transformers
- Logistic Regression

### NLP

- Regular Expressions
- Transformers
- Large Language Models

### Libraries

- Pandas
- NumPy

---

# 📂 Project Structure

```
nlp-log-classification/

│── server.py
│── classify.py
│── requirements.txt
│── README.md
│
├── models/
│
├── resources/
│
├── training/
│
├── processor_regex.py
├── processor_bert.py
└── processor_llm.py
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Muskan136/nlp-log-classification.git
```

Move into the project folder

```bash
cd nlp-log-classification
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Start the FastAPI server

```bash
uvicorn server:app --reload
```

Application

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation

```
http://127.0.0.1:8000/redoc
```

---

# 📥 Input

Upload a CSV containing the following columns:

| Column |
|----------|
| source |
| log_message |

---

# 📤 Output

The application generates a CSV containing:

| Column |
|----------|
| target_label |

---

# 🎯 Applications

- Enterprise Log Analysis
- Security Monitoring
- DevOps Automation
- Cloud Monitoring
- Incident Detection
- IT Infrastructure Monitoring
- System Health Monitoring

---

# 🚀 Future Improvements

- Real-Time Log Streaming
- Interactive Dashboard
- Docker Deployment
- Kubernetes Support
- Confidence Score Visualization
- Model Retraining Pipeline
- Multi-language Log Classification

---

# 📸 Project Preview

> Add screenshots of your application here.

Example:

```
screenshots/
    home.png
    prediction.png
```

Then include:

```markdown
<p align="center">
<img src="screenshots/home.png" width="100%">
</p>
```

---

# 👩‍💻 Author

## Muskan Sondhiya

Computer Science (Data Science)

Machine Learning | Artificial Intelligence | NLP | Python | FastAPI | Generative AI

GitHub:
https://github.com/Muskan136

LinkedIn:
(Add your LinkedIn profile here)

---

## ⭐ If you found this project useful, please consider giving it a Star.
