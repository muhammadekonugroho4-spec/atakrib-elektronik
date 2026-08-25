import streamlit as st

# 1. Konfigurasi Halaman (Lebar penuh / Wide)
st.set_page_config(page_title="Katalog Atakrib", layout="wide")

# 2. Menyembunyikan menu bawaan Streamlit agar terlihat seperti web asli
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. Header & Kolom Pencarian (Meniru bagian atas Inaproc)
st.markdown("### ⚡ Katalog Elektronik Atakrib")
cari = st.text_input("🔍 Cari produk & penyedia di sini...", placeholder="Ketik nama barang...")

# 4. Banner (Menggunakan gambar placeholder sebagai contoh)
st.image("https://images.unsplash.com/photo-1550009158-9a4f6f466bba?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80", use_column_width=True)

st.markdown("#### Produk Pilihan & Terlaris di Jogja")
st.write("") # Spasi kosong

# 5. Data Produk (Menggunakan gambar URL asli agar terlihat nyata)
produk = [
    {
        "nama": "Kulkas 2 Pintu LG Smart Inverter",
        "harga": "Rp 3.850.000,00",
        "label": "Barang",
        "lokasi": "KOTA YOGYAKARTA",
        "terjual": 12,
        "gambar": "https://images.unsplash.com/photo-1584568694244-14fbdf83bd30?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
    },
    {
        "nama": "AC Daikin Standard 1 PK",
        "harga": "Rp 4.100.000,00",
        "label": "Barang",
        "lokasi": "KOTA YOGYAKARTA",
        "terjual": 8,
        "gambar": "https://images.unsplash.com/photo-1618220179428-22790b46a0eb?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
    },
    {
        "nama": "Mesin Cuci Samsung Top Load 9kg",
        "harga": "Rp 2.950.000,00",
        "label": "Pre Order",
        "lokasi": "KAB. SLEMAN",
        "terjual": 0,
        "gambar": "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
    },
    {
        "nama": "Smart TV Samsung 43 Inch 4K UHD",
        "harga": "Rp 4.500.000,00",
        "label": "Barang",
        "lokasi": "KOTA YOGYAKARTA",
        "terjual": 25,
        "gambar": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
    },
    {
        "nama": "Microwave Sharp 20 Liter",
        "harga": "Rp 950.000,00",
        "label": "Barang",
        "lokasi": "KOTA BANTUL",
        "terjual": 5,
        "gambar": "https://images.unsplash.com/photo-1574269909862-7e1d70bb8078?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
    }
]

# 6. Membuat Layout Grid (5 Kolom seperti Inaproc)
cols = st.columns(5)

# 7. Menyisipkan HTML & CSS untuk membuat Kartu (Card) yang rapi
for i, p in enumerate(produk):
    with cols[i % 5]:
        # Desain Card HTML
        card_html = f"""
        <div style="
            border: 1px solid #e0e0e0; 
            border-radius: 8px; 
            padding: 15px; 
            background-color: white; 
            height: 380px; 
            display: flex; 
            flex-direction: column;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            transition: 0.3s;
        ">
            <!-- Label -->
            <div style="margin-bottom: 10px;">
                <span style="background-color: #e3f2fd; color: #1976d2; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;">
                    {p['label']}
                </span>
            </div>
            
            <!-- Area Gambar -->
            <div style="height: 140px; display: flex; align-items: center; justify-content: center; overflow: hidden; margin-bottom: 15px;">
                <img src="{p['gambar']}" style="max-height: 100%; max-width: 100%; object-fit: contain;">
            </div>
            
            <!-- Judul Produk -->
            <div style="font-weight: 600; font-size: 14px; line-height: 1.3; color: #333; margin-bottom: 10px; flex-grow: 1;">
                {p['nama']}
            </div>
            
            <!-- Harga -->
            <div style="font-weight: 800; font-size: 16px; color: #2c3e50; margin-bottom: 10px;">
                {p['harga']}
            </div>
            
            <!-- Info Lokasi & Terjual -->
            <div style="font-size: 11px; color: #7f8c8d; border-top: 1px solid #eee; padding-top: 8px;">
                📍 {p['lokasi']}<br>
                Terjual {p['terjual']}
            </div>
        </div>
        <br>
        """
        # Menampilkan Card
        st.markdown(card_html, unsafe_allow_html=True)
        
        # Tombol interaktif (Streamlit native) di bawah setiap card
        if st.button("Lihat Detail", key=f"btn_{i}", use_container_width=True):
            st.success(f"Masuk ke halaman detail {p['nama']}")import streamlit as st

# 1. Konfigurasi Halaman (Lebar penuh / Wide)
st.set_page_config(page_title="Katalog Atakrib", layout="wide")

# 2. Menyembunyikan menu bawaan Streamlit agar terlihat seperti web asli
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. Header & Kolom Pencarian (Meniru bagian atas Inaproc)
st.markdown("### ⚡ Katalog Elektronik Atakrib")
cari = st.text_input("🔍 Cari produk & penyedia di sini...", placeholder="Ketik nama barang...")

# 4. Banner (Menggunakan gambar placeholder sebagai contoh)
st.image("https://images.unsplash.com/photo-1550009158-9a4f6f466bba?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80", use_column_width=True)

st.markdown("#### Produk Pilihan & Terlaris di Jogja")
st.write("") # Spasi kosong

# 5. Data Produk (Menggunakan gambar URL asli agar terlihat nyata)
produk = [
    {
        "nama": "Kulkas 2 Pintu LG Smart Inverter",
        "harga": "Rp 3.850.000,00",
        "label": "Barang",
        "lokasi": "KOTA YOGYAKARTA",
        "terjual": 12,
        "gambar": "https://images.unsplash.com/photo-1584568694244-14fbdf83bd30?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
    },
    {
        "nama": "AC Daikin Standard 1 PK",
        "harga": "Rp 4.100.000,00",
        "label": "Barang",
        "lokasi": "KOTA YOGYAKARTA",
        "terjual": 8,
        "gambar": "https://images.unsplash.com/photo-1618220179428-22790b46a0eb?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
    },
    {
        "nama": "Mesin Cuci Samsung Top Load 9kg",
        "harga": "Rp 2.950.000,00",
        "label": "Pre Order",
        "lokasi": "KAB. SLEMAN",
        "terjual": 0,
        "gambar": "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
    },
    {
        "nama": "Smart TV Samsung 43 Inch 4K UHD",
        "harga": "Rp 4.500.000,00",
        "label": "Barang",
        "lokasi": "KOTA YOGYAKARTA",
        "terjual": 25,
        "gambar": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
    },
    {
        "nama": "Microwave Sharp 20 Liter",
        "harga": "Rp 950.000,00",
        "label": "Barang",
        "lokasi": "KOTA BANTUL",
        "terjual": 5,
        "gambar": "https://images.unsplash.com/photo-1574269909862-7e1d70bb8078?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80"
    }
]

# 6. Membuat Layout Grid (5 Kolom seperti Inaproc)
cols = st.columns(5)

# 7. Menyisipkan HTML & CSS untuk membuat Kartu (Card) yang rapi
for i, p in enumerate(produk):
    with cols[i % 5]:
        # Desain Card HTML
        card_html = f"""
        <div style="
            border: 1px solid #e0e0e0; 
            border-radius: 8px; 
            padding: 15px; 
            background-color: white; 
            height: 380px; 
            display: flex; 
            flex-direction: column;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            transition: 0.3s;
        ">
            <!-- Label -->
            <div style="margin-bottom: 10px;">
                <span style="background-color: #e3f2fd; color: #1976d2; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;">
                    {p['label']}
                </span>
            </div>
            
            <!-- Area Gambar -->
            <div style="height: 140px; display: flex; align-items: center; justify-content: center; overflow: hidden; margin-bottom: 15px;">
                <img src="{p['gambar']}" style="max-height: 100%; max-width: 100%; object-fit: contain;">
            </div>
            
            <!-- Judul Produk -->
            <div style="font-weight: 600; font-size: 14px; line-height: 1.3; color: #333; margin-bottom: 10px; flex-grow: 1;">
                {p['nama']}
            </div>
            
            <!-- Harga -->
            <div style="font-weight: 800; font-size: 16px; color: #2c3e50; margin-bottom: 10px;">
                {p['harga']}
            </div>
            
            <!-- Info Lokasi & Terjual -->
            <div style="font-size: 11px; color: #7f8c8d; border-top: 1px solid #eee; padding-top: 8px;">
                📍 {p['lokasi']}<br>
                Terjual {p['terjual']}
            </div>
        </div>
        <br>
        """
        # Menampilkan Card
        st.markdown(card_html, unsafe_allow_html=True)
        
        # Tombol interaktif (Streamlit native) di bawah setiap card
        if st.button("Lihat Detail", key=f"btn_{i}", use_container_width=True):
            st.success(f"Masuk ke halaman detail {p['nama']}")