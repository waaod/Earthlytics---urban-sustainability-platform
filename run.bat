@echo off
REM Earthlytics Platform Launcher for Windows
REM Automated setup and execution script

echo.
echo 🌍 Earthlytics - Urban Sustainability Platform
echo =============================================
echo.
echo Interactive platform for urban sustainability data visualization
echo and environmental policy simulation.
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js not found. Please install Node.js 16+
    pause
    exit /b 1
)

echo ✅ System requirements met
echo.

REM Setup backend
echo 🐍 Setting up Python backend...
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

echo 📦 Installing Python dependencies...
call venv\Scripts\activate.bat
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install Python dependencies
    pause
    exit /b 1
)

REM Setup environment file
if not exist ".env" (
    if exist "env.example" (
        copy env.example .env
        echo 📝 Created .env file from template
        echo ⚠️  Please edit .env file and add your OpenAI API key
    )
)

echo ✅ Backend setup completed
echo.

REM Setup frontend
echo ⚛️  Setting up React frontend...
if not exist "frontend" (
    echo ❌ Frontend directory not found
    pause
    exit /b 1
)

echo 📦 Installing Node.js dependencies...
cd frontend
npm install
if errorlevel 1 (
    echo ❌ Failed to install Node.js dependencies
    pause
    exit /b 1
)

cd ..
echo ✅ Frontend setup completed
echo.

echo 🎉 Setup completed successfully!
echo.
echo 🚀 Starting Earthlytics platform...
echo.

REM Start backend in background
echo 🚀 Starting backend server...
start "Earthlytics Backend" cmd /k "call venv\Scripts\activate.bat && python backend\app.py"

REM Wait for backend to start
timeout /t 3 /nobreak >nul

REM Start frontend in background
echo 🌐 Starting frontend server...
cd frontend
start "Earthlytics Frontend" cmd /k "npm start"
cd ..

REM Wait for frontend to start
timeout /t 5 /nobreak >nul

REM Open browser
echo 🌐 Opening Earthlytics in browser...
timeout /t 2 /nobreak >nul
start http://localhost:3000

echo.
echo ==================================================
echo 🌍 Earthlytics is now running!
echo ==================================================
echo 📍 Frontend: http://localhost:3000
echo 📍 Backend API: http://localhost:5000
echo 📍 API Health: http://localhost:5000/api/health
echo.
echo 💡 Tips:
echo    • Close the command windows to stop the servers
echo    • Check the browser for the interactive platform
echo    • Edit .env file to add your OpenAI API key for AI features
echo    • Explore different tabs: Heatmap, Simulator, Dashboard, AI Insights, Equity Analysis
echo.
echo 🎯 Ready to explore urban sustainability!
echo.
pause
