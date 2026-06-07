import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# 1. Chargement d d-data mzyan (Eviter les erreurs d'encodage)
print("⏳ Chargement des données en cours...")
df = pd.read_csv('DataCoSupplyChainDataset.csv', encoding='latin1')

# 2. Sggmdi les dates d l-ventes
df['order date (DateOrders)'] = pd.to_datetime(df['order date (DateOrders)'])

print(f"✅ Données chargées : {df.shape[0]} lignes et {df.shape[1]} colonnes.")

# ==========================================
# 🔥 PARTIE 1 : L-CALCUL DIAL L'ANALYSE ABC
# ==========================================
print("\n📊 Calcul de l'Analyse ABC...")

# Groupby par produit pour calculer le CA global de chacun
abc_df = df.groupby('Product Name')['Sales'].sum().reset_index()
abc_df = abc_df.sort_values(by='Sales', ascending=False).reset_index(drop=True)

# Calcul du pourcentage cumulé du Chiffre d'Affaires
abc_df['Revenue_Share'] = abc_df['Sales'] / abc_df['Sales'].sum()
abc_df['Cum_Share'] = abc_df['Revenue_Share'].cumsum()

# Assignation des Classes A (80%), B (15%), C (5%) b l-mft7
def assign_abc_class(cum_share):
    if cum_share <= 0.80:
        return 'Classe A (Top 80% CA)'
    elif cum_share <= 0.95:
        return 'Classe B (Medium 15% CA)'
    else:
        return 'Classe C (Low 5% CA)'

abc_df['ABC_Class'] = abc_df['Cum_Share'].apply(assign_abc_class)

# Affichage des résultats pour le recruteur
print("\n🎯 Résultats de la Segmentation ABC :")
print(abc_df['ABC_Class'].value_counts())

# Save les résultats f CSV m9add
abc_df.to_csv('product_abc_segmentation.csv', index=False)
print("💾 Fichier 'product_abc_segmentation.csv' sauvegardé !")

# ==========================================
# 📈 PARTIE 2 : DECOMPOSITION DE SERIES TEMPORELLES
# ==========================================
print("\n📉 Extraction de la Saisonnalité des Ventes...")

# Groupby par Date (par exemple par semaine ou par mois pour lisser le flux)
ts_data = df.set_index('order date (DateOrders)').resample('W')['Sales'].sum().fillna(0)

# Décomposition saisonnière (Modèle Additif sur base de 52 semaines par an)
decomposition = seasonal_decompose(ts_data, model='additive', period=52)

# Sauvegarder les composantes pour Power BI
ts_exported = pd.DataFrame({
    'Actual_Sales': ts_data,
    'Trend': decomposition.trend,
    'Seasonal': decomposition.seasonal,
    'Residual': decomposition.resid
}).reset_index()

ts_exported.to_csv('time_series_decomposition.csv', index=False)
print("💾 Fichier 'time_series_decomposition.csv' sauvegardé pour Power BI !")
print("🚀 Analyse terminée avec succès !")