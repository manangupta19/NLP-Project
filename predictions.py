import pandas as pd
import numpy as np
import joblib

def counts(df):

    loaded_vec = joblib.load('vectorizer.sav')
    loaded_model = joblib.load('model.sav')

    vec = loaded_vec.transform(df['comment'])

    preds = loaded_model.predict(vec)

    neg = np.count_nonzero((preds==0)|(preds==1))
    neu = np.count_nonzero(preds==2)
    pos = np.count_nonzero((preds==3)|(preds==4))

    return neg,neu,pos
