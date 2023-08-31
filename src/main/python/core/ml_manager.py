import logging
import pickle
from pathlib import Path


# TODO : implémenter la logique de gestion des modèles

LOGGER = logging.getLogger(__name__)

MODELS_DIR = Path("models")
SUMMARY_MODEL_PATH = MODELS_DIR / "summary_model.pkl"
CHATBOT_MODEL_PATH = MODELS_DIR / "chatbot_model.pkl"


class BaseModelManager:
    def __init__(self, model_path, text):
        # TODO : remplacer la ligne suivante par celle commentée
        self.model = None
        # self.model = self.load_model(model_path)
        self.context = self.preprocess(text)

    def preprocess(self, text):
        raise NotImplementedError("preprocess() must be overridden in the subclass!")

    def generate(self):
        raise NotImplementedError("generate() must be overridden in the subclass!")

    @staticmethod
    def load_model(model_path):
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        return model


class SummaryModelManager(BaseModelManager):
    def __init__(self, text):
        super().__init__(SUMMARY_MODEL_PATH, text)

    def preprocess(self, text):
        LOGGER.debug(f"{self.__class__.__name__}.preprocess()")
        # TODO : ajouter la pipeline ici
        return text

    def generate(self):
        LOGGER.debug(f"{self.__class__.__name__}.generate()")
        # TODO : implémenter génération de résumé
        return "Résumé généré"


class ChatBotModelManager(BaseModelManager):
    def __init__(self, text):
        super().__init__(CHATBOT_MODEL_PATH, text)

    def preprocess(self, text):
        LOGGER.debug(f"{self.__class__.__name__}.preprocess()")
        # TODO : ajouter la pipeline ici
        return text

    def generate(self, question):
        LOGGER.debug(f"{self.__class__.__name__}.generate()")
        # TODO : implémenter génération de réponse
        return "Réponse générée"


class ModelsManager:
    def __init__(self, text):
        self.summary = SummaryModelManager(text)
        self.chat_bot = ChatBotModelManager(text)

    def generate_summary(self):
        LOGGER.debug(f"{self.__class__.__name__}.generate_summary()")
        return self.summary.generate()

    def generate_answer(self, question):
        LOGGER.debug(f"{self.__class__.__name__}.generate_answer()")
        return self.chat_bot.generate(question)
