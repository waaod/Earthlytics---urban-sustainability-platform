# 🚀 Earthlytics Setup Guide

Complete setup instructions for the Earthlytics Urban Sustainability Platform.

## 📋 Prerequisites

Before starting, ensure you have the following installed:

### Required Software
- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **Node.js 16+** - [Download Node.js](https://nodejs.org/)
- **Git** - [Download Git](https://git-scm.com/)

### Optional but Recommended
- **Visual Studio Code** - [Download VS Code](https://code.visualstudio.com/)
- **Postman** - For API testing
- **Chrome DevTools** - For debugging

## 🔧 Step-by-Step Installation

### 1. Clone the Repository

```bash
# Clone the repository
git clone <repository-url>
cd earthlytics

# Verify the project structure
ls -la
```

You should see:
```
earthlytics/
├── backend/
├── frontend/
├── Earthlytics_Datasets/
├── requirements.txt
├── env.example
└── README.md
```

### 2. Backend Setup

#### Install Python Dependencies
```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Configure Environment Variables
```bash
# Copy the example environment file
cp env.example .env

# Edit the .env file with your API keys
# You'll need an OpenAI API key for AI features
```

**Required Environment Variables:**
```env
# OpenAI API Key (required for AI insights)
OPENAI_API_KEY=sk-your-openai-api-key-here

# Optional: Mapbox token for enhanced mapping
MAPBOX_ACCESS_TOKEN=pk.your-mapbox-token-here
```

#### Test Backend Installation
```bash
# Navigate to backend directory
cd backend

# Run the Flask application
python app.py
```

You should see:
```
🌍 Earthlytics Backend Starting...
📊 Data loaded successfully
🤖 AI integration ready
🚀 Server starting on http://localhost:5000
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://[::1]:5000
```

**Test the API:**
```bash
# In a new terminal, test the health endpoint
curl http://localhost:5000/api/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00.000Z"
}
```

### 3. Frontend Setup

#### Install Node.js Dependencies
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Verify installation
npm list --depth=0
```

#### Test Frontend Installation
```bash
# Start the development server
npm start
```

You should see:
```
Compiled successfully!

You can now view earthlytics-frontend in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://192.168.1.100:3000

Note that the development build is not optimized.
To create a production build, use npm run build.
```

### 4. Verify Complete Setup

1. **Backend is running** on `http://localhost:5000`
2. **Frontend is running** on `http://localhost:3000`
3. **Open your browser** to `http://localhost:3000`

You should see the Earthlytics platform with:
- Interactive navigation menu
- Welcome section with feature cards
- Working heatmap visualization
- All tabs functional (Heatmap, Simulator, Dashboard, AI Insights, Equity Analysis)

## 🔍 Troubleshooting

### Common Issues

#### Backend Issues

**Issue: "Module not found" errors**
```bash
# Solution: Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

**Issue: "Port 5000 already in use"**
```bash
# Find and kill the process using port 5000
lsof -ti:5000 | xargs kill -9  # macOS/Linux
netstat -ano | findstr :5000    # Windows

# Or change the port in backend/app.py
app.run(debug=True, host='0.0.0.0', port=5001)
```

**Issue: "OpenAI API key not found"**
```bash
# Check your .env file exists and contains the key
cat .env

# Ensure the key is valid and has sufficient credits
# Test with: curl -H "Authorization: Bearer YOUR_KEY" https://api.openai.com/v1/models
```

#### Frontend Issues

**Issue: "npm install" fails**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

**Issue: "Module not found" in React**
```bash
# Ensure you're in the frontend directory
cd frontend

# Check package.json exists
ls package.json

# Reinstall dependencies
npm install
```

**Issue: "Proxy error" or "Network Error"**
```bash
# Check backend is running on port 5000
curl http://localhost:5000/api/health

# If backend is on different port, update frontend/package.json:
# "proxy": "http://localhost:5001"
```

#### Data Issues

**Issue: "No data available"**
```bash
# Check data files exist
ls Earthlytics_Datasets/*/

# Verify CSV files have correct format
head Earthlytics_Datasets/Population_Density/population_density.csv
```

**Issue: "CORS error"**
```bash
# Ensure Flask-CORS is installed
pip install Flask-CORS

# Check backend/app.py has CORS(app) configured
```

### Performance Issues

**Issue: Slow loading**
```bash
# Check data file sizes
du -sh Earthlytics_Datasets/*/

# Consider reducing dataset size for development
# Or implement data pagination
```

**Issue: Memory usage**
```bash
# Monitor Python memory usage
pip install memory-profiler
python -m memory_profiler backend/app.py

# Monitor Node.js memory usage
node --max-old-space-size=4096 frontend/node_modules/.bin/react-scripts start
```

## 🧪 Testing the Platform

### 1. Test Interactive Heatmaps
- Navigate to the "Interactive Heatmap" tab
- Select different metrics (Population, Air Quality, Green Cover, Equity)
- Click on neighborhoods to see detailed information
- Verify heatmap colors change with different metrics

### 2. Test Policy Simulator
- Go to "Policy Simulator" tab
- Select "Plant Trees" policy
- Set parameters (e.g., 100 trees)
- Choose target neighborhoods
- Click "Simulate Policy"
- Verify impact results appear

### 3. Test AI Insights
- Navigate to "AI Insights" tab
- Click "Generate AI Insights"
- Verify AI-generated text appears
- Check for any API errors in browser console

### 4. Test Dashboard
- Go to "Dashboard" tab
- Verify charts and graphs load
- Test sorting functionality in data table
- Try exporting data as CSV

### 5. Test Equity Analysis
- Navigate to "Equity Analysis" tab
- Check equity scores and rankings
- Verify correlation charts load
- Test sorting by different metrics

## 🚀 Production Deployment

### Backend Deployment (Python/Flask)

**Option 1: Heroku**
```bash
# Install Heroku CLI
# Create Procfile
echo "web: gunicorn backend.app:app" > Procfile

# Create requirements.txt for production
pip freeze > requirements.txt

# Deploy to Heroku
heroku create your-app-name
git push heroku main
```

**Option 2: AWS/GCP/Azure**
```bash
# Use Docker for containerization
# Create Dockerfile for backend
# Deploy to cloud container service
```

### Frontend Deployment (React)

**Option 1: Netlify**
```bash
# Build for production
npm run build

# Deploy to Netlify
# Connect GitHub repository
# Set build command: npm run build
# Set publish directory: build
```

**Option 2: Vercel**
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

## 📊 Data Management

### Adding New Datasets

1. **Prepare CSV files** with required columns:
   ```csv
   Neighborhood Name,Borough,Latitude,Longitude,Population,NO2_AQI,NDVI,Flood_Risk
   ```

2. **Place files** in appropriate directories:
   ```
   Earthlytics_Datasets/
   ├── Population_Density/
   ├── Air_Pollution_NO2/
   ├── Green_Cover_NDVI/
   └── Flood_Risk/
   ```

3. **Update backend** to load new data:
   ```python
   # In backend/app.py, update DataProcessor.load_all_data()
   ```

### Data Validation

```bash
# Check CSV format
python -c "
import pandas as pd
df = pd.read_csv('Earthlytics_Datasets/Population_Density/population_density.csv')
print(df.columns.tolist())
print(df.head())
"
```

## 🔧 Development Workflow

### Daily Development
```bash
# Start backend
cd backend
python app.py

# Start frontend (in new terminal)
cd frontend
npm start

# Make changes to code
# Test in browser
# Commit changes
git add .
git commit -m "Add new feature"
git push
```

### Code Quality
```bash
# Python linting
pip install flake8 black
flake8 backend/
black backend/

# JavaScript linting
cd frontend
npm install --save-dev eslint prettier
npm run lint
```

## 📞 Getting Help

### Documentation
- Check this SETUP.md file
- Review README.md for feature documentation
- Examine code comments for implementation details

### Community Support
- Create GitHub issues for bugs
- Use GitHub discussions for questions
- Check existing issues for solutions

### Professional Support
- Contact the development team
- Schedule a consultation
- Request custom features

---

**Happy coding! 🌍✨**
