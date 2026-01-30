# SmartAssess - An Intelligent Assessment Recommendation System

An AI-powered platform that intelligently matches job requirements and skills to the most relevant assessments. Built with semantic search, LLM analysis, and modern full-stack technologies.

## ✨ Features

- **🎯 Skill-Based Matching** — Recommends assessments based on technical and soft skills
- **📝 Job Description Analysis** — Extracts skills from job postings and suggests relevant assessments
- **🤖 AI-Powered Analysis** — Uses Google Gemini API to understand job requirements and skills
- **🔍 Semantic Search** — FAISS vector database + sentence-transformers for intelligent similarity matching
- **🔐 User Authentication** — Secure login and signup with MySQL database
- **🎨 Professional UI** — Modern, responsive frontend with smooth animations and dark theme
- **⚡ Fast Performance** — Millisecond-level recommendation generation

## 🛠️ Technology Stack

### Backend
- **FastAPI** — High-performance async API framework for recommendations
- **Flask** — Lightweight framework for authentication and web pages
- **Google Gemini API** — LLM for intelligent skill extraction and analysis
- **Sentence Transformers** — `all-MiniLM-L6-v2` model for semantic embeddings
- **FAISS** — Facebook's vector similarity search library for fast indexing
- **MySQL** — Relational database for user and assessment data

### Frontend
- **HTML5 / CSS3** — Semantic markup with modern, responsive styling
- **Vanilla JavaScript** — Interactive features and API integration
- **Responsive Design** — Mobile-first approach, works across all devices

### Infrastructure
- **Python 3.10+** — Core runtime environment
- **Virtual Environment** — Isolated Python dependencies
- **Docker-ready** — Includes Dockerfile for containerization

## 📋 Prerequisites

Before getting started, ensure you have:

- **Python 3.10+** (3.11+ recommended for better performance)
- **MySQL Server** (5.7+ or MariaDB equivalent)
- **Virtual environment tool** (venv or conda)
- **Internet connection** (for downloading AI models from Hugging Face)
- **Google Gemini API key** (free at [Google AI Studio](https://aistudio.google.com/app/apikey))

## 🚀 Quick Start Guide

### Step 1: Clone and Setup Environment

```bash
# Clone the repository
cd Assignment-recomendation-System-main

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Configure API Keys and Environment

Create a `.env` file in the root directory or set environment variables:

**On Windows PowerShell:**
```powershell
$env:GEMINI_API_KEY = "your_google_gemini_api_key_here"
```

**Or on Windows CMD:**
```bash
set GEMINI_API_KEY=your_google_gemini_api_key_here
```

**Optional - For offline embedding model:**
```bash
set EMBED_MODEL_PATH=all-MiniLM-L6-v2  # or path to local model
```

### Step 3: Setup MySQL Database

Ensure MySQL is running, then create the database and tables:

```bash
# Using MySQL command line
mysql -u root -p < setup.sql
```

Or manually create the database:
```sql
CREATE DATABASE smartassess;
USE smartassess;
-- Add table definitions as needed
```

**Update database credentials in `app.py`:**
```python
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="smartassess"
    )
```

### Step 4: Start the Application

Open **two separate terminal windows**:

**Terminal 1 - Start FastAPI Server** (recommendations engine):
```bash
uvicorn api.main:app --host 127.0.0.1 --port 8000 --reload
```
You should see: `INFO: Uvicorn running on http://127.0.0.1:8000`

**Terminal 2 - Start Flask Server** (web interface):
```bash
python app.py
```
You should see: `Running on http://127.0.0.1:5000`

### Step 5: Access the Application

- **Homepage:** http://127.0.0.1:5000
- **Sign Up:** http://127.0.0.1:5000/signup
- **Login:** http://127.0.0.1:5000/login
- **Recommendations:** http://127.0.0.1:5000/recommend-page (after login)
- **API Documentation:** http://127.0.0.1:8000/docs

## 📁 Project Structure

```
Assignment-recomendation-System-main/
│
├── app.py                          # Flask web server (auth, login, signup, UI)
├── requirements.txt                # Python package dependencies
├── Dockerfile                      # Docker container configuration
├── Procfile                        # Heroku/Railway deployment config
├── railway.json                    # Railway.app deployment config
├── SETUP_GUIDE.md                  # Detailed setup and configuration guide
├── RAILWAY_DEPLOYMENT.md           # Deployment instructions
│
├── api/
│   ├── main.py                     # FastAPI recommendation engine
│   ├── __init__.py
│   └── __pycache__/
│
├── frontend/
│   ├── index.html                  # Homepage
│   ├── login.html                  # User login page
│   ├── login-error.html            # Login error page
│   ├── signup.html                 # User registration page
│   └── recommend.html              # Recommendation results interface
│
├── static/
│   ├── style.css                   # Global styles and animations
│   └── images/                     # Background and UI images
│
├── embeddings/
│   ├── build_index.py              # FAISS index builder script
│   ├── prepare_data.py             # Data cleaning and preparation
│   └── faiss.index                 # Pre-built vector search index
│
├── data/
│   ├── shl_catalog.csv             # Assessment catalog (original)
│   ├── shl_catalog_raw.json        # Assessment data (raw format)
│   └── shl_catalog_clean.csv       # Assessment data (cleaned)
│
├── outputs/
│   ├── generate_predictions.py     # Prediction generation script
│   └── predictions.csv             # Output predictions
│
├── evaluation/
│   └── recall_at_10.py             # Model evaluation metrics
│
└── README.md                       # This file
```

## ⚙️ Configuration

### Google Gemini API Setup

1. **Get your API key:**
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create a new API key (free tier available)
   - Set it in environment variables

2. **Set environment variable:**
   ```powershell
   # Windows PowerShell
   $env:GEMINI_API_KEY = "your_api_key_here"
   ```
   ```bash
   # Windows CMD or Linux/Mac
   export GEMINI_API_KEY="your_api_key_here"
   ```

### MySQL Database Connection

Edit the `get_connection()` function in [app.py](app.py) to match your MySQL setup:

```python
def get_connection():
    return mysql.connector.connect(
        host="localhost",         # MySQL server address
        user="root",              # MySQL username
        password="your_password", # MySQL password
        database="smartassess"    # Database name
    )
```

### Embedding Model Configuration

**Default setup** uses `all-MiniLM-L6-v2` from Hugging Face (downloaded automatically on first run).

**For offline/local use:**
```bash
set EMBED_MODEL_PATH=C:\path\to\local\model
```

Or modify [api/main.py](api/main.py):
```python
model_path = os.getenv("EMBED_MODEL_PATH", "all-MiniLM-L6-v2")
model = SentenceTransformer(model_path)
```

## 🔧 Troubleshooting

### ❌ "Failed to load embedding model" Error

**Cause:** Network issue downloading the model from Hugging Face

**Solutions:**
1. Check your internet connection
2. If behind a proxy, set environment variables:
   ```powershell
   $env:HTTP_PROXY = "http://proxy.company.com:8080"
   $env:HTTPS_PROXY = "http://proxy.company.com:8080"
   ```
3. Download the model offline and set `EMBED_MODEL_PATH`
4. Try running again (may timeout on first attempt)

### ❌ Port Already in Use

**Error:** `Address already in use`

**Solution:**
```bash
# Find process using port 8000 (or 5000)
netstat -ano | findstr :8000

# Kill the process (replace PID with actual process ID)
taskkill /PID <PID> /F

# Or use different ports
uvicorn api.main:app --port 8001
python app.py --port 5001
```

### ❌ MySQL Connection Error

**Error:** `Access denied for user 'root'@'localhost'`

**Solutions:**
1. Verify MySQL is running:
   ```bash
   mysql -u root -p -e "SELECT 1"
   ```
2. Check credentials in [app.py](app.py)
3. Reset MySQL password if forgotten
4. Ensure database `smartassess` exists:
   ```bash
   mysql -u root -p -e "CREATE DATABASE smartassess;"
   ```

### ❌ Gemini API Error

**Error:** `API key not valid` or `Authentication failed`

**Solutions:**
1. Verify the API key is correct (copy from [Google AI Studio](https://aistudio.google.com/app/apikey))
2. Confirm environment variable is set:
   ```powershell
   # Check if set correctly
   $env:GEMINI_API_KEY
   ```
3. Ensure you have billing enabled (if applicable)
4. Check if API key has appropriate quotas/limits

### ❌ Python Version Warning

**Warning:** Python 3.10 deprecated in October 2026

**Recommendation:** Upgrade to Python 3.11+

```bash
# Upgrade existing venv
python -m venv venv --upgrade

# Or create new venv with newer Python
python3.11 -m venv venv
```

### ❌ ModuleNotFoundError

**Error:** `No module named 'fastapi'` or other package

**Solution:**
```bash
# Ensure virtual environment is activated
venv\Scripts\activate

# Reinstall all dependencies
pip install -r requirements.txt

# Check installation
pip list
```

## 📊 How the System Works

### Recommendation Engine Flow

The AI-powered recommendation system follows this pipeline:

```
User Input (Job Description / Skills)
         ↓
[Gemini API Analysis] - Extract technical & soft skills, identify focus area
         ↓
[Embedding Generation] - Convert query to vector using sentence-transformers
         ↓
[FAISS Vector Search] - Find top 20 most similar assessments from index
         ↓
[Re-ranking & Sorting] - Prioritize by skill alignment and focus area
         ↓
Response - Return top 10 recommended assessments with details
```

### Data Processing Pipeline

1. **Data Preparation** → [embeddings/prepare_data.py](embeddings/prepare_data.py)
   - Load assessment catalog (CSV/JSON)
   - Clean and standardize data
   - Extract assessment metadata

2. **Index Building** → [embeddings/build_index.py](embeddings/build_index.py)
   - Convert assessments to embeddings using sentence-transformers
   - Build FAISS vector index for fast similarity search
   - Save index for production use

3. **Runtime Recommendation** → [api/main.py](api/main.py)
   - Load pre-built FAISS index
   - Process user queries through Gemini API
   - Perform vector similarity search
   - Return ranked results

### Key Technologies in Action

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **LLM** | Google Gemini | Intelligent skill extraction and understanding |
| **Embeddings** | Sentence Transformers | Convert text to numerical vectors (384-dim) |
| **Search** | FAISS | Fast approximate nearest neighbor search |
| **API** | FastAPI | High-performance async recommendation engine |
| **Web** | Flask | Authentication and web interface |
| **Database** | MySQL | User profiles and session management |

## 🎨 UI/UX Highlights

- **🎭 Smooth Animations** — Hover effects, entrance animations, micro-interactions for engaging UX
- **📱 Responsive Layout** — Mobile-first design with adaptive grid system (3-column cards on desktop, single column on mobile)
- **🌙 Dark Theme** — Modern dark mode with orange accent colors for visual appeal
- **🌌 Aesthetic Effects** — Blurred background with depth (40px blur), glassmorphism elements
- **⚠️ Professional Error Handling** — Beautiful error pages with guidance instead of plain error messages
- **♿ Accessibility** — Proper labels, form validation, autofocus, semantic HTML

## 📚 API Endpoints

### FastAPI Server (Port 8000)

| Method | Endpoint | Purpose | Request Body |
|--------|----------|---------|--------------|
| `GET` | `/health` | Health check | — |
| `POST` | `/recommend` | Get recommendations | `{"query": "job description or skills"}` |
| `GET` | `/docs` | Interactive API documentation (Swagger UI) | — |
| `GET` | `/redoc` | API documentation (ReDoc) | — |

**Example Request:**
```bash
curl -X POST "http://127.0.0.1:8000/recommend" \
  -H "Content-Type: application/json" \
  -d '{"query": "Python developer with machine learning experience"}'
```

### Flask Server (Port 5000)

| Method | Endpoint | Purpose |
|--------|----------|---------|
| `GET` | `/` | Homepage |
| `GET/POST` | `/signup` | User registration page and handler |
| `GET/POST` | `/login` | User login page and handler |
| `GET` | `/recommend-page` | Recommendation interface (requires login) |
| `GET` | `/logout` | User logout and session termination |

**Example Login Flow:**
1. Visit `http://127.0.0.1:5000/signup` to create account
2. Visit `http://127.0.0.1:5000/login` to authenticate
3. Access `http://127.0.0.1:5000/recommend-page` to use recommendations

## 🔐 Security Considerations

### ⚠️ Current Implementation (Demo/Development Only)

The current implementation is optimized for demonstration and learning purposes:

- Passwords stored in plain text (NOT suitable for production)
- Flask secret key hardcoded in source code
- CORS enabled for all origins (`*`)
- No rate limiting or request validation
- API endpoints publicly accessible

### 🛡️ Recommendations for Production Deployment

**Authentication & Passwords:**
```python
# Use bcrypt or argon2 for password hashing
from werkzeug.security import generate_password_hash, check_password_hash

# Hash password before storage
hashed = generate_password_hash(password, method='pbkdf2:sha256')

# Verify password on login
is_valid = check_password_hash(hashed, password_input)
```

**Secret Management:**
```python
# Use environment variables for sensitive data
SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'dev-key-change-in-production')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
DB_PASSWORD = os.getenv('DB_PASSWORD')
```

**CORS Policy:**
```python
# Restrict to specific origins
CORS(app, resources={
    r"/api/*": {"origins": ["https://yourdomain.com"]}
})
```

**Additional Security Measures:**
- Implement rate limiting (Flask-Limiter)
- Add HTTPS/SSL certificates
- Use API keys with expiration
- Implement request signing
- Add input validation and sanitization
- Use database connection pooling
- Enable SQL injection prevention
- Implement logging and monitoring
- Add authentication tokens (JWT)

**Before Going to Production:**
1. Set strong `FLASK_SECRET_KEY` environment variable
2. Hash all user passwords with bcrypt/argon2
3. Enable HTTPS/SSL
4. Restrict CORS to specific domains
5. Implement rate limiting
6. Add comprehensive logging
7. Set up monitoring and alerts
8. Regular security audits

## 🧪 Testing & Evaluation

The project includes evaluation scripts to assess model performance:

- **[evaluation/recall_at_10.py](evaluation/recall_at_10.py)** — Evaluates recommendation accuracy at top-10 results
- **[outputs/generate_predictions.py](outputs/generate_predictions.py)** — Generates batch predictions
- **[outputs/predictions.csv](outputs/predictions.csv)** — Sample output results

Run evaluation:
```bash
python evaluation/recall_at_10.py
python outputs/generate_predictions.py
```

## 📖 Documentation

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** — Detailed setup instructions and configuration
- **[RAILWAY_DEPLOYMENT.md](RAILWAY_DEPLOYMENT.md)** — Railway.app deployment guide
- **[how to run.txt](how%20to%20run.txt)** — Quick reference for running the application
- **[Dockerfile](Dockerfile)** — Container configuration
- **[Procfile](Procfile)** — Process configuration for Heroku/Railway

## 📝 License

This project is provided as-is for educational and commercial use.

## 👤 Author & Support

**SmartAssess** was created as an intelligent assessment recommendation system to streamline the process for recruiters, educators, and students to find the most relevant assessments based on job requirements and skills.

### Getting Help

If you encounter issues:

1. **Check Documentation:** Review [SETUP_GUIDE.md](SETUP_GUIDE.md) and section above
2. **Verify Setup:** Ensure all prerequisites are met and environment variables are set
3. **Check Logs:** Review Flask/FastAPI server output for error messages
4. **Troubleshooting:** See the **Troubleshooting** section above for common issues
5. **Verify Credentials:** Confirm API keys, database credentials, and Python environment

### Requirements Recap

- Python 3.10+ (3.11+ recommended)
- MySQL 5.7+
- Google Gemini API key
- 2GB+ RAM for embedding model

---

**Last Updated:** January 2026  
**Python Version:** 3.10+ (3.11+ recommended)  
**Status:** ✅ Active Development  
**Deployment Ready:** Docker, Railway, Heroku  
**License Type:** MIT/Custom (specify as needed)
