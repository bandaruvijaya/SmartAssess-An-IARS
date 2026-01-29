# SmartAssess - Frontend & Backend Connection Guide

## Architecture Overview

The system now has **two separate servers**:
- **Flask Server** (app.py): Handles authentication, login, signup, and serves HTML templates
- **FastAPI Server** (api/main.py): Handles the AI-powered assessment recommendation engine

The frontend JavaScript communicates with the FastAPI server for recommendations.

## Prerequisites

Make sure you have installed all requirements:
```bash
pip install -r requirements.txt
```

You'll also need:
- A Gemini API key set in your environment variables
- MySQL database running (for user authentication)

## Running the System

### Step 1: Set Environment Variables

Before starting, set your Gemini API key:

**On Windows PowerShell:**
```powershell
$env:GEMINI_API_KEY = "your-gemini-api-key-here"
```

**Or add it to your system environment variables permanently**

### Step 2: Start the FastAPI Server

Open a terminal and run:
```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Step 3: Start the Flask Server (in a new terminal)

```bash
python app.py
```

You should see:
```
Running on http://127.0.0.1:5000
```

## Testing the Connection

1. Open your browser and go to: `http://localhost:5000`
2. Sign up or login
3. Navigate to the recommendations page
4. Enter a job description or skills
5. Click "Get Recommendations"

The frontend will automatically call the FastAPI server at `http://localhost:8000/recommend`

## API Endpoints

### FastAPI (Port 8000)
- **GET** `/health` - Health check
- **POST** `/recommend` - Get assessment recommendations
  - Request body: `{"query": "job description or skills"}`
  - Returns: List of recommended assessments with URLs

### Flask (Port 5000)
- **GET** `/` - Landing page
- **GET/POST** `/signup` - User registration
- **GET/POST** `/login` - User login
- **GET** `/recommend-page` - Recommendation interface (requires login)
- **GET** `/logout` - Logout

## Troubleshooting

### Error: "Failed to connect to FastAPI"
- Make sure the FastAPI server is running on port 8000
- Check that CORS is enabled (it should be in the updated api/main.py)
- Check browser console (F12) for detailed error messages

### Error: "Empty query"
- Make sure you've entered text in the query field before submitting

### Error: "GEMINI_API_KEY not set"
- Set your environment variable before starting the FastAPI server

## File Changes Made

- **api/main.py**: Added CORS middleware for frontend communication
- **frontend/recommend.html**: Converted to JavaScript-based API calls instead of form submission
- **app.py**: Removed conflicting `/recommend` POST route (now handled by FastAPI)

## Notes

- The FAISS index and embeddings must be pre-built (see `embeddings/` folder)
- Make sure your data files are in the `data/` folder
- Frontend files are served by Flask from the `frontend/` folder
- The system uses Sentence Transformers for embeddings and Gemini AI for query analysis
