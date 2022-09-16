import pandas as pd
import re
from textblob import TextBlob
import streamlit as st



def sentiment_analysis(my_comment):
    
    sentiments=TextBlob(my_comment).sentiment.polarity
    if (sentiments>0):
        return "Positive"
    elif(sentiments<0):
        return "Negative"
    else:
        return "Neutral"
    


def sentiment_dep():
    # st.title("SENTIMENT ANALYSIS")
    html="""
    <div style="background-color:cyan;padding:13px">
    <h1 style ="color:black;text-align:center;">SENTIMENT ANALYSIS</h1>
    </div>
    """
    st.markdown(html,unsafe_allow_html=True)
    comment=st.text_area("",placeholder="Write comments here",height=100)

    result=""
    if st.button("Check_Sentiment"):
        result=sentiment_analysis(comment)
    
    if(result=="Positive"):
        st.success(result)
    elif(result=="Negative"):
        st.error(result)
    else:
        st.info(result)

sentiment_dep()
