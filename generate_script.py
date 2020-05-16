from fastai.text import *
from fastai import *

learner = load_learner(path = '.',file="script.pkl")

TEXT = ""
n_words = 20000
print(learner.predict(TEXT,n_words=n_words))