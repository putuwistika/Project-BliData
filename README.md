
# Exploratory Data Analysis  
**BLI DATA - Group 1 Final Project Rakamin Batch 49**  

---

## WHO WE ARE?  
**Bli Data** is a dedicated team of data specialists based in Indonesia, committed to empowering the e-commerce industry with data-driven solutions.  

We specialize in harnessing the power of:  
- **Analytics**  
- **Machine Learning**  
- **Business Intelligence**  

Our focus is to:  
- Optimize operations  
- Enhance customer experiences  
- Drive growth for our partners  

With a deep understanding of Indonesia's dynamic e-commerce landscape, Bli Data offers tailored strategies and cutting-edge insights that help businesses thrive in a competitive market.  

**Our mission**: To transform data into actionable value, enabling sustainable success for our clients.  

---

## TEAM MEMBERS  
- **<span style="color:#27AE60">Febriyan Chandra</span>** — Project Manager  
- **<span style="color:#2980B9">Ramadani Saputra</span>** — Data Engineer  
- **<span style="color:#8E44AD">I Putu Ferry Wistika</span>** — Data Scientist  

---

## PROJECT SUMMARY  
This project focuses on **Exploratory Data Analysis (EDA)** for e-commerce data, aiming to uncover insights, improve decision-making, and support growth strategies.  

### Key Objectives:  
1. Understand customer behavior and trends.  
2. Identify patterns and anomalies in sales and operations data.  
3. Provide actionable recommendations to improve business outcomes.  

---

## GETTING STARTED  
To run this project locally, follow these steps:  
1. Clone the repository:  
   ```bash
   git clone https://github.com/putuwistika/EDA-Project-BliData.git
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Set up environment variables in a `.env` file:  
   ```env
   DB_USER=your_username
   DB_PASSWORD=your_password
   DB_HOST=your_host
   DB_PORT=your_port
   DB_NAME=your_database
   ```   
---

## TECHNOLOGIES USED  
- Python  
- Pandas  
- Matplotlib  
- Plotly  
- PostgreSQL

## 1. DESCRIPTIVE STATISTICS

### A. Apakah ada kolom dengan tipe data kurang sesuai, atau nama kolom dan isinya kurang sesuai?
1. **Kolom bertipe data tidak sesuai**:
   - `order_estimated_delivery_date` bertipe `object`, seharusnya `datetime64`.
   - `order_item_id` bertipe `float64`, sebaiknya diubah ke `integer`.

2. **Kolom yang perlu diperbaiki**:
   - `review_creation_date` seharusnya diubah ke `datetime64`.

### B. Apakah ada kolom yang memiliki nilai kosong?
| Kolom                        | Jumlah Data Kosong |
|------------------------------|--------------------|
| `order_approved_at`          | 176               |
| `order_delivered_carrier_date` | 2.067           |
| `order_delivered_customer_date` | 3.390          |
| `order_item_id`              | 1.051             |
| `product_id`                 | 1.051             |
| `product_category_name`      | 1.051             |
| `product_name_length`        | 2.750             |
| `product_description_length` | 2.750             |
| `product_photos_qty`         | 2.750             |
| `product_weight_g`           | 1.071             |
| `product_length_cm`          | 1.071             |
| `product_height_cm`          | 1.071             |
| `product_width_cm`           | 1.071             |
| `review_id`                  | 704               |
| `review_score`               | 704               |
| `review_creation_date`       | 704               |
| `review_answer_timestamp`    | 704               |

**Rekomendasi Next Action**:
- Identifikasi kolom penting.
- Skala prioritas untuk penanganan data kosong.
- Analisis akar penyebab data kosong.

### C. Apakah ada kolom yang memiliki nilai summary agak aneh?
1. **`product_weight_g`**: 
   - Min: 0 gram → Periksa data asli atau anggap ini sebagai anomali.
2. **`product_photos_qty`**:
   - Max: 20 foto → Perlu verifikasi relevansi data.
3. **`payment_value`**: 
   - Min: 0 → Periksa apakah ini karena pembatalan pesanan atau kesalahan data.

---

## 2. UNIVARIATE ANALYSIS

### Analisis:
- Distribusi sangat miring dapat distabilkan dengan transformasi (log atau Box-Cox).
- Outlier harus diverifikasi apakah data valid atau anomali.

**Rekomendasi Pre-Processing**:
- Normalisasi data.
- Transformasi distribusi yang miring.
- Validasi data outlier.
- Normalisasi fitur dengan skala besar (contoh: `customer_zip_code_prefix`).

---

## 3. MULTIVARIATE ANALYSIS

### A. Korelasi Antar Feature dan Label
1. **`payment_value`**: Korelasi moderat dengan `payment_installments`.
2. **`product_weight_g`**: Korelasi moderat dengan dimensi produk.
3. **`review_score`**: Tidak memiliki korelasi signifikan dengan fitur lain.

### B. Korelasi Antar Feature
1. **Dimensi Produk**:
   - Korelasi kuat antara `product_length_cm`, `product_height_cm`, dan `product_width_cm`.
2. **Geolokasi**:
   - Korelasi negatif antara `geolocation_lat` dan `geolocation_lng`.

**Rekomendasi**:
- Reduksi dimensi produk menjadi satu fitur seperti volume.
- Gabungkan geolokasi menjadi representasi jarak atau cluster wilayah.

---

## 4. BUSINESS INSIGHT

### Insight 1: Kategori Produk Terpopuler
- **Data**: Kategori *Bed, Bath, and Table* memiliki jumlah pesanan tertinggi.
- **Rekomendasi**:
  - Tingkatkan stok dan variasi produk.
  - Kampanye promosi khusus seperti diskon musiman.

### Insight 2: Distribusi Skor Ulasan
- **Data**: Mayoritas ulasan berada di kisaran 4.5–5.0.
- **Rekomendasi**:
  - Pertahankan kualitas produk dan pelayanan.
  - Analisis ulasan dengan skor rendah untuk perbaikan layanan.

### Insight 3: Tren Penjualan Bulanan
- **Data**: Puncak penjualan pada Oktober 2017, penurunan tajam pada akhir 2018.
- **Rekomendasi**:
  - Analisis penyebab penurunan.
  - Replikasi strategi sukses di Oktober 2017.
  - Diversifikasi produk atau pasar untuk mengurangi risiko.
