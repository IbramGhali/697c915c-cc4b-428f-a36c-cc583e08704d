from flask import Flask, request, jsonify

app = Flask(__name__)

knowledge_base = {
    "project_manager": [
        {"name": "Kayla", "experience": 10, "contractor": True},
        {"name": "Beneil", "experience": 20, "contractor": False}
    ],
    "diversity_inclusiveness_researcher": [
        {"name": "Miesha", "experience": 10, "contractor": False},
        {"name": "Israel", "experience": 20, "contractor": True}
    ]
}

def find_people(criteria):
    results = []
    for role, people in knowledge_base.items():
        for person in people:
            if all(person.get(k) == v or (isinstance(v, list) and person.get(k) in v) for k, v in criteria.items()):
                results.append(person["name"])
    return results

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data['question'].lower()
    
    criteria = {}
    if "project manager" in question:
        criteria["role"] = ["project_manager"]
    if "diversity and inclusiveness researcher" in question:
        criteria["role"] = ["diversity_inclusiveness_researcher"]
    if "more than 15 years" in question:
        criteria["experience"] = range(16, 100)
    if "contractor" in question:
        criteria["contractor"] = True

    results = find_people(criteria)
    return jsonify({"answer": ", ".join(results) if results else "No result / Unknown"})

if __name__ == '__main__':
    app.run(debug=True)
