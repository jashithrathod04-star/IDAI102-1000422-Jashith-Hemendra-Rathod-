# 🌍 ShopImpact – Conscious Shopping & Eco Impact Tracker

ShopImpact is an interactive **Streamlit-based web application** designed to help users make more **eco-conscious purchasing decisions**. By tracking everyday purchases, estimating their **CO₂ impact**, and rewarding sustainable behavior, ShopImpact transforms shopping into a mindful, data-driven experience.

This project is built with a strong focus on **clear logic, structured data handling, and an engaging user interface**, making it ideal for academic assessments, competitions, and real-world demonstrations.

---

## 🎯 Target Audience
- Young adults and students  
- Eco-conscious individuals and families  
- Users interested in sustainability, data tracking, and responsible consumption  

---

## ✨ Key Features

### 🛒 Purchase Logging
Users can log purchases with:
- Product name  
- Brand  
- Category (Clothing, Electronics, Groceries, Furniture, etc.)  
- Price  
- Eco-friendly toggle  

Each entry is stored with the current date for accurate tracking.

---

### 🌱 Real-Time CO₂ Impact Calculation
- Each category has a predefined CO₂ multiplier  
- Eco-friendly purchases automatically reduce impact by **30%**  
- Daily CO₂ emissions and spending update instantly  

---

### 📊 Dashboard & Insights
- **CO₂ emitted today**
- **Money spent today**
- **Eco Score** (percentage of eco-friendly purchases)
- AI-style sustainability insights after each purchase  

---

### 🏆 Badges & Motivation
Earn achievement badges based on eco-friendly habits:
- 🎖️ Eco Beginner  
- 🏅 Eco Warrior  
- 🏆 Eco Legend  

Motivational quotes are displayed to encourage consistent sustainable behavior.

---

### 🔍 Advanced Features
- **Top Eco Category** – identifies where you make the most sustainable choices  
- **Eco Streak Tracker** – tracks consecutive days with eco-friendly purchases  
- **Weekly Summary** – shows CO₂ emissions, spending, and eco ratio for the last 7 days  
- **Eco Savings Calculator** – estimates money saved by choosing eco-friendly options  

---

### 📥 CSV Report Download
Users can download a **complete CSV report** of all logged purchases, including:
- Date  
- Product  
- Brand  
- Category  
- Price  
- Eco-friendly status  

This makes the app suitable for **data analysis, reports, and academic submission**.

---

## 🧠 Technical Design

### Data Management
- Uses Python dictionaries and lists stored in `st.session_state`
- Daily data grouped by date for accurate summaries
- Clean, modular functions for calculations and features  

### Interface Design
- Built entirely with **Streamlit**
- Wide layout with clear sections:
  - Input form at the top  
  - Dashboard metrics in the center  
  - Features and badges below  
- Earthy color palette (greens, neutrals) for an eco-friendly aesthetic  

---

## 🛠️ Technologies Used
- **Python**
- **Streamlit**
- **Pandas** (for CSV generation)

---

## 📁 Project Structure
