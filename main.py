import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Duomenų įkėlimas (pakeiskite failo pavadinimą)
data = pd.read_csv('housing.csv')

# Duomenų struktūros peržiūra
print(data.head())

# Tikslinės reikšmės ir funkcijų atskyrimas
X = data.drop('price', axis=1)  # Atskirti funkcijas nuo tikslo (price)
y = data['price']  # Tikslinė reikšmė - nekilnojamojo turto kaina

# Kategorinių ir skaitinių stulpelių atskyrimas
categorical_columns = X.select_dtypes(include=['object']).columns  # Kategoriniai stulpeliai
numerical_columns = X.select_dtypes(include=['number']).columns  # Skaitiniai stulpeliai

# Kategorinių stulpelių kodavimas naudojant OneHotEncoder
encoder = OneHotEncoder(sparse_output=False, drop='first')  # Sukuriamas encoderis
categorical_encoded = encoder.fit_transform(X[categorical_columns])  # Koduojame kategorinius stulpelius
categorical_encoded_df = pd.DataFrame(categorical_encoded, columns=encoder.get_feature_names_out(categorical_columns))

# Sujungiame skaitinius ir koduotus kategorinius stulpelius
X_transformed = pd.concat([X[numerical_columns].reset_index(drop=True), categorical_encoded_df.reset_index(drop=True)], axis=1)

# Skalavimas, kad visi kintamieji būtų toje pačioje skalėje
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_transformed)

# PCA su visais komponentais
pca = PCA()
pca.fit(X_scaled)

# Paaiškinamosios dispersijos procentai
explained_variance = pca.explained_variance_ratio_

# Sukuriame stulpelinę diagramą, kuri rodo paaiškinamąją dispersiją per komponentus
plt.figure(figsize=(10, 6))
sns.barplot(x=np.arange(1, len(explained_variance) + 1), y=explained_variance, palette="viridis")
plt.title('PCA Explained Variance per Component', fontsize=16)
plt.xlabel('Principal Component', fontsize=12)
plt.ylabel('Explained Variance Ratio', fontsize=12)
plt.xticks(np.arange(1, len(explained_variance) + 1))
plt.tight_layout()
plt.show()

# Parodome paaiškinamąją dispersiją
print(f"Explained variance ratio per component:\n{explained_variance}")

# Parodome pirmų 2 PCA komponentų paaiškinamąją dispersiją
pca_components = pca.components_

# Sukuriame duomenų rėmelį su pirmų 2 PCA komponentų reikšmėmis
pca_df = pd.DataFrame(pca_components[:2], columns=X_transformed.columns)
pca_df = pca_df.T  # Pakeičiame vietomis stulpelius ir eilučių pavadinimus

# Vizualizuojame pirmų 2 komponentų reikšmes kaip stulpelinę diagramą
plt.figure(figsize=(10, 6))
sns.barplot(x=pca_df.index, y=pca_df[0], palette="viridis")
plt.title('PCA First Component Loadings', fontsize=16)
plt.xlabel('Feature', fontsize=12)
plt.ylabel('Loadings', fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Vizualizuojame antrą komponentą
plt.figure(figsize=(10, 6))
sns.barplot(x=pca_df.index, y=pca_df[1], palette="viridis")
plt.title('PCA Second Component Loadings', fontsize=16)
plt.xlabel('Feature', fontsize=12)
plt.ylabel('Loadings', fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
