# 🌍 Earthlytics - Urban Sustainability Platform

**Interactive Urban Sustainability Platform for NYC Environmental Data Visualization and Policy Simulation**

Earthlytics is a comprehensive web-based platform that allows users to explore urban sustainability data through interactive heatmaps, simulate environmental policies, and gain AI-powered insights about environmental justice and equity across NYC neighborhoods.

## ✨ Features

### 🗺️ Interactive Heatmaps
- **Population Density**: Visualize population distribution across NYC neighborhoods
- **Air Quality (AQI)**: Real-time air pollution levels with color-coded indicators
- **Green Cover (NDVI)**: Vegetation and green space coverage analysis
- **Environmental Equity**: Social justice and environmental health indicators
- **Flood Risk**: Sea level and flood vulnerability assessment

### 🏛️ Policy Simulator
- **Tree Planting**: Simulate the impact of urban forestry initiatives
- **Traffic Reduction**: Test traffic management policies and their environmental effects
- **Flood Protection**: Evaluate infrastructure investments for climate resilience
- **Real-time Impact**: See immediate visual feedback on heatmaps when policies are applied

### 🤖 AI-Powered Insights
- **Natural Language Analysis**: Get clear, actionable insights from complex data
- **Policy Impact Assessment**: Understand the potential benefits of proposed changes
- **Environmental Justice**: Identify areas needing targeted interventions
- **Recommendations**: Data-driven suggestions for urban planning

### ⚖️ Equity Analysis
- **Environmental Justice Index**: Comprehensive scoring system for neighborhood equity
- **Social Impact Visualization**: Understand the relationship between demographics and environmental health
- **Vulnerability Assessment**: Identify communities most at risk from environmental hazards
- **Correlation Analysis**: Explore connections between air quality, green cover, and social equity

### 📊 Comprehensive Dashboard
- **Interactive Charts**: Bar charts, pie charts, and scatter plots for data exploration
- **Sortable Data Tables**: Detailed neighborhood-by-neighborhood analysis
- **Export Functionality**: Download data in CSV format for further analysis
- **Real-time Updates**: Dynamic visualization that updates with policy changes

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd earthlytics
   ```

2. **Set up the backend**
   ```bash
   # Install Python dependencies
   pip install -r requirements.txt
   
   # Set up environment variables
   cp env.example .env
   # Edit .env and add your OpenAI API key
   ```

3. **Set up the frontend**
   ```bash
   cd frontend
   npm install
   ```

4. **Start the application**
   ```bash
   # Terminal 1: Start the backend
   python backend/app.py
   
   # Terminal 2: Start the frontend
   cd frontend
   npm start
   ```

5. **Access the platform**
   - Open your browser to `http://localhost:3000`
   - The backend API runs on `http://localhost:5000`

## 📁 Project Structure

```
earthlytics/
├── backend/
│   └── app.py                 # Flask backend with API endpoints
├── frontend/
│   ├── public/
│   │   └── index.html        # HTML template
│   ├── src/
│   │   ├── components/       # React components
│   │   │   ├── InteractiveHeatmap.js
│   │   │   ├── PolicySimulator.js
│   │   │   ├── Dashboard.js
│   │   │   ├── AIInsights.js
│   │   │   └── EquityAnalysis.js
│   │   ├── context/
│   │   │   └── DataContext.js # Data management
│   │   ├── App.js            # Main application
│   │   ├── index.js          # Entry point
│   │   └── index.css         # Global styles
│   └── package.json          # Frontend dependencies
├── Earthlytics_Datasets/     # Data directory
│   ├── Population_Density/
│   ├── Air_Pollution_NO2/
│   ├── Green_Cover_NDVI/
│   └── Flood_Risk/
├── requirements.txt           # Python dependencies
├── env.example              # Environment variables template
└── README.md               # This file
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
# OpenAI API Key for AI storytelling
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Mapbox API Key for enhanced mapping
MAPBOX_ACCESS_TOKEN=your_mapbox_token_here
```

### Data Sources
The platform uses real NYC neighborhood data including:
- **Population Density**: NASA SEDAC, EU Copernicus GHSL, WorldPop
- **Air Quality**: NASA Earthdata Worldview, Air Quality Index
- **Green Cover**: NASA MODIS, NDVI satellite data
- **Flood Risk**: NASA SEDAC, sea level rise projections

## 🎯 Usage Guide

### 1. Interactive Heatmaps
- Select different visualization layers from the dropdown
- Click on neighborhoods to see detailed information
- Use the legend to understand color coding
- Toggle between different metrics to compare data

### 2. Policy Simulation
- Choose a policy type (Tree Planting, Traffic Reduction, Flood Protection)
- Set parameters (number of trees, traffic reduction percentage, etc.)
- Select target neighborhoods
- Click "Simulate Policy" to see immediate impact
- View results in the impact cards and updated heatmaps

### 3. AI Insights
- Click "Generate AI Insights" to get intelligent analysis
- Review city-wide metrics and trends
- Get recommendations for targeted interventions
- Understand the impact of applied policies

### 4. Equity Analysis
- Explore environmental justice scores across neighborhoods
- Identify high and low equity areas
- Analyze correlations between air quality and equity
- Use the ranking table to sort by different metrics

### 5. Dashboard
- View comprehensive charts and graphs
- Sort and filter data tables
- Export data for further analysis
- Monitor key performance indicators

## 🔬 Technical Details

### Backend Architecture
- **Framework**: Flask (Python)
- **Data Processing**: Pandas, NumPy, Scikit-learn
- **AI Integration**: OpenAI GPT-3.5-turbo
- **API**: RESTful endpoints with CORS support
- **Data Sources**: CSV files with neighborhood data

### Frontend Architecture
- **Framework**: React 18
- **Mapping**: Leaflet.js with React-Leaflet
- **Charts**: Recharts for data visualization
- **Styling**: Styled-components for CSS-in-JS
- **State Management**: React Context API

### Key Features
- **Real-time Updates**: Heatmaps update immediately when policies are applied
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Data Export**: Download filtered data in CSV format
- **AI Integration**: Natural language insights powered by OpenAI
- **Interactive Visualizations**: Click, hover, and zoom functionality

## 🛠️ Development

### Adding New Data Sources
1. Add CSV files to the appropriate directory in `Earthlytics_Datasets/`
2. Update the `DataProcessor` class in `backend/app.py`
3. Add new visualization options in the frontend components

### Extending Policy Simulations
1. Add new policy types to the `PolicySimulator` class
2. Implement impact calculation methods
3. Update the frontend policy selector

### Customizing AI Insights
1. Modify the prompt in the `AIStoryteller` class
2. Adjust the data summary preparation
3. Add new insight categories

## 📊 Data Format

### Required CSV Structure:
```csv
Neighborhood Name,Borough,Latitude,Longitude,Population,NO2_AQI,NDVI,Flood_Risk
Financial District,Manhattan,40.7074,-74.0113,15800,85,0.12,High
```

### Data Requirements:
- **Neighborhood Name**: Unique identifier for each area
- **Borough**: Administrative division (Manhattan, Brooklyn, etc.)
- **Latitude/Longitude**: Geographic coordinates for mapping
- **Population**: Number of residents
- **NO2_AQI**: Air Quality Index (0-500 scale)
- **NDVI**: Normalized Difference Vegetation Index (0-1 scale)
- **Flood_Risk**: Categorical risk level (Low, Medium, High)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Data Sources**: NASA, EU Copernicus, WorldPop, NYC Open Data
- **Mapping**: OpenStreetMap contributors
- **AI**: OpenAI for natural language processing
- **Visualization**: Recharts, Leaflet.js communities

## 📞 Support

For questions, issues, or feature requests:
- Create an issue in the GitHub repository
- Check the documentation for common solutions
- Review the code comments for implementation details

---

**Built with ❤️ for sustainable urban development and environmental justice**
