import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="Atakrib Elektronik Jogja", 
    page_icon="⚡", 
    layout="centered"
)

# Judul Utama
st.title("⚡ Atakrib Elektronik - Katalog & Asisten")
st.write("Temukan produk elektronik pilihan terbaik untuk wilayah Jogja. Konsultasi langsung via WhatsApp!")

# Sidebar untuk Filter Kategori
st.sidebar.header("Filter Produk")
kategori = st.sidebar.selectbox("Pilih Kategori:", ["Semua", "AC", "Mesin Cuci", "Televisi", "Kulkas"])

# Data Produk Sementara (Nanti bisa diperbarui sesuai barang asli di toko)
produk_list = [
    {
        "nama": "Smart TV 43 Inch Android", 
        "kategori": "Televisi", 
        "harga": "Rp 3.500.000", 
        "deskripsi": "Resolusi 4K tajam, suara jernih, garansi resmi.", 
        "gambar": "📺"
    },
    {
        "nama": "Mesin Cuci 2 Tabung 8kg", 
        "kategori": "Mesin Cuci", 
        "harga": "Rp 1.800.000", 
        "deskripsi": "Hemat listrik, tabung besar anti karat, awet.", 
        "gambar": "🌀"
    },
    {
        "nama": "AC Standard 1/2 PK", 
        "kategori": "AC", 
        "harga": "Rp 2.900.000", 
        "deskripsi": "Dingin cepat, freon ramah lingkungan, cocok untuk kamar.", 
        "gambar": "❄️"
    },
    {
        "nama": "Kulkas 2 Pintu Inverter", 
        "kategori": "Kulkas", 
        "harga": "Rp 3.800.000", 
        "deskripsi": "Hemat energi, bebas bunga es (no frost), kapasitas luas.", 
        "gambar": "🧊"
    }
]

# Filter produk berdasarkan pilihan kategori
if kategori == "Semua":
    filtered_products = produk_list
else:
    filtered_products = [p for p in produk_list if p['kategori'] == kategori]

# Tampilkan Daftar Produk dalam Card
st.header("📦 Katalog Pilihan")
for p in filtered_products:
    with st.container():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(f"<h1 style='text-align: center;'>{p['gambar']}</h1>", unsafe_allow_html=True)
        with col2:
            st.subheader(p['nama'])
            st.write(f"**Harga Estimasi:** {p['harga']}")
            st.write(p['deskripsi'])
            
            # Tombol Pesan via WhatsApp (Ganti nomor di bawah nanti dengan nomor WA Anda, format: 628xxxxxxxxxx)
            no_wa = "6281234567890" 
            pesan = f"Halo, saya tertarik dengan produk {p['nama']} ({p['harga']}) yang ada di web katalog Atakrib."
            link_wa = f"https://wa.me/{no_wa}?text={pesan.replace(' ', '%20')}"
            
            st.markdown(f"[📥 Pesan / Tanya via WhatsApp]({link_wa})", unsafe_allow_html=True)
        st.divider()

# Fitur Kotak Tanya Sederhana
st.subheader("🤖 Tanya Asisten Elektronik")
user_query = st.text_input("Bingung pilih barang? Ketik di sini (Cth: 'Cari AC hemat listrik untuk kamar 3x3'):")
if user_query:
    st.info(f"Asisten: Untuk pertanyaan '{user_query}', kami menyarankan produk AC Standard 1/2 PK atau kunjungi toko kami untuk konsultasi langsung.")