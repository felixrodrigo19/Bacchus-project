import os
import pickle

import numpy as np
from flask import Blueprint, render_template, request


class SiteBP(Blueprint):
    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        self.vocabulary = None
        self.model = None
        self.load_model()

    def load_model(self):
        vocab_path = os.path.abspath("bacchus/ext/site/resources/vocabulary.pkl")
        model_path = os.path.abspath("bacchus/ext/site/resources/model_adaboost.pkl")

        with open(vocab_path, "rb") as file:
            self.vocabulary = pickle.load(file)

        with open(model_path, "rb") as file:
            self.model = pickle.load(file)

    def count_words(self, text):
        frequency = [0] * len(self.vocabulary)

        for word in text:
            if word in self.vocabulary:
                position = self.vocabulary[word]
                frequency[position] += 1
        return frequency

    def predict_band(self, new_lyric):
        new_word = new_lyric.lower().split()
        new_freq = self.count_words(new_word)
        x = np.array(new_freq).reshape(1, -1)

        if self.model.predict(x) == 1:
            return "The Beatles"
        else:
            return "The Rolling Stones"

    @staticmethod
    def home():
        return render_template("main.html")

    @staticmethod
    def band_search():
        return render_template("bands.html")

    def music(self):
        new_lyric = request.values["trecho"]
        banda = self.predict_band(new_lyric)
        return render_template("musics.html", banda=banda)


site_bp = SiteBP("site", __name__)

site_bp.add_url_rule("/", view_func=site_bp.home)
site_bp.add_url_rule("/search", view_func=site_bp.band_search)
site_bp.add_url_rule("/banda", view_func=site_bp.music, methods=["POST"])
