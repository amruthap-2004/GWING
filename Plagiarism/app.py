from flask import Flask, render_template, request, jsonify
import joblib
import string
from nltk.corpus import stopwords
import nltk

# Ensure stopwords are downloaded
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

# Load model and vectorizer
model = joblib.load('plagiarism_model.pkl')
tfidf = joblib.load('tfidf_vectorizer.pkl')

app = Flask(__name__)

def preprocess_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    stop_words = set(stopwords.words('english'))
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    source = request.form['source']
    suspect = request.form['suspect']
    s = preprocess_text(source)
    t = preprocess_text(suspect)
    combined = s + ' ' + t
    features = tfidf.transform([combined])
    pred = model.predict(features)[0]
    prob = model.predict_proba(features)[0][1]
    result = "Plagiarized" if pred else "Not Plagiarized"
    percent = f"{prob * 100:.2f}%"
    return render_template('index.html', result=result, probability=percent, source=source, suspect=suspect)

if __name__ == '__main__':
    app.run(debug=True)
