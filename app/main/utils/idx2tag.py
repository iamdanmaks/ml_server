def prepare_output(predictions, idx2tag_vocab):
    predictions_tags = [
        [
            idx2tag_vocab[i] for i in row
        ] for row in predictions[0]
    ]
    
    predictions_tags = [
        pred[1:pred.index('[SEP]')] for pred in predictions_tags
    ]
    
    for pred in predictions_tags:
        for i in range(len(pred)):
            if pred[i] != 'O' and pred[i] != 'X' \
                and pred[i] != '[SEP]' and pred[i] != '[CLS]':
                pred[i] = pred[i][2:]

    return predictions_tags
