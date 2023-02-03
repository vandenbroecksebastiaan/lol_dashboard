from dash.dependencies import Input, Output
import plotly.express as px

from data import get_game_data, get_event_data


def stream_kills_callback(app):

    @app.callback(Output("graph_kills", "figure"),
                  [Input("interval_kills", "n_intervals")])
    def stream_kills(value):
        # Get the data
        event_data = get_event_data()
        all_players_data = get_game_data()["allPlayers"]
    
        champion_to_kills_map = {}
        champion_to_name_map = {}
    
        # Create a map from player_name to champion
        for i in all_players_data:
            champion_to_name_map[i["championName"]] = i["summonerName"]
    
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
    
        # Add the champions without kills
        for i in champion_to_name_map.values():
            if i not in champion_to_kills_map.keys():
                champion_to_kills_map[i] = 0
    
        # Change user name to champion name
        name_to_champion_map = {j:i for i,j in champion_to_name_map.items()}
        champion_to_kills_map = {name_to_champion_map[i]:j for i,j in champion_to_kills_map.items()}
    
        # Make the visualization
        fig = px.bar(x=list(champion_to_kills_map.keys()),
                     y=list(champion_to_kills_map.values()))
    
        fig.update_layout(margin=dict(l=10, r=10, t=0, b=0),
                          template="plotly_dark",
                          paper_bgcolor="#44475a",
                          plot_bgcolor="#44475a",
                          colorway=["#b2b2b2"])

        fig.update_traces(marker_color="#b2b2b2",
                          opacity=0.5,
                          textposition="outside")

        tickvals = list(range(max(champion_to_kills_map.values())))
        fig.update_yaxes(title="Number of kills", tickvals=tickvals)
        fig.update_xaxes(title="")
    
        return fig

    return app