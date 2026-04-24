import streamlit as st

st.set_page_config(page_title="Contact", page_icon="📬", layout="wide")

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

input, textarea {
    background-color: #020617 !important;
    color: white !important;
}

.stButton>button {
    background: linear-gradient(90deg, #22d3ee, #6366f1);
    color: white;
    border-radius: 10px;
    border: none;
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
    <h1>📬 Contact Me</h1>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-title">📞 Contact Information</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <p>📧 Email: youremail@example.com</p>
        <p>📱 Phone: 09XXXXXXXXX</p>
        <p>🌐 GitHub: github.com/yourusername</p>
        <p>📍 Location: Philippines</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-title">✉️ Send a Message</div>', unsafe_allow_html=True)

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submitted = st.form_submit_button("Send Message")

        if submitted:
            if name and email and message:
                st.success("✅ Message sent successfully! (demo only)")
            else:
                st.error("❌ Please fill in all fields.")
                
st.markdown("""
<div style="text-align:center; margin-top:40px; color:gray;">
    <p>Thank you for visiting my portfolio.</p>
</div>
""", unsafe_allow_html=True)