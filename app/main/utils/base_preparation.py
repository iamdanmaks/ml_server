from .. import nlp
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences


def sentence_tokenizer(text):
    doc = nlp(text)
    return [str(s) for s in list(doc.sents)]


def prepare_sentences(sentences, tokenizer, max_len, 
                        ordinary_tokenizer=True, bert=True):
    if not ordinary_tokenizer:
        token_lists = [
            ['[CLS]'] + tokenizer.tokenize(sent) + ['[SEP]'] \
                for sent in sentences
        ]
        token_lists = [
            tokenizer.convert_tokens_to_ids(lst) for lst in token_lists
        ]
    else:
        token_lists = [tokenizer.tokenize(sent) for sent in sentences]

    token_lists = pad_sequences(token_lists,
                          maxlen=max_len, dtype="long", 
                          truncating="post", padding="post")
    
    if bert:
        attention_masks = np.array(
            [
                [
                    int(i>0) for i in lst
                ] for lst in token_lists
            ]
        )
        segments_ids = np.array(
            [
                [0] * len(lst) for lst in token_lists
            ]
        )
        segments_ids = np.array(
            [[0] * len(input_id) for input_id in token_lists]
        )
        return token_lists, attention_masks, segments_ids
    
    return token_lists
