from src.database.db import db
from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]  # Definindo o nome da coleção

    def __init__(self, data):
        super().__init__(data)

    def to_dict(self):
        return {
            "name": self.data.get("name"),
            "acronym": self.data.get("acronym"),
        }

    @classmethod
    def list_dicts(cls):
        languages = cls.find()
        return [language.to_dict() for language in languages]
