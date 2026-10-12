import streamlit as st
import pandas as pd


# Konfigurasi Halaman
st.set_page_config(page_title="UTS Analisis Multivariat", layout = "wide")
st.title("Analisis Preferensi Konsumen Produk Skincare")
st.header("UTS Analisis Multivariat")
st.subheader("Dibuat oleh: Benhard Leroy Situmorang")

st.markdown("---")

# Navigation Sidebar
menu = st.sidebar.radio(
    "Navigasi Tata Presentasi",
    ["1. Teori (CA)", "2. Data Awal", "3. Implementasi R & Output", "4. Kesimpulan Akhir (Secara Bisnis)"]
)

if menu == "1. Teori (CA)":
  st.header("Landasan Teori Analisis Multivariat")

  st.subheader("a. Konsep dan Tujuan Correspondonce Analysis (CA)")
  st.markdown("""
  * **Konsep:** Correspondonce Analysis (CA) atau Analisis Korespondensi adalah sebuah algoritma statistik multivariat yang digunakan untuk menganalisis hubungan antara dua variabel kategori dalam tabel kontingensi.
  * **Tujuan:** Melihat hubungan antara dua atau lebih variabel kategori dalam tabel kontingensi dan menyajikannya secara visual dalam grafik berdimensi rendah.
  """)

  st.subheader("b. Langkah kunci penerapan Correspondonce Analysis di R")
  st.markdown("""
  1. **Menyiapkan Data dan Membuat Tabel Kontingensi**: CA dibutuhkan input data kategorik yang telah dibuat menjadi tabel kontingensi menggunakan fungsi `matrix() dan `as.table()`.
  2. **Pemodelan CA:** Menjalankan algoritma CA menggunakan fungsi `CA()` untuk menghitung nilai koordinat, inersia (eigenvalue), dan kontribusi dari setiap baris dan kolom.
  3. **Visualisasi Peta Distribusi CA:**  Menampilkan nilai statistik (eigenvalue, koordinat, kontribusi) dan visualisasikan peta biplot menggunakan paket `factoextra` (`fviz_ca_biplot()`) atau `ggplot2` (tergantung pada dimensi).
  """)

elif menu == "2. Data Awal":

  st.header("Data Awal Survei Konsumen")
  st.write("Sebuah perusahaan skincare ingin menganalisis hubungan antara **tipe produksi skincare** berdasarkan **kelompok usia** dan **jenis kelamin**. Data survei dikumpulkan dari ** 300 responden** disajikan dalam tabel kontingensi sebagai berikut:")

  col1, col2 = st.columns(2)

  with col1:
    st.subheader("Tabel 1: Tipe Produk vs Kelompok Usia")
    data_tabel_1 = pd.DataFrame({
        "Muda (18-25)": [40, 25, 30, 20],
        "Dewasa (26-40)": [30, 35, 15, 25],
        "Tua (>40)": [20, 30, 10, 25]
    }, index=["Moisturizer", "Sunscreen", "Serum", "Cleanser"])
    st.table(data_tabel_1)

  with col2:
    st.subheader("Tabel 2: Tipe Produk vs Jenis Kelamin")
    data_tabel_2 = pd.DataFrame({
        "Pria": [45, 50, 25, 30],
        "Wanita": [45, 40, 30, 40],
    }, index=["Moisturizer", "Sunscreen", "Serum", "Cleanser"])
    st.table(data_tabel_2)

elif menu == "3. Implementasi R & Output":

  st.header("Kode R, Output, dan Visualisasi Peta CA ")
  st.subheader("a. Sintaks Kode R")
  st.write("Persiapan Dataset")
  st.code("""
# Mengimpor paket R yang diperlukan
library(ca)
library(FactoMineR)
library(factoextra)
library(ggplot2)
  """, language = "r")

  st.write("Buat Tabel Kontingensi 1 dan 2")
  st.code("""
# Buat Tabel 1
data_tabel_1 <- matrix(c(40, 30, 20,
                    25, 35, 30,
                    30, 15, 10,
                    20, 25, 25),
                  nrow = 4, byrow = TRUE)

colnames(data_tabel_1) <- c("Muda (18-25)", "Dewasa (26-40)", "Tua (>40)")
rownames(data_tabel_1) <- c("Moisturizer", "Sunscreen", "Serum", "Cleanser")
print("--- Tabel 1 ---")
Tabel_1 <- as.table(data_tabel_1)
print(Tabel_1)

# Buat Tabel 2
data_tabel_2 <- matrix(c(45, 45,
                    50, 40,
                    25, 30,
                    30, 40),
                  nrow = 4, byrow = TRUE)

colnames(data_tabel_2) <- c("Pria", "Wanita")
rownames(data_tabel_2) <- c("Moisturizer", "Sunscreen", "Serum", "Cleanser")
print("--- Tabel 2 ---")
Tabel_2 <- as.table(data_tabel_2)
print(Tabel_2)
  """, language = "r")

  st.text("""
"--- Tabel 1 (Tipe Produk vs Kelompok Usia)  ---"
                  Muda (18-25)  Dewasa (26-40)  Tua (>40)
Moisturizer           40              30           20
Sunscreen             25              35           30
Serum                 30              15           10
Cleanser              20              25           25

"--- Tabel 2 (Tipe Produk vs Jenis Kelamin)---"
             Pria    Wanita
Moisturizer   45       45
Sunscreen     50       40
Serum         25       30
Cleanser      30       40
  """)
  st.markdown("---")

  st.subheader("b & c. Hasil CA & Visualisasi Tabel 1 (Tipe Produk vs Usia)")
  st.write("Hitung hasil CA pada tabel 1")
  st.code("""
res.ca1 <- CA(Tabel_1, graph = FALSE)
print(summary(res.ca1))
  """, language = "r")
  st.text("""
The chi square of independence between the two variables is equal to 15.91721 (p-value =  0.01420528 ).

Eigenvalues
                       Dim.1   Dim.2
Variance               0.051   0.001
% of var.             97.796   2.204
Cumulative % of var.  97.796   100.000

Rows
                  Iner*1000   Dim.1     ctr     cos2      Dim.2     ctr     cos2
Moisturizer     |   7.033 |  -0.151   13.234   0.960  |  -0.031   24.246   0.040 |
Sunscreen       |  12.581 |   0.205   24.284   0.985  |  -0.025   16.265   0.015 |
Serum           |  22.316 |  -0.350   43.354   0.992  |   0.032   16.473   0.008 |
Cleanser        |  10.257 |   0.206   19.128   0.952  |   0.046   43.016   0.048 |

Columns
                Iner*1000     Dim.1    ctr    cos2        Dim.2    ctr     cos2
Muda (18-25)   |   29.909 |  -0.281   58.516  0.999   |   0.011   3.779   0.001 |
Dewasa (26-40) |   4.600  |   0.107   7.710   0.855   |  -0.044   57.864  0.145 |
Tua (>40)      |   17.679 |   0.249   33.774  0.975   |   0.040   38.357  0.025 |
NULL
  """)

  st.write("Visualisasi Peta CA tabel 1")
  st.code("""
fviz_ca_biplot(res.ca1,
               repel = TRUE,
               title = "Visualisasi CA: Tipe Produk vs Kelompok Usia",
               col.row = "blue",
               col.col = "red"))
  """, language = "r")
  st.image("Visualisasi CA Tabel 1.png", caption = "Visualisasi CA: Tipe Produk vs Kelompok Usia")

  st.info("""
  **Interpretasi Biplot Tabel 1:**
  * **Serum:** Memiliki kedekatan koordinat yang kuat, menunjukkan usia muda menggemari produk Serum.
  * **Moisturizer:** Tipe produk tidak memiliki kedekatan koordinat yang kuat, namun tipe ini terletak di antara kelompok muda dan dewasa.
  * **Sunscreen:** Berada relatif dekat dengan kelompok usia dewasa.
  * **Cleanser:** Berada relatif dekat dengan kelompok usia Tua.
  """)
  st.markdown("---")

  st.subheader("d & e. Hasil CA & Visualisasi Tabel 1 (Tipe Produk vs Usia)")
  st.write("Hitung hasil CA pada tabel 2")
  st.code("""
res.ca2 <- CA(Tabel_2, graph = FALSE)
print(summary(res.ca2))

# Tampilkan Eigenvalues
print("--- Eigenvalues ---")
print(res.ca2$eig)

# Tampilkan Koordinat Baris (Tipe Produk)
print("--- Koordinat Baris (Tipe Produk) ---")
print(res.ca2$row$coord)

# Tampilkan Koordinat Kolom (Jenis Kelamin)
print("--- Koordinat Kolom (Jenis Kelamin) ---")
print(res.ca2$col$coord)

# Tampilkan Kontribusi tiap kategori
print("--- Koordinat Tiap Kategori ---")
print(res.ca2$row$contrib)
print(res.ca2$col$contrib)
  """, language = "r")
  st.text("""
"--- Eigenvalues ---"
      eigenvalue      percentage of variance     cumulative percentage of variance
dim1 0.009550963               100                                   100

"--- Koordinat Baris (Tipe Produk) ---"
Moisturizer   Sunscreen     Serum     Cleanser
-0.01639565 -0.12752169  0.07452566  0.12648070

"--- Koordinat Kolom (Jenis Kelamin) ---"
Pria   -0.09934449
Wanita  0.09613983

"--- Koordinat Tiap Kategori ---"
Moisturizer    Sunscreen      Serum        Cleanser
0.8305247      50.2416205    10.4864236    38.4414312

Pria   50.81967
Wanita 49.18033
   """)
  st.write("Visualisasi Peta CA tabel 2")
  st.code("""
baris_koordinat <- data.frame(
  Kategori = rownames(Tabel_2),
  Jarak = as.vector(res.ca2$row$coord),
  Jenis = "Produk"
)

kolom_koordinat <- data.frame(
  Kategori = colnames(Tabel_2),
  Jarak = as.vector(res.ca2$col$coord),
  Jenis = "Jenis Kelamin"
)

data_plot <- rbind(baris_koordinat, kolom_koordinat)

ggplot(data_plot, aes(x = Jarak, y = Kategori, color = Jenis)) +
  geom_point(size = 5) +
  geom_vline(xintercept = 0, linetype = "dashed", color = "gray") +
  labs(title = "Visualisasi CA 1-Dimensi: Tipe Produk vs Jenis Kelamin",
       x = "Dimensi 1 (100%)",
       y = "") +
  theme_minimal() +
  theme(text = element_text(size = 12))
    """, language="r")
  st.image("Visualisasi CA Tabel 2.png", caption = "Visualisasi CA: Tipe Produk vs Jenis Kelamin")
  st.info("""
  **Interpretasi Plot 1-Dimensi Tabel 2:**
  * **Sunscreen & Moisturizer:** Memiliki koordinat yang dekat dengan segmen **Pria** (Pria mendominasi proporsi penggunaan Sunscreen dan Moisturizer).
  * **Cleanser & Serum:** Memiliki koordinat yang dekat dengan segmen **Wanita** (Wanita cenderung lebih dominan pada pembersih dan perawatan khusus ).
  """)

elif menu == "4. Kesimpulan Akhir (Secara Bisnis)":
  st.header("Kode R, Output, dan Visualisasi Peta CA ")

  st.subheader("a. Pola Preferensi Produk Berdasarkan Kelompok Usia")
  st.markdown("""
  * **Konsumen Usia Muda**: Memiliki preferensi yang kuat pada skincare perawatan dan hidrasi muka seperti produk **Serum** dan **Moisturizer**, terutama pada produk **Serum**.
  * **Konsumen Usia Dewasa**: Memiliki preferensi yang kuat antara skincare hidrasi dan proteksi muka dari sinar UV seperti produk **Moisturizer** dan **Sunscreen** dimana kelompok umur mereka mulai berusia.
  * **Konsumen Usia Tua**: Memiliki preferensi yang kuat skincare pembersihan mendasar dan perlindungan harian seperti produk **Cleanser** dan **Sunscreen** untuk menjaga kulit muka.)
  """)

  st.subheader("b. Pola Preferensi Produk Berdasarkan Jenis Kelamin")
  st.markdown("""
  * **Konsumen Pria**: Memiliki preferensi yang kuat pada skincare fungsional dan praktis untuk melindungi kulit saat beraktivitas di luar ruangan seperti produk **Sunscreen** dan **Moisturizer**, terutama pada produk **Sunscreen**.
  * **Konsumen Wanita**: Memiliki preferensi yang kuat pada kelihatan dan pembersihan permukaan , dengan penerapan tahapan perawatan kulit yang lebih kompleks dan bertahap, seperti produk skincare **Serum** dan **Cleanser**.
  """)

  st.subheader("c. Rekomendasi Strategis Bisnis")
  st.markdown("""
  1. **Targeting Usia:** Kemas produk Serum dan Moisturizer dengan tema trendi/aesthetic untuk media sosial guna memikat segmen Muda.
  2. **Branding Gender:** Luncurkan lini *Men's Sunscreen* dengan klaim tidak lengket karena konsumen pria terbukti memiliki keterikatan tinggi pada produk perlindungan sinar UV ini.
  3. **Product Bundling:** Buat paket bundling *Cleansing & Serum Kit* yang difokuskan untuk target pasar wanita.
  """)
