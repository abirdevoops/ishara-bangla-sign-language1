import streamlit as st
def inject_css():
 st.markdown('''<style>
.stApp{background:#f6f8fb}.hero{padding:3rem 1rem 2rem;text-align:center;background:linear-gradient(135deg,#0b1f3a,#174a68);color:white;border-radius:24px;margin-bottom:2rem}.brand{letter-spacing:.28em;font-weight:800}.hero h1{font-size:3rem;margin:.5rem}.card,.result{background:white;border:1px solid #e4e9ef;border-radius:18px;padding:1.3rem;box-shadow:0 5px 20px rgba(0,0,0,.04)}.card{min-height:170px}.icon{font-size:2rem}.emergency{font-size:2rem;padding:2rem;text-align:center;background:#fff3f3;border:2px solid #ffb7b7;border-radius:18px;margin-top:1rem}
</style>''',unsafe_allow_html=True)
