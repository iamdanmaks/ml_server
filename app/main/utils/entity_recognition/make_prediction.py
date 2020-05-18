import numpy as np

from app.main import ner_model


def predict(prepared):
    return np.argmax(
        ner_model.predict(
            [prepared[0], prepared[1], prepared[2]]
        ), 
        axis=-1
    )
