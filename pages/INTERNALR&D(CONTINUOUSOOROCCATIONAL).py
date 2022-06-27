import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
def EDA():
    df = pd.read_csv('nigeria-innovation.csv')
    select = st.sidebar.selectbox("TABLE REPORT ANALYSIS",['TABLE'],key =1)
    if select == 'TABLE':
        st.subheader('Internal R&D Against Innovation Activities  wheather it is Continuous OR Occational')
        d3 = {
    'Continuous R&D':[147,284],
    'Occassional R&D':[284,147]
}
        ITCRDORD = pd.DataFrame(d3,index = ['YES','NO'])
        st.table(ITCRDORD)
        if st.checkbox('Innovation Activities Against Their Total Expenditure'):
            df2 =  pd.read_excel('output.xlsx',sheet_name = 'Sheet3')
            df2.rename({'Unnamed: 0':'x'},axis =1,inplace=True)
            df2.drop('x',axis = 1,inplace=True)
            st.table(df2)
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
st.markdown("#TABLE REPORT ANALYSIS")
st.header(
        """This TABLE ANALYSIS REPORT""")
EDA()   