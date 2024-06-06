from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import time


app = Flask(__name__)
CORS(app)  # Enable CORS

# Load a pre-trained model and tokenizer
gemini_api_key = 'AIzaSyANnRNEWUe5gdpw2KOK6piArkOPT2MQe_Y'
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-pro')

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]
safety_settings=safety_settings


template = """You are given a set of data about various employees. Your role is to answer any questions based on this information and output the answer only without adding any additional information. If the information doesn't exist in the provided data you should output 'No result / Unknown' result . Below is the provided data:

{
    "Kayla": {
        "role": "Project Manager",
        "experience": 10,
        "contractor": true
    },
    "Beneil": {
        "role": "Project Manager",
        "experience": 20,
        "contractor": false
    },
    "Miesha": {
        "role": "Diversity and Inclusiveness Researcher",
        "experience": 10,
        "contractor": false
    },
    "Israel": {
        "role": "Diversity and Inclusiveness Researcher",
        "experience": 20,
        "contractor": true
    }
}

Question:

"""

def get_answer(question):
    final_temp = template + question + "\nThink step by step and then output the answers in a list."
    try:
        response = model.generate_content(final_temp)
        time.sleep(1)
        
        temp2 = f"Given the output, get the final answer only in a list.\nThe output:\n{response.text}"
        feedback = model.generate_content(temp2)
        
        return feedback.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data['question']
    answer = get_answer(question)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)