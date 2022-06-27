import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
def EDA():
    df = pd.read_csv('nigeria-innovation.csv')
    select = st.sidebar.selectbox("FACTORS AFFECTING INNOVATION ACTIVITIES",['FACTORS AFFECTING INNOVATION ACTIVITIES'],key =1)
    if select == 'TABLE':
         df21 = pd.read_csv('obstacle.csv')
         df21.rename({'obstacle_cost1':'Obstacle - lack of in-house funds',
            'obstacle_cost2':'Obstacle - lack of external financing',
            'obstacle_cost3':'Obstacle - high costs of innovation',
            'obstacle_cost4':'Obstacle - economic risk',
            'obstacle_cost5':'Obstacle - expensive environment-friendly R&D',
            'obstacle_knowledge1':'Obstacle - lack of qualified personnel',
            'obstacle_knowledge2':'Obstacle - lack of tech information',
            'obstacle_knowledge3':'Obstacle - lack of market information',
            'obstacle_knowledge4':'Obstacle - difficult to find coop partners',
            'obstacle_market1':'Obstacle - mkt dominated by large ent.',
            'obstacle_market2':'Obstacle - uncertain demand',
            'obstacle_market3':'Obstacle - mkt dominated by foreign substitutes',
            'obstacle_market4':'Obstacle - consumers unwilling to pay',
            'obstacle_market5':'Obstacle - imitation',
            'obstacle_infra1':'Obstacle - poor basic infrastructure',
            'obstacle_infra2':'Obstacle - inadequate facilities',
            'obstacle_need1':'Obstacle - no need due to prior innovation',
            'obstacle_need2':'Obstacle - no need due to no demand for innovation',
            'obstacle_other1':'Obstacle - internal organisational rigidities',
            'obstacle_other2':'Obstacle - inflexible regulations/standards',
            'obstacle_other3':'Obstacle - limitation of S&T public policies'},axis =1,inplace=True) 
         st.table(df21)
         if st.checkbox('FACTORS AFFECTING INNOVATION ACTIVITIES CHART'):
            df2 = df[['obstacle_cost1','obstacle_cost2','obstacle_cost3','obstacle_cost4','obstacle_cost5','obstacle_knowledge1','obstacle_knowledge2',
    'obstacle_knowledge3','obstacle_knowledge4','obstacle_market1','obstacle_market2','obstacle_market3','obstacle_market4','obstacle_market5',
    'obstacle_infra1','obstacle_infra2','obstacle_need1','obstacle_need2','obstacle_other1','obstacle_other2','obstacle_other3']]
            df2.replace({'3':'High','2':'Medium','1':'Low','0':'Not experienced',' ':'Unspecified'},inplace=True)
             if st.checkbox('Obstacle - lack of in-house funds'):
                    fig = px.histogram(df2, x="obstacle_cost1", color="obstacle_cost1",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                        paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - lack of external financing'):
                    fig = px.histogram(df2, x="obstacle_cost2", color="obstacle_cost2",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - high costs of innovation'):
                    fig = px.histogram(df2, x="obstacle_cost3", color="obstacle_cost3",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - economic risk'):
                    fig = px.histogram(df2, x="obstacle_cost4", color="obstacle_cost4",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - expensive environment-friendly R&D'):
                    fig = px.histogram(df2, x="obstacle_cost5", color="obstacle_cost5",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - lack of qualified personnel'):
                    fig = px.histogram(df2, x="obstacle_knowledge1", color="obstacle_knowledge1",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - lack of tech information'):
                    fig = px.histogram(df2, x="obstacle_knowledge2", color="obstacle_knowledge2",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox(':Obstacle - lack of market information'):
                    fig = px.histogram(df2, x="obstacle_knowledge3", color="obstacle_knowledge3",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox(':Obstacle - difficult to find coop partners'):
                    fig = px.histogram(df2, x="obstacle_knowledge4", color="obstacle_knowledge4",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - mkt dominated by large ent'):
                    fig = px.histogram(df2, x="obstacle_market1", color="obstacle_market1",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - uncertain demand'):
                    fig = px.histogram(df2, x="obstacle_market2", color="obstacle_market2",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                        paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - mkt dominated by foreign substitutes'):
                    fig = px.histogram(df2, x="obstacle_market3", color="obstacle_market3",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox(':Obstacle - consumers unwilling to pay'):
                    fig = px.histogram(df2, x="obstacle_market4", color="obstacle_market4",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - imitation'):
                    fig = px.histogram(df2, x="obstacle_market5", color="obstacle_market5",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - poor basic infrastructure'):
                    fig = px.histogram(df2, x="obstacle_infra1", color="obstacle_infra1",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - inadequate facilities'):
                    fig = px.histogram(df2, x="obstacle_infra2", color="obstacle_infra2",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - no need due to prior innovation'):
                    fig = px.histogram(df2, x="obstacle_need1", color="obstacle_need1",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - no need due to no demand for innovation'):
                    fig = px.histogram(df2, x="obstacle_need2", color="obstacle_need2",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - internal organisational rigidities'):
                    fig = px.histogram(df2, x="obstacle_other1", color="obstacle_other1",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - inflexible regulations/standards'):
                    fig = px.histogram(df2, x="obstacle_other2", color="obstacle_other2",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                    st.plotly_chart(fig)
             if st.checkbox('Obstacle - limitation of S&T public policies'):
                    fig = px.histogram(df2, x="obstacle_other3", color="obstacle_other3",width=800, height=600)
                    fig.update_layout(margin= dict(l=20, r=20, t=20, b=20),
                                                    paper_bgcolor="#202A44",)

                st.plotly_chart(fig)
st.set_page_config(page_title="FACTORS AFFECTING INNOVATION ACTIVITIES", page_icon="📈")
st.markdown("#FACTORS AFFECTING INNOVATION ACTIVITIES ANALYSIS")
st.header(
        """FACTORS AFFECTING INNOVATION ACTIVITIES ANALYSIS""")
EDA()   
