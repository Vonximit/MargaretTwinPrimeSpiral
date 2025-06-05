import plotly.graph_objects as go
import numpy as np
from math import pi, log, e

# Datos base
twin_pairs = [(17, 19), (29, 31), (41, 43)]
fibonacci_seq = [1, 1, 2, 3, 5, 8, 13, 21, 34]

# Parámetros espiral logarítmica
a = 0.1
b = 0.15

# Crear figura
fig = go.Figure()

for idx, (p1, p2) in enumerate(twin_pairs):
    # Definir rango angular
    theta = np.linspace(0, 2 * pi * p2, 1000)
    r = a * np.exp(b * theta)

    # Trazar espiral
    fig.add_trace(go.Scatterpolar(
        theta=theta,
        r=r,
        mode='lines',
        line=dict(color='#FFD700'),
        opacity=0.7,
        name=f'Par {p1}-{p2}',
        hovertemplate=f'<b>Par: {p1}-{p2}</b><br>Theta: %{{theta:.2f}}<br>Radio: %{{r:.2f}}<extra></extra>'
    ))

    # Calcular posición de los primos
    theta_p1 = 2 * pi * p1
    theta_p2 = 2 * pi * p2
    r_p1 = a * np.exp(b * theta_p1)
    r_p2 = a * np.exp(b * theta_p2)

    # Añadir marcadores para los primos
    fig.add_trace(go.Scatterpolar(
        theta=[theta_p1, theta_p2],
        r=[r_p1, r_p2],
        mode='markers',
        marker=dict(
            symbol='star',
            size=15,
            color=['#FF4D4D', '#4DFF4D']
        ),
        name=f'Primos {p1} y {p2}',
        hovertemplate=f'Primo: %{{text}}<br>Theta: %{{theta:.2f}}<br>Radio: %{{r:.2f}}<extra></extra>',
        text=[p1, p2]  # Texto para mostrar en hover
    ))

# Diseño
fig.update_layout(
    title='ESPIRAL MARGARET: Primos Gemelos en la Espiral Logarítmica',
    polar=dict(
        radialaxis=dict(visible=True, range=[0, max(a * np.exp(b * 2 * pi * max(p2 for _, p2 in twin_pairs)) * 1.1 for _, p2 in twin_pairs)]),
        angularaxis=dict(direction="clockwise", rotation=90)
    ),
    showlegend=True
)

fig.show()
