# Ethiopia Financial Inclusion Dashboard

Interactive Streamlit dashboard for exploring Ethiopia's financial inclusion data, understanding event impacts, and viewing forecasts.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment activated
- Processed financial inclusion data available

### Installation & Setup

1. **Navigate to dashboard directory**
```bash
cd dashboard
```

2. **Install required packages**
```bash
pip install streamlit plotly pandas numpy seaborn scikit-learn
```

3. **Launch the dashboard**
```bash
streamlit run app.py
```

4. **Access the dashboard**
Open your browser and go to: `http://localhost:8501`

## 📊 Dashboard Features

### 🏠 Overview Page
- **Key Metrics Cards**: Current account ownership, digital payments, mobile money adoption
- **P2P/ATM Crossover Ratio**: Digital vs traditional banking indicator
- **Growth Rate Analysis**: Year-over-year growth by indicator
- **Recent Events Timeline**: Financial inclusion events chronology
- **Key Insights**: Automated analysis and recommendations

### 📈 Trends Page
- **Interactive Time Series**: Multiple visualization types (line, area, bar)
- **Date Range Selector**: Custom time period analysis
- **Channel Comparison**: Mobile money vs digital payments vs ATM usage
- **Correlation Analysis**: Indicator relationships heatmap
- **Multi-Indicator Support**: Select and compare multiple metrics

### 🔮 Forecasts Page
- **Model Selection**: Linear, Polynomial, Event-Adjusted, Ensemble models
- **Confidence Intervals**: 95% uncertainty bounds for all forecasts
- **Key Milestones**: NFIS-II target achievement tracking
- **Multi-Year Forecasts**: 2025-2027 projections with detailed tables
- **Visual Validation**: Historical vs forecast comparison charts

### 🎯 Inclusion Projections Page
- **Scenario Analysis**: Optimistic, Base Case, Pessimistic scenarios
- **Target Progress**: 60% and 70% (NFIS-II) achievement tracking
- **Policy Insights**: Answers to consortium's key questions
- **Gender Gap Analysis**: Projected inclusion disparities
- **Investment Priorities**: Data-driven recommendations

## 🎛️ Interactive Controls

### Sidebar Navigation
- **Page Selection**: Switch between 4 main dashboard pages
- **Date Range Filter**: Analyze specific time periods
- **Indicator Selection**: Choose metrics to display
- **Data Download**: Export filtered data as CSV

### Visualization Controls
- **Plot Type Selection**: Line, area, or bar charts
- **Scenario Selection**: Choose forecast scenarios
- **Model Selection**: Pick forecasting methodology
- **Zoom & Pan**: Interactive chart exploration

## 📋 Data Requirements

### Required Files
```
../data/processed/ethiopia_fi_enriched_data.csv  # Main dataset
```

### Data Structure
The dashboard expects data with the following structure:
- **observations**: Financial inclusion metrics over time
- **events**: Policy and market intervention events
- **impact_links**: Event-indicator relationships
- **targets**: Forecast targets and milestones

### Key Indicators
- `access_account_ownership`: Overall account ownership rate
- `usage_digital_payment`: Digital payment usage
- `usage_mm_account`: Mobile money account ownership
- `access_account_male/female`: Gender-disaggregated ownership
- `infra_mobile_penetration`: Mobile network coverage
- `usage_p2p_payment`: Person-to-person payment usage

## 🎨 Dashboard Design

### Visual Elements
- **Metric Cards**: Key performance indicators with trend arrows
- **Interactive Charts**: Plotly-based responsive visualizations
- **Color Coding**: Intuitive color schemes for scenarios
- **Responsive Layout**: Works on desktop and mobile devices

### User Experience
- **Real-time Updates**: Instant response to filter changes
- **Data Export**: Download filtered datasets
- **Tooltips**: Hover information for all charts
- **Help Sections**: Expandable methodology documentation

## 🔧 Technical Implementation

### Core Technologies
- **Streamlit**: Dashboard framework and UI components
- **Plotly**: Interactive visualizations and charts
- **Pandas**: Data processing and analysis
- **NumPy**: Numerical computations and forecasting

### Key Features
- **Data Caching**: Efficient data loading with `@st.cache_data`
- **Responsive Design**: Mobile-friendly layout
- **Error Handling**: Graceful data loading failures
- **Performance**: Optimized for large datasets

### Custom Components
- **Metric Cards**: Styled KPI displays
- **Scenario Analysis**: Interactive forecast comparison
- **Correlation Heatmaps**: Multi-indicator relationships
- **Timeline Visualizations**: Event chronology display

## 📊 Usage Examples

### Basic Navigation
```python
# Launch dashboard
streamlit run app.py

# Navigate pages via sidebar:
# 1. Overview - Key metrics and insights
# 2. Trends - Historical analysis
# 3. Forecasts - Future projections
# 4. Inclusion Projections - Policy analysis
```

### Data Analysis Workflow
1. **Start with Overview**: Get current state and key metrics
2. **Explore Trends**: Understand historical patterns
3. **Review Forecasts**: See future projections
4. **Analyze Scenarios**: Evaluate policy impacts

### Export Functionality
- Use sidebar "Download Filtered Data" button
- Select date range and indicators first
- CSV file includes all selected observations

## 🎯 Business Questions Answered

### Consortium Key Questions
1. **NFIS-II Target Achievement**: Will Ethiopia reach 70% account ownership by 2027?
2. **Policy ROI**: Which interventions yield highest financial inclusion returns?
3. **Infrastructure Impact**: What investments accelerate digital adoption?
4. **Gender Gap Evolution**: How do inclusion disparities change over time?
5. **Investment Priorities**: Where should resources be allocated?

### Decision Support
- **Scenario Planning**: Evaluate different policy implementation paths
- **Resource Allocation**: Identify high-impact investment areas
- **Target Monitoring**: Track progress toward inclusion goals
- **Risk Assessment**: Understand uncertainties in projections

## 🔍 Methodology & Limitations

### Forecasting Approach
- **Multi-Model Ensemble**: Combines linear, polynomial, and event-adjusted models
- **Uncertainty Quantification**: 95% confidence intervals for all projections
- **Scenario Analysis**: Optimistic, base, and pessimistic pathways
- **Event Impact Modeling**: Policy and market intervention effects

### Data Limitations
- **Temporal Frequency**: 5 survey points over 13 years
- **Regional Aggregation**: No geographic disaggregation
- **Event Attribution**: Multiple simultaneous interventions
- **External Factors**: GDP, inflation not fully modeled

### Assumptions
- **Trend Continuation**: Historical patterns continue unless disrupted
- **Event Effects**: Policy impacts based on similar historical events
- **Scenario Parameters**: Optimistic/pessimistic bounds based on expert judgment

## 🚀 Production Deployment

### Local Development
```bash
# Development server
streamlit run app.py --server.port 8501

# With file watching for auto-reload
streamlit run app.py --server.runOnSave true
```

### Production Settings
```bash
# Production configuration
streamlit run app.py \
  --server.port 8501 \
  --server.address 0.0.0.0 \
  --server.headless true \
  --browser.gatherUsageStats false
```

### Docker Deployment (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## 📞 Support & Maintenance

### Contact Information
- **Developer**: Selam Analytics Consortium
- **Email**: analytics@selam.com
- **Phone**: +251 123 456 789
- **Location**: Addis Ababa, Ethiopia

### Version Information
- **Dashboard Version**: 1.0
- **Last Updated**: February 2025
- **Data Currency**: Through December 2024
- **Next Review**: August 2025

### Troubleshooting
- **Data Loading Errors**: Check file paths and data format
- **Performance Issues**: Reduce date range or selected indicators
- **Visualization Problems**: Refresh browser or clear cache
- **Export Failures**: Ensure data filters are applied before download

## 🔄 Updates & Enhancements

### Planned Features
- **Real-time Data Integration**: API connections for live updates
- **Advanced Analytics**: Machine learning-based predictions
- **Geographic Analysis**: Regional inclusion mapping
- **Mobile Optimization**: Enhanced mobile experience

### Maintenance Schedule
- **Monthly**: Data refresh and validation
- **Quarterly**: Model retraining and updates
- **Annually**: Comprehensive review and enhancement

---

**Dashboard Access**: `http://localhost:8501`  
**Documentation**: See parent directory README.md  
**Support**: analytics@selam.com
