from dash.dependencies import Input, Output
import plotly.graph_objects as go
from data import get_champion_data


def stream_max_health_callback(app):
    # Attack damage graph
    @app.callback(Output("graph_max_health", "figure"),
                  [Input("interval_max_health", "n_intervals")])
    def stream_max_health(value):
        # Get the data
        champion_data = get_champion_data()
        # Update the visualization
        fig = go.Figure(data=[go.Scatter(x=champion_data.index,
                                         y=champion_data["maxHealth"],
                                         fill="tozeroy")])
        fig.update_layout(margin=dict(l=10, r=10, t=0, b=0),
                          xaxis={"showticklabels": False},
                          template="plotly_dark",
                          paper_bgcolor="#44475a",
                          plot_bgcolor="#44475a",
                          colorway=["#b2b2b2"])

        return fig

    return app