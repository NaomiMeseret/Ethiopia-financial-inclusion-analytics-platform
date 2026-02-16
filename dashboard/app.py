import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Ethiopia Financial Inclusion Dashboard"

# Define the layout
app.layout = html.Div([
    html.H1("Ethiopia Financial Inclusion Forecasting Dashboard"),
    html.P("Interactive dashboard for tracking Ethiopia's digital financial transformation"),
    
    html.Div([
        html.H2("Account Ownership Trend"),
        dcc.Graph(id="account-ownership-chart")
    ]),
    
    html.Div([
        html.H2("Digital Payment Adoption"),
        dcc.Graph(id="digital-payment-chart")
    ]),
    
    html.Div([
        html.H2("Key Events Timeline"),
        dcc.Graph(id="events-timeline")
    ])
])

@app.callback(
    Output("account-ownership-chart", "figure"),
    Input("account-ownership-chart", "id")
)
def update_account_chart(_):
    # Placeholder - will be updated with actual data
    fig = px.line(
        title="Account Ownership (2011-2024)"
    )
    return fig

@app.callback(
    Output("digital-payment-chart", "figure"), 
    Input("digital-payment-chart", "id")
)
def update_payment_chart(_):
    # Placeholder - will be updated with actual data
    fig = px.line(
        title="Digital Payment Adoption (2014-2024)"
    )
    return fig

@app.callback(
    Output("events-timeline", "figure"),
    Input("events-timeline", "id")
)
def update_timeline(_):
    # Placeholder - will be updated with actual data
    fig = px.timeline(
        title="Financial Inclusion Events"
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
