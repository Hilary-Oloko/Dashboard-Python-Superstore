import psycopg2
import pandas as pd


def connexion_db():
    # Connexion to data
    # connexion BDD
    host = "localhost"
    database = "DB_SUPERSTORE"
    user = "your user name"
    password = "your password"
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    return conn


def get_data_page1():
    # Récupérer les données pour la création de la page 1
    # Créer un curseur
    conn = connexion_db()
    cur = conn.cursor()

    # Exécuter la requête SQL order
    cur.execute("SELECT order_id, order_date, sales, quantity, profit, category, sub_category, c.customer_id, segment, ship_mode FROM s_superstore.tb_order o\
        JOIN s_superstore.tb_product p ON o.product_id = p.product_id\
        JOIN s_superstore.tb_customer c ON c.customer_id = o.customer_id")
    data = cur.fetchall()
    # Transformer les résultats en DataFrame Pandas
    page1_df = pd.DataFrame(data, columns=['order_id', 'order_date', 'sales', 'quantity', 'profit', 'category', 'sub_category',
                                           'customer_id', 'segment', 'ship_mode'])
    page1_df['order_date'] = pd.to_datetime(page1_df['order_date'])

    return page1_df


def get_data_page2():
    # Récupérer les données pour la création de la page 1
    # Créer un curseur
    conn = connexion_db()
    cur = conn.cursor()

    # Exécuter la requête SQL order
    cur.execute("SELECT p.product_id,p.product_name,p.category,p.sub_category,p.unit_price,order_date,\
        SUM(o.profit) AS total_profit, SUM(o.quantity) AS quantity FROM s_superstore.tb_order o\
        JOIN s_superstore.tb_product p ON p.product_id = o.product_id\
        GROUP BY p.product_id,p.product_name,p.category,p.sub_category,p.unit_price,order_date")
    data = cur.fetchall()
    # Transformer les résultats en DataFrame Pandas
    page2_df = pd.DataFrame(data, columns=['product_id', 'product_name', 'category', 'sub_category',
                                           'unit_price', 'order_date', 'total_profit', 'quantity'])
    page2_df['order_date'] = pd.to_datetime(page2_df['order_date'])
    return page2_df


def get_data_page4():
    # Récupérer les données pour la création de la page 1
    # Créer un curseur
    conn = connexion_db()
    cur = conn.cursor()

    # Exécuter la requête SQL order
    cur.execute("SELECT c.customer_id, segment, state, order_id, ship_mode,order_date FROM s_superstore.tb_customer c\
        JOIN s_superstore.tb_order o ON c.customer_id= o.customer_id")
    data = cur.fetchall()
    # Transformer les résultats en DataFrame Pandas
    page4_df = pd.DataFrame(data, columns=['customer_id', 'segment', 'state', 'order_id', 'ship_mode',
                                           'order_date'])
    page4_df['order_date'] = pd.to_datetime(page4_df['order_date'])
    return page4_df
