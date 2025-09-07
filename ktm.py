import streamlit as st
from streamlit_option_menu import option_menu  # pakai yang kemarin aja

# Data akun + mahasiswa
users = {
    "wisnu": {
        "password": "1234",
        "data": {
            "NIM": "25156341090",
            "Nama": "I Made Wisnu Danu Artha",
            "Program Studi": "Magister Akuntansi",
            "Angkatan": 2025,
            "KTM_png": "ktm-danu2.png"
        }
    },
    "linda": {
        "password": "123456",
        "data": {
            "NIM": "25156341091",
            "Nama": "Ni Putu Linda Christina",
            "Program Studi": "Magister Akuntansi",
            "Angkatan": 2025,
            "KTM_png": "ktm-linda.png"
        }
    },
    "diah": {
        "password": "12345678",
        "data": {
            "NIM": "25156341092",
            "Nama": "Luh Diah Permata Saraswati Eka Cahyani",
            "Program Studi": "Magister Akuntansi",
            "Angkatan": 2025,
            "KTM_png": "ktm-diah.png"
        }
    }
}

# Inisialisasi session
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

# Login page
if not st.session_state.logged_in:
    st.title("🔐 Login Mahasiswa")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login berhasil! Silakan pilih menu di sidebar.")
        else:
            st.error("Username atau password salah.")

# Dashboard
else:
    user_data = users[st.session_state.username]["data"]

    with st.sidebar:
        selected = option_menu(
            "Menu",
            ["DATA MAHASISWA", "KRS", "KHS", "KTM", "Logout"],
            icons=["person", "book", "bar-chart", "credit-card", "box-arrow-right"],
            menu_icon="cast",
            default_index=0,
        )

    if selected == "DATA MAHASISWA":
        st.subheader("Data Mahasiswa")
        
        # Bikin data dalam bentuk tabel
        data = {
            "Field": ["Nama", "NIM", "Program Studi", "Angkatan"],
            "Value": [user_data["Nama"], user_data["NIM"], user_data["Program Studi"], user_data["Angkatan"]]
        }
        st.dataframe(data, use_container_width=True, height=200)

    elif selected == "KRS":
        st.subheader("📖 Kartu Rencana Studi (KRS)")
        st.info("Data KRS belum tersedia.")

    elif selected == "KHS":
        st.subheader("📊 Kartu Hasil Studi (KHS)")
        st.info("Data KHS belum tersedia.")

    elif selected == "KTM":
        st.subheader("🎓 Kartu Tanda Mahasiswa (KTM)")
        try:
            st.image(user_data["KTM_png"], caption=f"KTM {user_data['Nama']}", use_container_width=True)
        except Exception as e:
            st.error(f"Gagal membuka file KTM: {e}")

    elif selected == "Logout":
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()
