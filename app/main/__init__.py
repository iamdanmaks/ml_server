import spacy

from flask_cors import CORS
from flask_babel import Babel
from flask import Flask
from flask import request

from .config import config_by_name
from .utils.load_objects import load


cors = CORS(resources={r"/api/*": {"origins": "*"}})
babel = Babel()
nlp = spacy.load('en_core_web_sm')
ner_model, ner_tokenizer, ner_idx2tag = load('ner')


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    cors.init_app(app)
    babel.init_app(app)

    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(app.config['LANGUAGES'].keys())
    
    return app
