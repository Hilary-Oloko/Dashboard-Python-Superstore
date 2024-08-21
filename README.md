You can find the **french** translation below.
Vous pourrez trouver la traduction en **français** plus bas.

## English

## Interactive Sales Tracking Dashboard with Dash

This repository contains the source code for an interactive sales dashboard developed using the Python Dash library. The dashboard allows you to explore and analyze sales data of a company.

## Metrics and Preliminary Analysis

Before building the dashboard, a preliminary analysis of the data was performed:

```python
print(df.describe())
print(df['category'].hist())
print(df['region'].hist())
```

This analysis revealed:

- The data only concerns the United States, so the 'Country' column is unnecessary and has been removed.
- Four distinct regions of the USA are present in the data.
- Three main product categories are identified.
- Five order rows do not contain quantity or price, so these have been removed.
- Duplicates were detected for product names and product IDs. These duplicates were corrected by applying logical rules based on product names and subcategories (see Data Formatting).

## Creating Tables and Loading into PostgreSQL

The data has been structured into three tables:

- **Product:** Product_ID, Sub_category, Product_name, unit_price (with two digits after the decimal point).
- **Customer:** Name, segmant, city, state, postal code, region.
- **Order:** Order_ID, Customer_ID, Product_ID, Order_date, Ship_date, ship_mode, sale, Quantity, discount, profit.

These tables have been loaded into a PostgreSQL database. This step is not mandatory but allows you to practice data transformation with Python and loading into a SQL database.

It is possible to build the report without doing this step.

The code for creating the different tables is located in the SQL folder.

## Developing the Dashboard with Dash

The dashboard is composed of four distinct pages, each offering a different perspective on the sales data:

**Page 1: Overview**

- **Key Metrics:** Total sales, total profits, total quantity, total number of customers.
- **Bar or Column Chart:** Comparison of sales and profits over the year.
- **Line Chart:** Evolution of profits over the year.
- **Pie Chart:** Breakdown of sales or profits by customer segment.

**Page 2: Product Analysis**

- **Detailed Table:** Product ID, name, category, subcategory, sales, quantity, profits.
- **Line Chart:** Evolution of quantities sold over time.
- **Treemap:** Top 10 products sold with their quantity.

**Page 3: Order Analysis**

- **Detailed Table:** Order ID, order date, shipping date, shipping mode, sales, quantity, discount, profits.
- **Line Chart:** Evolution of orders over time.
- **Pie Chart:** Breakdown of orders by shipping mode.

**Page 4: Customer Analysis**

- **Line Chart:** Number of new customers per month.
- **Top 10 Cities:** Cities with the most customers.

## Installation and Usage

To use the dashboard, you need to install the necessary dependencies:

```bash
pip install dash
```

Then, run the main Python script to start the dashboard. The dashboard will be accessible via a local web server using http://127.0.0.1:8050/.

![image](https://github.com/user-attachments/assets/26b8cb4e-903f-48e1-8795-a2a61c5a0bf8)


## Remarks

This report is a basic example and can be customized and extended based on your specific needs. You can add new pages, additional metrics, more complex visualizations, and interactive features.

Feel free to explore the source code and make your own modifications to improve the report and consult the Dash documentation.

## Français

## Dashboard de suivi des ventes interactif avec Dash

Ce repository contient le code source d'un dashboard interactif de ventes développé avec la librairie Python Dash. Le dashboard permet d'explorer et d'analyser les données de vente d'une entreprise.

## Métriques et Analyse Préalable

Avant de construire le dashboard, une analyse préalable des données a été effectuée :

```python
print(df.describe())
print(df['category'].hist())
print(df['region'].hist())
```

Cette analyse a permis de constater :

- Les données concernent uniquement les États-Unis donc la colonne 'Country' est inutile et a été supprimée.
- Quatre régions distinctes des USA sont présentes dans les données.
- Trois catégories de produits principales sont identifiées.
- Cinq lignes de commande ne contiennent ni quantité ni prix, celle-ci on donc été supprimé.
- Des doublons ont été détectés pour les noms de produits et les ID de produits. Ces doublons ont été corrigés en appliquant des règles logiques basées sur les noms et les sous-catégories des produits (voir Mise en forme des données).

## Création des Tables et Chargement dans PostgreSQL

Les données ont été structurées en trois tables :

- **Product:** Product_ID, Sub_category, Product_name, unit_price (avec deux chiffres après la virgule).
- **Customer:** Name, segmant, city, state, postal code, region.
- **Order:** Order_ID, Customer_ID, Product_ID, Order_date, Ship_date, ship_mode, sale, Quantity, discount, profit.

Ces tables ont été chargées dans une base de données PostgreSQL. Cette étape n'est pas obligatoire mais permet de s'entraîner à la transformation de données avec Python et au chargement dans une base de données SQL.

Il est possible de réaliser le rapport sans la réaliser.

Le code permettant la création des différentes tables se trouve dans le dossier SQL

## Développement du Dashboard avec Dash

Le dashboard est composé de quatre pages distinctes, chacune offrant une perspective différente sur les données de vente :

**Page 1 : Vue d'ensemble**

- **Métriques clés:** Ventes totales, bénéfices totaux, quantité totale, nombre de clients total.
- **Graphique en barres ou en colonnes:** Comparaison des ventes et des bénéfices au cours de l'année.
- **Graphique en ligne:** Évolution des profits au cours de l'année.
- **Graphique en secteurs:** Répartition des ventes ou des bénéfices par segment de clients.

**Page 2 : Analyse des produits**

- **Tableau détaillé:** ID produit, nom, catégorie, sous-catégorie, ventes, quantité, bénéfices.
- **Graphique en lignes:** Évolution des quantités vendues dans le temps.
- **Treemap:** Top 10 produits vendus avec leur quantité.

**Page 3 : Analyse des commandes**

- **Tableau détaillé:** ID commande, date de commande, date d'expédition, mode d'expédition, ventes, quantité, rabais, bénéfices.
- **Graphique en lignes:** Évolution des commandes dans le temps.
- **Graphique en secteurs:** Répartition des commandes par mode d'expédition.

**Page 4 : Analyse des clients**

- **Graphique en ligne:** Nombre de nouveaux clients par mois.
- **Top 10 villes:** Villes avec le plus de clients.

## Installation et Utilisation

Pour utiliser le dashboard, vous devez installer les dépendances nécessaires :

```bash
pip install dash
```

Ensuite, lancez le script Python principal pour démarrer le dashboard. Le dashboard sera accessible via un serveur web local en utilisant http://127.0.0.1:8050/.

![image](https://github.com/user-attachments/assets/890dab20-c263-4d97-99f1-23cd30e3e422)


## Remarques

Ce rapport est un exemple de base et peut être personnalisé et étendu en fonction de vos besoins spécifiques. Vous pouvez ajouter de nouvelles pages, des métriques supplémentaires, des visualisations plus complexes et des fonctionnalités d'interaction.

N'hésitez pas à explorer le code source et à apporter vos propres modifications pour améliorer le rapport et à consulter la documentaion Dash.
