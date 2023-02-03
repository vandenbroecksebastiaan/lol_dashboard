from dash.dependencies import Input, Output
import plotly.graph_objects as go
import numpy as np

from data import get_game_data, get_event_data, get_champion_data


def stream_kills_per_min_callback(app):

    @app.callback(Output("graph_kills_per_min", "figure"),
                  [Input("interval_kills_per_min", "n_intervals")])
    def stream_kills_per_min(value):
        event_data = get_event_data()
        game_data = get_game_data()
        champion_data = get_champion_data()
        active_player_name = game_data["activePlayer"]["summonerName"]
        time = game_data["gameData"]["gameTime"]

        champion_to_kills_map = {}
        
        # Collect the number of kills for each champion
        for i in event_data:
            if i["EventName"] == "ChampionKill":
                # TODO: change this to a list of all turret names
                if "Turret" in i["KillerName"]: break
                # Increment kill counter
                if i["KillerName"] not in champion_to_kills_map.keys():
                    champion_to_kills_map[i["KillerName"]] = 1
                else:
                    champion_to_kills_map[i["KillerName"]] += 1

        if active_player_name not in champion_to_kills_map.keys():
            champion_to_kills_map[active_player_name] = 0

        if "cum_kills" not in champion_data.columns:
            champion_data["cum_kills"] = np.nan

        champion_data.loc[int(time), "cum_kills"] = champion_to_kills_map[active_player_name]

        # Make the visualization
        fig = go.Figure(data=[go.Scatter(x=champion_data.index,
                                         y=champion_data["cum_kills"] / (time*60),
                                         fill="tozeroy")])
        fig.update_layout(margin=dict(l=10, r=10, t=0, b=0),
                          xaxis={"showticklabels": False},
                          template="plotly_dark",
                          paper_bgcolor="#44475a",
                          plot_bgcolor="#44475a",
                          colorway=["#b2b2b2"])

        tickvals = list(range(max(champion_to_kills_map.values())))
        fig.update_yaxes(tickvals=tickvals)

        return fig

    return app