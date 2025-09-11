# Vitamin-Personalizer
🧠 Vitamin Personalizer
📌 Overview

The Vitamin Personalizer is a Python-based system that analyzes lab test results along with personal information (age, sex, weight, etc.) to provide personalized vitamin and nutrition recommendations.

It’s designed to help users better understand their bloodwork by comparing values against dynamic reference ranges and generating a custom health report in PDF format.

🚀 Features

✅ Accepts lab test values (40+ metrics supported).

✅ Allows skipping values using PASS or 0.

✅ Uses dynamic reference ranges based on age, sex, weight, and height.

✅ Highlights abnormal results with suggestions for improvement.

✅ Generates a personalized PDF report.

✅ Modular design using User, LabResult, VitaminData, VitaminAnalyzer, and VitaminInfo classes.

✅ Stores results in a MySQL database for tracking progress over time.

🛠️ Tech Stack

Programming Language: Python

Database: MySQL

Libraries: Pandas, Matplotlib (if you visualize), ReportLab (PDF generation)

System Design: Modular OOP structure

📂 Project Structure
VitaminPersonalizer/
│── data/                 # Lab reference data
│── src/                  # Core Python modules
│   │── user.py           # User class
│   │── lab_result.py     # Lab result parser
│   │── vitamin_data.py   # Reference ranges
│   │── analyzer.py       # VitaminAnalyzer logic
│   │── report.py         # PDF generation
│── output/               # Generated reports
│── requirements.txt      # Dependencies
│── main.py               # Run the program
│── README.md             # Documentation

⚙️ Installation & Setup

Clone the repository:

git clone https://github.com/yourusername/vitamin-personalizer.git
cd vitamin-personalizer


Install dependencies:

pip install -r requirements.txt


Setup MySQL database (example):

CREATE DATABASE vitamin_personalizer;


Run the program:

python main.py

Example Of Usage: 
![vitm](https://github.com/user-attachments/assets/88e57e64-483b-475f-9970-629cb4f609c7)
