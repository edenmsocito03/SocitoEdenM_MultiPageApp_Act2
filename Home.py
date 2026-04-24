import streamlit as st

st.set_page_config(page_title="🌐 My Portfolio", layout="wide")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(120deg, #1f2937, #111827);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

.glass {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(12px);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 20px;
}

.profile {
    text-align: center;
}

.profile img {
    border-radius: 50%;
    border: 4px solid white;
}

.title {
    font-size: 36px;
    font-weight: bold;
    background: linear-gradient(90deg, #60a5fa, #22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.timeline {
    border-left: 3px solid #22d3ee;
    padding-left: 20px;
}

.timeline-item {
    margin-bottom: 20px;
}

.skill {
    padding: 10px;
    border-radius: 10px;
    background: rgba(255,255,255,0.1);
    margin-bottom: 10px;
}

.btn {
    background: linear-gradient(90deg, #22d3ee, #60a5fa);
    padding: 10px 20px;
    border-radius: 10px;
    color: white;
    text-align: center;
    display: inline-block;
}

.feature {
    flex: 1;
    min-width: 200px;
    padding: 20px;
    border-radius: 15px;
    background: rgba(255,255,255,0.06);
    transition: 0.3s;
}

.feature:hover {
    transform: translateY(-8px) scale(1.02);
    background: rgba(255,255,255,0.12);
}

.stat-box {
    text-align: center;
    transition: 0.3s;
}

.stat-box:hover {
    transform: translateY(-5px);
}

.btn:hover {
    opacity: 0.85;
    cursor: pointer;
}

</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

with col1:
    st.markdown("<div class='glass profile'>", unsafe_allow_html=True)

    st.image("pages/8e0c337f-69c9-4165-a761-9ad5a4ac69b0.jpg", width=260)

    st.markdown("""
    <h2>Eden M. Socito</h2>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="glass">
    <h3>🌐 My Portfolio</h3>
<p>
    This portfolio is a personal project that I designed and developed using 
    Python and Streamlit. It showcases my skills, projects, and progress as 
    an aspiring software developer.
</p>

<p>
    I built this application with a focus on clean design, user-friendly layout, 
    and interactive elements. It uses custom HTML and CSS styling to create a 
    modern interface, including glassmorphism effects, responsive sections, 
    and structured content.
</p>

<p>
    Through this project, I practiced front-end styling, layout structuring, 
    and integrating design with functionality. This portfolio reflects not only 
    my technical skills but also my creativity and attention to detail.
</p>

<p>
    I will continue improving this project by adding more features, enhancing 
    the design, and showcasing more of my work as I grow in my development journey.
</p>
</div>
""", unsafe_allow_html=True)
    
st.markdown("""
<div class="glass">
    <h3>🚀 Why Choose Me</h3>

<div class="highlight">
    <div class="icon">⚡</div>
        <div>
        <h4>Fast & Efficient Development</h4>
    <p>
            I focus on building systems that are not only functional but also optimized 
            for performance and usability.
    </p>
    </div>
</div>

<div class="highlight">
    <div class="icon">🎨</div>
        <div>
        <h4>Modern & Clean Design</h4>
        <p>
            I create interfaces that are visually appealing, easy to navigate, 
            and designed with the user in mind.
        </p>
    </div>
</div>

<div class="highlight">
    <div class="icon">🧠</div>
        <div>
        <h4>Real-World Problem Solver</h4>
        <p>
            My projects are built to solve actual problems, especially in school 
            systems and organizational workflows.
        </p>
    </div>
</div>

</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="glass stat-box">
        <h2>🚀 5+</h2>
        <p>Projects Built</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass stat-box">
        <h2>💻 4+</h2>
        <p>Technologies Used</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="glass stat-box">
        <h2>📈 Growing</h2>
        <p>Continuous Learning</p>
    </div>
    """, unsafe_allow_html=True)

