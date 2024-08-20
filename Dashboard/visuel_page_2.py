import plotly.express as px
import plotly.graph_objects as go


def line2(data):
    # Création du graphique
    fig = go.Figure()

    # Ajout de la trace de la ligne
    fig.add_trace(go.Scatter(
        x=data["order_date"],
        y=data["quantity"],
        mode="lines+markers",
        name="quantity",
        marker={
            'size': 10,
            'color': '#0094c6',
            'line': {'width': 2, 'color': 'white'}
        },
        text=data["quantity"].apply(lambda x: f"{x:.2f}"),
        textposition="top center"
    ))

    # Formatage de l'axe des x
    fig.update_xaxes(
        tickvals=data["order_date"].unique(),
        tickformat="%b %Y",
        tickangle=90
    )

    # Mise en forme du graphique
    fig.update_layout(
        title="Monthly Quantity sold",
    )

    return [fig]


def top_10_treemap(df):

    # Créer le treemap
    fig = px.treemap(
        df,
        path=['product_id'],
        values='quantity',
        color='category',
        title="Top 10 Products Sold"
    )

    return fig
