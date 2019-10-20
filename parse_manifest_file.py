import json
import os.path

from local_utils import _get_local_json
from galaxy.api.consts import Platform

def _get_translated_platform():
    manifest = _get_local_json("manifest.json")
    targetPlatform = manifest["platform"]
    targetName = ""

    for platform in Platform:
        if platform.value == targetPlatform:
            targetName = platform.name
            break

    if targetName == "":
        print("TODO: Add Galaxy errors")
    else:
        return targetName

if __name__ == "__main__":
    _get_translated_platform()