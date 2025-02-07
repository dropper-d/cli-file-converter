import json, yaml, toml

LOADERS = {'json': json.load, 'yaml': yaml.safe_load, 'toml': toml.load}
DUMPERS = {'json': lambda d: json.dumps(d, indent=4),
           'yaml': lambda d: yaml.dump(d, default_flow_style=False),
           'toml': toml.dumps}

def load_file(fp, fmt):
    with open(fp, 'r') as f:
        return LOADERS[fmt](f)

def dump_data(data, fmt):
    return DUMPERS[fmt](data)

def save_output(fp, content):
    with open(fp, 'w') as f:
        f.write(content)

def convert_file(input_path, input_fmt, output_path, output_fmt):
    save_output(output_path, dump_data(load_file(input_path, input_fmt), output_fmt))
