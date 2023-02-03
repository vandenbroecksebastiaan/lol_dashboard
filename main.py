import dash
import dash_bootstrap_components as dbc
import warnings
warnings.filterwarnings("ignore")


from layout import layout
from callbacks.stream_kills_callback import stream_kills_callback
from callbacks.stream_time_callback import stream_time_callback
from callbacks.stream_armor_callback import stream_armor_callback
from callbacks.stream_MR_callback import stream_MR_callback
from callbacks.stream_AD_callback import stream_AD_callback
from callbacks.stream_AP_callback import stream_AP_callback
from callbacks.stream_current_health_callback import stream_current_health_callback
from callbacks.stream_max_health_callback import stream_max_health_callback
from callbacks.stream_cum_kills_callback import stream_cum_kills_callback
from callbacks.stream_kills_per_min_callback import stream_kills_per_min_callback
from callbacks.stream_event_log_callback import stream_event_log_callback


# TODO: add charts for total and current gold
# TODO: add a button for writing event data


champion_variables = [
    "abilityHaste", "abilityPower", "armor", "armorPenetrationFlat",
    "armorPenetrationPercent", "attackDamage", "attackRange", "attackSpeed",
    "bonusArmorPenetrationPercent", "bonusMagicPenetrationPercent",
    "critChance", "critDamage", "currentHealth", "healShieldPower",
    "healthRegenRate", "lifeSteal", "magicLethality",
    "magicPenetrationFlat", "magicPenetrationPercent", "magicResist",
    "maxHealth", "moveSpeed", "omnivamp", "physicalLethality",
    "physicalVamp", "resourceMax", "resourceRegenRate", "resourceType",
    "resourceValue", "spellVamp", "tenacity"
]

all_player_variables = [
    'championName', 'isBot', 'isDead', 'items', 'level', 'position',
    'rawChampionName', 'respawnTimer', 'runes', 'scores', 'skinID',
    'summonerName', 'summonerSpells', 'team'
]


# Instantiate the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = layout

# Add callbacks to the client
app = stream_time_callback(app)
app = stream_armor_callback(app)
app = stream_MR_callback(app)
app = stream_AD_callback(app)
app = stream_AP_callback(app)
app = stream_kills_callback(app)
app = stream_current_health_callback(app)
app = stream_max_health_callback(app)
app = stream_cum_kills_callback(app)
app = stream_kills_per_min_callback(app)
app = stream_event_log_callback(app)

app.run_server(debug=True, threaded=True)