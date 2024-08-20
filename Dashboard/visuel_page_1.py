from dash import html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go


def generate_card(title, value):
    return html.Div(
        dbc.Card([
            dbc.CardBody([
                html.P(value, className="card-value",
                       style={'margin': '0px', 'fontSize': '25px', 'fontWeight': 'bold', 'color': 'white'}),
                html.H4(title, className="card-title",
                        style={'margin': '0px', 'fontSize': '15px', 'color': 'white'})
            ], style={'textAlign': 'center'}),
        ], style={"backgroundColor": '#0077b6', 'border': 'none', 'borderRadius': '10px'})
    )


def line1(data):
    # Création du graphique
    fig = go.Figure()

    # Ajout de la trace de la ligne
    fig.add_trace(go.Scatter(
        x=data["order_date"],
        y=data["profit"],
        mode="lines+markers",
        name="Profit",
        marker={
            'size': 10,
            'color': 'red',
            'line': {'width': 2, 'color': 'white'}
        },
        text=data["profit"].apply(lambda x: f"{x:.2f}"),
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
        title="Monthly Profit",
    )

    return [fig]


def barh(data):
    # Création du graphique
    fig = go.Figure()

    # Ajout des traces pour le profit et les ventes
    fig.add_trace(go.Bar(
        x=data['profit'],
        y=data['mois'],
        name='Profit',
        orientation='h'
    ))

    fig.add_trace(go.Bar(
        x=data['sales'],
        y=data['mois'],
        name='Ventes',
        orientation='h'
    ))

    # Mise en forme du graphique
    fig.update_layout(
        title='Profits and sales by category',
        bargap=0.1
    )

    return [fig]
