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
        df101 = pd.read_csv('infosource.csv')
        df101.replace({'sinfo1':'Information source - Internal','sinfo2':'Information source - Suppliers','sinfo3':'Information source - Customers','sinfo4':'Information source - Competitors','sinfo5':'Information source - Consultants, commercial labs or private R&D institutes','sinfo6':'Information source - Universities, other higher ed. Institutions','sinfo7':'Information source - Public research institutes','sinfo8':'Information source - Conferences, fairs, exhibitions','sinfo9':'Information source - Journals, trade publications','sinfo10':'Information source - Professional, industry associations'},inplace=True)
        st.table(df101)
        if st.checkbox('INFORMATION SOURCE Chart'):
            df2 = df[['sinfo1','sinfo2','sinfo3','sinfo4','sinfo5','sinfo6','sinfo7','sinfo8','sinfo9','sinfo10']]
            df2.replace({'3':'High','2':'Medium','1':'Low','0':'Not Used',' ':'Unspecified'},inplace=True)
            if st.checkbox('Information source - Internal'):
                fig = px.histogram(df2, x="sinfo1", color="sinfo1",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)
                st.plotly_chart(fig)
            if st.checkbox('Information source - Suppliers'):
                fig = px.histogram(df2, x="sinfo2", color="sinfo2",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

                st.plotly_chart(fig)
            if st.checkbox('Information source - Customers'):
                fig = px.histogram(df2, x="sinfo3", color="sinfo3",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

                st.plotly_chart(fig)
            if st.checkbox('Information source - Competitors'):
                fig = px.histogram(df2, x="sinfo4", color="sinfo4",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

                st.plotly_chart(fig)
            if st.checkbox('Information source -  Consultants, commercial labs or private R&D institutes'):
                fig = px.histogram(df2, x="sinfo5", color="sinfo5",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

                st.plotly_chart(fig)
            if st.checkbox('Information source - Universities, other higher ed. Institutions'):
                fig = px.histogram(df2, x="sinfo6", color="sinfo6",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

                st.plotly_chart(fig)
            if st.checkbox('Information source - Public research institutes'):
                fig = px.histogram(df2, x="sinfo7", color="sinfo7",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

                st.plotly_chart(fig)
            if st.checkbox('Information source - Conferences, fairs, exhibitions'):
                fig = px.histogram(df2, x="sinfo8", color="sinfo8",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

                st.plotly_chart(fig)
            if st.checkbox('Information source - ournals, trade publications'):
                fig = px.histogram(df2, x="sinfo9", color="sinfo9",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

                st.plotly_chart(fig)
            if st.checkbox('Information source - Professional, industry associations'):
                fig = px.histogram(df2, x="sinfo10", color="sinfo10",width=800, height=600)
                fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                paper_bgcolor="#202A44",)

                st.plotly_chart(fig)


       
            
            
st.set_page_config(page_title="INFORMATION SOURCE", page_icon="📈")
st.markdown("#INFORMATION SOURCE ANALYSIS")
st.header(
        """Information source of Sector for both WAVE1 and WAVE2""")
EDA()   
