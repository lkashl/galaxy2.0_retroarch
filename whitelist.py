from local_utils import _get_local_json, _get_json_target, _get_local_dir

# Create a whitelist entity that will be used to determine games for inclusion/exclusion
class WhitelistEntity: 
    def __init__(self, is_pass, score):
        self.is_pass = is_pass
        self.score = score

# Check if a criteria is present in a title
def _is_present(title, list):
    for item in list:
        if item in title:
            return True

# Get amount of criteria present in the title
def _get_count_of(title, list):
    count = 0
    for item in list:
        if item in title:
            count+=1
    
    return count

# Process whitelisting instructions
def _determine_whitelist(type, title):
    title = title.lower()
    
    settings = _get_local_json("./target_params.json")

    must_be_present = settings[type]["must_be_present"]
    must_not_be_present = settings[type]["must_not_be_present"]

    if must_be_present.__len__() != 0 and not _is_present(title, must_be_present):
        return WhitelistEntity(False, 0)
    
    if must_not_be_present.__len__() !=0 and _is_present(title, must_not_be_present):
        return WhitelistEntity(False, 0)

    # Title is a binary outcome and does not support points
    if type=="titles":
        return WhitelistEntity(True, 0)

    points_if_present = settings[type]["points_if_present"]
    points_if_absent = settings[type]["points_if_absent"]

    positives = _get_count_of(title, points_if_present)
    negatives = _get_count_of(title, points_if_absent)
    
    overall_score = positives - negatives

    return WhitelistEntity(True, overall_score)
