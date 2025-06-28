# 🧭 Yukti: India Tourism Insights Dashboard 🏛️
A comprehensive data analytics platform that transforms India's tourism landscape through advanced visualization, machine learning insights, and real-time environmental monitoring.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://zeny1303-yukti-app-6ch1dn.streamlit.app/) ![Python](https://img.shields.io/badge/python-3.8+-blue.svg) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

## 🎯 Project Overview
Yukti is an intelligent tourism analytics platform that leverages advanced data science techniques to uncover hidden patterns in India's tourism ecosystem. Built with multi-dimensional data analysis, it provides actionable insights for sustainable tourism development, heritage site optimization, and climate-aware travel planning across India's diverse landscape.

## 🌟 Why Yukti?
- **🔍 Smart Analytics**: Advanced statistical modeling and trend analysis for tourism patterns
- **🗺️ Interactive Mapping**: Dynamic 3D visualizations of heritage sites and tourist hotspots  
- **🌡️ Climate Intelligence**: Real-time weather and pollution correlation analysis
- **📊 Data-Driven Insights**: Evidence-based recommendations for tourism development
- **🏛️ Heritage Focus**: Specialized analysis of UNESCO sites and cultural monuments
- **🌱 Sustainability Metrics**: Environmental impact assessment for responsible tourism

## 🛠 Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Frontend** | Streamlit | Interactive web application |
| **Data Visualization** | Plotly, Altair | Dynamic charts and statistical plots |
| **3D Mapping** | Pydeck | Geospatial visualization and mapping |  
| **Data Processing** | Pandas, NumPy | Data manipulation and analysis |
| **Statistical Analysis** | SciPy, Scikit-learn | Advanced analytics and modeling |
| **Deployment** | Streamlit Cloud | Production hosting |


## 📊 Core Components

- **app.py** - Main Streamlit application with dashboard overview and navigation
- **pages/** - Multi-page application modules for different analysis sections
- **Cultural_Heritage_Data/** - Comprehensive heritage site datasets and analysis files
- **Countries_datasets/** - Tourism statistics, demographics, and country-wise data
- **src/** - Core processing modules for data analysis and visualization utilities




## 🚀 Quick Start

### 🌐 **Try Online (Recommended)**
Experience Yukti instantly without any setup:

**🔗 [Launch Yukti Dashboard](https://zeny1303-yukti-app-6ch1dn.streamlit.app/)**

### 💻 **Local Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Zeny1303/Yukti.git
   cd yukti-tourism-dashboard
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

4. **Access the Dashboard**
   Open your browser and navigate to `http://localhost:8501`

## ⚙️ Configuration

- **Data Sources**: Government APIs and official tourism statistics
- **Update Frequency**: Daily refresh for environmental data, monthly for tourism statistics
- **Geographic Coverage**: All 28 states and 8 union territories of India
- **Time Range**: Historical data from 2010, real-time current data

## 📈 Performance Metrics

- **Dataset Size**: 175,000+ records across multiple domains
- **Query Speed**: <3 seconds for complex multi-dimensional analysis
- **Visualization Rendering**: Real-time interactive charts and maps
- **Data Freshness**: Daily updates for environmental metrics
- **Uptime**: 99.9% availability on Streamlit Cloud






### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run data validation tests
python -m pytest tests/

# Start development server with auto-reload
streamlit run app.py --server.runOnSave true
```


*Discover, Analyze, and Promote India's Hidden Gems with Yukti 🌍*
