from dash.dependencies import Input, Output
import plotly.graph_objects as go
from data import get_champion_data


def stream_MR_callback(app):
    # Magic resist graph
    @app.callback(Output("graph_MR", "figure"),
                  [Input("interval_MR", "n_intervals")])
    def stream_MR(value):
        # Get the data
        champion_data = get_champion_data()
        # Update the visualization
        fig = go.Figure(data=[go.Scatter(x=champion_data.index,
                                         y=champion_data["magicResist"],
                                         fill="tozeroy")])
        fig.update_layout(margin=dict(l=10, r=10, t=0, b=0),
                          yaxis_range=[0, 300],
                          xaxis={"showticklabels": False},
                          template="plotly_dark",
                          paper_bgcolor="#44475a",
                          plot_bgcolor="#44475a",
                          colorway=["#b2b2b2"])

        return fig

    return app