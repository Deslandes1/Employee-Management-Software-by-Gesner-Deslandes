import streamlit as st
import pandas as pd
import datetime
import random
import time

# ========== PAGE CONFIGURATION ==========
st.set_page_config(
    page_title="Employee Management Software - built by Gesner Deslandes",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== COLORFUL CSS ==========
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f9f3e6 0%, #ffe6f0 100%);
    }
    .main-header {
        background: linear-gradient(90deg, #ff6b6b, #feca57, #48dbfb, #ff9ff3);
        padding: 1.5rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .card {
        background-color: white;
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: transform 0.2s;
        height: 100%;
        border-left: 8px solid #ff9ff3;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 20px;
        padding: 1rem;
        text-align: center;
    }
    .metric {
        font-size: 2rem;
        font-weight: bold;
    }
    .sidebar .sidebar-content {
        background-color: #2c3e50;
    }
    h2, h3 {
        color: #ff6b6b;
    }
    .stButton>button {
        background: linear-gradient(90deg, #ff6b6b, #feca57);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    .logout-btn {
        background: linear-gradient(90deg, #e74c3c, #c0392b) !important;
    }
    .geofence-badge {
        background-color: #00cec9;
        color: white;
        border-radius: 20px;
        padding: 0.2rem 0.8rem;
        display: inline-block;
    }
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ========== SESSION STATE ==========
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "role" not in st.session_state:
    st.session_state.role = ""

# ========== LOGIN PAGE ==========
def login_page():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 style="color: #ff6b6b;">👥 Employee Management Software</h1>
            <h3 style="color: #feca57;">built by Gesner Deslandes</h3>
            <p style="color: #555;">AI Scheduling | Geofencing | Time Tracking | Payroll Integration</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("login_form"):
            username = st.text_input("👤 Username")
            password = st.text_input("🔒 Password", type="password")
            role = st.selectbox("👨‍💼 Role", ["Admin", "Manager", "Employee"])
            submit = st.form_submit_button("🚀 Sign In", use_container_width=True)
            
            if submit:
                # Demo credentials – any non-empty works
                if username and password:
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.session_state.role = role
                    st.rerun()
                else:
                    st.error("❌ Please enter username and password.")
        
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem;">
            <p>✨ <strong>Demo credentials:</strong> any username / any password</p>
            <p>🏆 Trusted by 500+ businesses worldwide</p>
        </div>
        """, unsafe_allow_html=True)

# ========== MAIN DASHBOARD ==========
def main_dashboard():
    # Sidebar with company info, contact, and pricing
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/null/teamwork--v1.png", width=80)
        st.markdown(f"**Welcome, {st.session_state.username}**  \n👔 Role: **{st.session_state.role}**")
        st.markdown("---")
        
        # Company Information
        st.markdown("### 🌐 GlobalInternet.py")
        st.markdown("**Founder:** Gesner Deslandes")
        st.markdown("📞 **Phone / WhatsApp:** (509) 4738-5663")
        st.markdown("✉️ **Email:** deslandes78@gmail.com")
        st.markdown("🌐 [Visit our website](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
        st.markdown("---")
        
        # Competitive Price
        st.markdown("### 💰 Pricing")
        st.markdown("""
        **One‑time license:** **$12,500 USD**  
        *Full source code, 1 year support, lifetime updates*  
        
        **Monthly subscription:** **$299 USD / month**  
        *Includes all features + priority support*
        """)
        st.markdown("---")
        
        if st.button("🚪 Logout", use_container_width=True, key="logout"):
            st.session_state.authenticated = False
            st.rerun()
        
        st.markdown("---")
        st.caption("© 2026 GlobalInternet.py – built by Gesner Deslandes")
    
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>👥 Employee Management Software</h1>
        <p>built by Gesner Deslandes – AI Scheduling | Time Tracking | Geofencing | Payroll | Team Chat</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="stat-card"><div class="metric">24</div><p>Active Employees</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card"><div class="metric">168</div><p>Hours Tracked This Week</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-card"><div class="metric">98%</div><p>On-Time Attendance</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-card"><div class="metric">12</div><p>Geofenced Locations</p></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Tabs for features
    tabs = st.tabs(["🏠 Dashboard", "📅 AI Scheduling", "⏱️ Time Tracking", "📍 Geofencing", "💰 Payroll", "💬 Team Chat", "📊 Reports"])
    
    # ---------- TAB 0: DASHBOARD ----------
    with tabs[0]:
        col_left, col_right = st.columns(2)
        with col_left:
            st.subheader("📌 Today's Schedule")
            schedule_df = pd.DataFrame({
                "Employee": ["Alice Johnson", "Bob Smith", "Carol Davis", "David Lee"],
                "Shift": ["9 AM - 5 PM", "10 AM - 6 PM", "8 AM - 4 PM", "1 PM - 9 PM"],
                "Location": ["HQ", "Remote", "Site A", "HQ"]
            })
            st.dataframe(schedule_df, use_container_width=True)
        with col_right:
            st.subheader("⚠️ Alerts & Notifications")
            st.info("🔔 3 employees haven't clocked in yet.")
            st.warning("📍 Geofence violation at Site B (2 mins ago).")
            st.success("✅ Payroll for April processed successfully.")
    
    # ---------- TAB 1: AI SCHEDULING ----------
    with tabs[1]:
        st.subheader("🤖 AI-Powered Shift Scheduling")
        st.markdown("Let our AI optimize your team's schedule based on availability, skills, and labor laws.")
        
        col1, col2 = st.columns(2)
        with col1:
            num_employees = st.slider("Number of Employees", 5, 100, 20)
            shift_duration = st.selectbox("Shift Duration", ["6 hours", "8 hours", "10 hours", "12 hours"])
        with col2:
            coverage_needed = st.number_input("Minimum Employees per Shift", 2, 20, 5)
            optimize_for = st.selectbox("Optimize For", ["Cost Efficiency", "Employee Preference", "Fairness"])
        
        if st.button("🚀 Generate AI Schedule"):
            with st.spinner("AI is generating optimal schedule..."):
                time.sleep(1.5)
            st.success("✅ Schedule generated! Download as CSV.")
            st.dataframe(pd.DataFrame({
                "Date": ["2026-04-25", "2026-04-25", "2026-04-26", "2026-04-26"],
                "Shift": ["Morning", "Evening", "Morning", "Evening"],
                "Employees": ["5", "6", "7", "5"]
            }), use_container_width=True)
    
    # ---------- TAB 2: TIME TRACKING ----------
    with tabs[2]:
        st.subheader("⏱️ Real-Time Time Tracking")
        st.markdown("Employees can clock in/out with GPS verification.")
        
        col1, col2 = st.columns(2)
        with col1:
            employee_name = st.selectbox("Select Employee", ["Alice Johnson", "Bob Smith", "Carol Davis", "David Lee"])
            if st.button("🕒 Clock In"):
                st.success(f"{employee_name} clocked in at {datetime.datetime.now().strftime('%H:%M:%S')}")
        with col2:
            st.subheader("Today's Log")
            log_df = pd.DataFrame({
                "Employee": ["Alice J.", "Bob S.", "Carol D."],
                "Clock In": ["09:02 AM", "10:05 AM", "07:58 AM"],
                "Clock Out": ["05:00 PM", "06:00 PM", "04:02 PM"],
                "Total Hours": ["7.97", "7.92", "8.07"]
            })
            st.dataframe(log_df, use_container_width=True)
    
    # ---------- TAB 3: GEOFENCING ----------
    with tabs[3]:
        st.subheader("📍 Geofencing for Field Teams")
        st.markdown("Set virtual boundaries and get alerts when employees enter or leave.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🗺️ Active Geofences")
            geofences = ["HQ Office (Radius 500m)", "Site A (Construction)", "Site B (Warehouse)", "Client X Premises"]
            for gf in geofences:
                st.markdown(f'<span class="geofence-badge">{gf}</span>', unsafe_allow_html=True)
                st.markdown("")
        with col2:
            st.markdown("#### 🚨 Recent Alerts")
            st.warning("🚶 Bob Smith left Site B at 2:30 PM (unauthorized)")
            st.info("✅ Carol Davis entered HQ at 8:00 AM")
        
        if st.button("➕ Add New Geofence"):
            st.info("Open the map to draw a new geofence (feature coming soon).")
    
    # ---------- TAB 4: PAYROLL ----------
    with tabs[4]:
        st.subheader("💰 Seamless Payroll Integration")
        st.markdown("Calculate wages, taxes, and generate payslips automatically.")
        
        payroll_period = st.selectbox("Pay Period", ["April 1-15, 2026", "April 16-30, 2026", "May 1-15, 2026"])
        if st.button("📄 Generate Payroll Report"):
            st.dataframe(pd.DataFrame({
                "Employee": ["Alice Johnson", "Bob Smith", "Carol Davis"],
                "Regular Hours": [80, 85, 78],
                "Overtime": [2, 5, 0],
                "Gross Pay": ["$1,280", "$1,425", "$1,170"],
                "Net Pay": ["$1,024", "$1,140", "$936"]
            }), use_container_width=True)
            st.success("✅ Payroll report ready. Connect to your accounting software.")
    
    # ---------- TAB 5: TEAM CHAT ----------
    with tabs[5]:
        st.subheader("💬 Team Communication")
        st.markdown("Real-time messaging and announcements.")
        
        # Simple chat simulation
        messages = [
            ("Admin", "Welcome to the team chat! Use @ to mention."),
            ("Alice", "Anyone available for a quick meeting at 3 PM?"),
            ("Bob", "I'm free. Let's do it."),
        ]
        for sender, msg in messages:
            st.markdown(f"**{sender}:** {msg}")
        
        new_msg = st.text_input("Your message")
        if st.button("Send"):
            st.success("Message sent (demo mode).")
    
    # ---------- TAB 6: REPORTS ----------
    with tabs[6]:
        st.subheader("📊 Advanced Analytics & Reports")
        report_type = st.selectbox("Select Report", ["Attendance Summary", "Overtime Analysis", "Productivity by Department", "Geofence Compliance"])
        if st.button("Generate Report"):
            st.dataframe(pd.DataFrame({
                "Metric": ["Total Hours", "Late Arrivals", "Early Departures", "Geofence Violations"],
                "Value": ["1,245", "12", "5", "3"]
            }), use_container_width=True)
            st.line_chart(pd.DataFrame({
                "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
                "Hours": [185, 192, 178, 201, 195]
            }).set_index("Day"))
    
    st.markdown("---")
    st.caption("Built with 💖 by Gesner Deslandes | GlobalInternet.py")

# ========== APP ROUTING ==========
if not st.session_state.authenticated:
    login_page()
else:
    main_dashboard()
