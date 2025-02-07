import json
import yaml
import toml

def convert_json_to_yaml(json_data):
    return yaml.dump(json_data, default_flow_style=False)

def convert_json_to_toml(json_data):
    return toml.dumps(json_data)

def convert_yaml_to_json(yaml_data):
    return json.dumps(yaml_data, indent=4)

def convert_yaml_to_toml(yaml_data):
    return toml.dumps(yaml_data)

def convert_toml_to_json(toml_data):
    return json.dumps(toml_data, indent=4)

def convert_toml_to_yaml(toml_data):
    return yaml.dump(toml_data, default_flow_style=False)

def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def load_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

def load_toml(file_path):
    with open(file_path, "r") as file:
        return toml.load(file)

def save_output(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)