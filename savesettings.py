import sys
import json


def save(field, value):
    path = 'settings.json'
    with open(path, 'r') as f:
        content = json.load(f)
    
    content[field] = value

    with open(path, 'w') as f:
        json.dump(content, f, indent=4)

def decode(data):
    return json.loads(data)