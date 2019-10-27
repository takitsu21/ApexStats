from src.utils import _request, PlayerNotFound, platform_convert, headers
import datetime as dt

def get_match_history(player, platform):
    mh_url = f"https://public-api.tracker.gg/v2/apex/standard/profile/{platform_convert(platform)}/{player}/sessions"
    try:
        r = _request(mh_url, headers=headers, call="json")
        return r["data"]
    except Exception as e:
        raise PlayerNotFound(e)

def parse_history(history):
    all_matches = []
    for session in history["items"]:
        for matches in session["matches"]:
            metadata = matches["metadata"]
            match_stat = matches["stats"]
            d = dt.datetime.strptime(metadata['endDate']['value'], '%Y-%m-%dT%H:%M:%S.%fZ')
            match = f"`{d.month}/{d.day}` - **{metadata['character']['displayValue']}** - Level `{match_stat['level']['value']}` - `{match_stat['kills']['value']}` kills"
            all_matches.append(match)
    return all_matches