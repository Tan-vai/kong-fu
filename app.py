from PIL import Image
import requests as re
import streamlit as st 
#from streamlit_lottie import st_lottie
st.set_page_config(page_title="Abu Tanim", page_icon=":tada:",layout="wide")
st.subheader("Hi, I am Abu Tanim :wave:")
def load_lottieurl(url):
    r= re.get(url)
    if r.status_code !=200:
        return None
    return r.json()
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
  
st.title("C.E.O of DEATH CYBER ARMY")
st.write("This is demo website for using python")
#left_column, right_column = st.columns(2)
#with left_column:
   # st_lottie(lottie_coding, height=300, key="coding")
 
with st.container():
    st.write("---")
left_column, right_column = st.columns([2, 1]) 

with left_column:
    st.header("About me")
    st.write(
    """
I am Abu Tanim, a skilled Python programmer with a passion for security and automation. I have hands-on experience in creating and using Termux executors, developing spammers, and performing SQL injection techniques. My expertise lies in understanding and exploiting system vulnerabilities, and I’m always eager to learn new ways to improve my skills. 

As a Python developer, I’ve built various scripts to automate tasks and enhance functionality. I specialize in penetration testing and web security, using tools and techniques to test and strengthen the security of applications. Termux has been a key tool in my toolkit, allowing me to carry out security testing even on Android devices. 

My journey in coding and security continues to drive my ambition to explore and master more advanced concepts in the field.
    
    """)
    st.write("##")
    img = Image.open("images/mrtan.jpg")
    st.write("[contact me >] (https://facebook.com/MrTan0fficial1)")
    st.write("Copyright ©2025 Chottogram, Bangladesh. All rights reserved.")
    #st.image(img, use_container_width=True, caption="Abu Tanim") 
      

with right_column:
    img_resized = img.resize((img.width, 930))  # Resize height to 300px
    st.image(img_resized, use_container_width=True)  # Display resized image
    st.container()


    

   
   
     
      
