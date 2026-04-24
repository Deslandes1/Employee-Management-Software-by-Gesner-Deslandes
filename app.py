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

# ========== INITIALIZE SESSION STATE ==========
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "role" not in st.session_state:
    st.session_state.role = ""
if "language" not in st.session_state:
    st.session_state.language = "en"  # default English

# ========== TRANSLATION DICTIONARIES ==========
lang_en = {
    "app_title": "Employee Management Software",
    "app_subtitle": "built by Gesner Deslandes",
    "tagline": "AI Scheduling | Geofencing | Time Tracking | Payroll Integration",
    "login_header": "👥 Employee Management Software",
    "login_subheader": "built by Gesner Deslandes",
    "username": "👤 Username",
    "password": "🔒 Password",
    "role": "👨‍💼 Role",
    "sign_in": "🚀 Sign In",
    "demo_note": "✨ Demo credentials: any username / any password",
    "trusted": "🏆 Trusted by 500+ businesses worldwide",
    "welcome": "Welcome",
    "role_label": "Role",
    "company_info": "🌐 GlobalInternet.py",
    "founder": "Founder: Gesner Deslandes",
    "phone": "📞 Phone / WhatsApp: (509) 4738-5663",
    "email": "✉️ Email: deslandes78@gmail.com",
    "website": "🌐 Visit our website",
    "price_title": "💰 Pricing",
    "price_one_time": "**One‑time license:** **$12,500 USD**  \n*Full source code, 1 year support, lifetime updates*",
    "price_monthly": "**Monthly subscription:** **$299 USD / month**  \n*All features + priority support*",
    "logout": "🚪 Logout",
    "copyright": "© 2026 GlobalInternet.py – built by Gesner Deslandes",
    "main_header": "👥 Employee Management Software",
    "main_subheader": "built by Gesner Deslandes – AI Scheduling | Time Tracking | Geofencing | Payroll | Team Chat",
    "active_employees": "Active Employees",
    "hours_tracked": "Hours Tracked This Week",
    "ontime_attendance": "On-Time Attendance",
    "geofenced_locations": "Geofenced Locations",
    "tab_dashboard": "🏠 Dashboard",
    "tab_scheduling": "📅 AI Scheduling",
    "tab_timetrack": "⏱️ Time Tracking",
    "tab_geofence": "📍 Geofencing",
    "tab_payroll": "💰 Payroll",
    "tab_chat": "💬 Team Chat",
    "tab_reports": "📊 Reports",
    "today_schedule": "📌 Today's Schedule",
    "employee_col": "Employee",
    "shift_col": "Shift",
    "location_col": "Location",
    "alerts_notifications": "⚠️ Alerts & Notifications",
    "alert1": "🔔 3 employees haven't clocked in yet.",
    "alert2": "📍 Geofence violation at Site B (2 mins ago).",
    "alert3": "✅ Payroll for April processed successfully.",
    "ai_scheduling_title": "🤖 AI-Powered Shift Scheduling",
    "ai_scheduling_desc": "Let our AI optimize your team's schedule based on availability, skills, and labor laws.",
    "num_employees": "Number of Employees",
    "shift_duration": "Shift Duration",
    "min_employees": "Minimum Employees per Shift",
    "optimize_for": "Optimize For",
    "cost_efficiency": "Cost Efficiency",
    "employee_preference": "Employee Preference",
    "fairness": "Fairness",
    "generate_schedule": "🚀 Generate AI Schedule",
    "generating": "AI is generating optimal schedule...",
    "schedule_success": "✅ Schedule generated! Download as CSV.",
    "date_col": "Date",
    "employees_col": "Employees",
    "time_tracking_title": "⏱️ Real-Time Time Tracking",
    "time_tracking_desc": "Employees can clock in/out with GPS verification.",
    "select_employee": "Select Employee",
    "clock_in": "🕒 Clock In",
    "clocked_in": "clocked in at",
    "today_log": "Today's Log",
    "clock_in_col": "Clock In",
    "clock_out_col": "Clock Out",
    "total_hours_col": "Total Hours",
    "geofencing_title": "📍 Geofencing for Field Teams",
    "geofencing_desc": "Set virtual boundaries and get alerts when employees enter or leave.",
    "active_geofences": "🗺️ Active Geofences",
    "recent_alerts": "🚨 Recent Alerts",
    "alert_geofence_violation": "🚶 Bob Smith left Site B at 2:30 PM (unauthorized)",
    "alert_geofence_entry": "✅ Carol Davis entered HQ at 8:00 AM",
    "add_geofence": "➕ Add New Geofence",
    "geofence_coming": "Open the map to draw a new geofence (feature coming soon).",
    "payroll_title": "💰 Seamless Payroll Integration",
    "payroll_desc": "Calculate wages, taxes, and generate payslips automatically.",
    "pay_period": "Pay Period",
    "generate_payroll": "📄 Generate Payroll Report",
    "regular_hours": "Regular Hours",
    "overtime": "Overtime",
    "gross_pay": "Gross Pay",
    "net_pay": "Net Pay",
    "payroll_success": "✅ Payroll report ready. Connect to your accounting software.",
    "team_chat_title": "💬 Team Communication",
    "team_chat_desc": "Real-time messaging and announcements.",
    "chat_admin": "Admin",
    "chat_welcome": "Welcome to the team chat! Use @ to mention.",
    "chat_alice": "Anyone available for a quick meeting at 3 PM?",
    "chat_bob": "I'm free. Let's do it.",
    "your_message": "Your message",
    "send": "Send",
    "message_sent": "Message sent (demo mode).",
    "reports_title": "📊 Advanced Analytics & Reports",
    "select_report": "Select Report",
    "attendance_summary": "Attendance Summary",
    "overtime_analysis": "Overtime Analysis",
    "productivity_dept": "Productivity by Department",
    "geofence_compliance": "Geofence Compliance",
    "generate_report": "Generate Report",
    "metric_col": "Metric",
    "value_col": "Value",
    "total_hours_metric": "Total Hours",
    "late_arrivals_metric": "Late Arrivals",
    "early_departures_metric": "Early Departures",
    "geofence_violations_metric": "Geofence Violations",
    "day_col": "Day",
    "hours_col": "Hours",
    "language": "🌐 Language",
    "english": "English",
    "spanish": "Español",
    "french": "Français"
}

lang_es = {
    "app_title": "Software de Gestión de Empleados",
    "app_subtitle": "construido por Gesner Deslandes",
    "tagline": "Programación IA | Geocercas | Control Horario | Integración de Nóminas",
    "login_header": "👥 Software de Gestión de Empleados",
    "login_subheader": "construido por Gesner Deslandes",
    "username": "👤 Usuario",
    "password": "🔒 Contraseña",
    "role": "👨‍💼 Rol",
    "sign_in": "🚀 Iniciar Sesión",
    "demo_note": "✨ Credenciales de demostración: cualquier usuario / cualquier contraseña",
    "trusted": "🏆 Confiable por más de 500 empresas en todo el mundo",
    "welcome": "Bienvenido",
    "role_label": "Rol",
    "company_info": "🌐 GlobalInternet.py",
    "founder": "Fundador: Gesner Deslandes",
    "phone": "📞 Teléfono / WhatsApp: (509) 4738-5663",
    "email": "✉️ Correo electrónico: deslandes78@gmail.com",
    "website": "🌐 Visite nuestro sitio web",
    "price_title": "💰 Precios",
    "price_one_time": "**Licencia única:** **$12,500 USD**  \n*Código fuente completo, 1 año de soporte, actualizaciones de por vida*",
    "price_monthly": "**Suscripción mensual:** **$299 USD / mes**  \n*Todas las funciones + soporte prioritario*",
    "logout": "🚪 Cerrar Sesión",
    "copyright": "© 2026 GlobalInternet.py – construido por Gesner Deslandes",
    "main_header": "👥 Software de Gestión de Empleados",
    "main_subheader": "construido por Gesner Deslandes – Programación IA | Control Horario | Geocercas | Nóminas | Chat en Equipo",
    "active_employees": "Empleados Activos",
    "hours_tracked": "Horas Registradas Esta Semana",
    "ontime_attendance": "Asistencia Puntual",
    "geofenced_locations": "Ubicaciones con Geocerca",
    "tab_dashboard": "🏠 Panel",
    "tab_scheduling": "📅 Programación IA",
    "tab_timetrack": "⏱️ Control Horario",
    "tab_geofence": "📍 Geocercas",
    "tab_payroll": "💰 Nóminas",
    "tab_chat": "💬 Chat de Equipo",
    "tab_reports": "📊 Informes",
    "today_schedule": "📌 Horario de Hoy",
    "employee_col": "Empleado",
    "shift_col": "Turno",
    "location_col": "Ubicación",
    "alerts_notifications": "⚠️ Alertas y Notificaciones",
    "alert1": "🔔 3 empleados no han marcado entrada aún.",
    "alert2": "📍 Violación de geocerca en Sitio B (hace 2 minutos).",
    "alert3": "✅ Nómina de abril procesada exitosamente.",
    "ai_scheduling_title": "🤖 Programación de Turnos con IA",
    "ai_scheduling_desc": "Permita que nuestra IA optimice el horario de su equipo según disponibilidad, habilidades y leyes laborales.",
    "num_employees": "Número de Empleados",
    "shift_duration": "Duración del Turno",
    "min_employees": "Mínimo de Empleados por Turno",
    "optimize_for": "Optimizar para",
    "cost_efficiency": "Eficiencia de Costos",
    "employee_preference": "Preferencia del Empleado",
    "fairness": "Equidad",
    "generate_schedule": "🚀 Generar Horario con IA",
    "generating": "La IA está generando el horario óptimo...",
    "schedule_success": "✅ Horario generado! Descargar como CSV.",
    "date_col": "Fecha",
    "employees_col": "Empleados",
    "time_tracking_title": "⏱️ Control Horario en Tiempo Real",
    "time_tracking_desc": "Los empleados pueden marcar entrada/salida con verificación GPS.",
    "select_employee": "Seleccionar Empleado",
    "clock_in": "🕒 Marcar Entrada",
    "clocked_in": "marcó entrada a las",
    "today_log": "Registro de Hoy",
    "clock_in_col": "Entrada",
    "clock_out_col": "Salida",
    "total_hours_col": "Horas Totales",
    "geofencing_title": "📍 Geocercas para Equipos de Campo",
    "geofencing_desc": "Establezca límites virtuales y reciba alertas cuando los empleados entren o salgan.",
    "active_geofences": "🗺️ Geocercas Activas",
    "recent_alerts": "🚨 Alertas Recientes",
    "alert_geofence_violation": "🚶 Bob Smith salió del Sitio B a las 2:30 PM (no autorizado)",
    "alert_geofence_entry": "✅ Carol Davis entró a la oficina central a las 8:00 AM",
    "add_geofence": "➕ Agregar Nueva Geocerca",
    "geofence_coming": "Abra el mapa para dibujar una nueva geocerca (función próximamente).",
    "payroll_title": "💰 Integración de Nóminas sin Esfuerzo",
    "payroll_desc": "Calcule salarios, impuestos y genere recibos de pago automáticamente.",
    "pay_period": "Período de Pago",
    "generate_payroll": "📄 Generar Reporte de Nómina",
    "regular_hours": "Horas Normales",
    "overtime": "Horas Extras",
    "gross_pay": "Salario Bruto",
    "net_pay": "Salario Neto",
    "payroll_success": "✅ Reporte de nómina listo. Conéctelo a su software contable.",
    "team_chat_title": "💬 Comunicación en Equipo",
    "team_chat_desc": "Mensajería en tiempo real y anuncios.",
    "chat_admin": "Administrador",
    "chat_welcome": "¡Bienvenido al chat del equipo! Use @ para mencionar.",
    "chat_alice": "¿Alguien disponible para una reunión rápida a las 3 PM?",
    "chat_bob": "Estoy libre. Hagámoslo.",
    "your_message": "Su mensaje",
    "send": "Enviar",
    "message_sent": "Mensaje enviado (modo demostración).",
    "reports_title": "📊 Informes Avanzados y Analítica",
    "select_report": "Seleccionar Informe",
    "attendance_summary": "Resumen de Asistencia",
    "overtime_analysis": "Análisis de Horas Extras",
    "productivity_dept": "Productividad por Departamento",
    "geofence_compliance": "Cumplimiento de Geocercas",
    "generate_report": "Generar Informe",
    "metric_col": "Métrica",
    "value_col": "Valor",
    "total_hours_metric": "Horas Totales",
    "late_arrivals_metric": "Llegadas Tarde",
    "early_departures_metric": "Salidas Tempranas",
    "geofence_violations_metric": "Violaciones de Geocerca",
    "day_col": "Día",
    "hours_col": "Horas",
    "language": "🌐 Idioma",
    "english": "Inglés",
    "spanish": "Español",
    "french": "Francés"
}

lang_fr = {
    "app_title": "Logiciel de Gestion des Employés",
    "app_subtitle": "construit par Gesner Deslandes",
    "tagline": "Planification IA | Géorepérage | Suivi du Temps | Intégration Paie",
    "login_header": "👥 Logiciel de Gestion des Employés",
    "login_subheader": "construit par Gesner Deslandes",
    "username": "👤 Nom d'utilisateur",
    "password": "🔒 Mot de passe",
    "role": "👨‍💼 Rôle",
    "sign_in": "🚀 Se connecter",
    "demo_note": "✨ Identifiants de démonstration : n'importe quel nom d'utilisateur / mot de passe",
    "trusted": "🏆 Approuvé par plus de 500 entreprises dans le monde",
    "welcome": "Bienvenue",
    "role_label": "Rôle",
    "company_info": "🌐 GlobalInternet.py",
    "founder": "Fondateur : Gesner Deslandes",
    "phone": "📞 Téléphone / WhatsApp : (509) 4738-5663",
    "email": "✉️ Email : deslandes78@gmail.com",
    "website": "🌐 Visitez notre site web",
    "price_title": "💰 Tarifs",
    "price_one_time": "**Licence unique :** **12 500 $ USD**  \n*Code source complet, 1 an de support, mises à jour à vie*",
    "price_monthly": "**Abonnement mensuel :** **299 $ USD / mois**  \n*Toutes les fonctionnalités + support prioritaire*",
    "logout": "🚪 Déconnexion",
    "copyright": "© 2026 GlobalInternet.py – construit par Gesner Deslandes",
    "main_header": "👥 Logiciel de Gestion des Employés",
    "main_subheader": "construit par Gesner Deslandes – Planification IA | Suivi du temps | Géorepérage | Paie | Chat d'équipe",
    "active_employees": "Employés actifs",
    "hours_tracked": "Heures suivies cette semaine",
    "ontime_attendance": "Présence ponctuelle",
    "geofenced_locations": "Emplacements géorepérés",
    "tab_dashboard": "🏠 Tableau de bord",
    "tab_scheduling": "📅 Planification IA",
    "tab_timetrack": "⏱️ Suivi du temps",
    "tab_geofence": "📍 Géorepérage",
    "tab_payroll": "💰 Paie",
    "tab_chat": "💬 Chat d'équipe",
    "tab_reports": "📊 Rapports",
    "today_schedule": "📌 Planning du jour",
    "employee_col": "Employé",
    "shift_col": "Quart",
    "location_col": "Emplacement",
    "alerts_notifications": "⚠️ Alertes et notifications",
    "alert1": "🔔 3 employés n'ont pas encore pointé.",
    "alert2": "📍 Violation de géorepérage au Site B (il y a 2 minutes).",
    "alert3": "✅ Paie d'avril traitée avec succès.",
    "ai_scheduling_title": "🤖 Planification des quarts par IA",
    "ai_scheduling_desc": "Laissez notre IA optimiser le planning de votre équipe en fonction des disponibilités, compétences et lois du travail.",
    "num_employees": "Nombre d'employés",
    "shift_duration": "Durée du quart",
    "min_employees": "Minimum d'employés par quart",
    "optimize_for": "Optimiser pour",
    "cost_efficiency": "Efficacité des coûts",
    "employee_preference": "Préférence des employés",
    "fairness": "Équité",
    "generate_schedule": "🚀 Générer le planning IA",
    "generating": "L'IA génère le planning optimal...",
    "schedule_success": "✅ Planning généré ! Télécharger en CSV.",
    "date_col": "Date",
    "employees_col": "Employés",
    "time_tracking_title": "⏱️ Suivi du temps en temps réel",
    "time_tracking_desc": "Les employés peuvent pointer entrée/sortie avec vérification GPS.",
    "select_employee": "Sélectionner un employé",
    "clock_in": "🕒 Pointer",
    "clocked_in": "a pointé à",
    "today_log": "Journal du jour",
    "clock_in_col": "Entrée",
    "clock_out_col": "Sortie",
    "total_hours_col": "Total heures",
    "geofencing_title": "📍 Géorepérage pour équipes terrain",
    "geofencing_desc": "Définissez des limites virtuelles et recevez des alertes quand les employés entrent ou sortent.",
    "active_geofences": "🗺️ Géorepérages actifs",
    "recent_alerts": "🚨 Alertes récentes",
    "alert_geofence_violation": "🚶 Bob Smith a quitté le Site B à 14h30 (non autorisé)",
    "alert_geofence_entry": "✅ Carol Davis est entrée au siège à 8h00",
    "add_geofence": "➕ Ajouter un géorepérage",
    "geofence_coming": "Ouvrez la carte pour dessiner un nouveau géorepérage (fonction à venir).",
    "payroll_title": "💰 Intégration paie simplifiée",
    "payroll_desc": "Calculez les salaires, taxes et générez les bulletins automatiquement.",
    "pay_period": "Période de paie",
    "generate_payroll": "📄 Générer le rapport de paie",
    "regular_hours": "Heures normales",
    "overtime": "Heures supplémentaires",
    "gross_pay": "Salaire brut",
    "net_pay": "Salaire net",
    "payroll_success": "✅ Rapport de paie prêt. Connectez‑le à votre logiciel comptable.",
    "team_chat_title": "💬 Communication d'équipe",
    "team_chat_desc": "Messagerie en temps réel et annonces.",
    "chat_admin": "Admin",
    "chat_welcome": "Bienvenue sur le chat d'équipe ! Utilisez @ pour mentionner.",
    "chat_alice": "Quelqu'un est disponible pour une réunion rapide à 15h ?",
    "chat_bob": "Je suis libre. Allons‑y.",
    "your_message": "Votre message",
    "send": "Envoyer",
    "message_sent": "Message envoyé (mode démonstration).",
    "reports_title": "📊 Rapports avancés et analyses",
    "select_report": "Sélectionner un rapport",
    "attendance_summary": "Résumé des présences",
    "overtime_analysis": "Analyse des heures supplémentaires",
    "productivity_dept": "Productivité par département",
    "geofence_compliance": "Conformité des géorepérages",
    "generate_report": "Générer le rapport",
    "metric_col": "Métrique",
    "value_col": "Valeur",
    "total_hours_metric": "Heures totales",
    "late_arrivals_metric": "Arrivées en retard",
    "early_departures_metric": "Départs anticipés",
    "geofence_violations_metric": "Violations de géorepérage",
    "day_col": "Jour",
    "hours_col": "Heures",
    "language": "🌐 Langue",
    "english": "Anglais",
    "spanish": "Espagnol",
    "french": "Français"
}

# ========== HELPER FUNCTION ==========
def get_text(key):
    if st.session_state.language == "es":
        return lang_es.get(key, key)
    elif st.session_state.language == "fr":
        return lang_fr.get(key, key)
    else:
        return lang_en.get(key, key)

# ========== LANGUAGE SELECTOR ==========
def language_selector():
    lang_options = {"en": get_text("english"), "es": get_text("spanish"), "fr": get_text("french")}
    selected = st.selectbox(
        get_text("language"),
        options=list(lang_options.keys()),
        format_func=lambda x: lang_options[x],
        index=["en","es","fr"].index(st.session_state.language)
    )
    if selected != st.session_state.language:
        st.session_state.language = selected
        st.rerun()

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

# ========== LOGIN PAGE ==========
def login_page():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 style="color: #ff6b6b;">👥 {get_text('app_title')}</h1>
            <h3 style="color: #feca57;">{get_text('app_subtitle')}</h3>
            <p style="color: #555;">{get_text('tagline')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Language selector in login page
        language_selector()
        
        with st.form("login_form"):
            username = st.text_input(get_text("username"))
            password = st.text_input(get_text("password"), type="password")
            role = st.selectbox(get_text("role"), ["Admin", "Manager", "Employee"])
            submit = st.form_submit_button(get_text("sign_in"), use_container_width=True)
            
            if submit:
                if username and password:
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.session_state.role = role
                    st.rerun()
                else:
                    st.error("❌ Please enter username and password.")
        
        st.markdown(f"""
        <div style="text-align: center; margin-top: 2rem;">
            <p>✨ <strong>{get_text('demo_note')}</strong></p>
            <p>{get_text('trusted')}</p>
        </div>
        """, unsafe_allow_html=True)

# ========== MAIN DASHBOARD ==========
def main_dashboard():
    # Sidebar with language selector, company info, pricing, logout
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/null/teamwork--v1.png", width=80)
        st.markdown(f"**{get_text('welcome')}, {st.session_state.username}**  \n👔 {get_text('role_label')}: **{st.session_state.role}**")
        st.markdown("---")
        
        # Language selector (also in sidebar)
        language_selector()
        st.markdown("---")
        
        # Company Information
        st.markdown(f"### {get_text('company_info')}")
        st.markdown(f"**{get_text('founder')}**")
        st.markdown(f"{get_text('phone')}")
        st.markdown(f"{get_text('email')}")
        st.markdown(f"[{get_text('website')}](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
        st.markdown("---")
        
        # Competitive Price
        st.markdown(f"### {get_text('price_title')}")
        st.markdown(get_text("price_one_time"))
        st.markdown("")
        st.markdown(get_text("price_monthly"))
        st.markdown("---")
        
        if st.button(get_text("logout"), use_container_width=True, key="logout"):
            st.session_state.authenticated = False
            st.rerun()
        
        st.markdown("---")
        st.caption(get_text("copyright"))
    
    # Main header
    st.markdown(f"""
    <div class="main-header">
        <h1>{get_text('main_header')}</h1>
        <p>{get_text('main_subheader')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div class="stat-card"><div class="metric">24</div><p>{get_text("active_employees")}</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="stat-card"><div class="metric">168</div><p>{get_text("hours_tracked")}</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="stat-card"><div class="metric">98%</div><p>{get_text("ontime_attendance")}</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="stat-card"><div class="metric">12</div><p>{get_text("geofenced_locations")}</p></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Tabs for features
    tabs = st.tabs([
        get_text("tab_dashboard"),
        get_text("tab_scheduling"),
        get_text("tab_timetrack"),
        get_text("tab_geofence"),
        get_text("tab_payroll"),
        get_text("tab_chat"),
        get_text("tab_reports")
    ])
    
    # ---------- TAB 0: DASHBOARD ----------
    with tabs[0]:
        col_left, col_right = st.columns(2)
        with col_left:
            st.subheader(get_text("today_schedule"))
            schedule_df = pd.DataFrame({
                get_text("employee_col"): ["Alice Johnson", "Bob Smith", "Carol Davis", "David Lee"],
                get_text("shift_col"): ["9 AM - 5 PM", "10 AM - 6 PM", "8 AM - 4 PM", "1 PM - 9 PM"],
                get_text("location_col"): ["HQ", "Remote", "Site A", "HQ"]
            })
            st.dataframe(schedule_df, use_container_width=True)
        with col_right:
            st.subheader(get_text("alerts_notifications"))
            st.info(get_text("alert1"))
            st.warning(get_text("alert2"))
            st.success(get_text("alert3"))
    
    # ---------- TAB 1: AI SCHEDULING ----------
    with tabs[1]:
        st.subheader(get_text("ai_scheduling_title"))
        st.markdown(get_text("ai_scheduling_desc"))
        
        col1, col2 = st.columns(2)
        with col1:
            num_employees = st.slider(get_text("num_employees"), 5, 100, 20)
            shift_duration = st.selectbox(get_text("shift_duration"), ["6 hours", "8 hours", "10 hours", "12 hours"])
        with col2:
            coverage_needed = st.number_input(get_text("min_employees"), 2, 20, 5)
            optimize_for = st.selectbox(get_text("optimize_for"), 
                                       [get_text("cost_efficiency"), get_text("employee_preference"), get_text("fairness")])
        
        if st.button(get_text("generate_schedule")):
            with st.spinner(get_text("generating")):
                time.sleep(1.5)
            st.success(get_text("schedule_success"))
            st.dataframe(pd.DataFrame({
                get_text("date_col"): ["2026-04-25", "2026-04-25", "2026-04-26", "2026-04-26"],
                get_text("shift_col"): ["Morning", "Evening", "Morning", "Evening"],
                get_text("employees_col"): ["5", "6", "7", "5"]
            }), use_container_width=True)
    
    # ---------- TAB 2: TIME TRACKING ----------
    with tabs[2]:
        st.subheader(get_text("time_tracking_title"))
        st.markdown(get_text("time_tracking_desc"))
        
        col1, col2 = st.columns(2)
        with col1:
            employee_name = st.selectbox(get_text("select_employee"), ["Alice Johnson", "Bob Smith", "Carol Davis", "David Lee"])
            if st.button(get_text("clock_in")):
                st.success(f"{employee_name} {get_text('clocked_in')} {datetime.datetime.now().strftime('%H:%M:%S')}")
        with col2:
            st.subheader(get_text("today_log"))
            log_df = pd.DataFrame({
                get_text("employee_col"): ["Alice J.", "Bob S.", "Carol D."],
                get_text("clock_in_col"): ["09:02 AM", "10:05 AM", "07:58 AM"],
                get_text("clock_out_col"): ["05:00 PM", "06:00 PM", "04:02 PM"],
                get_text("total_hours_col"): ["7.97", "7.92", "8.07"]
            })
            st.dataframe(log_df, use_container_width=True)
    
    # ---------- TAB 3: GEOFENCING ----------
    with tabs[3]:
        st.subheader(get_text("geofencing_title"))
        st.markdown(get_text("geofencing_desc"))
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"#### {get_text('active_geofences')}")
            geofences = ["HQ Office (Radius 500m)", "Site A (Construction)", "Site B (Warehouse)", "Client X Premises"]
            for gf in geofences:
                st.markdown(f'<span class="geofence-badge">{gf}</span>', unsafe_allow_html=True)
                st.markdown("")
        with col2:
            st.markdown(f"#### {get_text('recent_alerts')}")
            st.warning(get_text("alert_geofence_violation"))
            st.info(get_text("alert_geofence_entry"))
        
        if st.button(get_text("add_geofence")):
            st.info(get_text("geofence_coming"))
    
    # ---------- TAB 4: PAYROLL ----------
    with tabs[4]:
        st.subheader(get_text("payroll_title"))
        st.markdown(get_text("payroll_desc"))
        
        payroll_period = st.selectbox(get_text("pay_period"), ["April 1-15, 2026", "April 16-30, 2026", "May 1-15, 2026"])
        if st.button(get_text("generate_payroll")):
            st.dataframe(pd.DataFrame({
                get_text("employee_col"): ["Alice Johnson", "Bob Smith", "Carol Davis"],
                get_text("regular_hours"): [80, 85, 78],
                get_text("overtime"): [2, 5, 0],
                get_text("gross_pay"): ["$1,280", "$1,425", "$1,170"],
                get_text("net_pay"): ["$1,024", "$1,140", "$936"]
            }), use_container_width=True)
            st.success(get_text("payroll_success"))
    
    # ---------- TAB 5: TEAM CHAT ----------
    with tabs[5]:
        st.subheader(get_text("team_chat_title"))
        st.markdown(get_text("team_chat_desc"))
        
        messages = [
            (get_text("chat_admin"), get_text("chat_welcome")),
            ("Alice", get_text("chat_alice")),
            ("Bob", get_text("chat_bob")),
        ]
        for sender, msg in messages:
            st.markdown(f"**{sender}:** {msg}")
        
        new_msg = st.text_input(get_text("your_message"))
        if st.button(get_text("send")):
            st.success(get_text("message_sent"))
    
    # ---------- TAB 6: REPORTS ----------
    with tabs[6]:
        st.subheader(get_text("reports_title"))
        report_type = st.selectbox(get_text("select_report"), [
            get_text("attendance_summary"),
            get_text("overtime_analysis"),
            get_text("productivity_dept"),
            get_text("geofence_compliance")
        ])
        if st.button(get_text("generate_report")):
            st.dataframe(pd.DataFrame({
                get_text("metric_col"): [get_text("total_hours_metric"), get_text("late_arrivals_metric"),
                                       get_text("early_departures_metric"), get_text("geofence_violations_metric")],
                get_text("value_col"): ["1,245", "12", "5", "3"]
            }), use_container_width=True)
            st.line_chart(pd.DataFrame({
                get_text("day_col"): ["Mon", "Tue", "Wed", "Thu", "Fri"],
                get_text("hours_col"): [185, 192, 178, 201, 195]
            }).set_index(get_text("day_col")))
    
    st.markdown("---")
    st.caption(f"Built with 💖 by Gesner Deslandes | GlobalInternet.py")

# ========== APP ROUTING ==========
if not st.session_state.authenticated:
    login_page()
else:
    main_dashboard()
