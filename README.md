Supply Chain Operations & Logistics Performance Analytics

An end-to-end data analytics solution that processes enterprise supply chain datasets using Python for data engineering and statistical modeling, combined with an interactive Power BI Executive Dashboard for operational intelligence.

## Core Features & Insights
* **Executive KPIs:** Real-time visibility into overall Sales, Total Units Sold, and Global Late Delivery Risk Factor.
* **Inventory Optimization (ABC Analysis):** Automated Pareto principle ($80/20$ rule) product segmentation dynamically classifying warehouse inventory into strategic priority tiers.
* **Logistics & Shipping Breakdown:** Deep-dive distribution metrics analyzing performance and revenue generation across various shipping modes and market regions.
* **Time-Series Decomposition:** Trend and baseline analysis mapping order dates against product demand trajectories.

## Tech Stack & Architecture
* **Data Engineering:** Python (Pandas, NumPy)
* **Business Intelligence:** Microsoft Power BI Desktop
* **Source Dataset:** DataCo Supply Chain Dataset

## Project Dashboard Preview
![Executive Dashboard Overview](dashboard_overview.png)

## How to Run the Project
1. Clone the repository: `git clone https://github.com/AOUATEF785/Supply-Chain-Operations-Analytics.git`
2. Run the pipeline setup script: `python analysis.py`
3. Open `supply_chain_dashboard.pbix` in Power BI Desktop to view the live dashboard.


Description des Graphiques & Insights du Dashboard (Scannability Pro)
Ce tableau de bord 360° unifié offre une visibilité totale sur la performance commerciale, la logistique et l'optimisation des stocks de l'entreprise. Voici l'explication technique de chaque élément :

1. Les Cartes KPI (Indicateurs Stratégiques Globaux)
Placées tout en haut, elles permettent aux décideurs de capter la santé de l'entreprise en un seul coup d'œil :

Somme de Sales (Chiffre d'Affaires - 391T) : Représente le volume financier total généré par l'ensemble des commandes. C'est l'indicateur clé de la croissance du marché.

Somme de Order Item Quantity (Volume de Ventes - 384K) : Indique le nombre total de pièces vendues et expédiées. Il permet de mesurer la charge de travail opérationnelle de l'entrepôt.

Moyenne de Late Delivery Risk (Taux de Risque de Retard - 55,00%) : L'insight critique du projet. Il montre que 55% des commandes présentent un risque majeur de retard de livraison. C'est le point de douleur opérationnel que la supply chain doit corriger en priorité.

2. Le Treemap : Analyse des Ventes par Région
Structure : Un ensemble de rectangles colorés où la taille de chaque bloc est proportionnelle au Chiffre d'Affaires (Sales) généré par zone géographique (Order Region).

Insight Business : Il permet d'identifier instantanément les marchés moteurs (les grands blocs) par rapport aux marchés secondaires ou en baisse (les petits blocs), optimisant ainsi la répartition des efforts marketing et logistiques.

3. Le Graphique en Anneau (Donut Chart) : Segmentation des Modes d'Expédition
Structure : Répartition sectorielle du Chiffre d'Affaires selon les types de livraison choisis par les clients (Shipping Mode : Standard Class, First Class, Second Class, Same Day).

Insight Business : Permet d'analyser les préférences de transport des clients. Si le mode Standard domine largement, cela montre que les clients privilégient le coût au délai, ce qui donne une marge de manœuvre pour réorganiser les flux face au taux de retard de 55%.

📊 4. L'Histogramme de l'Analyse ABC : Optimisation des Stocks (Loi de Pareto)
Structure : Trois colonnes distinctes basées sur le principe des 80/20. L'axe Y affiche le nombre exact de références produits (Count/Nombre de Sales).

Insight Business :

Classe A (Top 80% du CA) : Regroupe un très petit nombre de produits (les produits stars). Ils nécessitent un suivi strict et un objectif de Zéro Rupture de Stock.

Classe C (Low 5% du CA) : Contient la grande majorité des produits. Ce sont des produits à faible rotation qui encombrent inutilement l'espace de stockage et dorment dans l'entrepôt.

5. Le Graphique Linéaire : Évolution Temporelle & Saisonnalité (Time-Series)
Structure : Analyse chronologique croisant l'historique des dates de commande (order date) avec deux courbes : le Chiffre d'Affaires réel (Actual_Sales) et la ligne lissée de tendance (Trend).

Insight Business : La courbe Trend montre la trajectoire de croissance à long terme de l'entreprise (en hausse ou en baisse), tandis que les fluctuations de la courbe Actual_Sales mettent en évidence les pics de saisonnalité (périodes de fêtes, soldes, variations mensuelles), permettant d'anticiper la demande et de planifier les capacités logistiques futures.
