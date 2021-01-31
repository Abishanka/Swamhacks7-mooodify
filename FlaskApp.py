# Imports
from flask import Flask, render_template, request
import tensorflow_datasets as tfds
import tensorflow as tf

app = Flask(__name__)

yourmood = ''

# Python ML Code
dataset, info = tfds.load('imdb_reviews/subwords8k', with_info=True, as_supervised=True)
train_dataset, test_dataset = dataset['train'], dataset['test']
encoder = info.features['text'].encoder
# Defining Model
model = tf.keras.models.load_model('model.h5')


# Python ML code necessary functions
# Pads the dataset
def pad_to_size(vec, size):
    zeros = [0] * (size - len(vec))
    vec.extend(zeros)
    return vec

    # Implements the pad to the prediction


def sample_predict(sentence, pad):
    encoded_sample_predict_text = encoder.encode(sentence)
    if pad:
        encoded_sample_predict_text = pad_to_size(encoded_sample_predict_text, 64)
    encoded_sample_predict_text = tf.cast(encoded_sample_predict_text, tf.float32)
    predictions = model.predict(tf.expand_dims(encoded_sample_predict_text, 0))

    return predictions


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route("/mood", methods=['POST', 'GET'])
def mood():
    # Spitting Out an Output
    sample_text = str(request.form.get('input'))
    predictions = sample_predict(sample_text, pad=True) * 100
    if predictions > 60:
        yourmood = 'You are very positive!'
    elif predictions > 30:
        yourmood = 'You are very neutral!'
    else:
        yourmood = 'Someone is having a bad day...'

    return render_template("mood.html", yourmood=yourmood)
