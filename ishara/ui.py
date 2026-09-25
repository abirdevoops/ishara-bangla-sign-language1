import streamlit as st


def inject_css():
    st.markdown("""
    <style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #F7FAFC 0%, #EEF6F7 100%);
    }

    /* Main content */
    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #073B4C 0%, #0B5563 100%);
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Hero */
    .hero {
        padding: 2rem;
        border-radius: 24px;
        background: linear-gradient(135deg, #073B4C, #118AB2);
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 12px 30px rgba(7, 59, 76, 0.18);
    }

    .hero h1 {
        font-size: 42px;
        margin-bottom: 5px;
        color: white;
    }

    .hero p {
        font-size: 20px;
        margin-bottom: 5px;
        color: #E8F8F8;
    }

    .hero small {
        color: #D5F3F4;
    }

    /* Cards */
    .card {
        padding: 1.3rem;
        border-radius: 18px;
        background: white;
        border: 1px solid #DCE7EA;
        box-shadow: 0 7px 22px rgba(7, 59, 76, 0.08);
        margin-bottom: 1rem;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 12px;
        border: none;
        background: #118AB2;
        color: white;
        font-weight: 600;
        padding: 0.55rem 1rem;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background: #073B4C;
        color: white;
        transform: translateY(-1px);
    }

    /* Inputs */
    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 10px;
    }

    /* Success */
    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

    /* Metric */
    div[data-testid="stMetric"] {
        background: white;
        padding: 1rem;
        border-radius: 16px;
        border: 1px solid #DCE7EA;
        box-shadow: 0 5px 18px rgba(7, 59, 76, 0.06);
    }

    </style>
    """, unsafe_allow_html=True)


def topbar(title="Ishara", subtitle="Bangla Sign Language Translator",
           tagline="From Gesture to Meaning, From Silence to Conversation."):

    st.markdown(
        f"""
        <div class="hero">
            <h1>🤟 {title}</h1>
            <p>{subtitle}</p>
            <small>{tagline}</small>
        </div>
        """,
        unsafe_allow_html=True
    )
