# 🧠 Text Pattern Analyzer

**Full Stack Project**  
**Backend:** Python (FastAPI)  
**Frontend:** Next.js  

---

## 🔹 Project Overview

Text Pattern Analyzer হল একটি ওয়েব অ্যাপ্লিকেশন যা ব্যবহারকারীর দেওয়া text বা `.txt` file analyze করে।  

**Features:**

- Top 2-word and 3-word repeated phrases
- Sentence complexity analysis
- Most complex & simplest sentence
- Estimated reading time
- Text input via textarea or .txt file
- Dark/Light mode friendly UI
- Error handling (empty input / invalid file)

**Tech Stack:**

- **Backend:** Python, FastAPI
- **Frontend:** Next.js (React)
- **No database required**
- **CORS enabled** for frontend-backend communication

---

## 🏗 Folder Structure

```

TextPatternAnalyzer/
│
├── backend/
│   ├── app/
│   │   ├── main.py         # FastAPI endpoints
│   │   └── analyzer.py     # Text analysis logic
│   ├── requirements.txt
│   └── venv/
│
└── frontend/
└── app/page.js         # Next.js frontend

````

---

## ⚡ Backend Setup (FastAPI)

1. Navigate to backend folder:

```bash
cd backend
````

2. Create virtual environment and activate:

```bash
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Mac/Linux
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Run the backend server:

```bash
uvicorn app.main:app --reload
```

5. API docs available at:

```
http://127.0.0.1:8000/docs
```

---

## ⚡ Frontend Setup (Next.js)

1. Navigate to frontend folder:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Run frontend development server:

```bash
npm run dev
```

4. Open in browser:

```
http://localhost:3000
```

---

## 🛠 Usage

1. **Paste Text:**

   * Type or paste text in the textarea.
2. **Upload File:**

   * Upload `.txt` file (only text files accepted)
3. **Click Analyze:**

   * Results will show in **card view**
   * Top phrases, reading time, sentence complexity

---

## 🌈 Features Highlights

* **Dark/Light mode safe design**
* **Smart error handling**
* **Responsive and clean layout**
* **Simple API structure, easy to extend**

---

## 📌 Notes

* Average reading speed: 200 words/min
* Sentence complexity = `word_count * avg_word_length`
* Frontend communicates with backend using **CORS enabled POST request**

---

## 🔮 Next Possible Enhancements

* Sentence search/filter
* Charts (Top phrases frequency)
* Drag & drop file upload
* Real-time streaming analysis for huge text

```


