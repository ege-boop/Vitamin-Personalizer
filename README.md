# Vitamin Personalizer

## Overview

The Vitamin Personalizer is a Python-based system that analyzes lab test results alongside personal information (age, sex, weight, height) to provide personalized vitamin and nutrition recommendations. The system helps users interpret their bloodwork by comparing values against dynamic reference ranges and generating custom health reports in PDF format.

[Watch the video explanation](https://youtu.be/4DPUY7C_CjQ)

## Features

- Accepts 40+ lab test metrics with flexible input handling
- Allows skipping values using PASS or 0
- Applies dynamic reference ranges based on age, sex, weight, and height
- Identifies abnormal results with actionable suggestions
- Generates personalized PDF health reports
- Modular object-oriented architecture
- MySQL database integration for historical tracking and progress monitoring

## Tech Stack

**Language:** Python  
**Database:** MySQL  
**Key Libraries:**
- Pandas - data processing
- Matplotlib - visualization
- ReportLab - PDF generation

**Architecture:** Modular OOP design with separation of concerns

## Project Structure
```
VitaminPersonalizer/
├── data/                 # Lab reference data and ranges
├── src/                  # Core Python modules
│   ├── user.py           # User data model
│   ├── lab_result.py     # Lab result parsing and validation
│   ├── vitamin_data.py   # Reference range management
│   ├── analyzer.py       # Analysis and recommendation engine
│   └── report.py         # PDF report generation
├── output/               # Generated health reports
├── requirements.txt      # Python dependencies
├── main.py               # Application entry point
└── README.md             # Project documentation
```

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/ege-boop/vitamin-personalizer.git
cd vitamin-personalizer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure MySQL database
```sql
CREATE DATABASE vitamin_personalizer;
```

Update database credentials in your configuration file.

### 4. Run the application
```bash
python main.py
```

## Usage

The system follows a straightforward workflow:

1. Enter personal information (age, sex, weight, height)
2. Input lab test values or skip with PASS/0
3. System analyzes results against personalized reference ranges
4. Receive comprehensive PDF report with recommendations

## How It Works

The Vitamin Personalizer uses a modular architecture with five core components:

- **User**: Manages personal demographic information
- **LabResult**: Parses and validates lab test inputs
- **VitaminData**: Maintains dynamic reference ranges
- **VitaminAnalyzer**: Performs analysis and generates recommendations
- **VitaminInfo**: Handles PDF report generation

## Example Output

The system generates detailed reports highlighting abnormal values and providing targeted vitamin and nutrition recommendations based on individual test results and demographic factors.

## Contributing

Contributions are welcome. Please fork the repository and submit a pull request with your proposed changes.

## License

This project is provided for educational and informational purposes. Always consult healthcare professionals before making changes to your supplement or nutrition regimen based on lab results.

## Disclaimer

This tool is designed to help interpret lab results but should not replace professional medical advice. Always consult with a qualified healthcare provider before making any decisions about vitamins, supplements, or health interventions.
