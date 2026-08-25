import streamlit as st

# 1. Konfigurasi Halaman (Lebar penuh agar mirip web portal profesional)
st.set_page_config(
    page_title="Katalog Elektronik Atakrib Jogja", 
    page_icon="⚡", 
    layout="wide"
)

# 2. Header & Banner Sederhana
st.title("⚡ Katalog Resmi Atakrib Elektronik Jogja")
st.markdown("Direktori produk elektronik pilihan terbaik, transparan, dan terpercaya di Yogyakarta.")
st.markdown("---")

# 3. Sidebar untuk Filter & Pencarian Utama
st.sidebar.header("🔍 Filter Katalog")
keyword = st.sidebar.text_input("Cari nama produk...")
kategori_pilih = st.sidebar.selectbox("Pilih Kategori:", ["Semua", "AC", "Mesin Cuci", "Televisi", "Kulkas"])

# 4. Database Contoh Produk (Nanti bisa ditambah banyak)
produk_list = [
    {"nama": "Smart TV 43 Inch Android", "kategori": "Televisi", "harga": "Rp 3.500.000", "deskripsi": "Resolusi 4K tajam, suara jernih, garansi resmi.", "gambar": "📺"},
    {"nama": "Mesin Cuci 2 Tabung 8kg", "kategori": "Mesin Cuci", "harga": "Rp 1.800.000", "deskripsi": "Hemat listrik, tabung besar anti karat, awet.", "gambar": "🌀"},
    {"nama": "AC Standard 1/2 PK", "kategori": "AC", "harga": "Rp 2.900.000", "deskripsi": "Dingin cepat, freon ramah lingkungan, cocok untuk kamar.", "gambar": "❄️"},
    {"nama": "Kulkas 2 Pintu Inverter", "kategori": "Kulkas", "harga": "Rp 3.800.000", "deskripsi": "Hemat energi, bebas bunga es (no frost), kapasitas luas.", "gambar": "🧊"},
    {"nama": "Smart TV 32 Inch", "kategori": "Televisi", "harga": "Rp 2.100.000", "deskripsi": "HD Ready, built-in YouTube & Netflix, hemat daya.", "gambar": "📺"},
    {"nama": "Mesin Cuci Front Loading 7kg", "kategori": "Mesin Cuci", "harga": "Rp 4.500.000", "deskripsi": "Pencucian dengan air panas,, pakaian lebih terjaga.", "gambar": "🌀"}
]

# 5. Logika Filter Pencarian
filtered = produk_list
if kategori_pilih != "Semua":
    filtered = [p for p in filtered if p['kategori'] == kategori_pilih]
if keyword:
    filtered = [p for p in filtered if keyword.lower() in p['nama'].lower() or keyword.lower() in p['deskripsi'].lower()]

# 6. Tampilan Grid (Membuat Kotak-kotak Produk / Card ala Katalog Web)
st.subheader(f"Daftar Produk ({len(filtered)} ditemukan)")

if not filtered:
    st.warning("Produk yang Anda cari tidak ditemukan.")
else:
    # Membuat 3 kolom menyamping agar tampak seperti web portal profesional
    cols = st.columns(3)
    
    for index, p in enumerate(filtered):
        col = cols[index % 3] # Membagi item ke 3 kolom secara bergantian
        with col:
            # Menggunakan kontainer dengan border agar mirip "card" produk
            with st.container(border=True):
                st.markdown(f"<h2 style='text-align: center; margin: 0;'>{p['gambar']}</h2>", unsafe_allow_html=True)
                st.markdown(f"### **{p['nama']}**")
                st.caption(f"Kategori: {p['kategori']}")
                st.write(f"**{p['harga']}**")
                st.write(p['deskripsi'])
                
                # Tombol Aksi WhatsApp
                no_wa = "6281234567890" # Ganti nanti dengan nomor WA Anda
                pesan = f"Halo, saya tertarik dengan produk {p['nama']} ({p['harga']}) di katalog web."
                link_wa = f"https://wa.me/{no_wa}?text={pesan.replace(' ', '%20')}"
                
                st.markdown(f"[📥 Pesan via WhatsApp]({link_wa})", unsafe_allow_html=True)

# Footer sederhana
st.markdown("---")
st.caption("© 2026 Atakrib Elektronik Jogja • Dikembangkan secara mandiri untuk kemudahan layanan konsumen.")