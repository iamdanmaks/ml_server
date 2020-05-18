from cachetools import cached, LRUCache

from .. import ner_tokenizer
from .. import ner_model
from .. import ner_idx2tag

from ..utils.base_preparation import sentence_tokenizer
from ..utils.base_preparation import prepare_sentences
from ..utils.idx2tag import prepare_output
from ..utils.entity_recognition.make_prediction import predict


MAX_LEN = 80

@cached(cache=LRUCache(maxsize=32))
def find_entities(text):
    sentences = sentence_tokenizer(text)
    sentences = prepare_sentences(
        sentences, 
        ner_tokenizer, 
        MAX_LEN, 
        ordinary_tokenizer=False, 
        bert=True
    )
    
    predictions = prepare_output(
        predict(sentences), 
        ner_idx2tag
    )

    response_object = {
        'status': 'success',
        'result': predictions
    }

    return response_object, 200
