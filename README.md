🌍 ShopImpact – Conscious Shopping & Eco Impact Tracker

Live App: https://g8c78moyzdezy4cvqvjmat.streamlit.app/

📌 Project Overview

ShopImpact is an interactive Streamlit-based web application that helps users make eco-conscious purchasing decisions by tracking shopping habits and estimating their CO₂ impact.

The application converts everyday purchases into clear, data-driven sustainability insights using real-time calculations, dashboards, and gamified rewards. It emphasizes progress over perfection, encouraging responsible consumption without guilt-based messaging.

ShopImpact demonstrates the complete lifecycle of an interactive Python application, including logic design, state management, UI customization, data visualization, and cloud deployment.

🧭 Problem Statement

Modern consumers face key sustainability challenges:

Environmental impact is invisible at checkout

Sustainable choices lack feedback and motivation

Climate data is complex and overwhelming

ShopImpact addresses these challenges by:

Translating purchases into understandable CO₂ estimates

Reinforcing eco-friendly behavior through positive gamification

Presenting insights in a calm, user-friendly interface

🔗 Integration Details

ShopImpact integrates multiple Python and Streamlit components into a unified system.

State Management

Uses st.session_state to store:

Purchase history

Daily CO₂ emissions

Spending data

Eco scores, streaks, and badges

Logic & Calculations

Category-based CO₂ multipliers

Eco-friendly purchases automatically reduce impact

Modular functions handle:

Purchase logging

Impact calculation

Streak tracking

Badge unlocking

Weekly summaries

User Interface Integration

Streamlit tabs organize:

Dashboard

Analytics

Badges & Rewards

Motivation & Insights

Settings

Custom CSS applied using st.markdown() for:

Light and dark themes

Accent colors

Clear visual hierarchy

Visualization & Export

Pandas used for data structuring and CSV export

Streamlit charts visualize:

CO₂ trends

Eco-friendly behavior patterns

🚀 Deployment Instructions

Local Deployment

git clone <repository-url>
cd ShopImpact
pip install -r requirements.txt
streamlit run app.py


The app runs at: http://localhost:8501

Streamlit Cloud Deployment

Push the project to GitHub

Log in to Streamlit Cloud

Click New App

Select:

Repository: ShopImpact

Main file: app.py

Click Deploy

The application becomes publicly accessible via a Streamlit-generated link.

🎯 Target Audience

Students and young adults

Eco-conscious individuals and families

Sustainability and data-tracking enthusiasts

Educators demonstrating applied Python and Streamlit

✨ Key Features

Purchase logging with product, brand, category, price, and eco-friendly toggle

Real-time CO₂ impact calculation

Interactive dashboards with daily insights

Gamified badges and streak tracking

Weekly sustainability summaries

CSV export for transparency and academic use

🛒 Purchase Logging

Each purchase captures:

Product name

Brand

Category

Price

Eco-friendly status

Automatic date tracking

All data is stored in structured session memory for accurate analysis.

🌱 Real-Time CO₂ Impact Calculation

Category-based CO₂ multipliers

Eco-friendly purchases reduce impact by 30%

Instant updates to:

Daily CO₂ emissions

Daily spending

📊 Dashboard & Insights

CO₂ emitted today

Money spent today

Eco Score (eco-friendly purchase ratio)

AI-style sustainability insights after each entry

🏆 Badges & Motivation

Users earn achievement badges based on eco-friendly habits:

🎖️ Eco Beginner

🏅 Eco Warrior

🏆 Eco Legend

Motivational quotes reinforce consistency and positive behavior.

🔍 Advanced Features

Top Eco Category detection

Eco Streak Tracker

Weekly CO₂ and spending summaries

Eco Savings estimation

📥 CSV Report Download

Users can export a complete CSV file containing:

Date

Product

Brand

Category

Price

Eco-friendly status

This supports academic submissions and deeper data analysis.

🧠 Design Philosophy

Behavior-driven gamification

Transparent calculations

Minimal cognitive load

Focus on awareness, not guilt

🧪 Testing & Reliability

The application has been tested for:

Multiple purchase scenarios

Edge cases and empty inputs

Repeated eco vs non-eco behavior

Session state consistency

🛠️ Technologies Used

Python

Streamlit

Pandas

🌍 Ethical & Social Impact

ShopImpact promotes:

Conscious consumerism

Environmental literacy

Long-term habit formation

Positive engagement with climate action

🔮 Future Enhancements

Monthly and yearly impact charts

Brand sustainability ratings

Greener alternative suggestions

Community challenges and leaderboards

PDF and long-term reports

🌟 Final Reflection

ShopImpact demonstrates how technology, data, and design can combine to create meaningful sustainability tools.

When awareness meets action, impact follows. 🌱
