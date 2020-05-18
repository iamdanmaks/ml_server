from flask_restplus import Api
from flask import Blueprint

from .main.controller.entity_controller import api as ner_ns


blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Deep NLP',
    version='1.0',
    description='Documentation for Deep NLP API'
)

api.add_namespace(ner_ns, path='/api/ner')
