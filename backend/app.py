from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load a pre-trained model and tokenizer
nlp = pipeline("question-answering")

knowledge_base = {
    "Kayla": {"role": "Project Manager", "experience": 10, "contractor": True},
    "Beneil": {"role": "Project Manager", "experience": 20, "contractor": False},
    "Miesha": {"role": "Diversity and Inclusiveness Researcher", "experience": 10, "contractor": False},
    "Israel": {"role": "Diversity and Inclusiveness Researcher", "experience": 20, "contractor": True},
}

def get_answer(question):
    context = " ".join([f"{name} is a {info['role']} with {info['experience']} years of experience. {'They are a contractor.' if info['contractor'] else 'They are not a contractor.'}" for name, info in knowledge_base.items()])
    result = nlp(question=question, context=context)
    return result['answer']

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data['question']
    answer = get_answer(question)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
