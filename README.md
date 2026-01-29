# SmartAssess - An  intelligent Assessment Recommendation System

An intelligent assessment recommendation platform that matches skills and job requirements to the perfect assessments using AI and semantic search.

## 🎯 Features

- **Skill-Based Matching** — Recommends assessments based on technical and soft skills
- **Job Description Analysis** — Extracts skills from job postings and suggests relevant assessments
- **AI-Powered Analysis** — Uses Google Gemini to understand job requirements and skills
- **Semantic Search** — FAISS + sentence-transformers for intelligent similarity matching
- **User Authentication** — Secure login and signup system with MySQL database
- **Professional UI** — Modern, responsive frontend with smooth animations
- **Fast Performance** — Millisecond-level recommendation generation

## 🛠️ Tech Stack

### Backend
- **FastAPI** — High-performance API for recommendations
- **Flask** — Web framework for user authentication and pages
- **Google Gemini API** — Large language model for skill extraction and analysis
- **Sentence Transformers** — `all-MiniLM-L6-v2` for semantic embeddings
- **FAISS** — Vector similarity search and indexing
- **MySQL** — User and assessment data storage

### Frontend
- **HTML5 / CSS3** — Semantic markup with modern styling
- **JavaScript** — Interactive features and API integration
- **Responsive Design** — Mobile-first, works on all devices

## 📋 Prerequisites

- Python 3.10+ (3.11+ recommended)
- MySQL Server
- Virtual environment tool (venv or conda)
- Internet connection (for Hugging Face model downloads)

## 🚀 Quick Start

### 1. Clone and Setup

```bash
cd Assignment-recomendation-System-main
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file or set environment variables:

```bash
set GEMINI_API_KEY=your_google_gemini_api_key
set EMBED_MODEL_PATH=all-MiniLM-L6-v2  # Optional: local path to model
```

### 3. Database Setup

Create MySQL database and tables (see `SETUP_GUIDE.md`):

```bash
mysql -u root -p < setup.sql
```

### 4. Start the Application

**Terminal 1 - API Server** (recommendations):
```bash
uvicorn api.main:app --host 127.0.0.1 --port 8000 --reload
```

**Terminal 2 - Web Server** (auth & UI):
```bash
python app.py
```

### 5. Access the App

- Homepage: http://127.0.0.1:5000
- API Docs: http://127.0.0.1:8000/docs
- Sign Up: http://127.0.0.1:5000/signup
- Login: http://127.0.0.1:5000/login
- Recommendations: http://127.0.0.1:5000/recommend-page (after login)

## 📁 Project Structure

```
├── api/
│   ├── main.py                 # FastAPI recommendation engine
│   └── __init__.py
├── frontend/
│   ├── index.html              # Homepage
│   ├── login.html              # Login page
│   ├── login-error.html        # Login error page
│   ├── signup.html             # Signup page
│   └── recommend.html          # Recommendations page
├── static/
│   ├── style.css               # Global styles + animations
│   └── images/                 # Background images
├── embeddings/
│   ├── build_index.py          # FAISS index builder
│   ├── prepare_data.py         # Data preparation
│   └── faiss.index             # Vector search index
├── data/
│   ├── shl_catalog.csv         # Assessment catalog
│   └── shl_catalog_clean.csv   # Cleaned version
├── app.py                      # Flask web server
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## ⚙️ Configuration

### Google Gemini API

1. Get API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Set environment variable:
   ```bash
   set GEMINI_API_KEY=your_key_here
   ```

### Database Connection

Edit `app.py` to match your MySQL setup:
```python
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="smartassess"
    )
```

### Embedding Model

By default uses `all-MiniLM-L6-v2` from Hugging Face. For offline use:

```bash
set EMBED_MODEL_PATH=C:\path\to\local\model
```

## 🔧 Troubleshooting

### "Failed to load embedding model" Error

**Cause:** Network connection issue downloading from Hugging Face

**Solutions:**
1. Check internet connection
2. If behind proxy, set environment variables:
   ```bash
   set HTTP_PROXY=http://proxy:port
   set HTTPS_PROXY=http://proxy:port
   ```
3. Download model offline and set `EMBED_MODEL_PATH`

### Python Version Warning

Current setup uses Python 3.10.11. Google deprecates support in Oct 2026.

**Recommendation:** Upgrade to Python 3.11+
```bash
# Recreate venv with new Python version
python -m venv venv --upgrade
```

### Deprecated google.generativeai

Current version uses deprecated `google.generativeai`. To upgrade to `google-genai`:

```bash
pip install --upgrade google-genai
```

Then update `api/main.py`:
```python
# Old
import google.generativeai as genai

# New
import google.genai as genai
```

### Invalid Login Credentials

Shows professional error page (`login-error.html`) instead of plain text.

## 📊 How It Works

### Recommendation Flow

1. **User Input** — Job description or skill list
2. **Gemini Analysis** — Extracts technical/soft skills and focus area
3. **Embedding** — Query converted to vector using sentence-transformers
4. **FAISS Search** — Find top 20 similar assessments
5. **Re-ranking** — Sort by focus (Knowledge, Practical, Assessment mix)
6. **Response** — Return top 10 assessments with details

### Data Pipeline

1. `prepare_data.py` — Cleans assessment catalog
2. `build_index.py` — Creates FAISS vector index
3. `api/main.py` — Loads index and handles requests

## 🎨 UI/UX Features

- **Smooth Animations** — Hover effects, entrance animations, micro-interactions
- **Responsive Grid** — 3-column feature cards, adapts to mobile
- **Dark Theme** — Modern dark mode with accent orange colors
- **Blurred Background** — Aesthetic depth with 40px blur effect
- **Professional Error Handling** — Beautiful error pages with guidance
- **Accessible Forms** — Proper labels, validation, autofocus

## 📚 API Endpoints

### FastAPI (Port 8000)

- `GET /health` — Server health check
- `POST /recommend` — Get recommendations (body: `{"query": "..."}`)

### Flask (Port 5000)

- `GET /` — Homepage
- `GET/POST /signup` — User registration
- `GET/POST /login` — User authentication
- `GET /recommend-page` — Recommendation interface
- `GET /logout` — User logout

## 🔐 Security Notes

⚠️ **Current Implementation:**
- Passwords stored in plain text (demo only!)
- Secret key hardcoded (change in production)
- CORS enabled for all origins

**For Production:**
- Hash passwords with bcrypt/argon2
- Use environment variables for secrets
- Implement proper CORS policy
- Add rate limiting
- Use HTTPS

## 📝 License

[Add your license here]

## 👤 Author

Created as an AI-powered assessment recommendation system for efficient recruiter and student workflows.

## 🤝 Contributing

[Add contribution guidelines here]

## 📞 Support

For issues or questions:
1. Check troubleshooting section above
2. Review `SETUP_GUIDE.md`
3. Verify all environment variables are set
4. Check database connection

---

**Last Updated:** January 2026  
**Python:** 3.10.11+ (3.11+ recommended)  
**Status:** Active Development
