from dash.dependencies import Input, Output
import plotly.graph_objects as go
from data import get_champion_data


def stream_AP_callback(app):
    # Ability power graph
    @app.callback(Output("graph_AP", "figure"),
                  [Input("interval_AP", "n_intervals")])
    def stream_AP(value):
        # Get the data
        champion_data = get_champion_data()
        # Update the visualization
        fig = go.Figure(data=[go.Scatter(x=champion_data.index,
                                         y=champion_data["abilityPower"],
                                         fill="tozeroy")])
        fig.update_layout(margin=dict(l=10, r=10, t=0, b=0),
                          yaxis_range=[0, 600],
                          xaxis={"showticklabels": False},
                          template="plotly_dark",
                          paper_bgcolor="#44475a",
                          plot_bgcolor="#44475a",
                          colorway=["#b2b2b2"])

        return fig

    return app