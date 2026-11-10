
import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="Biochar AI",
    page_icon="🌱",
    layout="wide"
)

# หัวข้อหลัก
st.title("🌱 Biochar AI")
st.subheader("Biochar Analysis & Performance Platform")

st.write(
    "แพลตฟอร์มวิเคราะห์ประสิทธิภาพไบโอชาร์ "
    "และติดตามการดูดซับสารปนเปื้อน"
)

st.divider()

# เมนูด้านข้าง
menu = st.sidebar.selectbox(
    "เมนูหลัก",
    [
        "Dashboard",
        "Biochar Profile",
        "Performance Analyzer",
        "Reuse Tracker",
        "AI Advisor"
    ]
)

if menu == "Dashboard":
    st.header("Dashboard")
    st.write("ภาพรวมข้อมูลไบโอชาร์ของคุณ")

    col1, col2, col3 = st.columns(3)

    col1.metric("Biochar Samples", "3")
    col2.metric("Pollutant Types", "2")
    col3.metric("Reuse Cycles", "0")

    st.info(
        "เริ่มต้นด้วยการบันทึกข้อมูลตัวอย่าง "
        "BC-30, BC-45 และ BC-60"
    )

elif menu == "Biochar Profile":
    st.header("Biochar Profile")
    st.write("ข้อมูลตัวอย่างไบโอชาร์")

    sample = st.selectbox(
        "เลือกตัวอย่าง",
        ["BC-30", "BC-45", "BC-60"]
    )

    temperature = st.number_input(
        "อุณหภูมิการผลิต (°C)",
        min_value=0,
        value=400
    )

    duration = st.number_input(
        "ระยะเวลาให้ความร้อน (นาที)",
        min_value=0,
        value=30 if sample == "BC-30"
        else 45 if sample == "BC-45" else 60
    )

    feedstock = st.text_input(
        "วัตถุดิบ",
        "เปลือกกล้วย"
    )

    if st.button("บันทึกข้อมูล"):
        st.success(f"บันทึกข้อมูล {sample} แล้ว")
        st.write("วัตถุดิบ:", feedstock)
        st.write("อุณหภูมิ:", temperature, "°C")
        st.write("เวลา:", duration, "นาที")

elif menu == "Performance Analyzer":
    st.header("Performance Analyzer")

    pollutant = st.selectbox(
        "เลือกสารที่ต้องการวิเคราะห์",
        ["Methylene Blue", "Lead (Pb)"]
    )

    c0 = st.number_input(
        "ความเข้มข้นเริ่มต้น C0 (mg/L)",
        min_value=0.0,
        value=10.0
    )

    ce = st.number_input(
        "ความเข้มข้นหลังการดูดซับ Ce (mg/L)",
        min_value=0.0,
        value=5.0
    )

    volume = st.number_input(
        "ปริมาตรสารละลาย (L)",
        min_value=0.001,
        value=0.1
    )

    mass = st.number_input(
        "มวลไบโอชาร์ (g)",
        min_value=0.001,
        value=1.0
    )

    if st.button("วิเคราะห์ประสิทธิภาพ"):
        if c0 <= 0 or ce > c0:
            st.error("กรุณาตรวจสอบความเข้มข้น C0 และ Ce")
        else:
            removal = ((c0 - ce) / c0) * 100
            qe = ((c0 - ce) * volume) / mass

            st.metric(
                "Removal Efficiency",
                f"{removal:.2f}%"
            )

            st.metric(
                "Adsorption Capacity",
                f"{qe:.2f} mg/g"
            )

            st.caption(
                f"ผลการคำนวณสำหรับ {pollutant} "
                "ไม่ใช่การรับรองความปลอดภัยของน้ำ"
            )

elif menu == "Reuse Tracker":
    st.header("Reuse Tracker")
    st.info("ส่วนติดตามประสิทธิภาพการใช้ซ้ำจะพัฒนาในขั้นต่อไป")

elif menu == "AI Advisor":
    st.header("AI Advisor")
    st.info("ระบบช่วยวิเคราะห์และให้คำแนะนำจะพัฒนาในขั้นต่อไป")

st.divider()
st.caption("Biochar AI | Research Prototype")
