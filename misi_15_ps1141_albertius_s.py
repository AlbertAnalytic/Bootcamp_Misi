# -*- coding: utf-8 -*-
"""Misi 15-PS1141-Albertius S.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zPdSdOlvn1CmX83RFYmeemVCycA_zMx2

#Identifikasi Masalah
## 1. Ketidaktepatan strategi penjualan di tiap cabang Superstore
## 2. Program Diskon besar saat tingkat penjualan sedang tinggi sehingga mengalami kerugian toko.
"""



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics  import mean_squared_error
from sklearn.cluster import KMeans

df= pd.read_csv('/content/SuperStore - data.csv')

df

df.info()

df.describe()

df.dropna(inplace=True)

#Memilih fitur untukn clasterisasi
features = df[['Sales','Profit','Discount']]

#Normalisasi
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
Scaled_features = scaler.fit_transform(features)

"""Pemilihan Jumlah Cluster"""

# Metode Elbow
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(Scaled_features)
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 11), inertia)
plt.xlabel('Jumlah Cluster')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

k = 3  # Misalkan jumlah cluster yang dipilih berdasarkan analisis Elbow
kmeans = KMeans(n_clusters=k, random_state=0)
kmeans.fit(Scaled_features)

# Tambahkan label cluster ke DataFrame
df['Cluster'] = kmeans.labels_

# Visualisasikan hasil clustering dengan warna yang lebih jelas
plt.figure(figsize=(10, 6))
palette = sns.color_palette('tab10', n_colors=k)
sns.scatterplot(x='Sales', y='Profit', hue='Cluster', palette=palette, data=df, s=100, alpha=0.7, edgecolor='k')
plt.title('Clustering Sales vs Profit')
plt.legend(title='Cluster')
plt.show()

"""# Kesimpulan
1. Cluster Biru terdiri dari cabang superstore dengan sales dan profit yang rendah (Kemungkinan cabang tersebut terletak di daerah dengan populasi kecil dengan tingkat persaingan yang tinggi)
2. Cluster Hijau cabang superstore dengan sales dan profit yang tinggi (Kemungkinan cabang tersebut terletak di daerah dengan populasi yang besar atau tingkat persaingan yang rendah)
3. Cluster Orange ialah cabang superstore dengan sales dan profit yang beragam (Kemungkinan kluster ini mewakili cabng yang memiliki performa yang tidak konsisten atau dipengaruhi oleh faktor-faktor lain )

#Interpretasi

1. Cluster Biru : Membutuhkan strategi penjualan yang fokus pada peningkatan visibilitas dan atraksi pelanggan. hal ini dilakukan dengan meningkatkan promosi, mengadakan event atau menawarkan program diskon yang menarik.
2. Cluster Hijau : Cluster ini dapat menerapkan strategi penjualan yang fokus pada mempertahankan pelanggan dan meningkatkan loyalitas. cluster dapat melakukan hal seperti menawarkan membership, memberikan reward kepada pelanggan setia atau meningkatkan kualitas layanan pelanggan.
3. Cluster Orange : Membutuhkan analisis yang lebih mendalam untuk menentukan strategi penjualan yang tepat. analisis faktor yang mungkin mempengaruhi kinerja cabang, seperti demografi pelanggan, trend pasar dan kondisi ekonomi.
"""

