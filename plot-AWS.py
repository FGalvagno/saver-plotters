import pandas as pd
import yaml
import plotly.graph_objects as go
from plotly.subplots import make_subplots
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

fig = make_subplots(rows=4, cols=4, 
                    specs=[[{"type": "xy", "colspan" : 4, "rowspan": 2}, None, None, None],
                           [None, None, None, None],
                           [{"type": "domain"}, {"type": "domain"}, {"type": "domain"}, {"type": "domain"}],
                           [{"type": "domain"}, {"type": "domain"}, {"type": "domain"}, {"type": "domain"}]],)

df = pd.read_csv(config.get("aws_file"), header=1, skiprows=[2,3])

## Indicadores

fig.add_trace(go.Indicator(
    mode = "number",
    number = {'suffix': '°C'},
    value = df['AirTemperature'].iloc[-1],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Temperatura"}),
    row=3, col=1)

fig.add_trace(go.Indicator(
    mode = "number",
    number = {'suffix': '%'},
    value = df['RelHumidity'].iloc[-1],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Humedad Relativa"}),
    row=3, col=2)

fig.add_trace(go.Indicator(
    mode = "number",
    number = {'suffix': '°C'},
    value = df['DewPoint'].iloc[-1],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Punto de Rocío"}),
    row=3, col=3)

fig.add_trace(go.Indicator(
    mode = "number",
    number = {'suffix': 'hPa'},
    value = df['AbsAirPressure'].iloc[-1],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Presión Absoluta"}),
    row=3, col=4)


# Plot Diario

fig.add_trace(go.Scatter(
    x=df['TIMESTAMP'].iloc[-150::],
    y=df['AirTemperature'].iloc[-150::],
    name="Temperatura"
))


fig.add_trace(go.Scatter(
    x=df['TIMESTAMP'].iloc[-150::],
    y=df['RelHumidity'].iloc[-150::],
    name="Humedad Relativa",
    yaxis="y2"
))

fig.add_trace(go.Scatter(
    x=df['TIMESTAMP'].iloc[-150::],
    y=df['DewPoint'].iloc[-150::],
    name="Punto de Rocío",
))

fig.add_trace(go.Scatter(
    x=df['TIMESTAMP'].iloc[-150::],
    y=df['AbsAirPressure'].iloc[-150::],
    name="Presión Absoluta",
    yaxis="y3"
))


# Create axis objects
fig.update_layout(
    xaxis=dict(
        domain=[0, 0.95]
    ),
    yaxis=dict(
        title=dict(
            text="yaxis title",
            font=dict(
                color="#1f77b4"
            )
        ),
        tickfont=dict(
            color="#1f77b4"
        )
    ),
    yaxis2=dict(
        title=dict(
            text="yaxis2 title",
            font=dict(
                color="#ff7f0e"
            )
        ),
        tickfont=dict(
            color="#ff7f0e"
        ),
        anchor="free",
        overlaying="y",
        side="right",
        position=0.99
    ),
    yaxis3=dict(
        title=dict(
            text="yaxis3 title",
            font=dict(
                color="#d62728"
            )
        ),
        tickfont=dict(
            color="#d62728"
        ),
        anchor="x",
        overlaying="y",
        side="right"
    )
)

#fig.add_trace(go.Scatter)
fig.update_layout(legend=dict(y=1, x=0)) 

# INDICADORES
fig.add_trace(go.Indicator(
    mode = "number",
    number = {'suffix': ' m/s'},
    value = df['WindSpeedAct'].iloc[-1],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Velocidad del Viento"}),
    row=4, col=1)

fig.add_trace(go.Indicator(
    mode = "number",
    number = {'suffix': ' °'},
    value = df['WindDirectionAct'].iloc[-1],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Dirección del Viento"}),
    row=4, col=2)

fig.add_trace(go.Indicator(
    mode = "number",
    number = {'suffix': 'mm/h'},
    value = df['PrecipitationIntensity'].iloc[-1],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Intensidad de Precipitación"}),
    row=4, col=3)

fig.add_trace(go.Indicator(
    mode = "number",
    number = {'suffix': 'mm'},
    value = df['PrecipDifference'].iloc[-1],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Precipitación Acumulada"}),
    row=4, col=4)



#fig.add_trace(go.Barpolar(theta = [df['WindDirectionAct'].iloc[-1]], r= [df['WindSpeedAct'].iloc[-1]], width = 3),
#              row=2, col=1)

              
fig.update_layout(title_text="AWS " + config.get("location") + ":" + df['TIMESTAMP'].iloc[-1] + " UTC-3")
fig.show()