# 🎯 AI-Powered Quiz Generator

🚀 An intelligent Multiple-Choice Question (MCQ) generator that automatically extracts key concepts from any given text and formulates well-structured quiz questions. Powered by **Hugging Face Transformers**, **spaCy**, and **FastAPI**.

---

## 🌟 Features
✅ Generates high-quality **MCQs** from any input text  
✅ Uses **Named Entity Recognition (NER)** for relevant question generation  
✅ Supports **Flan-T5** model for text-based question generation  
✅ Provides **API support** via FastAPI for seamless integration  
✅ Clean and structured **output format** (Question + 4 options)  

---

## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/ai-quiz-generator.git
cd ai-quiz-generator
```

### **2️⃣ Install Dependencies**
Ensure you have Python **3.8+** installed, then run:
```sh
pip install -r requirements.txt
```

### **3️⃣ Start the API Server**
```sh
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

---

## 📌 Usage

### **🔹 API Endpoint**
```http
POST /generate-mcq
```
**Request Body (JSON):**
```json
{
  "text": "Albert Einstein was a German-born physicist who developed the theory of relativity."
}
```
**Response Example:**
```json
{
  "question": "Who developed the theory of relativity?",
  "options": [
    "A. Isaac Newton",
    "B. Nikola Tesla",
    "C. Albert Einstein",
    "D. Galileo Galilei"
  ],
  "answer": "C"
}
```

---

## 🏠 Tech Stack

- **Backend:** FastAPI  
- **AI Model:** Hugging Face (Flan-T5)  
- **NLP Processing:** spaCy  
- **Deployment:** Uvicorn  

---

## 🤝 Contributing
Contributions are welcome! To contribute:  
1. **Fork** the repository  
2. **Create a new branch:** `git checkout -b feature-branch`  
3. **Commit your changes:** `git commit -m "Added a new feature"`  
4. **Push to the branch:** `git push origin feature-branch`  
5. **Open a Pull Request**  

---

## 🐝 License
This project is licensed under the **MIT License**.

---


