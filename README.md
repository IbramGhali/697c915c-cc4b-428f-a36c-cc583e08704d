
# Chatbot for DemoCo

This project is a chatbot that can be embedded on any web page. The chatbot answers questions about the people working at DemoCo, a fictitious company, based on a provided knowledge base. The chatbot uses a front end built with HTML, CSS, and JavaScript, and a back end built with Python and Flask. The chatbot's Q&A functionality is powered by an open-source Language Model (LLM) from Hugging Face Transformers.

## Table of Contents
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Known Issues](#known-issues)
- [Future Improvements](#future-improvements)
- [Contact](#contact)

## Project Structure
```
/chatbot-project
├── backend
│   ├── app.py
│   ├── requirements.txt
├── frontend
│   ├── index.html
│   ├── style.css
│   ├── script.js
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
git clone https://github.com/your-repo/chatbot-project.git
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

## Known Issues
- The model's responses are based on a simple knowledge base and may not cover all possible user queries.
- The Flask server must be running locally; deployment to a production server is not covered in this README.

## Future Improvements
- Improve the NLP pipeline for better question understanding and response accuracy.
- Enhance the frontend UI for a better user experience.
- Deploy the application to a cloud platform (e.g., Heroku, AWS).

## Contact
For any questions or issues, please contact support@advaise.app.

```

This `README.md` file provides a comprehensive guide to setting up, running, and using the chatbot application. It also includes sections for known issues and future improvements, making it easy for others to understand and contribute to the project.
