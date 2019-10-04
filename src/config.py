import configparser

class Config:
    def _do_token(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        return config["TOKENS"]["discord_o"]
    
    def _dt_token(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        return config["TOKENS"]["discord_t"]
        
    def _dbu_token(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        return config["TOKENS"]["database_url"]

    def _api_token(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        return config["TOKENS"]["trn_api_key"]