import configparser

def _wapi_token():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["TOKENS"]["weapon_api_key"]

def _d_token(debug=False):
    config = configparser.ConfigParser()
    config.read("config.ini")
    if not debug:
        return config["TOKENS"]["discord_o"]
    return config["TOKENS"]["discord_t"]

def _dbu_token():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["TOKENS"]["database_url"]

def _api_token():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["TOKENS"]["trn_api_key"]

def _dbl_token():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["TOKENS"]["dbl"]