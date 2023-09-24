import json
import params
import os
import json


class Config:
    def __init__(self):
        self.APP_NAME = 'VRChatOWOSuit'
        self.default_config = {
            "server_port": 9001,
            "owo_ip": "",
            "should_detect_ip": True,
            "should_connect_on_startup": False,
            "frequency": 100,
            "intensities": {
                params.owo_suit_Pectoral_L: 60,
                params.owo_suit_Pectoral_R: 60,
                params.owo_suit_Abdominal_L: 60,
                params.owo_suit_Abdominal_R: 60,
                params.owo_suit_Arm_L: 60,
                params.owo_suit_Arm_R: 60,
                params.owo_suit_Dorsal_L: 60,
                params.owo_suit_Dorsal_R: 60,
                params.owo_suit_Lumbar_L: 60,
                params.owo_suit_Lumbar_R: 60,
            }
        }
        self.current_config = None

    def get_by_key(self, key: str):
        return self.current_config.get(key)

    def update(self, key: str, nextValue):
        if (key in self.current_config):
            self.current_config[key] = nextValue

    def read_config_from_disk(self):
        appdata_path = os.environ.get('LOCALAPPDATA')
        app_directory = os.path.join(appdata_path, self.APP_NAME)
        os.makedirs(app_directory, exist_ok=True)
        config_path = os.path.join(app_directory, 'config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r') as file:
                data = json.load(file)
                return data
        else:
            with open(config_path, 'w') as file:
                json.dump(self.default_config, file, indent=4)
            return self.default_config

    def write_config_to_disk(self):
        if self.current_config == None:
            return
        appdata_path = os.environ.get('LOCALAPPDATA')
        app_directory = os.path.join(appdata_path, self.APP_NAME)
        os.makedirs(app_directory, exist_ok=True)
        config_path = os.path.join(app_directory, 'config.json')
        with open(config_path, 'w') as file:
            json.dump(self.current_config, file, indent=4)

    def init(self):
        self.current_config = self.read_config_from_disk()
