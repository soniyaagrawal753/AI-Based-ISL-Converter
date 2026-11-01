# AI-Based Indian Sign Language Converter

## About the Project

The AI-Based Indian Sign Language (ISL) Converter is an AI-powered web application designed to help bridge the communication gap between hearing-impaired individuals and people unfamiliar with Indian Sign Language.

The application allows users to upload sign language videos, which are processed using an AI-powered backend to generate corresponding text interpretations.

## Features

* Video upload functionality.
* AI-powered sign language interpretation.
* FastAPI-based backend processing.
* Interactive Gradio frontend.
* Integration with Google Gemini API.
* Text-based interpretation of uploaded sign language videos.

## Technologies Used

* Python
* FastAPI
* Gradio
* Google Gemini API
* Uvicorn
* REST API

## System Architecture

The application follows this workflow:

1. User uploads an ISL video through the Gradio interface.
2. Gradio sends the video to the FastAPI backend.
3. FastAPI processes the request through its prediction endpoint.
4. The backend integrates with the Google Gemini API for AI-based interpretation.
5. The generated text interpretation is returned to the frontend.
6. The user views the result.

**Workflow:**

Video Upload → Gradio Frontend → FastAPI Backend → Gemini API → Text Interpretation

## Application Screenshots

### Home Page

![ISL Application](screenshots/Screenshot%20\(1\).png)

### Application Interface

![ISL Interface](screenshots/Screenshot%202026-11-01110344.png)

## Project Structure

```text
sign_language_mediator/
│
├── backend/
│   ├── main.py
│   ├── model.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── screenshots/
├── .gitignore
├── run_project.bat
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd sign_language_mediator
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Environment

Windows:

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

Install the backend and frontend dependencies:

```bash
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```

### 6. Configure API Key

Create a `.env` file and add your Google Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Never upload your API key to GitHub.

### 7. Run the Application

Run the `run_project.bat` file to start the backend and frontend.

## Future Enhancements

* Improve sign interpretation accuracy.
* Expand support for different ISL gestures.
* Explore real-time sign language interpretation.
* Enhance the user interface and accessibility.

## Author

Developed as an AI-based academic project focused on improving communication accessibility through technology.
