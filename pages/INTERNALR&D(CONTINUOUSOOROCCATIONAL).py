import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
def EDA():
    df = pd.read_csv('nigeria-innovation.csv')
    select = st.sidebar.selectbox("INTERNAL R&D AGAINST INNOVATION ACTIVITIES  WHEATHER IT IS CONTINUOUS OR OCCATIONAL",['INTERNAL R&D AGAINST INNOVATION ACTIVITIES  WHEATHER IT IS CONTINUOUS OR OCCATIONAL'],key =1)
    if select == 'INTERNAL R&D AGAINST INNOVATION ACTIVITIES  WHEATHER IT IS CONTINUOUS OR OCCATIONAL':
        st.subheader('INTERNAL R&D AGAINST INNOVATION ACTIVITIES  WHEATHER IT IS CONTINUOUS OR OCCATIONAL')
        d3 = {
    'Continuous R&D':[147,284],
    'Occassional R&D':[284,147]
}
        ITCRDORD = pd.DataFrame(d3,index = ['YES','NO'])
        st.table(ITCRDORD)
        if st.checkbox('Continuous OR Occational RandD'):
            df = pd.read_excel('randd.xlsx')
            df2 = df[['iact1','crd','ord']]
            df2.dropna(inplace=True)
            d1 = pd.crosstab(df2['iact1'],df2['ord'])
            d2 = pd.crosstab(df2['iact1'],df2['crd'])
            d3 = {
                'Continuous R&D':[147,284],
                'Occassional R&D':[284,147]
            }
            ITCRDORD = pd.DataFrame(d3,index = ['YES','NO'])
            ITCRDORD.rename({0:'NO',1:'YES'},axis = 0,inplace =True)
            ITCRDORD.reset_index(inplace=True)
            ITCRDORD.rename({'index':'Outcome'},axis = 1,inplace =True)

            if st.checkbox('Continuous R&D'):
                fig = px.funnel(ITCRDORD, x="Outcome", y="Continuous R&D")
                st.plotly_chart(fig)
            if st.checkbox('Occassional R&D'):
                fig = px.funnel(ITCRDORD, x="Outcome", y="Occassional R&D")
                st.plotly_chart(fig)
st.set_page_config(page_title="TABLE", page_icon="📈")
st.markdown("#INTERNAL R&D AGAINST INNOVATION ACTIVITIES  WHEATHER IT IS CONTINUOUS OR OCCATIONAL ANALYSIS")
st.header(
        """INTERNAL R&D AGAINST INNOVATION ACTIVITIES  WHEATHER IT IS CONTINUOUS OR OCCATIONAL ANALYSIS""")
EDA()   
