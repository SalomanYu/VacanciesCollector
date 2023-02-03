import json
import os
import requests

JSON_FILE = "text.json"

def unicode_to_utf_8(jsonData: dict) -> dict:
    save_json_file(jsonData)
    data = read_json_file()
    return data

def save_json_file(data):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def read_json_file() -> dict:
    data = json.load(open(JSON_FILE, "r", encoding="utf-8"))
    os.remove(JSON_FILE)
    return data

def get_json(url: str) :
    response = requests.get(url)
    if response.status_code != 200: return
    return unicode_to_utf_8(response.json())
