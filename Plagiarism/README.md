# 🕵️‍♂️ Plagiarism Detector Web App

A bright, modern web application to detect plagiarism between two statements using machine learning (Python, Flask, scikit-learn, NLTK).

## 🚀 Features
- Enter two statements and check for plagiarism instantly
- Probability score shown as a percentage
- Colorful, responsive web interface
- Built with Flask, scikit-learn, and NLTK

## 📂 Project Structure
```
Plagiarism/
├── app.py
├── article50.csv
├── plagiarism_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

## 🛠️ Setup & Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Download NLTK stopwords (first run only):**
   The app will automatically download stopwords if not present.

4. **Run the app:**
   ```bash
   python app.py
   ```
5. **Open your browser:**
   Go to [http://localhost:5000](http://localhost:5000)

## 📝 Usage
- Enter a source statement and a suspect statement.
- Click "Check Plagiarism".
- View the result and probability.

## 📦 Requirements
- Python 3.7+
- Flask
- scikit-learn
- pandas
- nltk
- joblib

## 🙏 Credits
- UI inspired by modern gradient designs
- Machine learning workflow based on open-source tutorials

## 📄 License
MIT License 