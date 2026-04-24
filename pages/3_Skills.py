import streamlit as st

st.set_page_config(page_title="Skills", page_icon="💻", layout="wide")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(120deg, #0f172a, #020617);
    color: #e2e8f0;
    font-family: 'Segoe UI', sans-serif;
}

.hero {
    padding: 60px;
    border-radius: 20px;
    background: linear-gradient(135deg, #30364F, #576A8F);
    text-align: center;
    margin-bottom: 30px;
}

.card {
    background: #020617;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
    border: 1px solid #22d3ee;
}

.skill {
    margin-bottom: 18px;
}

.skill span {
    font-size: 14px;
}

.bar {
    height: 8px;
    border-radius: 10px;
    background: rgba(255,255,255,0.1);
    margin-top: 5px;
}

.fill {
    height: 8px;
    border-radius: 10px;
    background: linear-gradient(90deg, #22d3ee, #6366f1);
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    background: rgba(99,102,241,0.2);
    margin: 5px;
    font-size: 12px;
}

.section-title {
    font-size: 22px;
    margin-bottom: 15px;
    font-weight: 600;
    color: #38bdf8;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>💻 My Skills</h1>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-title">⚙️ Technical Skills</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    <div class="skill">
            <span>Python</span>
    <div class="bar"><div class="fill" style="width:85%"></div></div>
    </div>

    <div class="skill">
            <span>Streamlit</span>
    <div class="bar"><div class="fill" style="width:80%"></div></div>
    </div>

    <div class="skill">
            <span>HTML & CSS</span>
    <div class="bar"><div class="fill" style="width:75%"></div></div>
    </div>

    <div class="skill">
            <span>Basic JavaScript</span>
    <div class="bar"><div class="fill" style="width:60%"></div></div>
    </div>

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-title">🧠 Other Skills</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    <div class="badge">Problem Solving</div>
    <div class="badge">Critical Thinking</div>
    <div class="badge">System Design</div>
    <div class="badge">UI/UX Awareness</div>
    <div class="badge">Debugging</div>
    <div class="badge">Time Management</div>
    <div class="badge">Adaptability</div>
    <div class="badge">Continuous Learning</div>

    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">🚀 What I’m Currently Learning</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="badge">Advanced Python</div>
    <div class="badge">Database Management</div>
    <div class="badge">Web Development</div>
    <div class="badge">System Architecture</div>
</div>
""", unsafe_allow_html=True)