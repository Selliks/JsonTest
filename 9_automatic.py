import json


def save_to_json(data, filename):
    try:
        filenames = f"9_{filename}"
        with open(filenames, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"The data was saved in {filenames}.")
    except Exception as e:
        print(f"Error. {e}")


def load_from_json(filename):
    filenames = f"9_{filename}"
    try:
        with open(filenames, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error in {filenames}: {e}")
        return None


config_data = {
    "language": "ukrainian",
    "theme": "dark",
    "screen_resolution": "1920x1080"
}

config_filename = 'config.json'
save_to_json(config_data, config_filename)
