import logging
from pathlib import Path

# TODO : décommenter la ligne d'en dessous et supprimer les 3 classes provisoires
# from transformers import T5Tokenizer, T5ForConditionalGeneration

# TODO : implémenter la logique de gestion des modèles

LOGGER = logging.getLogger(__name__)

MODELS_DIR = Path("models")
SUMMARY_MODEL_PATH = MODELS_DIR / "summary_model.pkl"
CHATBOT_MODEL_PATH = MODELS_DIR / "chatbot_model.pkl"


# CLASSES PROVISOIRES
class T5:
    def from_pretrained(self, path):
        pass


class T5ForConditionalGeneration(T5):
    pass


class T5Tokenizer(T5):
    pass


# Abstract class
class BaseT5ModelManager:
    MODEL_PATH = None

    def __init__(self):
        self._model = None
        self._tokenizer = None

    def generate(self, text, *args):
        raise NotImplementedError("generate() must be overridden in the subclass!")

    @property
    def model(self):
        if self.MODEL_PATH is None:
            raise NotImplementedError("Class attribute 'MODEL_PATH' must be overriden in the subclass!")
        if self._model is None:
            model = T5ForConditionalGeneration.from_pretrained(self.MODEL_PATH)
            return model
        else:
            return self._model

    @property
    def tokenizer(self):
        if self.MODEL_PATH is None:
            raise NotImplementedError("Class attribute 'MODEL_PATH' must be overriden in the subclass!")
        if self._tokenizer is None:
            tokenizer = T5Tokenizer.from_pretrained(self.MODEL_PATH)
            return tokenizer
        else:
            return self._tokenizer


class SummaryModelManager(BaseT5ModelManager):
    MODEL_PATH = SUMMARY_MODEL_PATH

    def generate(self, text, *args):
        LOGGER.debug(f"{self.__class__.__name__}.generate()")
        # TODO : implémenter génération de résumé
        return "Résumé généré"


class ChatBotModelManager(BaseT5ModelManager):
    MODEL_PATH = CHATBOT_MODEL_PATH

    def generate(self, text, *args):
        LOGGER.debug(f"{self.__class__.__name__}.generate()")
        question = args[0]
        # TODO : implémenter génération de réponse
        return "Réponse générée"


class ModelsManager:
    def __init__(self):
        self.summary = SummaryModelManager()
        self.chat_bot = ChatBotModelManager()

    def generate_summary(self, text):
        LOGGER.debug(f"{self.__class__.__name__}.generate_summary()")
        return self.summary.generate(text)

    def generate_answer(self, text, question):
        LOGGER.debug(f"{self.__class__.__name__}.generate_answer()")
        return self.chat_bot.generate(text, question)
