from flask import Flask, jsonify, request

from ml_manager import ModelsManager

class APIServer:
    def __init__(self, host, port):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self._setup_routes()
        self.models_manager = ModelsManager()

    def _setup_routes(self):
        @self.app.route('/summarize', methods=['POST'])
        def summarize():
            data = request.get_json()
            text = data['text']
            response = self.models_manager.generate_summary(text)
            return jsonify({"response": response})

        @self.app.route('/answer', methods=['POST'])
        def answer():
            data = request.get_json()
            text = data['text']
            question = data["question"]
            response = self.models_manager.generate_answer(text, question)
            return jsonify({"response": response})

    def run(self):
        self.app.run(host=self.host, port=self.port)

if __name__ == "__main__":
    server = APIServer('127.0.0.1', 65432)
    server.run()