import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title ="OsandaLelum", page_icon=":tada" ,layout="wide")


def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

lc = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jjsrh4we.json")
code = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/1.PNG")
img_lottie_animation = Image.open("images/2.jpg")
AI = Image.open("images/Al.PNG")
me = Image.open("images/about.PNG")


with st.container():
    left_column,right_column =st.columns(2)
    with left_column:
        st.subheader("I am Osanda Lelum ")
        st.title("Lecturer || Full stack Developer")
        st.write("Reading Msc.Financial Mathematics || Bsc.in Computer science")
        st.write("I am passionate programmer, problem solver , chess lover, Leader and a person who seek opportunities to enhance knowledge in anything.")
        st.write("[Visit Me-->>](https://osandalelum.github.io/)")

    with right_column:
      st.image(me ,width=300)


with st.container():
    left_column,right_column =st.columns(2)
    with left_column:
        st.header("What I do ")
        st.write('##')
        st.write(
               """"     Full stack Developemt || Project management || Tuting|| Video editing || Graphic designing
                        Supply chain -process Apparel """

        )
        st.write("[Visit My Company-->>](https://satharavidhyapeetaya.github.io/)")

    with right_column:
        st_lottie(lc, height=300, key="coding")

       
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(AI)
    with text_column:
        st.subheader("Machine learning")
        st.write(
            """
            Machine learning will automate jobs that most people thought could only be done by people.
           
            """
        )
        st.markdown("[Github...](https://github.com/OsandaLelum/MachineLearning)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Restaurant Application")
        st.write(
            """
         Ordering Without Queues.
            """
        )
        st.markdown("[Github...](https://github.com/group-48)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
      <form action="https://formsubmit.co/osandalelum@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
      </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()