import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
def EDA():
    df = pd.read_csv('nigeria-innovation.csv')
    select = st.sidebar.selectbox("Innovation Activities Against Their Total Expenditure",['TABLE'],key =1)
    if select == 'TABLE':
        st.wtite('Innovation Activities Against Their Total Expenditure')
        df2 =  pd.read_excel('output.xlsx',sheet_name = 'Sheet3')
        df2.rename({'Unnamed: 0':'x'},axis =1,inplace=True)
        df2.drop('x',axis = 1,inplace=True)
        st.table(df2)
        if st.checkbox('Innovation and total expendiure Chart'):
            df7 = pd.read_excel('output.xlsx',sheet_name='Sheet3')
            df7.drop('Unnamed: 0',axis = 1,inplace =True)
            fig = px.scatter(df7, x="No of Innovations Engagement", y="Total Expenditure",size="Total Expenditure", color="Types of Selected R&D by  Enterprise",hover_name="Types of Selected R&D by  Enterprise"
                    , log_x=True, size_max=60)
            st.plotly_chart(fig)

       
            
            
st.set_page_config(page_title="Innovation and total expendiure", page_icon="📈")
st.markdown("#Innovation and total expendiure analysis")
st.header(
        """Innovation and total expendiure analysis""")
EDA()   