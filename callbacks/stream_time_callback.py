from dash.dependencies import Input, Output
import datetime
from data import get_game_data

def stream_time_callback(app):
    @app.callback(Output("game_time", "children"),
                  [Input("interval_game_time", "n_intervals")])
    def stream_time(value):
        time = get_game_data()["gameData"]["gameTime"]
        time = round(time)
        time = str(datetime.timedelta(seconds=time))
        return time

    return app