import streamlit as st

st.set_page_config(page_title="Projects", page_icon="📂", layout="wide")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(120deg, #0f172a, #020617);
    color: #e2e8f0;
    font-family: 'Segoe UI', sans-serif;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 20px;
    color: #38bdf8;
}

.project-card {
    background: #020617;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.08);
    transition: 0.3s;
    height: 100%;
}

.project-card:hover {
    transform: translateY(-8px);
    border: 1px solid #22d3ee;
}

.project-title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 10px;
}

.project-text {
    font-size: 14px;
    color: #cbd5f5;
}

.tag {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 20px;
    background: rgba(34,211,238,0.15);
    margin: 5px 5px 0 0;
    font-size: 12px;
}

.hero {
    padding: 60px;
    border-radius: 20px;
    background: linear-gradient(135deg, #30364F, #576A8F);
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.hero h1 {
    font-size: 40px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 16px;
    color: #e0f2fe;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>📂 My Projects</h1>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="project-card">
    <div class="project-title">📊 School Management System</div>
    <div class="project-text">
        I developed a system to manage student records, attendance, 
        and reports efficiently. This project helped me understand 
        real-world system structure and data organization.
    </div>

    <div class="tag">Python</div>
    <div class="tag">System Design</div>
    <div class="tag">Database</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="project-card">
    <div class="project-title">📈 Data Dashboard App</div>
    <div class="project-text">
        I built an interactive dashboard using Streamlit to visualize 
        data in a simple and user-friendly way. This improved my ability 
        to present data clearly and effectively.
    </div>

    <div class="tag">Streamlit</div>
    <div class="tag">Data Visualization</div>
    <div class="tag">UI Design</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="project-card">
    <div class="project-title">⚙️ Automation Tools</div>
    <div class="project-text">
        I created tools to automate repetitive tasks and improve workflow 
        efficiency. These projects helped me focus on practical and 
        time-saving solutions.
    </div>

    <div class="tag">Automation</div>
    <div class="tag">Productivity</div>
    <div class="tag">Python</div>
    </div>
    """, unsafe_allow_html=True)