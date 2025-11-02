### HauntHub – Mock Halloween Events Platform 

# Overview

HauntHub was created as part of a hackathon project to demonstrate end-to-end data analysis and visualization for a fictional Halloween events platform.
The project combines mock event listings with an interactive analytics dashboard to explore how event organizers might track ticket prices, attendance, and location-based trends.
All data is synthetic and designed purely for learning and demonstration purposes.

# Tech Stack

- Languages & Frameworks

  - Frontend: HTML, CSS (mock web interface)

  - Backend / Framework: Django (scaffold only)

  - Data Analytics: Python, Streamlit, Plotly, Pandas, Matplotlib

  - Data Storage: Local CSV (mock dataset)

- Structure

/Analytics/        # Streamlit analytics app
/Data/             # Mock event dataset (halloween_events.csv)
/static/ or /templates/  # Front-end mock files
requirements.txt           # Django + core packages
analytics_requirements.txt # Streamlit + data libraries

# Setup Instructions

1. Clone the repository

git clone https://github.com/judewoolls/HalloweenHackathon
cd HauntHub

2. Create and activate a virtual environment

python -m venv .venv
source .venv/bin/activate       # macOS/Linux
.venv\Scripts\activate          # Windows

3. Install dependencies

For the mock Django website: pip install -r requirements.txt

For the analytics dashboard: pip install -r analytics_requirements.txt

# Running the Project

- Run the mock website (optional placeholder)

The Django portion is scaffolded but non-functional in this mock version.
Static HTML and CSS files can be viewed directly in the browser or served via python manage.py runserver if Django is configured.

- Run the Streamlit Analytics Dashboard

streamlit run Analytics/streamlit_app.py

Then open the displayed local URL (usually http://localhost:8501)

# Data and Files

- Dataset: 
Data/halloween_events.csv
A mock CSV file representing events, cities, ticket prices, and attendance.

- Generated Visuals: 
Output images are saved automatically in the analytics output directory (OUT_DIR) when the dashboard is run.

# Analytics Features

- The Streamlit dashboard provides:

   - Raw Data Table: View the full dataset directly in Streamlit.

   - Filter by City: Select one or multiple cities from the sidebar.

   - Event Summary Metrics: Quick view of total events, average ticket price, and attendance.

- Visual Insights:

   - Events per city

   - Average attendance per city

   - Price per event

   - Attendance per event

   - Event timeline

   - Price vs. attendance correlation

- Plotly Integration: Interactive scatter and bar charts rendered within the dashboard.

# Contribution and Role

- Role:

- Developed the analytics component of HauntHub, including:
 
  - Streamlit dashboard implementation

  - Data cleaning and summarization with Pandas

  - Interactive visualization using Plotly and Matplotlib

  - Project documentation and environment setup

# Future Improvements

- Integrate live or user-uploaded event data

- Add dynamic filtering and search in Streamlit

- Connect dashboard outputs to a database

- Develop a working Django front end using the same dataset

- Implement authentication for personalized analytics views


