import plotly.graph_objects as go
import numpy as np

#x = np.linspace(0,10,100)
#y = np.sin(x)

#fig = go.Figure(
#    data = go.Scatter(x=x, y=y, mode="lines")
#)

#----------------------------

#x = 100
#a = np.linspace(0,10,x)
#randomY0 = np.random.randn(x) + 5
#randomY1 = np.random.randn(x)
#randomY2 = np.random.randn(x) - 5

#fig = go.Figure()
#fig.add_trace(go.Scatter(x=a,y=randomY0, mode="markers", name="Markers"))
#fig.add_trace(go.Scatter(x=a,y=randomY1, mode="lines", name="Lines"))
#fig.add_trace(go.Scatter(x=a,y=randomY2, mode="lines+markers", name="Lines and Markers"))

#fig.show()

#--------------------
fig=go.Figure(
    data= go.Scatter(
        x=[1,2,3,4],
        y=[10,11,12,13],
        mode="markers",
        marker=dict(
            size=[40,60,80,100],
            color=[0,1,2,3]
        )
    )
)

fig.show()