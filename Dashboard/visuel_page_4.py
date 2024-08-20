import plotly.graph_objects as go


def line4(data):
    # Création du graphique
    fig = go.Figure()

    # Ajout de la trace de la ligne
    fig.add_trace(go.Scatter(
        x=data["order_date"],
        y=data["new_customers"],
        mode="lines+markers",
        name="New Customers",
        marker={
            'size': 10,
            'color': 'blue',
            'line': {'width': 2, 'color': 'white'}
        },
        text=data["new_customers"].apply(lambda x: f"{x:.2f}"),
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
        title="Monthly New Customers",
    )

    return [fig]


# Créer la fonction heatmap4
def heatmap4(data):
    # Créer la heatmap
    fig = go.Figure(data=go.Heatmap(
        z=data['orders'],
        x=data['state'],
        y=['Orders'],
        colorscale='reds',
        colorbar_title="Orders"
    ))

    # Ajuster la mise en page
    fig.update_layout(
        title_text='Total Orders by State',
        xaxis_title='State',
        yaxis_title='Orders',
        xaxis_tickangle=-45
    )

    return (fig,)
