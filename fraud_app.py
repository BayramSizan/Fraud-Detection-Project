import pandas as pd
import pickle
import streamlit as st
from PIL import Image


html_temp = """
<div style="background-color:purple;padding:1.5px">
<h1 style="color:white;text-align:center;">Select Attributes</h1>
</div><br>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)

html_temp2 = """
<div style="background-color:red;padding:40px;border-radius: 20px 20px 20px 20px;">
<h1 style="color:white;text-align:center;">Credit Card Fraud Detection App</h1>
</div><br>"""

html_temp3 = """
<div style="background-color:black;padding:1px;border-radius: 20px 20px 20px 20px;">
<h3 style="color:white;text-align:center;font-family: Roboto, sans-serif">You can rest on your chair at peace! Here comes a crime prevention app in finance sector! </h1>
</div><br>"""

html_temp4 = """
<div style="background-color:darkblue;padding:1px; border-radius: 20px 20px 20px 20px;">
<h3 style="color:white;text-align:center;font-family: Comic Sans MS">Is it possible to predict a fraudulent transaction? The Answer is "Yes", Let's See!</h1>
</div><br>"""


st.markdown(html_temp2,unsafe_allow_html=True)

img = Image.open("crime-prevention.jpg")
#img = img.resize((100, 100))

st.image(img, width=100, use_column_width =True) 
st.markdown(html_temp3,unsafe_allow_html=True)
 
img2 = Image.open("image.png")
st.image(img2, width=500, use_column_width =True)
st.markdown(html_temp4,unsafe_allow_html=True)

st.info("**Please fill the attributes on the left hand side to make \
    run the model properly.**")



time = st.sidebar.number_input("Time (seconds)")
time_hour = st.sidebar.number_input("Time (hours)")
amount = st.sidebar.number_input("Amount")
V1 = st.sidebar.number_input("V1")
V2 = st.sidebar.number_input("V2")
V3 = st.sidebar.number_input("V3")
V4 = st.sidebar.number_input("V4")
V5 = st.sidebar.number_input("V5")
V6 = st.sidebar.number_input("V6")
V7 = st.sidebar.number_input("V7")
V8 = st.sidebar.number_input("V8")
V9 = st.sidebar.number_input("V9")
V10 = st.sidebar.number_input("V10")
V11 = st.sidebar.number_input("V11")
V12 = st.sidebar.number_input("V12")
V13 = st.sidebar.number_input("V13")
V14 = st.sidebar.number_input("V14")
V15 = st.sidebar.number_input("V15")
V16 = st.sidebar.number_input("V16")
V17= st.sidebar.number_input("V17")
V18= st.sidebar.number_input("V18")
V19= st.sidebar.number_input("V19")
V20= st.sidebar.number_input("V20")
V21= st.sidebar.number_input("V21")
V22= st.sidebar.number_input("V22")
V23= st.sidebar.number_input("V23")
V24 = st.sidebar.number_input("V24")
V25 = st.sidebar.number_input("V25")
V26 = st.sidebar.number_input("V26")
V27 = st.sidebar.number_input("V27")
V28 = st.sidebar.number_input("V28")
   




new_data = {"hour" : time,
            "time" : time_hour,
            "amount" : amount,
            "V1" : V1,
            "V2" : V2,
            "V3" : V3,
            "V4" : V4,
            "V5" : V5,
            "V6" : V6,
            "V7" : V7,
            "V8" : V8,
            "V9" : V9,
            "V10" : V10,
            "V11" : V11,
            "V12" : V12,
            "V13" : V13,
            "V14" : V14,
            "V15" : V15,
            "V16" : V16,
            "V17" : V17,
            "V18" : V18,
            "V19" : V19,
            "V20" : V20,
            "V21" : V21,
            "V22" : V22,
            "V23" : V23,
            "V24" : V24,
            "V25" : V25,
            "V26" : V26,
            "V27" : V27,
            "V28" : V28}
            



            

df = pd.DataFrame([new_data])

st.write(df)

final_model = pickle.load(open("model_final", "rb"))
st.info("**Check the features you selected from the table above. If correct, press the Predict button.**")
if st.button("Predict"):
    prediction = final_model.predict(df)
    if prediction == 1:
        prediction = "fraudulent"
    else:
        prediction = "not fraudulent"
    st.success(f"This transaction is ** {prediction}.**")