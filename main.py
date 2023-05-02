import streamlit as st
from streamlit_lottie import st_lottie 
import requests
import extract
import predictions
import matplotlib.pyplot as plt

def callback():
    url = st.session_state.url
    comments = extract.fetch_comments(url)
    neg,neu,pos = predictions.counts(comments)
    st.session_state['neg']=neg
    st.session_state['neu']=neu
    st.session_state['pos']=pos
    #st.write("The percentage of negative comments is: " + str(neg/(neg+neu+pos)*100))
        

st.set_page_config(page_title="senti_people", page_icon=":beaming_face_with_smiling_eyes:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_youtube = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_EAfMOs/Youtube.json")
lottie_fans = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_aaviocjd.json")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("WELCOME!")
        st.write(""" # How do your fans React to your video?""")
        st.subheader("Ever wondered how your video is being recieved by your audience?")
        st.write("In that case we are here for you. Enter your URL and find out every reaction")
    
    with right_column:
        st_lottie(lottie_fans, height=300, width= 300)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.text_input("Enter a URL",on_change = callback,key='url')
        if "neg" in st.session_state:
            neg = st.session_state.neg
            neu = st.session_state.neu
            pos = st.session_state.pos
            st.write("The percentage of negative comments is: "+str(neg/(neg+neu+pos)*100))
            st.write("The percentage of positive comments is: "+str(pos/(neg+neu+pos)*100))
            st.write("The percentage of neutral comments is: "+str(neu/(neg+neu+pos)*100))
            fig,ax = plt.subplots()
            y = [pos,neg,neu]
            mylabels=["positive","negative","neutral"]
            ax.pie(y,labels = mylabels)
            st.pyplot(fig)
        

    with right_column:
        st_lottie(lottie_youtube)


