import dash_bootstrap_components as dbc
from dash import html, dcc


layout = html.Div(children=[
    dbc.Row([
        dbc.Col(
            html.Div(html.H1("Champion statistics"), className="title"),
        ),
        dbc.Col(
            html.Div(
                [html.H1("Game time: ", style={"display": "inline"}),
                 html.H1(id="game_time", style={"display": "inline"}),
                 dcc.Interval(id="interval_game_time", interval=1000, n_intervals=0)],
                className="title"
            )
        )
    ]),

    dbc.Row([
        dbc.Col(
            html.Div(
                [html.H3("Armor", className="subtitle"),
                 dcc.Interval(id="interval_armor", interval=1000, n_intervals=0),
                 dcc.Graph(id="graph_armor")
                ], className="col-chart"
            )
        ),
        dbc.Col(
            html.Div(
                [html.H3("MR", className="subtitle"),
                 dcc.Interval(id="interval_MR", interval=1000, n_intervals=0),
                 dcc.Graph(id="graph_MR")
                ], className="col-chart"
            )
        ),
        dbc.Col(
            html.Div(
                [html.H3("Current health", className="subtitle"),
                 dcc.Interval(id="interval_current_health", interval=1000, n_intervals=0),
                 dcc.Graph(id="graph_current_health") 
                ], className="col-chart"
            )
        ),
        dbc.Col(
            html.Div(
                [html.H3("Max health", className="subtitle"),
                 dcc.Interval(id="interval_max_health", interval=1000, n_intervals=0),
                 dcc.Graph(id="graph_max_health") 
                ], className="col-chart"
            )
        )
    ]),
    dbc.Row([
        dbc.Col(
            html.Div(
                [html.H3("Attack damage", className="subtitle"),
                 dcc.Interval(id="interval_AD", interval=1000, n_intervals=0),
                 dcc.Graph(id="graph_AD")
                ], className="col-chart"
            )
        ),
        dbc.Col(
            html.Div(
                [html.H3("Ability power", className="subtitle"),
                 dcc.Interval(id="interval_AP", interval=1000, n_intervals=0),
                 dcc.Graph(id="graph_AP")
                ], className="col-chart"
            )
        ),
        dbc.Col(
            html.Div(
                [html.H3("Cumulative kills", className="subtitle"),
                 dcc.Interval(id="interval_cum_kills", interval=1000, n_intervals=0),
                 dcc.Graph(id="graph_cum_kills")
                ], className="col-chart"
            )
        ),
        dbc.Col(
            html.Div(
                [html.H3("Kills per minute", className="subtitle"),
                 dcc.Interval(id="interval_kills_per_min", interval=1000, n_intervals=0),
                 dcc.Graph(id="graph_kills_per_min")
                ], className="col-chart"
            )
        )
    ]),
    dbc.Row([
        dbc.Col(
            html.Div(
                [html.H3("Cumulative assists", className="subtitle")],
            )
        ),
        dbc.Col(
            html.Div(
                [html.H3("Assists per minute", className="subtitle")]
            )
        )
    ]),
    dbc.Row([
        dbc.Col(
            html.Div(
                [html.H3("Cumulative deaths", className="subtitle")],
            )
        ),
        dbc.Col(
            html.Div(
                [html.H3("Deaths per minute", className="subtitle")]
            )
        )
    ]),
    dbc.Row([
        dbc.Col(
            html.Div(
                [html.H3("Cumulative CS", className="subtitle")],
            )
        ),
        dbc.Col(
            html.Div(
                [html.H3("CS per minute", className="subtitle")]
            )
        )
    ]),

    dbc.Row(
        dbc.Col(
            html.Div(html.H1("Game statistics"), className="title"),
            style={"padding-top": "20px"}
        )
    ),

    dbc.Row([
        dbc.Col(
            html.Div(
                [html.H3("Kill log", className="subtitle"),
                 dcc.Interval(id="interval_kills", interval=1000, n_intervals=0),
                 dcc.Graph(id="graph_kills")
                 ], className="col-chart"
            )
        ),
        dbc.Col(
            html.Div(
                [html.H3("Event log", className="subtitle"),
                 html.P(id="event_log"),
                 dcc.Interval(id="interval_event_log", interval=1000, n_intervals=0)],
            ), className="col-chart"
        )
    ]),

    dbc.Row(
        dbc.Col(
            html.Div(html.H1("Team statistics"), className="title"),
            style={"padding-top": "20px"}
        )
    ),

    dbc.Row([
        dbc.Col(
            html.Div(
                html.H3("The average winrate will go here.")
            )
        ),
        dbc.Col(
            html.Div(
                html.H3("The average KDA will go here.")
            )
        ),
        dbc.Col(
            html.Div(
                html.H3("The average gold will go here.")
            )
        ),
        dbc.Col(
            html.Div(
                html.H3("The average damage will go here.")
            )
        )
    ]),
])
