import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

import pandas as pd
import numpy as np

import pathlib
import datetime
from datetime import datetime
import time

# ===========================================
# Pre Processing
startTime = time.time()

BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("data").resolve()

# print(DATA_PATH.joinpath('clinicalAnalysis.csv'))

# ===========================================
# Data Load
df = pd.read_csv(
    DATA_PATH.joinpath("clinicalAnalysis.csv"), sep=",", encoding="utf-8-sig"
)

clinicList = df["Clinic Name"].unique()

df["Admit Source"] = df["Admit Source"].fillna("Not Identified")
admitList = df["Admit Source"].unique()

df["Check-In Time"] = df["Check-In Time"].apply(
    lambda x: datetime.strptime(x, "%Y-%m-%d %I:%M:%S %p")
)

df["Week Day"] = df["Check-In Time"]
df["Check-In Hour"] = df["Check-In Time"]

df["Week Day"] = df["Week Day"].apply(lambda x: datetime.strftime(x, "%A"))
df["Check-In Hour"] = df["Check-In Hour"].apply(lambda x: datetime.strftime(x, "%I %p"))

daysList = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
checkInDuration = df["Check-In Time"].describe(datetime_is_numeric=False)
allDepos = df["Department"].unique().tolist()


# ===========================================
# Defined Functions
## Layout Functions
def descCard():
    return html.Div(
        id="descCard",
        children=[
            html.H5("Clinical Analitycs"),
            html.H3("Welcome to the Clinical Analitycs Dashboard"),
            html.Div(
                id="intro",
                children=[
                    "Explore clinic patient volume by the time of the day, waiting time and care score.",
                ],
            ),
        ],
    )


def generateControlCard():
    return html.Div(
        id="controlCard",
        children=[
            html.P("Select the Clinic"),
            dcc.Dropdown(
                id="clinicSelect",
                options=[{"label": x, "value": x} for x in clinicList],
                value=clinicList[0],
            ),
            html.P("Select the check in time"),
            dcc.DatePickerRange(
                id="dateSelect",
                start_date=df["Check-In Time"].min().date(),
                min_date_allowed=df["Check-In Time"].min().date(),
                end_date=df["Check-In Time"].max().date(),
                max_date_allowed=df["Check-In Time"].max().date(),
            ),
            html.P("Select Admit Format"),
            dcc.Dropdown(
                id="formatSelect",
                options=[{"label": x, "value": x} for x in admitList],
                value=admitList[:],
                multi=True,
            ),
        ],
    )


## Dashboard Functions
def patientVolumeHeatmap(timeStart, timeEnd, clinic, admitSource):
    dfFiltered = df[
        (df["Clinic Name"] == clinic) & (df["Admit Source"].isin(admitSource))
    ]
    dfFiltered = dfFiltered.sort_values("Check-In Time").set_index("Check-In Time")[
        timeStart:timeEnd
    ]

    xAxis = [datetime.time(i).strftime("%I %p ") for i in range(24)]
    yAxis = daysList

    z = np.zeros((7, 24))
    annotations = []

    for indY, day in enumerate(yAxis):
        dfDayFilter = dfFiltered[dfFiltered["Week Day"] == day]
        for indX, valX in enumerate(xAxis):
            sumOfRecords = dfDayFilter[dfDayFilter["Check-In Hour"] == valX][
                "Number of Records"
            ].sum()
            z[indY, indX] = sumOfRecords

            annDict = {
                "showarrow": False,
                "text": "<b>" + str(sumOfRecords) + "<b>",
                "x": valX,
                "y": day,
                "font": {"family": "sans-serif"},
            }
            annotations.append(annDict)

    hoverplate = "<b> %{y} %{x} <br><br> %{z} Patient Records"
    heatData = [
        {
            "x": xAxis,
            "y": yAxis,
            "z": z,
            "type": "heatmap",
            "hovertemplate": hoverplate,
            "showscale": False,
            "colorscale": [[0, "#caf3ff"], [1, "#2c82ff"]],
        }
    ]

    layout = dict(
        margin=dict(l=70, b=50, t=50, r=50),
        modebar={"orientation": "v"},
        font=dict(family="Open Sans"),
        annotations=annotations,
        xaxis=dict(
            side="top",
            ticks="",
            ticklen=2,
            tickfont=dict(family="sans-serif"),
            tickcolor="#ffffff",
        ),
        yaxis=dict(
            side="left", ticks="", tickfont=dict(family="sans-serif"), ticksuffix=" "
        ),
        hovermode="closest",
        showlegend=False,
    )

    return {"data": heatData, "layout": layout}


def generateTableRow(id, style, col1, col2, col3):
    return html.Div(
        id=id,
        className="row table-row",
        style=style,
        children=[
            html.Div(
                id=col1["id"],
                style={"display": "table", "height": "100%"},
                className="two columns row-department",
                children=col1["children"],
            ),
            html.Div(
                id=col2["id"],
                style={"textAlign": "center", "height": "100%"},
                className="five columns row-department",
                children=col2["children"],
            ),
            html.Div(
                id=col3["id"],
                style={"textAlign": "center", "height": "100%"},
                className="five columns row-department",
                children=col3["children"],
            ),
        ],
    )


# ===========================================
# Start App
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUX],
)

# ===========================================
# Layout

app.layout = html.Div(
    id="app-container",
    children=[
        html.Div(
            id="left-column",
            className="four columns",
            children=[descCard(), generateControlCard()],
        ),
        html.Div(
            id="placeholder",
            className="eight columns",
            children=["PLACEHOLDER FOR HEATMAP"],
        ),
    ],
)

# ===========================================
# Logic


execTime = time.time() - startTime
print("===========================================")
print(f"tempo de execução total: {execTime:0.5}s")


if __name__ == "__main__":
    print("carregando...")

    app.run_server(debug=True, port=8060)
