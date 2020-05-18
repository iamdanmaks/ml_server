from flask_restplus import Namespace, fields


class NerDto:
    api = Namespace('ner', description='NER related operations')
    ner = api.model('ner_details', {
        'text': fields.String(required=True, description='Text for named entities recognition'),
    })
