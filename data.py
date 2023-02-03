import requests
import pandas as pd
import json

champion_data = pd.DataFrame()


def get_champion_data():
    global champion_data

    all_game_data = requests.get(
        "https://127.0.0.1:2999/liveclientdata/allgamedata",
        verify=False
    ).json()

    new_champion_data = pd.DataFrame(
        all_game_data["activePlayer"]["championStats"],
        index=(int(all_game_data["gameData"]["gameTime"]),)
    )

    if len(champion_data.index) == 0:
        champion_data = pd.concat([champion_data, new_champion_data])

    if champion_data.index[-1] != new_champion_data.index[-1]:
        champion_data = pd.concat([champion_data, new_champion_data])

    return champion_data


def get_game_data():
    all_game_data = requests.get(
        "https://127.0.0.1:2999/liveclientdata/allgamedata",
        verify=False
    ).json()
    return all_game_data


def get_event_data():
    all_game_data = requests.get(
        "https://127.0.0.1:2999/liveclientdata/allgamedata",
        verify=False
    ).json()
    event_data = all_game_data["events"]["Events"]

    return event_data


def write_event_data():
    event_data = get_event_data()
    with open("data/event_data.txt", "w") as file:
        file.write(json.dumps(event_data))
        file.close()