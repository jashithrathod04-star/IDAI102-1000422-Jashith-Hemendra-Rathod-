🌍 ShopImpact – Conscious Shopping & Eco Impact Tracker

🔗 Live Application: https://g8c78moyzdezy4cvqvjmat.streamlit.app/

➢ Project Overview

ShopImpact is an interactive Streamlit-based web application designed to help users make eco-conscious purchasing decisions by tracking everyday shopping habits and estimating their environmental (CO₂) impact.

The application converts routine purchases into understandable sustainability metrics and reinforces positive behavior through gamification and real-time feedback. Rather than using fear-based messaging, ShopImpact promotes awareness, reflection, and gradual improvement.

This project demonstrates the complete lifecycle of an interactive Python application, including:

Logic design

Structured data handling

State management

UI customization

Data visualization

Cloud deployment

It is well-suited for academic assessments, sustainability projects, competitions, and real-world demonstrations.

➢ Problem Statement

Modern consumers face several challenges when trying to live sustainably:

Lack of visibility
The environmental impact of purchases is invisible at checkout.

Low engagement
Sustainable living often lacks feedback, motivation, and rewards.

Data overload
Climate data is frequently technical, abstract, and intimidating.

ShopImpact addresses these issues by:

Translating purchases into clear CO₂ estimates

Encouraging improvement through positive reinforcement and gamification

Presenting insights in a calm, user-friendly interface

The focus is on progress rather than perfection.

➢ Integration Details

ShopImpact integrates multiple Python components and Streamlit features into a cohesive system.

🔹 Data Handling & State Management

Uses st.session_state to persist:

Purchase history

Daily CO₂ emissions

Spending data

Eco scores, streaks, and badges

Data structures include lists, dictionaries, and grouped date-based summaries.

🔹 Logic & Calculations

Category-based CO₂ multipliers estimate environmental impact.

Eco-friendly purchases automatically reduce calculated impact.

Modular Python functions manage:

Purchase logging

Impact calculations

Streak tracking

Badge unlocking

Weekly summaries

🔹 User Interface Integration

Streamlit tabs organize the app into:

Dashboard

Analytics

Badges & Rewards

Motivation & AI Insights

Feedback

Settings

Custom CSS injected using st.markdown() enables:

Light and dark themes

Accent color control

Visual hierarchy and hover effects

🔹 Visualization & Export

Pandas structures data for charts and CSV export.

Streamlit charts visualize CO₂ trends and eco behavior.

All components update dynamically based on user interaction.

➢ Deployment Instructions
💻 Local Deployment
git clone <repository-url>
cd ShopImpact
pip install -r requirements.txt
streamlit run app.py


The app launches at: http://localhost:8501

☁️ Streamlit Cloud Deployment

Push the project to GitHub

Log in to Streamlit Cloud

Click New App and connect the repository

Select:

Repository: ShopImpact

Main file path: app.py

Click Deploy

The app becomes publicly accessible via a Streamlit-generated link.

📘 Detailed Project Documentation
🎯 Target Audience

Students and young adults

Eco-conscious individuals and families

Users interested in sustainability, data tracking, and responsible consumption

Educators demonstrating real-world applications of Python and Streamlit

✨ Key Features
🛒 Purchase Logging

Users can log purchases with:

Product name

Brand

Category (Clothing, Electronics, Groceries, Furniture, etc.)

Price

Eco-friendly toggle

Each entry is timestamped for accurate daily and weekly tracking.

🌱 Real-Time CO₂ Impact Calculation

Predefined CO₂ multipliers per category

Eco-friendly purchases reduce impact by 30%

Instant updates to:

Daily CO₂ emissions

Daily spending

📊 Dashboard & Insights

CO₂ emitted today

Money spent today

Eco Score (percentage of eco-friendly purchases)

AI-style sustainability insights after each purchase

🏆 Badges & Motivation

Achievement badges reward consistent eco-friendly behavior:

🎖️ Eco Beginner

🏅 Eco Warrior

🏆 Eco Legend

Motivational quotes encourage sustained engagement.

🔍 Advanced Features

Top Eco Category – identifies sustainable purchasing patterns

Eco Streak Tracker – tracks consecutive eco-friendly days

Weekly Summary – CO₂ emissions, spending, and eco ratio

Eco Savings Calculator – estimates financial savings

📥 CSV Report Download

Users can export a complete CSV report including:

Date

Product

Brand

Category

Price

Eco-friendly status

Suitable for analysis, reports, and academic submission.

🧠 Core Concepts Behind the App
1️⃣ Behavioral Science

Badges and rewards reinforce positive behavior

Streak tracking encourages consistency

Motivational messaging maintains engagement

2️⃣ Data-Driven Sustainability

Each purchase generates measurable CO₂ impact

Eco scores are based on behavior ratios

Weekly and cumulative summaries enable trend analysis

3️⃣ Responsible Technology Design

Transparent calculations

Minimal cognitive load

Focus on education and improvement rather than guilt

⚙️ How the App Works (High-Level Flow)

User logs purchases

CO₂ impact is calculated using category multipliers

Eco-friendly choices improve scores and streaks

Insights, badges, and summaries update instantly

Data can be exported for further analysis

📊 What Makes ShopImpact Stand Out

Real-time feedback after every action

Meaningful gamification

Clean, analyzable data structures

CSV export for transparency

Streamlit Cloud–ready deployment

🌍 Ethical & Social Impact

ShopImpact promotes:

Conscious consumerism

Environmental literacy

Positive engagement with climate action

Long-term habit change

🌟 Final Reflection

ShopImpact demonstrates how technology, data, and thoughtful design can work together to address real-world sustainability challenges.

When awareness meets action, impact follows. 🌱
