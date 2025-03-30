import json
import os

class Omnitags:
    def __init__(self):
        self.Aliases = {}
        self.Reverse = {}
        self.VInput = {}
        self.VPost = {}
        self.VGet = {}
        self.Flash1Msg = {}
        self.Flash = {}
        self.FlashFunc = {}
        self.FlashMsg = {}
        self.VUploadPath = {}
        self.Views = {}
        self.Titles = {}
        self.V = {}
        self.TL = {"ot": None, "a1": None}

        # Initialize V dynamically
        for i in range(1, 12):
            self.V[i] = f"contents/section_{i}"
            if i <= 6:
                self.Flash1Msg[f"flash_{i}"] = f"Flash message {i}"
            if i <= 5:
                self.FlashMsg[f"error_{i}"] = f"Error message {i}"

        # Initialize TL dynamically
        groups = {"b": 11, "c": 2, "d": 4, "e": 8, "f": 4}
        for group, count in groups.items():
            for i in range(1, count + 1):
                self.TL[f"{group}{i}"] = None

    def load_data(self, data):
        values = data.get("values", [])
        for item in values:
            if isinstance(item, dict):
                key = item.get("key")
                value = item.get("value")
                if key and value:
                    # Aliases & Reverse Mapping
                    self.Aliases[key] = value
                    self.Reverse[f"{value}_realname"] = key

                    # Input Fields
                    self.VInput.update({
                        f"{key}_input": f"txt_{value}",
                        f"{key}_filter1": f"min_{value}",
                        f"{key}_filter2": f"max_{value}",
                        f"{key}_old": f"old_{value}",
                        f"{key}_new": f"new_{value}",
                        f"{key}_confirm": f"confirm_{value}",
                    })

                    # Post & Get Requests
                    self.VPost.update({
                        key: f"txt_{value}",
                        f"{key}_old": f"old_{value}",
                        f"{key}_new": f"new_{value}",
                        f"{key}_confirm": f"confirm_{value}",
                    })
                    
                    self.VGet.update({
                        key: f"txt_{value}",
                        f"{key}_filter1": f"min_{value}",
                        f"{key}_filter2": f"max_{value}",
                    })
                    
                    # Flash Messages
                    self.Flash1Msg[key] = f"{value} successfully saved!"
                    self.Flash[key] = f"pesan_{value}"
                    self.FlashFunc[key] = f'$(".{value}").modal("show")'
                    self.FlashMsg[key] = f"{value} tidak bisa diupload!"
                    
                    # Upload Path
                    self.VUploadPath[key] = f"./assets/img/{key}/"
                    
                    # Views
                    self.Views.update({
                        key: f"contents/{key}/index",
                        f"{key}_daftar": f"contents/{key}/daftar",
                        f"{key}_admin": f"contents/{key}/admin",
                        f"{key}_laporan": f"contents/{key}/laporan",
                        f"{key}_print": f"contents/{key}/print",
                    })
                    
                    # Titles
                    self.Titles.update({
                        f"{key}_v1": value,
                        f"{key}_v2": f"List of {value}",
                        f"{key}_v3": f"{value} Data",
                        f"{key}_v4": f"{value} Report",
                        f"{key}_v5": f"{value} Data",
                        f"{key}_v6": f"{value} Profile",
                        f"{key}_v7": f"{value} Successful!",
                    })

    def get_value(self, field):
        return self.Aliases.get(field, "Unknown Field")


def read_config():
    global omnitags_config
    if 'omnitags_config' not in globals():
        omnitags_config = Omnitags()

        file_path = "app.postman_environment.json"
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    json_data = json.load(file)
                    omnitags_config.load_data(json_data)
            except (OSError, json.JSONDecodeError) as e:
                print("Error reading or parsing configuration file:", e)

    return omnitags_config

# Example Usage
if __name__ == "__main__":
    config = read_config()
    print(config.get_value("some_key"))
