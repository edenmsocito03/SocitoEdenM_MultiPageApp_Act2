import streamlit as st

st.set_page_config(page_title="About Me", page_icon="👤", layout="wide")

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

.section-title {
    font-size: 22px;
    margin-bottom: 15px;
    font-weight: 600;
    color: #38bdf8;
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

.profile {
    text-align: center;
}

.profile h2 {
    margin-bottom: 5px;
}

.skill {
    margin-bottom: 15px;
}

.skill span {
    font-size: 14px;
}

.bar {
    height: 6px;
    border-radius: 10px;
    background: rgba(255,255,255,0.1);
    margin-top: 5px;
}

.fill {
    height: 6px;
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

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>About Me</h1>
    <p>Aspiring Developer • Problem Solver • Continuous Learner</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<p>
Hi, I’m Eden — a student and aspiring developer who enjoys turning ideas 
into real, working systems. I’ve always been curious about how things work, 
and programming gave me a way to explore that curiosity in a practical way.
</p>

<p>
I started learning development by building small projects, and over time, 
I found myself enjoying the process of solving problems, fixing errors, 
and improving how systems function. For me, coding is not just about writing 
lines of code — it’s about creating solutions that can make tasks easier 
and more efficient.
</p>

<p>
I mainly work with Python and Streamlit, where I focus on building simple, 
clean, and user-friendly applications. I like designing systems that are 
not only functional but also easy for people to understand and use.
</p>

<p>
As I continue learning, I aim to grow into a professional developer who can 
contribute to meaningful projects. I want to build systems that are useful, 
reliable, and impactful — especially in environments like schools and 
organizations where efficiency really matters.
</p>

<p>
I’m still learning, still improving, and always looking for ways to get better.
</p>

</div>
""", unsafe_allow_html=True)

colA, colB = st.columns(2)

with colA:
    st.markdown("""
    <div class="card">
        <h3>🎯 Goals</h3>

    <div class="badge">Financial Stability</div>
    <div class="badge">Stable Future</div>
    <div class="badge">Meaningful Career</div>
    <div class="badge">Become a Professional Developer</div>
    <div class="badge">Build Real-World Systems</div>
    <div class="badge">Continuous Learning</div>
    <div class="badge">Improve Problem-Solving Skills</div>
    <div class="badge">Create User-Friendly Applications</div>
    <div class="badge">Work on Impactful Projects</div>
    <div class="badge">Gain Industry Experience</div>

    </div>
    """, unsafe_allow_html=True)
with colB:
    st.markdown("""
    <div class="card">
        <h3>🚀 Interests</h3>

    <div class="badge">System Development</div>
    <div class="badge">UI Design</div>
    <div class="badge">Problem Solving</div>
    <div class="badge">Web App Development</div>
    <div class="badge">Data Visualization</div>
    <div class="badge">Automation</div>
    <div class="badge">Learning New Technologies</div>
    <div class="badge">Debugging & Optimization</div>
    <div class="badge">User Experience (UX)</div>
    <div class="badge">Building Productivity Tools</div>

    </div>
    """, unsafe_allow_html=True)