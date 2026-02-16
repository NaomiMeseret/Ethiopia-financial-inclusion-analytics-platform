# 📊 Ethiopia Financial Inclusion Forecasting

> 🚀 **Predicting Ethiopia's digital financial transformation with time series analysis**

Built for **Selam Analytics** in partnership with development finance institutions and the National Bank of Ethiopia to forecast Ethiopia's progress on financial inclusion using World Bank Global Findex methodology.

## 🎯 Project Overview

Ethiopia is undergoing a rapid digital financial revolution:

- 📱 **Telebirr**: 54M+ users since 2021 launch
- 💰 **M-Pesa**: 10M+ users since 2023 entry
- 🏦 **Interoperable P2P**: Now surpasses ATM withdrawals
- 📊 **The Challenge**: Only 49% account ownership in 2024 (+3pp from 2021)

**Our mission**: Understand what drives financial inclusion and predict Ethiopia's progress through 2027.

## 📈 What We Forecast

### Access Indicators 🏦

- **Account Ownership Rate** - Adults with financial accounts
- **Gender Gap Analysis** - Male vs female inclusion
- **Regional Coverage** - Urban vs rural access

### Usage Indicators 💳

- **Digital Payment Adoption** - Mobile money, cards, online payments
- **Mobile Money Penetration** - Active vs registered accounts
- **Payment Use Cases** - P2P, merchant, bill pay, wages

## 🏗️ Project Structure

```
ethiopia-financial-inclusion-forecast/
├── 📁 data/                    # Datasets & sources
│   ├── raw/                   # Original data (never modify)
│   └── processed/              # Analysis-ready data
├── 📓 notebooks/               # Jupyter analysis
├── 🔧 src/                     # Python modules
├── 🧪 tests/                   # Test suites
├── 📊 reports/                 # Analysis reports
├── 📱 dashboard/               # Interactive dashboard
├── 🤖 models/                  # Trained models
└── 📚 docs/                    # Documentation
```

## 🚀 Quick Start

### Prerequisites 📋

- Python 3.9+
- pandas, numpy, matplotlib, seaborn
- plotly, dash, scikit-learn

### Installation ⚡

```bash
# Clone the repo
git clone https://github.com/yourusername/ethiopia-financial-inclusion-forecast.git

# Setup environment
cd ethiopia-financial-inclusion-forecast
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run Analysis 🏃‍♂️

```bash
# Exploratory analysis
jupyter notebook notebooks/

# Interactive dashboard
python dashboard/app.py

# Run tests
python -m pytest tests/ -v
```

## 📊 Key Findings

### 🔍 What Drives Financial Inclusion?

1. **📱 Infrastructure Matters** - 4G coverage (35%) correlates with digital payments
2. **⚖️ Policy Impact** - Mobile money regulation (2022) accelerated adoption
3. **👥 Gender Gap** - 18pp difference (58% male vs 40% female)
4. **📈 Growth Deceleration** - Only +3pp (2021-2024) vs +11pp (2017-2021)
5. **💳 Usage Paradox** - 35% digital payments vs 9.45% mobile money accounts

### 🎯 2025-2027 Forecasts

- **Account Ownership**: 52% → 58% → 64%
- **Digital Payments**: 38% → 42% → 47%
- **Gender Gap**: Expected to narrow to 15pp by 2027

## 📈 Methodology

### 🏛️ World Bank Global Findex Framework

- **Access**: Account ownership rate (15+ population)
- **Usage**: Digital payment adoption (past 12 months)
- **Frequency**: Every 3 years (2011, 2014, 2017, 2021, 2024)

### 🤖 Time Series Approach

- **Event Impact Modeling**: Regulatory changes, product launches
- **Infrastructure Variables**: 4G coverage, mobile penetration
- **Intervention Analysis**: Policy effects with lag times
- **Confidence Bounds**: Uncertainty quantification

## 📊 Data Sources

### 🏛️ Official Data

- **Global Findex Database** - World Bank (2011-2024)
- **National Bank of Ethiopia** - Financial sector reports
- **Ethiopia Communication Authority** - Infrastructure data

### 📱 Industry Data

- **Ethio Telecom** - Telebirr usage statistics
- **Safaricom Ethiopia** - M-Pesa market data
- **EthSwitch** - Interoperability metrics

### 🌍 International Sources

- **GSMA Mobile Economy** - Smartphone penetration
- **IMF FAS** - Financial access statistics
- **ITU** - Digital infrastructure indicators

## 🎯 Use Cases

### 👥 Policy Makers

- **National Strategy**: Monitor NFIS-II progress toward 70% target
- **Impact Assessment**: Evaluate policy effectiveness
- **Resource Allocation**: Identify underserved regions/groups

### 🏦 Financial Institutions

- **Market Intelligence**: Competitive landscape analysis
- **Product Development**: Identify unmet needs
- **Risk Assessment**: Inclusion trends and opportunities

### 📊 Development Partners

- **Impact Measurement**: Program effectiveness tracking
- **Evidence-Based**: Data-driven intervention design
- **Benchmarking**: Regional comparison analysis

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test suite
python -m pytest tests/test_data_validation.py -v

# Coverage report
python -m pytest --cov=src tests/
```


---

**🌟 Together, let's build Ethiopia's financially inclusive future!**
