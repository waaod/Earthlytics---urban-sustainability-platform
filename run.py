#!/usr/bin/env python3
"""
Earthlytics Platform Launcher
Automated setup and execution script for the complete platform
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

def print_banner():
    """Print the Earthlytics banner"""
    print("""
    🌍 Earthlytics - Urban Sustainability Platform
    =============================================
    
    Interactive platform for urban sustainability data visualization
    and environmental policy simulation.
    
    """)

def check_requirements():
    """Check if required software is installed"""
    print("🔍 Checking system requirements...")
    
    # Check Python
    try:
        python_version = sys.version_info
        if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
            print("❌ Python 3.8+ required. Current version:", sys.version)
            return False
        print(f"✅ Python {python_version.major}.{python_version.minor} detected")
    except Exception as e:
        print(f"❌ Python check failed: {e}")
        return False
    
    # Check Node.js
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Node.js {result.stdout.strip()} detected")
        else:
            print("❌ Node.js not found. Please install Node.js 16+")
            return False
    except FileNotFoundError:
        print("❌ Node.js not found. Please install Node.js 16+")
        return False
    
    # Check npm
    try:
        result = subprocess.run(['npm', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ npm {result.stdout.strip()} detected")
        else:
            print("❌ npm not found")
            return False
    except FileNotFoundError:
        print("❌ npm not found")
        return False
    
    return True

def setup_backend():
    """Set up the Python backend"""
    print("\n🐍 Setting up Python backend...")
    
    # Check if virtual environment exists
    venv_path = Path("venv")
    if not venv_path.exists():
        print("📦 Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    
    # Determine activation script based on OS
    if os.name == 'nt':  # Windows
        activate_script = "venv\\Scripts\\activate.bat"
        pip_path = "venv\\Scripts\\pip"
        python_path = "venv\\Scripts\\python"
    else:  # Unix-like
        activate_script = "source venv/bin/activate"
        pip_path = "venv/bin/pip"
        python_path = "venv/bin/python"
    
    # Install requirements
    print("📦 Installing Python dependencies...")
    try:
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
        print("✅ Python dependencies installed")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Python dependencies: {e}")
        return False
    
    # Check for .env file
    if not Path(".env").exists():
        print("⚙️  Setting up environment variables...")
        if Path("env.example").exists():
            subprocess.run(["cp", "env.example", ".env"] if os.name != 'nt' else ["copy", "env.example", ".env"])
            print("📝 Created .env file from template")
            print("⚠️  Please edit .env file and add your OpenAI API key")
        else:
            print("⚠️  No env.example found. Please create .env file manually")
    
    return True

def setup_frontend():
    """Set up the React frontend"""
    print("\n⚛️  Setting up React frontend...")
    
    frontend_path = Path("frontend")
    if not frontend_path.exists():
        print("❌ Frontend directory not found")
        return False
    
    # Install npm dependencies
    print("📦 Installing Node.js dependencies...")
    try:
        subprocess.run(["npm", "install"], cwd="frontend", check=True)
        print("✅ Node.js dependencies installed")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Node.js dependencies: {e}")
        return False
    
    return True

def start_backend():
    """Start the Flask backend"""
    print("\n🚀 Starting backend server...")
    
    # Determine Python path
    if os.name == 'nt':  # Windows
        python_path = "venv\\Scripts\\python"
    else:  # Unix-like
        python_path = "venv/bin/python"
    
    try:
        # Start backend in background
        backend_process = subprocess.Popen(
            [python_path, "backend/app.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait a moment for server to start
        time.sleep(3)
        
        # Check if server is running
        if backend_process.poll() is None:
            print("✅ Backend server started on http://localhost:5000")
            return backend_process
        else:
            stdout, stderr = backend_process.communicate()
            print(f"❌ Backend failed to start: {stderr.decode()}")
            return None
            
    except Exception as e:
        print(f"❌ Failed to start backend: {e}")
        return None

def start_frontend():
    """Start the React frontend"""
    print("\n🌐 Starting frontend server...")
    
    try:
        # Start frontend in background
        frontend_process = subprocess.Popen(
            ["npm", "start"],
            cwd="frontend",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait for server to start
        time.sleep(5)
        
        # Check if server is running
        if frontend_process.poll() is None:
            print("✅ Frontend server started on http://localhost:3000")
            return frontend_process
        else:
            stdout, stderr = frontend_process.communicate()
            print(f"❌ Frontend failed to start: {stderr.decode()}")
            return None
            
    except Exception as e:
        print(f"❌ Failed to start frontend: {e}")
        return None

def open_browser():
    """Open the application in browser"""
    print("\n🌐 Opening Earthlytics in browser...")
    time.sleep(2)  # Wait for servers to fully start
    
    try:
        webbrowser.open("http://localhost:3000")
        print("✅ Browser opened to http://localhost:3000")
    except Exception as e:
        print(f"⚠️  Could not open browser automatically: {e}")
        print("Please manually open http://localhost:3000 in your browser")

def main():
    """Main execution function"""
    print_banner()
    
    # Check requirements
    if not check_requirements():
        print("\n❌ System requirements not met. Please install required software.")
        sys.exit(1)
    
    # Setup backend
    if not setup_backend():
        print("\n❌ Backend setup failed")
        sys.exit(1)
    
    # Setup frontend
    if not setup_frontend():
        print("\n❌ Frontend setup failed")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n🚀 Starting Earthlytics platform...")
    
    # Start backend
    backend_process = start_backend()
    if not backend_process:
        print("\n❌ Failed to start backend")
        sys.exit(1)
    
    # Start frontend
    frontend_process = start_frontend()
    if not frontend_process:
        print("\n❌ Failed to start frontend")
        backend_process.terminate()
        sys.exit(1)
    
    # Open browser
    open_browser()
    
    print("\n" + "="*50)
    print("🌍 Earthlytics is now running!")
    print("="*50)
    print("📍 Frontend: http://localhost:3000")
    print("📍 Backend API: http://localhost:5000")
    print("📍 API Health: http://localhost:5000/api/health")
    print("\n💡 Tips:")
    print("   • Use Ctrl+C to stop both servers")
    print("   • Check the browser for the interactive platform")
    print("   • Edit .env file to add your OpenAI API key for AI features")
    print("   • Explore different tabs: Heatmap, Simulator, Dashboard, AI Insights, Equity Analysis")
    print("\n🎯 Ready to explore urban sustainability!")
    
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down Earthlytics...")
        backend_process.terminate()
        frontend_process.terminate()
        print("✅ Servers stopped. Goodbye! 👋")

if __name__ == "__main__":
    main()
