try:
    import streamlit as st
except ModuleNotFoundError:
    print("Install streamlit using: pip install streamlit")
    import sys
    sys.exit(1)

import datetime
from collections import defaultdict
import json
import os
import random
import pandas as pd

# ================= THEME =================
def apply_theme():
    st.markdown("""
    <style>
    .stApp {
        background-color: #ECFDF3;
        color: #064E3B;
    }

    section[data-testid="stSidebar"] {
        background-color: #D1FAE5;
    }

    .stButton > button {
        background-color: #10B981;
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: 600;
        padding: 8px 16px;
    }

    .stButton > button:hover {
        background-color: #059669;
        color: white;
    }

    div[data-testid="metric-container"] {
        background-color: #D1FAE5;
        border-radius: 14px;
        padding: 16px;
        border-left: 6px solid #059669;
    }
    </style>
    """, unsafe_allow_html=True)

# ================= DATA =================
CO2 = {
    "Clothing": 6,
    "Electronics": 20,
    "Groceries": 2,
    "Furniture": 15,
    "Other": 5
}

USER_FILE = "users.json"
FEEDBACK_FILE = "feedback.json"

# ================= SESSION =================
for key, default in {
    "daily_data": defaultdict(float),
    "spending_data": defaultdict(float),
    "eco_count": 0,
    "total_count": 0,
    "log_list": [],
    "logged_in": False
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# ================= USERS =================
def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            json.dump({}, f)
    return json.load(open(USER_FILE))

def save_users(users):
    json.dump(users, open(USER_FILE, "w"))

# ================= MAIN =================
def main():
    st.set_page_config("ShopImpact 🌍", layout="wide")
    apply_theme()

    if not st.session_state.logged_in:
        login_signup()
    else:
        open_main_app()

# ================= LOGIN =================
def login_signup():
    st.title("🌍 ShopImpact")
    st.caption("Track your shopping. Protect the planet.")

    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    c1, c2 = st.columns(2)

    with c1:
        if st.button("Login"):
            users = load_users()
            if u in users and users[u] == p:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid credentials")

    with c2:
        if st.button("Sign Up"):
            users = load_users()
            if u in users:
                st.error("User exists")
            else:
                users[u] = p
                save_users(users)
                st.success("Account created")

# ================= APP =================
def open_main_app():
    st.title("🌱 ShopImpact Dashboard")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Dashboard",
        "🛒 Log Purchase",
        "📈 Analytics",
        "🏅 Rewards",
        "💬 Feedback"
    ])

    with tab1:
        dashboard_tab()

    with tab2:
        purchase_tab()

    with tab3:
        analytics_tab()

    with tab4:
        rewards_tab()

    with tab5:
        feedback_tab()

# ================= DASHBOARD =================
def dashboard_tab():
    today = datetime.date.today().isoformat()
    eco_score = int((st.session_state.eco_count / st.session_state.total_count) * 100) if st.session_state.total_count else 0

    c1, c2, c3 = st.columns(3)
    c1.metric("CO₂ Today (kg)", f"{st.session_state.daily_data[today]:.2f}")
    c2.metric("Spent Today (₹)", f"{st.session_state.spending_data[today]:.2f}")
    c3.metric("Eco Score", f"{eco_score}/100")

    st.subheader("🌿 Daily Eco Progress")
    st.progress(eco_score)

# ================= PURCHASE =================
def purchase_tab():
    st.subheader("🛒 Log New Purchase")

    product = st.text_input("Product")
    brand = st.text_input("Brand")
    category = st.selectbox("Category", CO2.keys())
    price = st.number_input("Price ₹", min_value=0.0)
    eco = st.checkbox("Eco-Friendly 🌱")

    if st.button("Add Purchase"):
        add_purchase(product, brand, category, price, eco)

def add_purchase(product, brand, category, price, eco):
    if not product or not brand:
        st.error("Fill all fields")
        return

    impact = CO2[category] * (0.7 if eco else 1)
    today = datetime.date.today().isoformat()

    st.session_state.daily_data[today] += impact
    st.session_state.spending_data[today] += price
    st.session_state.total_count += 1
    if eco:
        st.session_state.eco_count += 1

    st.session_state.log_list.append(
        f"{today}|{product}|{brand}|{category}|₹{price}|{'Eco' if eco else 'Non-Eco'}"
    )

    st.success("✅ Purchase Added")
    if eco:
        st.snow()

# ================= ANALYTICS =================
def analytics_tab():
    if not st.session_state.log_list:
        st.info("No data yet")
        return

    st.subheader("📊 Daily CO₂ Trend")

    df = pd.DataFrame(
        list(st.session_state.daily_data.items()),
        columns=["Date", "CO₂"]
    )
    df["Date"] = pd.to_datetime(df["Date"])
    st.line_chart(df.set_index("Date"))

    show_visual_analytics()

# ================= VISUAL =================
def show_visual_analytics():
    category_co2 = defaultdict(float)
    for log in st.session_state.log_list:
        p = log.split("|")
        category = p[3]
        eco = "Eco" in p[5]
        impact = CO2[category] * (0.7 if eco else 1)
        category_co2[category] += impact

    df = pd.DataFrame({
        "Category": category_co2.keys(),
        "CO₂": category_co2.values()
    })

    st.bar_chart(df.set_index("Category"))

# ================= REWARDS =================
def rewards_tab():
    eco = st.session_state.eco_count
    st.subheader("🏅 Eco Achievements")

    if eco >= 30:
        st.success("🏆 Eco Legend")
        st.balloons()
    elif eco >= 15:
        st.success("🏅 Eco Warrior")
    elif eco >= 5:
        st.success("🎖️ Eco Beginner")
    else:
        st.info("Start making eco-friendly choices!")

# ================= FEEDBACK =================
def feedback_tab():
    st.subheader("💬 Feedback")

    name = st.text_input("Name")
    feedback = st.text_area("Your feedback")

    if st.button("Submit Feedback"):
        if not name or not feedback:
            st.error("Fill all fields")
            return

        data = []
        if os.path.exists(FEEDBACK_FILE):
            data = json.load(open(FEEDBACK_FILE))

        data.append({
            "name": name,
            "feedback": feedback,
            "date": str(datetime.date.today())
        })

        json.dump(data, open(FEEDBACK_FILE, "w"), indent=2)
        st.success("Thank you for your feedback 💚")

# ================= RUN =================
if __name__ == "__main__":
    main()
