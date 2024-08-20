import plotly.graph_objects as go


def line3(data):
    # Création du graphique
    fig = go.Figure()

    # Ajout de la trace de la ligne
    fig.add_trace(go.Scatter(
        x=data["order_date"],
        y=data["orders"],
        mode="lines+markers",
        name="Monthly Orders",
        marker={
            'size': 10,
            'color': 'blue',
            'line': {'width': 2, 'color': 'white'}
        },
        text=data["orders"].apply(lambda x: f"{x:.2f}"),
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
        title="Monthly Orders",
    )

    return [fig]


def bar3(data):
    bar3 = go.Figure()

    # Tracé des barres de ventes
    bar3.add_trace(go.Bar(
        x=data['segment'],
        y=data['orders'],
        name='Orders by segments',
        marker_color=data['segment'].map(
            {'Consumer': 'blue', 'Corporate': 'green', 'Home Office': 'red'}),
        text=data['orders'],  # Ajout de la propriété 'text'
        textposition='auto'  # Positionnement automatique du texte
    ))

    # Ajout des labels et du titre
    bar3.update_layout(
        title='Orders by segments',
        yaxis_title='Orders',

    )
    return [bar3]
