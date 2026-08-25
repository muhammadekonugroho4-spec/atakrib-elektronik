import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Detail Produk - Atakrib", layout="wide")

# 1. Menyiapkan Data 1 Barang Secara Tuntas
produk = {
    "nama": "COOCAA LED 32 32S3U Digital Smart TV Coolita 2.0",
    "harga": "Rp Rp2.069.000",
    "kategori": "Tv",
    "status": "Tersedia (Siap Kirim area Jogja)",
    "deskripsi": "Coocaa 32 inch Digital Smart TV (Model : Coocaa 32S3U) merupakan Smart TV berukuran 32 Inch yang cocok digunakan untuk menonton di rumah Anda. Bingkai televisi ini didesain dengan bentuk sederhana yang elegan dan sangat sesuai untuk berbagai jenis interior rumah Anda. Anda dapat memanfaatkan koneksi antarmuka menggunakan Opera TV yang praktis untuk menonton film dan main games melalui televisi Anda. Dan juga Anda dapat mirroring TV Anda dengan Smartphone Anda. Dengan warna TV yang jernih, dan dukungan dari Dolby Digital dan DTS juga memberikan Anda keleluasaan untuk dapat menikmati kualitas audio yang lebih tangguh.",
    "spesifikasi": {
        "Kapasitas": "205 Liter",
        "Daya Listrik": "70 Watt",
        "Dimensi": "555 x 1400 x 585 mm",
        "Garansi": "10 Tahun Kompresor"
    },
    # Link gambar dari internet (bisa diganti dengan foto asli nanti)
    "gambar_url": "https://down-id.img.susercontent.com/file/id-11134207-7r98y-llxawguy4sg706.webp",
    # Link video YouTube (contoh video review kulkas LG)
    "video_url": "https://youtu.be/U5b_lKQ8Y0g" 
}

st.markdown("### ⚡ Detail Produk Atakrib")
st.divider()

# 2. Membagi Layar Menjadi 2 Kolom (Kiri: Media, Kanan: Info)
col1, col2 = st.columns([1.2, 1])

# --- KOLOM KIRI (Untuk Gambar dan Video) ---
with col1:
    # Menampilkan Gambar Produk
    st.image(produk["gambar_url"], use_container_width=True, caption="Foto Representasi Produk")
    
    st.write("") # Spasi kosong
    
    # Menampilkan Video dari YouTube
    st.markdown("#### 🎥 Video Review / Tampilan Asli")
    st.video(produk["video_url"])

# --- KOLOM KANAN (Untuk Detail, Spesifikasi & Aksi) ---
with col2:
    # Nama dan Harga
    st.subheader(produk["nama"])
    st.markdown(f"<h2 style='color: #d35400;'>{produk['harga']}</h2>", unsafe_allow_html=True)
    
    # Status Barang
    st.info(f"📦 **Status:** {produk['status']}")
    
    # Deskripsi Produk
    st.markdown("#### Deskripsi")
    st.write(produk["deskripsi"])
    
    # Spesifikasi (Dibuat menjadi list)
    st.markdown("#### Spesifikasi Teknis")
    for kunci, nilai in produk["spesifikasi"].items():
        st.write(f"- **{kunci}:** {nilai}")
        
    st.write("") # Spasi kosong
    st.write("") # Spasi kosong
    
    # Tombol Aksi WhatsApp dengan Desain CSS
    no_wa = "6281234567890" # Ganti dengan nomor Anda
    pesan = f"Halo, saya ingin bertanya tentang {produk['nama']} seharga {produk['harga']} yang ada di katalog web."
    link_wa = f"https://wa.me/{no_wa}?text={pesan.replace(' ', '%20')}"
    
    tombol_wa_html = f"""
    <a href="{link_wa}" target="_blank" style="text-decoration: none;">
        <div style="background-color: #25D366; color: white; padding: 15px; text-align: center; border-radius: 8px; font-weight: bold; font-size: 16px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: 0.3s;">
            💬 Pesan / Tanya via WhatsApp
        </div>
    </a>
    """
    st.markdown(tombol_wa_html, unsafe_allow_html=True)

st.divider()
st.caption("© 2026 Atakrib Elektronik Jogja")