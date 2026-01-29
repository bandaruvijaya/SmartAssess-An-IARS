# Railway Deployment Guide

## Prerequisites

- GitHub account with this repository pushed
- Railway account (https://railway.app)
- Environment variables configured

## Step 1: Prepare Your Code

✓ Code is already configured for Railway deployment

## Step 2: Push to GitHub

```bash
git init
git add .
git commit -m "Deploy to Railway"
git push origin main
```

## Step 3: Create Railway Project

1. Go to https://railway.app
2. Click **"New Project"**
3. Select **"Deploy from GitHub"**
4. Authorize GitHub and select your repository
5. Click **"Deploy"**

## Step 4: Configure Environment Variables

In Railway Dashboard:
1. Go to **Variables**
2. Add the following:

```
GEMINI_API_KEY=your_google_gemini_api_key
DB_HOST=your_railway_mysql_host
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_NAME=smartassess
SECRET_KEY=generate_secure_random_string
```

## Step 5: Add MySQL Database (Optional)

If using Railway's MySQL:

1. Click **"Add Service"**
2. Select **"MySQL"**
3. Railway will auto-populate `DB_HOST`, `DB_USER`, `DB_PASSWORD`
4. Run migrations/create tables

## Step 6: Configure Build & Deploy

Railway auto-detects:
- `Procfile` → service definitions
- `Dockerfile` → container build
- `runtime.txt` → Python version (3.11.7)

## Step 7: Verify Deployment

Once deployed, Railway provides a public URL:
- Web (Flask): `https://your-project.up.railway.app`
- API (FastAPI): `https://your-project.up.railway.app:8000`

## Important Notes

### Port Configuration

Railway automatically assigns `PORT` environment variable. The app uses:
```python
port = int(os.getenv("PORT", 5000))
```

### Database Setup

After first deploy, you'll need to create tables:

```sql
CREATE DATABASE IF NOT EXISTS smartassess;
USE smartassess;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fullname VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE assessments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    assessment_name VARCHAR(255) NOT NULL,
    skills TEXT,
    url VARCHAR(500),
    test_type CHAR(1)
);
```

### Troubleshooting

**Build Fails:**
- Check `requirements.txt` for syntax errors
- Verify Python dependencies are compatible
- Check Dockerfile for any issues

**Runtime Errors:**
- Check Railway logs: `railway logs`
- Verify all environment variables are set
- Check database connectivity

**Embedding Model Issues:**
- If `sentence-transformers` fails to download, Railway will cache it
- Alternatively, download locally and use `EMBED_MODEL_PATH`

### Performance Tips

1. **Use CPU-only FAISS** (already in requirements)
2. **Cache models** in Docker layers
3. **Use Railway's MySQL** for better latency
4. **Enable Railway's auto-scaling** for load handling

### Monitoring

Railway Dashboard provides:
- Build logs
- Runtime logs
- Memory/CPU usage
- Deployment history

### Costs

Railway pricing:
- Free tier: 5GB storage, limited compute hours
- Pay-as-you-go: $0.50/GB storage, compute per hour
- See https://railway.app/pricing

## Deploy Command (Optional)

If using Railway CLI:

```bash
npm install -g @railway/cli
railway login
railway link
railway up
```

## Rollback

If deployment fails:
1. Go to **Deployments** tab
2. Select previous successful deployment
3. Click **"Rollback"**

---

For more help: https://docs.railway.app
