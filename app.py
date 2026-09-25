import streamlit as st
from ishara.auth import init_db, register_user, authenticate_user
from ishara.history import add_history, get_history, clear_history
from ishara.demo import DEMO_SIGNS, translate_demo
from ishara.ui import inject_css

st.set_page_config(page_title='Ishara — Bangla Sign Language', page_icon='🤟', layout='wide')
init_db(); inject_css()

if 'user' not in st.session_state: st.session_state.user=None
if 'page' not in st.session_state: st.session_state.page='Home'

if not st.session_state.user:
    st.markdown("<div class='hero'><div class='brand'>ISHARA</div><h1>From Gesture to Meaning</h1><p>Bangla Sign Language Communication Bridge</p></div>", unsafe_allow_html=True)
    a,b=st.tabs(['Sign in','Create account'])
    with a:
        with st.form('login'):
            email=st.text_input('Email'); password=st.text_input('Password',type='password')
            if st.form_submit_button('Sign in',use_container_width=True):
                user=authenticate_user(email,password)
                if user: st.session_state.user=user; st.rerun()
                else: st.error('Invalid email or password.')
    with b:
        with st.form('register'):
            name=st.text_input('Full name'); email=st.text_input('Email',key='re'); password=st.text_input('Password',type='password',key='rp'); confirm=st.text_input('Confirm password',type='password')
            if st.form_submit_button('Create account',use_container_width=True):
                if password!=confirm: st.error('Passwords do not match.')
                elif len(password)<6: st.error('Password must contain at least 6 characters.')
                else:
                    ok,msg=register_user(name,email,password); (st.success if ok else st.error)(msg)
    st.stop()

with st.sidebar:
    st.markdown('## ISHARA')
    st.caption('Bangla Sign Language Communication Bridge')
    pages=['Home','Live Translator','Conversation Mode','Emergency Ishara','Sign Library','History','About & Research']
    st.session_state.page=st.radio('Navigation',pages,index=pages.index(st.session_state.page))
    st.divider(); st.caption(f'Signed in as **{st.session_state.user[1]}**')
    if st.button('Sign out',use_container_width=True): st.session_state.user=None; st.rerun()

page=st.session_state.page
if page=='Home':
    st.markdown('# Welcome to Ishara')
    st.write('A modular prototype for inclusive Bangla Sign Language communication.')
    c1,c2,c3,c4=st.columns(4)
    for c,title,val in zip((c1,c2,c3,c4),('Direction','Mode','Safety','Data'),('Two-way','Real-time UX','Confidence-aware','Structured')): c.metric(title,val)
    st.markdown('## Core capabilities')
    cards=[('🤟','Sign → Bangla','Camera workflow and sign vocabulary.'),('🔄','Two-way bridge','Sign-side and Bangla-side conversation flow.'),('🎯','Uncertainty aware','Low-confidence results should request another capture.'),('🚨','Emergency Ishara','Fast, readable emergency phrases.')]
    cols=st.columns(4)
    for c,(i,t,b) in zip(cols,cards):
        with c: st.markdown(f"<div class='card'><div class='icon'>{i}</div><h3>{t}</h3><p>{b}</p></div>",unsafe_allow_html=True)

elif page=='Live Translator':
    st.markdown('# Live Translator')
    st.info('This downloadable build includes a transparent demo recognizer. The real recognition model must be connected through `ishara/model_adapter.py`; no fabricated accuracy is presented.')
    left,right=st.columns([1.1,1])
    with left:
        shot=st.camera_input('Capture a sign')
        if shot: st.image(shot,use_container_width=True)
    with right:
        label=st.selectbox('Presentation demo sign',list(DEMO_SIGNS.keys()))
        r=translate_demo(label)
        st.markdown(f"<div class='result'><small>DEMO INTERPRETATION</small><h2>{r['bn']}</h2><p>{r['en']}</p><b>Demo confidence: {r['confidence']}%</b></div>",unsafe_allow_html=True)
        st.caption('The displayed confidence is a demo UI value, not a measured model metric.')
        if st.button('Save translation',use_container_width=True):
            add_history(st.session_state.user[0],'Sign → Bangla',r['bn'],r['confidence']); st.success('Saved to your history.')

elif page=='Conversation Mode':
    st.markdown('# Ishara Live — Conversation Mode')
    l,r=st.columns(2)
    with l:
        st.markdown('### 🤟 Sign-language user')
        label=st.selectbox('Demo sign',list(DEMO_SIGNS.keys()),key='conv')
        if st.button('Translate sign',use_container_width=True):
            x=translate_demo(label); st.success(x['bn']); add_history(st.session_state.user[0],'Conversation — Sign → Bangla',x['bn'],x['confidence'])
    with r:
        st.markdown('### 👤 Bangla user')
        msg=st.text_area('Bangla message',placeholder='আপনি কেমন আছেন?')
        if st.button('Prepare sign representation',use_container_width=True):
            if msg.strip(): st.success('Message prepared for the sign-representation layer.'); st.write(msg)
            else: st.warning('Write a message first.')
    st.caption('Production extension: connect a trained text-to-sign avatar/pose module here.')

elif page=='Emergency Ishara':
    st.markdown('# 🚨 Emergency Ishara')
    st.warning('Communication aid prototype. It does not automatically call emergency services.')
    options={'🆘 Help':'আমার সাহায্য দরকার।','🏥 Hospital':'আমাকে হাসপাতালে নিতে হবে।','🤕 Pain':'আমার ব্যথা হচ্ছে।','💧 Water':'আমার পানি দরকার।','🍚 Food':'আমার খাবার দরকার।','📍 Location':'আমার অবস্থান জানাতে হবে।'}
    for idx,(lab,text) in enumerate(options.items()):
        if st.button(lab,key=f'e{idx}',use_container_width=True):
            st.markdown(f"<div class='emergency'>{text}</div>",unsafe_allow_html=True); add_history(st.session_state.user[0],'Emergency',text,100)

elif page=='Sign Library':
    st.markdown('# Bangla Sign Library')
    st.caption('Starter vocabulary. Replace/extend it with properly consented and annotated Bangla Sign Language data.')
    for bn,meta in DEMO_SIGNS.items():
        a,b,c=st.columns([1,1,2]); a.write(f'**{bn}**'); b.write(meta['en']); c.write(meta['context']); st.divider()

elif page=='History':
    st.markdown('# Translation History')
    rows=get_history(st.session_state.user[0])
    if not rows: st.info('No saved translations yet.')
    for text,mode,created,conf in rows:
        st.markdown(f'**{text}** · {conf}%  \n{mode} · {created}'); st.divider()
    if rows and st.button('Clear history'): clear_history(st.session_state.user[0]); st.rerun()

elif page=='About & Research':
    st.markdown('# About Ishara')
    st.markdown('''**Ishara — Bangla Sign Language Translator** is designed as a modular communication bridge.\n\n**Research pipeline**\n\nCamera → landmark extraction → temporal sequence model → sign classifier → context layer → Bangla sentence → text/voice.\n\n**Data governance**\n\nUse consented data, signer IDs that are pseudonymous, separate train/validation/test sets, and a signer-independent test split. Do not publish identifiable videos without permission.\n\n**Evaluation**\n\nReport accuracy, macro-F1, per-class precision/recall, confusion matrix, latency and signer-independent performance. Never label the demo mapping as measured AI performance.''')
# Ishara UI update - 2026
