import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
def EDA():
    df = pd.read_csv('nigeria-innovation.csv')
    select = st.sidebar.selectbox("SUPPORT POLICY PROGRAM",['TABLE'],key =1)
    if select == 'TABLE':
        df2 = pd.read_csv('policy.csv')
        df2.rename({'policysup1':'Importance of govt support policy/prog - R&D funding',
            'policysup2':'Importance of govt support policy/prog - Training',
            'policysup3':'Importance of govt support policy/prog - Subsidies',
            'policysup4':'Importance of govt support policy/prog - Tax rebates',
            'policysup5':'Importance of govt support policy/prog - Technical support/advice',
            'policysup6':'Importance of govt support policy/prog - Infrastructure support',
            'policysup7':'Importance of govt support policy/prog - Loans and grants',
            'policysup8':'Importance of govt support policy/prog - Others'},axis = 1,inplace=True) 
        st.table(df2)
        if st.checkbox('Support policy program Chart'):
            df3 = df[['policysup1',
'policysup2',
'policysup3',
'policysup4',
'policysup5',
'policysup6',
'policysup7',
'policysup8'
]]
        df3.replace({'3':'Highly important','2':'Moderately important','1':'Slightly important','0':'Not important',' ':'Unspecified'},inplace=True)
        st.subheader('Importance of govt support policy/prog')
                
        if st.checkbox('Importance of govt support policy/prog - R&D funding'):
            fig = px.histogram(df3, x="policysup1", color="policysup1",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Importance of govt support policy/prog - Training'):
            fig = px.histogram(df3, x="policysup2", color="policysup2",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Importance of govt support policy/prog - Subsidies'):
            fig = px.histogram(df3, x="policysup3", color="policysup3",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Importance of govt support policy/prog - Tax rebates'):
            fig = px.histogram(df3, x="policysup4", color="policysup4",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Importance of govt support policy/prog - Technical support/advice'):
            fig = px.histogram(df3, x="policysup5", color="policysup5",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Importance of govt support policy/prog - Infrastructure support'):
            fig = px.histogram(df3, x="policysup6", color="policysup6",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Importance of govt support policy/prog -  Loans and grants'):
            fig = px.histogram(df3, x="policysup7", color="policysup7",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)

            st.plotly_chart(fig)
        if st.checkbox('Importance of govt support policy/prog - Others'):
            fig = px.histogram(df3, x="policysup8", color="policysup8",width=800, height=600)
            fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                            paper_bgcolor="#202A44",)
            st.plotly_chart(fig)
st.set_page_config(page_title="Support policy program", page_icon="📈")
st.markdown("#Support policy program analysis")
st.header(
        """Support policy program analysis""")
EDA()  