import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd


# Display title & Description
st.title("Test Spreadsheet")
st.markdown("This apps will be used for gathering data")
# Establishing a google sheet connection
conn = st.experimental_connection("gsheets", type = GSheetsConnection)
# Fetch existing vendors data
existing_data = conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1z7UPC-LoZDsNvsVbGv4cYsAM8D65wdIKci3xBXGMTqw/edit?usp=sharing", usecols=list(range(3)), ttl=1)

st.subheader("Identitas")

# Pertanyaan Usia
Age = st.slider("Berapa usia Anda?", min_value=11, max_value=68, value=25)

# Pertanyaan Jenis Kelamin
Gender_options = ["Laki-laki", "Perempuan"]
Gender = st.selectbox("Jenis kelamin Anda apa?", Gender_options)

st.markdown("""---""")

st.subheader("Riwayat Kesehatan Mental")

# Pertanyaan Masalah Kesehatan Sebelumnya
Past_disorder_options = ["Iya","Tidak","Tidak tahu"]
Past_disorder = st.selectbox("Pernahkah Anda mengalami gangguan kesehatan mental sebelumnya?", Past_disorder_options)

Family_history_options = ["Iya", "Tidak", "Tidak tahu"]
Family_history = st.selectbox("Apakah ada riwayat gangguan kesehatan mental dalam keluarga Anda?", Family_history_options)

Mental_health_treatment_options = ["Iya", "Tidak"]
Mental_health_treatment = st.selectbox("Pernahkah Anda mencari perawatan dari profesional kesehatan mental untuk gangguan kesehatan mental?", Mental_health_treatment_options)

st.markdown("""---""")

st.subheader("Pentingnya Kesehatan Mental di Tempat Kerja")

# Pertanyaan Pentingnya Kesehatan Mental di Tempat Kerja
st.markdown("""Rentang nilai: 0 (Tidak Penting Sama Sekali) - 10 (Sangat Penting)""")
Employer_mental_health_importance2 = st.slider("Seberapa penting menurut Anda perusahaan Anda menghargai kesehatan mental?", min_value=0, max_value=10, value=1)

st.markdown("""Rentang nilai: 0 (Tidak Penting Sama Sekali) - 10 (Sangat Penting)""")
Employer_physical_health_importance1 = st.slider("Seberapa penting menurut Anda perusahaan Anda dalam menghargai kesehatan fisik?", min_value=0, max_value=10, value=1)

st.markdown("""Rentang nilai: 1 (Sangat Tidak Didukung) - 5 (Sangat Didukung)""")
Tech_industry_support = st.slider("Bagaimana menurut Anda dukungan yang diberikan perusahaan Anda kepada karyawan yang memiliki gangguan kesehatan mental?", min_value=0, max_value=5, value=1)

st.markdown("""---""")

st.subheader("Manfaat Kesehatan Mental di Tempat Kerja")

# Pertanyaan Manfaat Kesehatan Mental di Tempat Kerja
Health_benefits_options = ["Iya","Tidak","Tidak tahu"]
Health_benefits = st.selectbox("Apakah perusahaan Anda menyediakan manfaat kesehatan mental sebagai bagian dari cakupan perawatan kesehatan mental?", Health_benefits_options)

Previous_benefits_options = ["Iya","Tidak","Tidak tahu"]
Previous_benefits = st.selectbox("Apakah perusahaan – perusahaan sebelumnya Anda menyediakan manfaat kesehatan mental?", Previous_benefits_options)

Mental_health_options_options = ["Iya","Tidak","Tidak tahu"]
Mental_health_options = st.selectbox("Apakah Anda mengetahui opsi perawatan kesehatan mental yang disediakan oleh perusahaan – perusahaan sebelumnya tempat Anda bekerja?", Mental_health_options_options)

st.markdown("""---""")

st.subheader("Kenyamanan Berbicara tentang Kesehatan Mental")

# Pertanyaan Kenyamanan Berbicara tertang Kesehatan Mental
Share_mental_illness_options = ["Tidak berlaku untuk saya","Tidak terbuka sama sekali","Netral","Agak tidak terbuka","Agak terbuka","Sangat terbuka"]
Share_mental_illness = st.selectbox("Seberapa bersedia Anda untuk berbicara kepada teman dan keluarga bahwa Anda memiliki masalah kesehatan mental?", Share_mental_illness_options)

Supervisor_comfort_options = ["Iya","Tidak","Mungkin"]
Supervisor_comfort = st.selectbox("Apakah Anda merasa nyaman untuk berbicara tentang masalah kesehatan mental dengan atasan langsung Anda?", Supervisor_comfort_options)

Coworker_mental_health_discussion1_options = ["Iya","Tidak","Mungkin"]
Coworker_mental_health_discussion1 = st.selectbox("Apakah Anda merasa nyaman untuk berbicara tentang masalah kesehatan mental dengan rekan kerja Anda?", Coworker_mental_health_discussion1_options)

Coworker_mental_health_discussion2_options = ["Iya","Tidak"]
Coworker_mental_health_discussion2 = st.selectbox("Pernahkah Anda membicarakan masalah kesehatan mental dengan rekan kerja Anda?", Coworker_mental_health_discussion2_options)

Employer_mental_health_discussion_options = ["Iya","Tidak"]
Employer_mental_health_discussion = st.selectbox("Pernahkah Anda membicarakan masalah kesehatan mental dengan atasan Anda?", Employer_mental_health_discussion_options)

st.markdown("""---""")

st.subheader("Faktor – Faktor Tambahan")

# Pertanyaan Faktor - Faktor Tambahan
Employees_count_options = ["1-100","100-1000","Lebih dari 1000"]
Employees_count = st.selectbox("Berapa jumlah karyawan di perusahaan atau organisasi anda bekerja?", Employees_count_options)

Medical_leave_ease_options = ["Sulit","Saya tidak tahu","Agak sulit","Agak mudah","Sangat mudah"]
Medical_leave_ease = st.selectbox("Jika masalah kesehatan mental mendorong anda untuk mengajukan cuti medis dari pekerjaan, seberapa mudah atau sulitnya untuk meminta cuti tersebut?", Medical_leave_ease_options)

Health_disclosure_options = ["Iya","Tidak","Mungkin"]
Health_disclosure = st.selectbox("Apakah anda bersedia untuk membicarakan masalah kesehatan fisik dengan calon pemberi kerja dalam wawancara kerja?", Health_disclosure_options)

Emotions = st.text_input("Apa yang membuat Anda merasa cemas atau stres akhir-akhir ini?")
