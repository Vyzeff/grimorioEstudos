import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows= 1, cols=2)

fig.add_trace(go.Bar(x=[6,5,2], y=[1,4,5]), row=1, col=1)
fig.add_trace(go.Scatter(x=[6,5,2], y=[3,5,6], mode='lines'), row=1, col=2)

fig.update_layout(title_text='Usando o update_layout!', title_font_size=20)

fig.show()