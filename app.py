import streamlit as st
import pandas as pd
import numpy as np
import pickle

pickle_in = open('train_model.pkl', 'rb')
model = pickle.load(pickle_in)

st.sidebar.image("BV-Acharya.jpg", caption=None, width=300, use_column_width=None, clamp=False, channels='RGB', output_format='auto')
st.sidebar.header('📜Patent Valuation💰')
st.sidebar.header('Choose Prediction Model')

model_choice = st.sidebar.selectbox('Select Prediction Model', ['Prediction by Random Forest Algorithm','Other Algorithms'], key='1')

if model_choice == 'Prediction by Random Forest Algorithm':
    col1,col2,col3 = st.columns(3)
    with col2:
        # st.image("./pics/super_ai_logo.png", caption=None, width=200, use_column_width=None, clamp=False, channels='RGB',output_format='auto')
        st.image("unnamed-removebg-preview.png", caption=None, width=200, use_column_width=None, clamp=False, channels='RGB',output_format='auto')
    st.title('📜Patent Valuation💰')
    name = st.text_input("ชื่อสิทธิบัตรที่คุณต้องการประเมินมูลค่า:")
    # pregnancy = st.number_input("No. of times pregnant: ")
    st.text("Note: defaul value is average values. Actual value input need to be changed by users")
    st.header("กรุณาใส่ข้อมูลต่าง ๆ เพื่อทำการประเมินมูลค่าทรัพย์สินทางปัญญา")
    Pages = st.slider(":page_facing_up: จำนวนหน้าของเอกสารที่เกี่ยวกับทรัพย์สินทางปัญญาทั้งหมด: ", min_value= 1.0 , max_value= 1000.0 ,value= 12.0, step= 1.0)
    Assignees = st.slider( ":man_in_business_suit_levitating: จำนวนของผู้ถือสิทธิในปัจจุบัน: ", min_value=1 , max_value=25 ,value=2, step=1)
    Inventors = st.slider( ":male-scientist: จำนวนของผู้ประดิษฐ์: ", min_value=1 , max_value=50 ,value=4, step=1)
    Family = st.slider( ":earth_asia: จำนวนประเทศทั้งหมดที่สิทธิบัตรนั้น ๆ มีการยื่นจด: ", min_value=0 , max_value=50 ,value=2, step=1)
    Cited = st.slider( ":pencil: จำนวนสิทธิบัตรที่ได้มีการอ้างอิงผลงาน: ", min_value=0 , max_value=500 ,value=2, step=1)

    st.subheader(":ballot_box_with_check: สถานะของสิทธิบัตรในปัจจุบัน")
    legal_Ceased = st.radio("ยุติการคุ้มครอง: ถ้ายุติการคุ้มครองแล้วให้เลือก 1, ถ้ายังไม่ยุติการคุ้มครองให้เลือก 0", (0,1))
    legal_Examining = st.radio("กำลังตรวจสอบ: ถ้ากำลังตรวจสอบให้เลือก 1, ถ้าไม่ได้กำลังตรวจสอบให้เลือก 0", (0,1))
    legal_Expired = st.radio("หมดอายุการคุ้มครอง: ถ้าหมดอายุการคุ้มครองแล้วให้เลือก 1, ถ้ายังไม่หมดอายุการคุ้มครองให้เลือก 0", (0,1))
    legal_Granted = st.radio("ได้รับสิทธิในการคุ้มครอง: ถ้าได้รับสิทธิในการคุ้มครองแล้วให้เลือก 1, ถ้ายังไม่ได้รับสิทธิในการคุ้มครองให้เลือก 0", (0,1))
    legal_Non_payment = st.radio("ไม่มีการชำระเงิน: ถ้ายังไม่มีการชำระเงินให้เลือก 1, ถ้ามีการชำระเงินให้เลือก 0", (0,1))
    legal_Published = st.radio("ได้รับประกาศเป็นสาธารณะ: ถ้าได้รับประกาศเป็นสาธารณะแล้วให้เลือก 1, ถ้าไม่ได้รับประกาศเป็นสาธารณะให้เลือก 0", (0,1))
    legal_Withdrawn = st.radio("ถูกเพิกถอนสิทธิ: ถ้าถูกเพิกถอนสิทธิให้เลือก 1, ถ้าไม่ถูกเพิกถอนสิทธิให้เลือก 0", (0,1))

    st.subheader(":newspaper:ประเภทของสิทธิบัตร")
    type_Applications = st.radio("สิทธิบัตรที่กำลังขอยื่นจดทะเบียน: ถ้าเป็นสิทธิบัตรที่กำลังขอยื่นจดทะเบียนให้เลือก 1, ถ้าไม่เป็นสิทธิบัตรที่กำลังขอยื่นจดทะเบียนให้เลือก 0", (0,1))
    type_Patents = st.radio("สิทธิบัตรการประดิษฐ์: ถ้าเป็นสิทธิบัตรการประดิษฐ์ให้เลือก 1, ถ้าไม่เป็นสิทธิบัตรการประดิษฐ์ให้เลือก 0", (0,1))
    type_Utility_models = st.radio("อนุสิทธิบัตร: ถ้าเป็นอนุสิทธิบัตรให้เลือก 1, ถ้าไม่เป็นอนุสิทธิบัตรให้เลือก 0", (0,1))
    
    st.subheader(":receipt: สัญลักษณ์จำแนกหมวดหมู่การประดิษฐ์ระหว่างประเทศ")
    ipc_A = st.radio("หมวดหมู่ A: ถ้าอยู่ในหมวดหมู่ A ให้เลือก 1, ถ้าไม่อยู่ในหมวดหมู่ A ให้เลือก 0", (0,1))
    ipc_B = st.radio("หมวดหมู่ B: ถ้าอยู่ในหมวดหมู่ B ให้เลือก 1, ถ้าไม่อยู่ในหมวดหมู่ B ให้เลือก 0", (0,1))
    ipc_C = st.radio("หมวดหมู่ C: ถ้าอยู่ในหมวดหมู่ C ให้เลือก 1, ถ้าไม่อยู่ในหมวดหมู่ C ให้เลือก 0", (0,1))
    ipc_D = st.radio("หมวดหมู่ D: ถ้าอยู่ในหมวดหมู่ D ให้เลือก 1, ถ้าไม่อยู่ในหมวดหมู่ D ให้เลือก 0", (0,1))
    ipc_E = st.radio("หมวดหมู่ E: ถ้าอยู่ในหมวดหมู่ E ให้เลือก 1, ถ้าไม่อยู่ในหมวดหมู่ E ให้เลือก 0", (0,1))
    ipc_F = st.radio("หมวดหมู่ F: ถ้าอยู่ในหมวดหมู่ F ให้เลือก 1, ถ้าไม่อยู่ในหมวดหมู่ F ให้เลือก 0", (0,1))
    ipc_G = st.radio("หมวดหมู่ G: ถ้าอยู่ในหมวดหมู่ G ให้เลือก 1, ถ้าไม่อยู่ในหมวดหมู่ G ให้เลือก 0", (0,1))
    ipc_H = st.radio("หมวดหมู่ H: ถ้าอยู่ในหมวดหมู่ H ให้เลือก 1, ถ้าไม่อยู่ในหมวดหมู่ H ให้เลือก 0", (0,1))

    st.subheader(":large_green_circle:สถานะความคงอยู่ของสิทธิบัตร")
    simple_legal_Ac = st.radio("สถานะคือยังคงอยู่: ถ้าสถานะคือยังคงอยู่ให้เลือก 1, ถ้าไม่ใช่สถานะยังคงอยู่ให้เลือก 0", (0,1))
    simple_legal_In = st.radio("สถานะคือไม่คงอยู่แล้ว: ถ้าสถานะคือไม่คงอยู่แล้วให้เลือก 1, ถ้าไม่ใช่สถานะไม่คงอยู่แล้วให้เลือก 0", (0,1))
    simple_legal_Pen = st.radio("สถานะคือกำลังยื่นขอ: ถ้าสถานะคือกำลังยื่นขอให้เลือก 1, ถ้าไม่ใช่สถานะกำลังยื่นขอให้เลือก 0", (0,1))

    submit = st.button('Predict')
    if submit:
            # prediction = classifier.predict([["pregnancy", "glucose", "bp", "skin", "insulin", "bmi", "dpf", "age"]])
            prediction = model.predict([[Pages, Assignees, Inventors,  Family, Cited, legal_Ceased, legal_Examining,legal_Expired, legal_Granted, legal_Non_payment,legal_Published, legal_Withdrawn, type_Applications, type_Patents, type_Utility_models, ipc_A,ipc_B,ipc_C,ipc_D,ipc_E,ipc_F,ipc_G,ipc_H, simple_legal_Ac, simple_legal_In, simple_legal_Pen ]])
            if prediction >= 1:
                 st.balloons()
                 st.success(f"มูลค่าทรัพย์สินทางปัญญา {name} มีมูลค่าประมาณ {prediction} USD") 

                 exchange = st.write('หน่วยบาท')
                 if prediction>= 1:
                      st.success((prediction)*33.7)
                
if model_choice == 'Other predictions':
    col1,col2,col3 = st.columns(3)
    with col2:
        # st.image("./pics/super_ai_logo.png", caption=None, width=200, use_column_width=None, clamp=False, channels='RGB',output_format='auto')
        st.image("unnamed-removebg-preview.png", caption=None, width=200, use_column_width=None, clamp=False, channels='RGB',output_format='auto')
    st.title('Other prediction model to deploy')
    st.text("")
    st.text('To be added later on')