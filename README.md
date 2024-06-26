
# Chatbot for DemoCo

This project is a chatbot that can be embedded on any web page. The chatbot answers questions about the people working at DemoCo, a fictitious company, based on a provided knowledge base. The chatbot uses a front end built with HTML, CSS, and JavaScript, and a back end built with Python and Flask. The chatbot's Q&A functionality is powered by Google's Generative AI model.

## Table of Contents
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Example Questions](#example-questions)
- [Refining the Response](#refining-the-response)
- [Known Issues](#known-issues)
- [Future Improvements](#future-improvements)
- [Contact](#contact)

## Project Structure

```
chatbot-project
├── backend
│ ├── app.py
│ ├── requirements.txt
├── frontend
│ ├── index.html
│ ├── style.css
│ ├── script.js
├── README.md
├── .gitignore
```


## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- A modern web browser (Chrome, Firefox, etc.)

### Clone the Repository
Clone the repository created for you by Advaise Pty Ltd:
```bash
git clone https://github.com/IbramGhali/697c915c-cc4b-428f-a36c-cc583e08704d.git
cd chatbot-project

```

### Set Up the Backend

1. Navigate to the `backend` directory:
    ```bash
    cd backend
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Set Up the Frontend

No additional setup is needed for the frontend. The HTML, CSS, and JavaScript files are ready to use.

## How to Run

### Running the Backend
1. Ensure you are in the `backend` directory and the virtual environment is activated.
2. Start the Flask server:
    ```bash
    python app.py
    ```

The Flask server should be running at `http://localhost:5000`.

### Running the Frontend
1. Open `frontend/index.html` in your web browser.

## Usage
1. Enter a question about DemoCo staff in the input field and click the "Send" button.
2. The chatbot will display the user's question and provide a response based on the knowledge base.

### Example Questions:
- "Who are the project managers?"
- "Find people who are diversity and inclusiveness researchers with more than 15 years of experience."
## Refining the Response
### Problem
Current large language models (LLMs) lack standardized evaluation metrics due to their inconsistent responses. Although significant research has aimed to define universal evaluation metrics on benchmarks (e.g.,[MMLU](https://arxiv.org/abs/2009.03300), [Hallswag](https://arxiv.org/abs/1905.07830)), we observed inconsistencies in LLM outputs and were unable to achieve universally consistent results. To address this, we implemented a self-refinement approach, providing feedback that improved the model's performance.
## Solution
Inspired by the iterative refinement process described in the paper SELF-REFINE: Iterative Refinement with Self-Feedback by Madaan et al. (2023), we implemented a similar approach to improve our response generation.
## Approach
1. Initial Generation: The language model generates an initial output.
2. Feedback Loop: The same model provides feedback on its output, highlighting areas for improvement.
3. Refinement: The model uses this feedback to refine the output iteratively until a satisfactory result is achieved.
### Example
For code optimization, an initial solution is generated, followed by feedback emphasizing efficiency improvements, such as reducing time complexity. This feedback is then used to iteratively refine the code, resulting in a more optimized solution.
### Benefits
- Increased Relevance: Outputs are more aligned with user expectations.
- Higher Quality: Refinement leads to more polished and accurate results.
- Scalability: This approach is versatile and can be applied to various tasks without additional training data or supervision.
### Reference
[Madaan, A., et al.](https://arxiv.org/abs/2303.17651)
## Known Issues
- The model's responses are based on a simple knowledge base and may not cover all possible user queries.
- The Flask server must be running locally; deployment to a production server is not covered in this README.

## Future Improvements
- Explore Advanced Approaches: Investigate and implement advanced techniques and methodologies to further improve the model’s accuracy and consistency in generating responses. This includes leveraging state-of-the-art NLP models, fine-tuning with domain-specific data, and incorporating feedback loops similar to the iterative refinement process..
- Cloud Deployment: Deploy the application to a reliable cloud platform such as Heroku or AWS to ensure scalability, reliability, and ease of access. This will also facilitate continuous integration and deployment (CI/CD) practices, enabling seamless updates and improvements.

## Contact
For any questions or issues, please contact support@advaise.app.


