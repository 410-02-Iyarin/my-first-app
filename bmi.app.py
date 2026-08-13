import streamlit as st

st.markdown("#:red[⚖️คำนวนค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

weight=st.number_input("กรอกน้ำหนักของคุณ(กิโลกรัม):",min_value=1.0,value=1.0)
height_cm=st.number_input("กรอกส่วนสูงของคุณ(เซนติเมตร)",min_value=1.0,value=1.0)

if st.botton("คำนวนค่าBMI📝"):
    #แปลงส่วนสูงจากcmเป็น เมตร แล้วคำนวน BMI
    height_m=height_cm/100
    bmi=weight_cm/(height_m**2)

    st.write("---")
    st.header(f"ค่าbmiของคุณคือ:{bmi:2f})
