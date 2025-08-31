# 🤖 ChatGuard: AI-Powered Scam Detection Chatbot

![ChatGuard Demo](./chatguard-demo.gif)

> ⚡ *Real-time AI-powered scam detection system integrated within a chatbot interface.*

---

## 📌 Overview

**ChatGuard** is a proof-of-concept project that demonstrates how to build a **real-time scam detection system** inside a chatbot interface.  
It leverages **Machine Learning (Scikit-learn)** to classify messages as **"Scam"** or **"Legitimate"** and alerts the user instantly.

The project covers the **complete workflow**:  
✔️ Data processing  
✔️ Model training  
✔️ Real-time prediction  
✔️ Interactive chatbot application with **Streamlit**

---

## 🚀 Features

- **AI Scam Detection Engine** – Uses an ML pipeline (TF-IDF + Logistic Regression) to classify messages.  
- **Real-Time Analysis** – Every user message is analyzed instantly for potential risks.  
- **Interactive Chat Interface** – Built with Streamlit, simulating a real chat app.  
- **Clear Risk Alerts** – Displays scam warnings with confidence scores.  
- **Modular Codebase** – Separated into logical parts:  
  - `train_model.py` → Model training  
  - `chatguard.py` → Core detection engine  
  - `app_streamlit.py` → Frontend app  

---

## 🛠️ Tech Stack

- **Backend & ML**: Python, Scikit-learn, Pandas, Joblib  
- **Frontend**: Streamlit  
- **Dataset**: [SMS Spam Collection Dataset (Kaggle)](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)  

---

## 🔧 Getting Started

Follow these steps to run ChatGuard locally:

### ✅ Prerequisites
- Python 3.8+  
- `pip` (Python package installer)

### 📥 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/ChatGuard.git
cd ChatGuard

# Create a virtual environment
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
📊 Dataset
Download the SMS Spam Collection Dataset.

Place the spam.csv file in the project root.

▶️ Running the Project
1️⃣ Train the Model
bash
Copy code
python train_model.py
Processes spam.csv

Trains Logistic Regression model

Saves as chatguard_model.pkl

You’ll also see a classification report in the terminal.

2️⃣ Launch the Web App
bash
Copy code
streamlit run app_streamlit.py
Opens the Streamlit chatbot interface in your default browser.

Messages typed are analyzed in real-time.

🤖 How It Works
Text Vectorization (TF-IDF) – Converts text messages into numerical vectors. Uses ngram_range=(1, 2) to capture both words and phrases.

Classification (Logistic Regression) – Learns patterns of scam vs. legitimate messages. class_weight='balanced' ensures scam detection isn’t ignored due to class imbalance.

Prediction – Every new message is processed by the saved pipeline. If scam probability > threshold (50%), a warning alert is triggered.

📂 Project Structure
bash
Copy code
ChatGuard/
│
├── spam.csv               # Dataset (to be downloaded)
├── chatguard_model.pkl    # Trained AI model (auto-generated)
│
├── train_model.py         # Model training script
├── chatguard.py           # Scam detection engine
├── app_streamlit.py       # Streamlit frontend
│
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
📈 Future Improvements
🔹 Use transformer-based models (BERT, DistilBERT) for better accuracy.

🔹 Train on larger datasets including email phishing & social media scams.

🔹 Add URL analysis to detect suspicious links.

🔹 Containerize with Docker for easy deployment.

🔹 Upgrade chatbot to Rasa / Dialogflow for smarter interactions.

📜 License
This project is open-source and available under the MIT License.

🙌 Acknowledgments
Dataset: SMS Spam Collection Dataset

Tools: Python, Scikit-learn, Streamlit

