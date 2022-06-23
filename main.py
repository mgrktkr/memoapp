import streamlit as st
import requests
import json
import pandas as pd

page = st.sidebar.selectbox('Choose your page', ['registration', 'list'])

if page == 'registration':
    st.title('回答画面')
    with st.form(key='registration'):
        team: str = st.text_input('チーム名', max_chars=100)
        content: str = st.text_input('回答内容', max_chars=100)
        data = {
                'team': team, 'content': content
        }
        submit_button = st.form_submit_button(label='登録')

        if submit_button:
            url = 'http://127.0.0.1:8000/memos'
            res = requests.post(
                url,
                data=json.dumps(data)
            )
            st.write(res)
            if res.status_code == 200:
                st.success('登録完了')
                st.balloons()
                st.json(res.json())

elif page == 'list':
    st.title('回答一覧画面')
    res = requests.get('http://127.0.0.1:8000/memos')
    records = res.json()
    st.table(records)
    
    #for record in records:
    #    st.subheader('・' + record.get('content'))
