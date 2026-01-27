
**Live Application:**  
https://g8c78moyzdezy4cvqvjmat.streamlit.app/

---

## Project Overview

ShopImpact is an interactive **Streamlit-based web application** designed to help users make **eco-conscious purchasing decisions** by tracking shopping habits and estimating their **CO₂ impact**.

The application converts everyday purchases into **clear, data-driven sustainability insights** using real-time calculations, dashboards, and gamified rewards. It emphasizes **progress over perfection**, encouraging responsible consumption without guilt-based messaging.

ShopImpact demonstrates the **complete lifecycle of an interactive Python application**, including logic design, state management, UI customization, data visualization, and cloud deployment. It is suitable for academic assessments, competitions, and real-world demonstrations.

---

## Problem Statement

Modern consumers face several sustainability challenges:

- Environmental impact is invisible at the point of purchase  
- Sustainable living lacks engagement and feedback  
- Climate data is often technical and overwhelming  

ShopImpact addresses these challenges by:

- Translating purchases into **understandable CO₂ metrics**
- Reinforcing positive behavior through **gamification**
- Presenting insights in a **simple and user-friendly interface**

---

## Integration Details

ShopImpact integrates multiple Python components and Streamlit features into a unified system.

### Data Handling and State Management

- Uses `st.session_state` to store:
  - Purchase history  
  - Daily CO₂ emissions  
  - Spending data  
  - Eco-friendly counts, streaks, and badges  

- Data structures include lists and dictionaries for efficient aggregation.

### Logic and Calculations

- Category-based CO₂ multipliers estimate environmental impact  
- Eco-friendly purchases automatically reduce calculated impact  
- Modular Python functions handle:
  - Purchase logging  
  - Impact calculation  
  - Streak tracking  
  - Badge unlocking  
  - Weekly summaries  

### User Interface Integration

- Streamlit tabs organize the application into:
  - Dashboard  
  - Analytics  
  - Badges and Rewards  
  - Motivation and Insights  
  - Settings  

- Custom CSS is injected using `st.markdown()` to apply:
  - Light and dark themes  
  - Accent colors  
  - Visual hierarchy  

### Visualization and Export

- Pandas is used for structured data handling  
- CSV export functionality is provided  
- Streamlit charts visualize CO₂ trends and eco behavior  

---

## Deployment Instructions

### Local Deployment

```bash
git clone <repository-url>
cd ShopImpact
pip install -r requirements.txt
streamlit run app.py
```

The application runs at:  
`http://localhost:8501`

### Streamlit Cloud Deployment

- Push the project to a GitHub repository  
- Log in to Streamlit Cloud  
- Click **New App**  
- Select:
  - Repository: ShopImpact  
  - Main file path: `app.py`  
- Click **Deploy**

The application becomes publicly accessible via a Streamlit-generated URL.

---

## Stage 1: Planning & Design
- Focused on mapping the user flow, defining core features (purchase logging, CO₂ tracking, badges), and sketching a clean, eco-themed interface aligned with ShopImpact’s goals.
Low-fidelity wireframes and an earthy color palette were used to visualize dashboards, rewards, and analytics before implementation.

<img width="1536" height="1024" alt="ChatGPT Image Jan 27, 2026, 10_42_56 PM" src="https://github.com/user-attachments/assets/2ebb5187-59ff-4194-a40b-d4816c9e761d" />

---

## Stage 2: Build the Python Logic
- implementing core data structures and functions to store purchases, calculate CO₂ impact, track eco-friendly behavior, and manage streaks and badges.
Clear, modular Python logic ensured accurate calculations, reliable session-state handling, and smooth integration with the Streamlit interface.

## Stage 3: Interactive Interface
- focused on designing a clean, intuitive Streamlit layout that allows users to log purchases, view impact metrics, and track progress effortlessly.
Custom themes, dashboards, and visual feedback were integrated to enhance usability while maintaining a calm, eco-friendly aesthetic.

## App Screenshots

#Dashboard
<img width="1920" height="881" alt="image" src="https://github.com/user-attachments/assets/25fa4d90-d2da-48e8-bfd0-c36c4b6c21eb" />

# Visual Analytics 
<img width="1920" height="882" alt="image" src="https://github.com/user-attachments/assets/1dec1a3b-0cb9-4c8b-a9a0-ffdc630d0c77" />

# Badges and Rewards
<img width="1920" height="874" alt="image" src="https://github.com/user-attachments/assets/3eb25b1b-2b44-4cf4-826b-9fe8091847ba" />

# Motivational Message and AI Insights
<img width="1806" height="396" alt="image" src="https://github.com/user-attachments/assets/abec743b-332f-4b54-bc09-b7286418e1cd" />

# Feedback
<img width="1821" height="592" alt="image" src="https://github.com/user-attachments/assets/b8aa0cdc-0ee2-4992-9584-5fea5f152700" />

# Settings 
<img width="1920" height="872" alt="image" src="https://github.com/user-attachments/assets/ebfdcf6b-cf32-4c47-a0cf-faf0a11edd77" />

# Light Mode 
<img width="1838" height="806" alt="image" src="https://github.com/user-attachments/assets/8b231cc9-0dd4-45ba-b589-39fe4e56a7cc" />

# Sidebar
<img width="1146" height="874" alt="image" src="https://github.com/user-attachments/assets/1792a2cc-ff41-4236-85e5-286dd4d1c626" />

---

## Stage 4: Testing & Gamification
- involved validating all calculations, streak logic, and badge unlock conditions through multiple simulated purchase scenarios.
Gamified elements such as badges, streaks, and motivational feedback were refined to ensure consistent rewards and sustained user engagement.

## Stage 5: Deployment
- focused on preparing the application for public use by configuring dependencies, organizing the project structure, and ensuring smooth execution.
The app was deployed on Streamlit Cloud, making ShopImpact accessible online through a shareable link for demos, evaluations, and real-world use.




## Target Audience

- Students and young adults  
- Eco-conscious individuals and families  
- Users interested in sustainability and data tracking  
- Educators demonstrating applied Python and Streamlit  

---

## Key Features

- Intelligent purchase logging  
- Real-time CO₂ impact calculation  
- Interactive dashboards and insights  
- Gamified badges and motivation  
- Weekly sustainability summaries  
- CSV data export  

---

## Purchase Logging

Users can log purchases by entering:

- Product name  
- Brand  
- Category (Clothing, Electronics, Groceries, Furniture, etc.)  
- Price  
- Eco-friendly toggle  

Each purchase is automatically timestamped for accurate tracking.

---

## Real-Time CO₂ Impact Calculation

- Category-specific CO₂ multipliers  
- Eco-friendly purchases reduce impact by **30%**  
- Daily emissions and spending update instantly  

---

## Dashboard and Insights

The dashboard displays:

- CO₂ emitted today  
- Money spent today  
- Eco Score (eco-friendly purchase percentage)  
- AI-style sustainability insights  

---

## Badges and Motivation

Users earn badges based on eco-friendly behavior:

- Eco Beginner  
- Eco Warrior  
- Eco Legend  

Motivational quotes encourage consistent sustainable habits.

---

## Advanced Features

- Top Eco Category identification  
- Eco Streak Tracker  
- Weekly CO₂ and spending summaries  
- Eco Savings Calculator  

---

## CSV Report Download

Users can download a complete CSV report containing:

- Date  
- Product  
- Brand  
- Category  
- Price  
- Eco-friendly status  

This supports academic analysis and reporting.

---

## Technical Design

- Python dictionaries and lists stored in `st.session_state`  
- Daily data grouped by date  
- Clean, modular function design  

---

## Technologies Used

- Python  
- Streamlit  
- Pandas  

---

## Testing and Reliability

The application has been tested for:

- Multiple purchase scenarios  
- Empty and edge-case inputs  
- Repeated eco vs non-eco patterns  
- Session persistence and stability  

---

## Ethical and Social Impact

ShopImpact promotes:

- Conscious consumerism  
- Environmental awareness  
- Long-term habit formation  
- Positive engagement with sustainability  

---

## Future Enhancements

- Monthly and yearly trend graphs  
- Brand-based sustainability ratings  
- Greener alternative suggestions  
- Community leaderboards  
- PDF impact reports  

---

## Final Reflection

ShopImpact demonstrates how **technology, data, and thoughtful design** can work together to address real-world sustainability challenges.

**When awareness meets action, impact follows.**

