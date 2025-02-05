import pygal
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import random

# Jumlah data yang seragam (misalnya 12 bulan)
num_samples = 12

# Simulasi data transaksi e-commerce
data = {
    "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"],
    "Jumlah Transaksi": [120, 150, 170, 160, 180, 200, 220, 210, 230, 250, 270, 300],
    "Nilai Transaksi": [random.randint(50, 500) for _ in range(num_samples)],  # Harus 12, bukan 100
    "Jumlah Pembelian": [random.randint(1, 20) for _ in range(num_samples)],   # Harus 12
    "Pendapatan": [random.randint(100, 5000) for _ in range(num_samples)]      # Harus 12
}

df = pd.DataFrame(data)

# ======== 1. Line Chart dengan Pygal (Tren Jumlah Transaksi per Bulan) ========
line_chart = pygal.Line()
line_chart.title = "Tren Jumlah Transaksi per Bulan"
line_chart.x_labels = data["Bulan"]
line_chart.add("Jumlah Transaksi", data["Jumlah Transaksi"])
line_chart.render_to_file("line_chart.svg")  # Simpan sebagai file SVG

# ======== 2. Histogram dengan Seaborn (Distribusi Nilai Transaksi) ========
plt.figure(figsize=(8, 5))
sns.histplot(df["Nilai Transaksi"], bins=12, kde=True, color='blue')
plt.title("Distribusi Nilai Transaksi")
plt.xlabel("Nilai Transaksi")
plt.ylabel("Frekuensi")
plt.grid()
plt.show()

# ======== 3. Scatter Plot dengan Matplotlib & Seaborn (Hubungan Jumlah Pembelian vs Pendapatan) ========
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Jumlah Pembelian"], y=df["Pendapatan"], color='red')
plt.title("Hubungan Jumlah Pembelian dengan Pendapatan")
plt.xlabel("Jumlah Pembelian")
plt.ylabel("Pendapatan (IDR)")
plt.grid()
plt.show()
