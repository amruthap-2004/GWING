from flask import Flask, render_template, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load small model and tokenizer data
word_index = np.load('small_tokenizer_word_index.npy', allow_pickle=True).item()
max_sequence_len = int(np.load('small_max_sequence_len.npy')[0])
model = load_model('small_model.h5')

def sample_with_temperature(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds + 1e-8) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def generate_text(seed_text, next_words=10, temperature=1.0):
    for _ in range(next_words):
        token_list = [word_index.get(word, 0) for word in seed_text.lower().split()]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        preds = model.predict(token_list, verbose=0)[0]
        predicted = sample_with_temperature(preds, temperature)
        output_word = None
        for word, index in word_index.items():
            if index == predicted:
                output_word = word
                break
        if output_word is None:
            break
        seed_text += ' ' + output_word
    return seed_text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    seed_text = data.get('seed_text', '')
    next_words = data.get('next_words', 10)
    temperature = data.get('temperature', 1.0)
    
    try:
        generated_text = generate_text(seed_text, next_words, temperature)
        return jsonify({'success': True, 'generated_text': generated_text})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 