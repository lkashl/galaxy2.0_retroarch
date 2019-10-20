import sys
import logging
import os.path
import os

from galaxy.api.plugin import Plugin, create_and_run_plugin
from galaxy.api.consts import Platform
from galaxy.api.types import Authentication, Game, LicenseInfo, LicenseType, LocalGame, LocalGameState

from parse_retroarch_file import _get_games_list, _get_game_launch, ROM
from parse_manifest_file import _get_translated_platform
from local_utils import _get_local_json, _get_json_target, _get_local_dir

class RetroarchPlugin(Plugin):
    def __init__(self, reader, writer, token):
        super().__init__(
            Platform[_get_translated_platform()], 
            "0.1",
            reader,
            writer,
            token
        )
        # Cache settings: User will have to restart galaxy to update settings and games list
        # This makes process lighter for thousands of games
        self.settings = _get_local_json("./target_params.json")
        self.games_cache = _get_games_list(self.settings)

    # Always authenticate as retroarch user
    async def authenticate(self, stored_credentials=None):
        return Authentication("retroarch", "retroarch")

    # Ask relevant library (currently retroarch) for a games list
    async def get_owned_games(self):
        games_retroarch = []

        for rom in self.games_cache:
            games_retroarch.append(Game(
                rom,
                rom,
                None,
                LicenseInfo(LicenseType.SinglePurchase, None)
            ))

        return games_retroarch

    # All games are defined as being local
    async def get_local_games(self):
        games_retroarch = []
        for rom in self.games_cache:
            games_retroarch.append(LocalGame(rom, LocalGameState(1)))

        return games_retroarch

    # Launch game using retroarch
    async def launch_game(self, game_id): 
        roms = _get_game_launch(self.games_cache, game_id, self.settings)
        save_path = "C:\\Users\\lkash\\Desktop\\test21.txt"
        fs = open(save_path, "w")
        fs.write("Finding reference")
        fs.write(roms)
        os.system(roms)

def main():
    create_and_run_plugin(RetroarchPlugin, sys.argv)

if __name__ == "__main__":
    main()