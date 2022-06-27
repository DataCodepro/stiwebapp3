import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
def EDA():
    df = pd.read_csv('nigeria-innovation.csv')
    select = st.sidebar.selectbox("INFORMATION SOURCE",['TABLE'],key =1)
    if select == 'TABLE':
        df2 = pd.read_csv('effect.csv')
        df2.rename({'ieffect_org1':'Effect of innovation (organisational) - reduced response time to customer needs',
            'ieffect_org2':'Effect of innovation (organisational) - improved quality of goods/services','ieffect_org3':'Effect of innovation (organisational) - reduced costs per unit output','ieffect_org4':'Effect of innovation (organisational) - improved staff satisfaction/reduced turn','ieffect_org5':'Effect of innovation (organisational) - increased or maitained market share'},axis = 1,inplace=True)
        st.table(df2)
        if st.checkbox('Effect of innovation Chart'):
            df4=df[['ieffect_org1',
    'ieffect_org2',
    'ieffect_org3',
    'ieffect_org4',
    'ieffect_org5'
    ]]
            df4.replace({'3':'High','2':'Medium','1':'Low','0':'Not experienced',' ':'Unspecified'},inplace=True)
            if st.checkbox('Effect of innovation (organisational) - reduced response time to customer needs'):
                fig = px.histogram(df4, x="ieffect_org1", color="ieffect_org1",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                st.plotly_chart(fig)
            if st.checkbox('Effect of innovation (organisational) - improved quality of goods/services'):
                fig = px.histogram(df4, x="ieffect_org2", color="ieffect_org2",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

                st.plotly_chart(fig)
            if st.checkbox('Effect of innovation (organisational) - reduced costs per unit output'):
                fig = px.histogram(df4, x="ieffect_org3", color="ieffect_org3",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

                st.plotly_chart(fig)
            if st.checkbox('Effect of innovation (organisational) - improved staff satisfaction/reduced turn'):
                fig = px.histogram(df4, x="ieffect_org4", color="ieffect_org4",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

                st.plotly_chart(fig)
            if st.checkbox('Effect of innovation (organisational) - increased or maitained market share'):
                fig = px.histogram(df4, x="ieffect_org5", color="ieffect_org5",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

                st.plotly_chart(fig)
st.set_page_config(page_title="Effect of innovation", page_icon="📈")
st.markdown("#Effect of innovation analysis")
st.header(
        """Effect of innovation analysis""")
EDA()  