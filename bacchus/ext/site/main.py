from flask import abort
from flask import Blueprint
from flask import jsonify
from flask import render_template
from flask import request
from flask import redirect
import numpy as np
import pickle
import os


bp = Blueprint("site", __name__)


def count_words(text, vocabulary):
    frequency = [0] * len(vocabulary)

    for word in text:
        if word in vocabulary:
            position = vocabulary[word]
            frequency[position] += 1
    return frequency


@bp.route('/')
def home():
   return render_template("main.html")


@bp.route('/search')
def band_search():
    return render_template("bands.html")


@bp.route("/banda", methods=["POST"])
def music(banda=None):
    vocab = os.path.abspath('bacchus/ext/site/resources/vocabulary.pkl')
    mdl = os.path.abspath('bacchus/ext/site/resources/model_adaboost.pkl')

    with open(vocab, 'rb') as file:
        vocabulary = pickle.load(file)


    with open(mdl, 'rb') as file:
        model = pickle.load(file)
    

    new_lyric = request.values["trecho"]
    new_word = new_lyric.lower().split()
    new_freq = count_words(new_word, vocabulary)

    x = np.array(new_freq).reshape(1, -1)
    if model.predict(x) == 1:
        banda = "The Beatles"
    else:
        banda = "The Rolling Stones"

    return render_template("musics.html",banda=banda)