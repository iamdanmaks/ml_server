from flask import request
from flask_restplus import Resource

from ..service.entity_service import find_entities
from ..utils.dto.ner_dto import NerDto


api = NerDto.api
_ner = NerDto.ner


@api.route('/')
class Ner(Resource):
    @api.response(200, 'NERs are found.')
    @api.doc('find ners')
    @api.expect(_ner, validate=True)
    def post(self):
        return find_entities(
            request.json.get('text')
        )
