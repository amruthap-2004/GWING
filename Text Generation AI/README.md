# Text Generation AI - Next Word Prediction

A creative web app that predicts and generates text using a neural network trained on your own dataset! Built with TensorFlow/Keras, Flask, and a modern HTML/JS frontend.

---

## 🚀 Features
- Train a neural network to predict the next word in a sequence
- Generate creative text with temperature sampling
- Beautiful, animated web interface (light/dark mode, confetti, gradients)
- Supports large datasets (e.g., Shakespeare, books, articles)
- Easy to customize and extend

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is missing, install: tensorflow, flask, numpy)*

3. **Prepare your dataset**
   - Place your text data in `data.txt` (or use the provided script to download Shakespeare).

4. **Preprocess the data**
   ```bash
   python prepare_data.py
   ```

5. **Train the model**
   ```bash
   python train_model.py
   ```
   - You can adjust the number of epochs in `train_model.py` for better results.

6. **Run the web app**
   ```bash
   python app.py
   ```
   - Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000) (or the port you set).

---

## 🌐 Web App Usage
- Enter a seed statement, choose the number of words and creativity (temperature), and click "Generate Text".
- Toggle between light and dark mode with the 🌙/☀️ button.
- Enjoy confetti and animated gradients for a fun experience!

---

## 🧠 Model Training
- The model uses an Embedding + LSTM architecture.
- You can use your own dataset by editing `data.txt`.
- For large datasets, the code uses sparse categorical crossentropy for efficiency.

---

## ⚙️ Customization
- **Change the dataset:** Replace `data.txt` with your own text.
- **Tweak the model:** Edit `train_model.py` for more layers or different architectures.
- **Style the UI:** Edit `templates/index.html` for more creative effects.

---

## 📄 Credits
- Inspired by [NeuralNine's YouTube tutorial](https://github.com/NeuralNine/youtube-tutorials/tree/main/Text%20Generation%20AI%20-%20Next%20Word%20Prediction)
- Built with TensorFlow, Flask, and lots of creativity!

---

**Enjoy generating creative text!** 