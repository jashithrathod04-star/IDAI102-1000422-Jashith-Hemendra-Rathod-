try:
    import streamlit as st
except ModuleNotFoundError:
    print("Error: Streamlit module not found. Please install it using 'pip install streamlit' before running this app.")
    import sys
    sys.exit(1)

import datetime
from collections import defaultdict
import json
import os
import random
import pandas as pd

def apply_theme():
    st.markdown("""
    <style>
    .stApp {
        background-color: #0c7c37;
        color: #041107;
    }

    section[data-testid="stSidebar"] {
        background-color: #87ee8c;
    }

    .stButton > button {
        background-color: #dae8df;
        color: #041107;
        border-radius: 12px;
        border: none;
        font-weight: 600;
        padding: 8px 16px;
    }

    .stButton > button:hover {
        background-color: #87ee8c;
    }

    input, textarea, select {
        border-radius: 10px !important;
        border: 1px solid #041107 !important;
    }

    div[data-testid="metric-container"] {
        background-color: #87ee8c;
        border-radius: 14px;
        padding: 14px;
        border-left: 6px solid #041107;
    }

    div[data-testid="stProgress"] > div > div {
        background-color: #041107;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------- DATA ----------------
CO2 = {
    "Clothing": 6,
    "Electronics": 20,
    "Groceries": 2,
    "Furniture": 15,
    "Other": 5
}

# ---------------- SESSION STATE ----------------
if 'daily_data' not in st.session_state:
    st.session_state.daily_data = defaultdict(float)
if 'spending_data' not in st.session_state:
    st.session_state.spending_data = defaultdict(float)
if 'eco_count' not in st.session_state:
    st.session_state.eco_count = 0
if 'total_count' not in st.session_state:
    st.session_state.total_count = 0
if 'log_list' not in st.session_state:
    st.session_state.log_list = []
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

USER_FILE = "users.json"

# ---------------- MOTIVATIONAL QUOTES ----------------
QUOTES = [
    "🌱 Every small eco-friendly choice counts!",
    "💚 Your green habits shape the planet's future!",
    "🌿 Sustainability is not a trend, it is a responsibility.",
    "♻️ Choose wisely today for a healthier tomorrow.",
    "🌎 Small actions, global impact."
]

# ---------------- USER MANAGEMENT ----------------
def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            json.dump({}, f)
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

# ---------------- AI SUGGESTION ----------------
def ai_suggestion(category, eco):
    if eco:
        return "AI Insight: Excellent sustainable choice 🌿 Keep reinforcing this habit."
    return f"AI Insight: Switching to an eco-friendly {category.lower()} option could reduce CO₂ emissions by approximately 30%."

# ---------------- MAIN ----------------
def main():
    st.set_page_config(page_title="ShopImpact 🌍", layout="wide")
    apply_theme()   # 👈 ADD THIS LINE
    if not st.session_state.logged_in:
        login_signup()
    else:
        open_main_app()

# ---------------- LOGIN / SIGNUP ----------------
def login_signup():
    st.title("Welcome to ShopImpact 🌍")
    st.caption("Track your purchases. Understand your impact. Choose a greener future.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            users = load_users()
            if username in users and users[username] == password:
                st.success(f"Welcome back, {username}!")
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid username or password.")

    with col2:
        if st.button("Sign Up"):
            users = load_users()
            if not username or not password:
                st.error("Please enter both username and password.")
                return
            if username in users:
                st.error("Username already exists.")
                return
            users[username] = password
            save_users(users)
            st.success("Account created successfully. Please login.")

# ---------------- MAIN APP ----------------
def open_main_app():
    st.title("ShopImpact 🌍 – Conscious Shopping Dashboard")
    

    today = datetime.date.today().isoformat()
    daily_co2 = st.session_state.daily_data.get(today, 0)
    daily_spend = st.session_state.spending_data.get(today, 0)
    eco_score = int((st.session_state.eco_count / st.session_state.total_count) * 100) if st.session_state.total_count else 0

    col1, col2, col3 = st.columns(3)
    col1.metric("CO₂ Emissions Today (kg)", f"{daily_co2:.2f}")
    col2.metric("Amount Spent Today (₹)", f"{daily_spend:.2f}")
    col3.metric("Eco Score", f"{eco_score}/100")
    st.subheader("🌿 Eco Progress")
    progress = st.progress(0)

    for i in range(eco_score + 1):
     progress.progress(i)

    st.markdown("""
<style>
.glow {
    font-size: 42px;
    animation: glow 1.5s ease-in-out infinite alternate;
}
@keyframes glow {
    from { text-shadow: 0 0 5px #7CFF9E; }
    to { text-shadow: 0 0 20px #1DB954; }
}
</style>
""", unsafe_allow_html=True)
    
    


    st.divider()

    st.subheader("Log a New Purchase")
    product = st.text_input("Product Name")
    brand = st.text_input("Brand")
    category = st.selectbox("Category", list(CO2.keys()))
    price = st.number_input("Price (₹)", min_value=0.0, format="%.2f")
    eco = st.checkbox("Eco-Friendly Choice 🌱")

    if st.button("Add Purchase"):
        add_purchase(product, brand, category, price, eco)

    st.subheader("Purchase History")
    for log in reversed(st.session_state.log_list):
        st.text(log)

    if st.session_state.log_list:
        last_log = st.session_state.log_list[-1]
        last_category = last_log.split('|')[3].strip()
        last_eco = 'Eco' in last_log
        st.info(ai_suggestion(last_category, last_eco))

    st.subheader("Insights & Tools")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("Top Eco Category"):
            top_eco_category()
    with c2:
        if st.button("Eco Streak"):
            eco_streak()
    with c3:
        if st.button("Weekly Summary"):
            weekly_summary()
    with c4:
        if st.button("Eco Savings"):
            eco_savings()

    st.subheader("Download Your Report")
    download_csv()

    st.success(random.choice(QUOTES))
    check_awards()
    show_badges()
    show_visual_analytics()






# ---------------- ADD PURCHASE ----------------
def add_purchase(product, brand, category, price, eco):
    if not product.strip() or not brand.strip():
        st.error("❌ Please enter a valid product name and brand.")
        return

    with st.spinner("💾 Saving your purchase..."):
        impact = CO2[category]

        if eco:
            impact *= 0.7
            st.session_state.eco_count += 1

        today = datetime.date.today().isoformat()
        st.session_state.daily_data[today] += impact
        st.session_state.spending_data[today] += price
        st.session_state.total_count += 1

        log = f"{today} | {product} | {brand} | {category} | ₹{price} | {'Eco' if eco else 'Non-Eco'}"
        st.session_state.log_list.append(log)

    # ---------- PURCHASE CONFIRMED UX ----------
    st.success("✅ Purchase Confirmed!")

    st.markdown(
        f"""
        <div style="
            background-color:#E8FFF3;
            padding:16px;
            border-radius:12px;
            border-left:6px solid #2ECC71;
            margin-top:10px;
        ">
            <b>🛒 Product:</b> {product}<br>
            <b>🏷 Brand:</b> {brand}<br>
            <b>📦 Category:</b> {category}<br>
            <b>💰 Price:</b> ₹{price:.2f}<br>
            <b>🌱 Choice:</b> {"Eco-Friendly" if eco else "Standard"}
        </div>
        """,
        unsafe_allow_html=True
    )

    if eco:
        st.snow()
        st.info("🌍 Thank you for choosing a sustainable option!")
    else:
        st.warning("♻️ Consider eco-friendly alternatives to reduce impact.")



# ---------------- CSV DOWNLOAD ----------------
def download_csv():
    if not st.session_state.log_list:
        st.info("No data available to download yet.")
        return

    records = []
    for log in st.session_state.log_list:
        parts = [p.strip() for p in log.split('|')]
        records.append({
            "Date": parts[0],
            "Product": parts[1],
            "Brand": parts[2],
            "Category": parts[3],
            "Price (₹)": parts[4].replace('₹', ''),
            "Eco Friendly": parts[5]
        })

    df = pd.DataFrame(records)
    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="⬇️ Download CSV Report",
        data=csv,
        file_name="shopimpact_report.csv",
        mime="text/csv"
    )

# ---------------- AWARDS ----------------
def check_awards():
    eco = st.session_state.eco_count
    if eco >= 30:
        st.success("🏆 Eco Legend – Outstanding commitment to sustainability!")
        st.balloons()

    elif eco >= 15:
        st.success("🏅 Eco Warrior – You are making a difference!")
        st.balloons()

    elif eco >= 5:
        st.success("🎖️ Eco Beginner – A great sustainable start!")
        st.balloons()


# ---------------- FEATURES ----------------
def top_eco_category():
    data = defaultdict(int)
    for log in st.session_state.log_list:
        if 'Eco' in log:
            category = log.split('|')[3].strip()
            data[category] += 1
    if data:
        st.info(f"Your most eco-conscious purchases are in the **{max(data, key=data.get)}** category.")
    else:
        st.info("No eco-friendly purchases logged yet.")

def eco_streak():
    days = sorted(st.session_state.daily_data.keys())
    streak = max_streak = 0
    for d in days:
        if any('Eco' in log and d in log for log in st.session_state.log_list):
            streak += 1
        else:
            streak = 0
        max_streak = max(max_streak, streak)
    st.info(f"Your longest eco-friendly streak is **{max_streak} day(s)**.")

def weekly_summary():
    today = datetime.date.today()
    last_week = [(today - datetime.timedelta(days=i)).isoformat() for i in range(7)]
    co2 = sum(st.session_state.daily_data.get(d, 0) for d in last_week)
    spend = sum(st.session_state.spending_data.get(d, 0) for d in last_week)
    ratio = (st.session_state.eco_count / st.session_state.total_count * 100) if st.session_state.total_count else 0
    st.info(f"Weekly Summary 🌿\nCO₂ Emissions: {co2:.2f} kg\nTotal Spend: ₹{spend:.2f}\nEco Ratio: {ratio:.0f}%")

def eco_savings():
    saved = 0
    for log in st.session_state.log_list:
        if 'Eco' in log:
            price = float(log.split('|')[4].replace('₹', '').strip())
            saved += price * 0.3
    st.info(f"Estimated savings from eco-friendly choices: **₹{saved:.2f}**")
def show_badges():
    eco = st.session_state.eco_count
    

    st.subheader("🏅 Your Eco Badges")

    st.image(
    "https://pngtree.com/so/eco-friendly-logo",
    width=200
)


    b1, b2, b3 = st.columns(3)

    with b1:
        if eco >= 5:
            st.success("🎖️ Eco Beginner\n(5 Eco Purchases)")
        else:
            st.info("🔒 Eco Beginner\n(5 Eco Purchases)")

    with b2:
        if eco >= 15:
            st.success("🏅 Eco Warrior\n(15 Eco Purchases)")
        else:
            st.info("🔒 Eco Warrior\n(15 Eco Purchases)")

    with b3:
        if eco >= 30:
            st.markdown('<div class="glow">🏆 Eco Legend</div>', unsafe_allow_html=True)
        else:
            st.info("🔒 Eco Legend\n(30 Eco Purchases)")

def show_visual_analytics():
    st.subheader("📊 Visual Analytics")

    if not st.session_state.log_list:
        st.info("Log purchases to view analytics.")
        return

    # -------- Category-wise CO2 --------
    category_co2 = defaultdict(float)

    for log in st.session_state.log_list:
        parts = [p.strip() for p in log.split('|')]
        category = parts[3]
        eco = parts[5] == "Eco"

        impact = CO2[category]
        if eco:
            impact *= 0.7

        category_co2[category] += impact

    df_co2 = pd.DataFrame({
        "Category": category_co2.keys(),
        "CO₂ Emissions (kg)": category_co2.values()
    })

    st.markdown("**CO₂ Emissions by Category**")
    st.bar_chart(df_co2.set_index("Category"))

    # -------- Eco vs Non-Eco --------
    eco_count = sum(1 for log in st.session_state.log_list if "Eco" in log)
    non_eco_count = len(st.session_state.log_list) - eco_count

    df_eco = pd.DataFrame({
        "Type": ["Eco-Friendly", "Non-Eco"],
        "Count": [eco_count, non_eco_count]
    })

    st.markdown("**Eco vs Non-Eco Purchases**")
    st.bar_chart(df_eco.set_index("Type"))

# ---------------- RUN ----------------

if __name__ == '__main__':
    main()
