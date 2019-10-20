import json
import os.path

def _get_local_dir():
    return os.path.dirname(os.path.realpath(__file__))

def _get_local_dir_asset_path(asset):
    return os.path.join(_get_local_dir(), asset)

def _get_json_target(target):
    return json.load(open(target))

def _get_local_json(target):
    code_dir=_get_local_dir()
    actual_file=os.path.join(code_dir, target)
    return _get_json_target(actual_file)
