import json
import os.path
import operator

from local_utils import _get_local_json, _get_json_target, _get_local_dir
from whitelist import _determine_whitelist

# Create a ROM class containing all information relevant to a ROM
class ROM:
    def __init__(self, title, variable_title, path, index):
        self.title = title
        self.variable_title = variable_title
        self.path = path
        self.index = index

# Support initial get of games list
def _get_games_list(settings):

    retroarch_file = os.path.join(
        settings["retroarch_dir"], settings["retroarch_playlist"])
    retroarch_file_content = _get_json_target(retroarch_file)

    games = {}
    for i in range(len(retroarch_file_content["items"])):
        
        game = retroarch_file_content["items"][i]
        title = game["label"]
        
        if not _determine_whitelist("titles", title).is_pass:
            continue

        # Sanitise the game name
        trimlocation = title.find(" (")
        if trimlocation >= 0:
            title = title[0:trimlocation]
        title = title.replace("!", "").replace(" -", ":").replace("'", "").strip()

        if not title in games:
            games[title] = [ROM(title, game["label"], game["path"], i)]
        else:
            games[title].append(ROM(title, game["label"], game["path"], i))

    return games


# Return the reference with the highest qualifying score for localisation
def _get_game_reference(games_cache, game_id):
    highest = None
    highest_game = None 
    for game in games_cache[game_id]:
        whitelist = _determine_whitelist("localisation", game.variable_title)
        if whitelist.is_pass:
            if highest == None or whitelist.score > highest:
                highest_game = game
                highest = whitelist.score

    return highest_game

# Get the combined launch args for the title
def _get_game_launch(games_cache, game_id, settings):
    retroarch_path = os.path.normpath(os.path.join(settings["retroarch_root"], "retroarch.exe"))
    retroarch_core = os.path.normpath(os.path.join(settings["retroarch_root"], ".\cores\snes9x_libretro.dll"))
    retroarch_launcher = retroarch_path + " -L " + retroarch_core
    
    reference = _get_game_reference(games_cache, game_id)
    
    return retroarch_launcher + " \"" + reference.path + "\""

# Test stub
if __name__ == "__main__":
    settings = _get_local_json("./target_params.json")
    _get_game_launch(_get_games_list(settings), "Killer Instinct", settings)
