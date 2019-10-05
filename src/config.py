import configparser

def _wapi_token():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["TOKENS"]["weapon_api_key"]

def _do_token():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["TOKENS"]["discord_o"]

def _dt_token():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["TOKENS"]["discord_t"]
    
def _dbu_token():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["TOKENS"]["database_url"]

def _api_token():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["TOKENS"]["trn_api_key"]