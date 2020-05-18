import pickle

from transformers import TFBertForTokenClassification


def load(name):
    try:
        with open(f'./app/main/models/utils/{name}_idx2tag.pickle', 'rb') as handle:
            idx2tag = pickle.load(handle)
    except FileNotFoundError:
        idx2tag = None

    if name == 'ner':
        model = TFBertForTokenClassification.from_pretrained(
            'bert-base-uncased', 
            num_labels=len(idx2tag) 
        )
    
    with open(f'./app/main/models/weights/{name}.pickle', 'rb') as handle:
        model.set_weights(pickle.load(handle))
    
    with open(f'./app/main/models/tokenizers/{name}.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    
    return model, tokenizer, idx2tag
