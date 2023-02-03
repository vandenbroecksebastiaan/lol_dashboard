from dash.dependencies import Input, Output
from dash import html
import datetime
from data import get_event_data, write_event_data

def stream_event_log_callback(app):

    @app.callback(Output("event_log", "children"),
                  [Input("interval_event_log", "n_intervals")])
    def stream_event_log(value):

        write_event_data()

        event_data = get_event_data()
        event_log = []
        for event in event_data:
            event_name = event["EventName"]
            event_time = str(datetime.timedelta(seconds=event["EventTime"]))

            event_message = event_time[2:7] + "\t|\t" + event_name

            event_log.append(html.P(event_message, className="event-text"))
        
        return event_log

    return app