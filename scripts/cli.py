import typer
import json
import yaml
from .converter import (
    convert_json_to_yaml,
    convert_json_to_toml,
    convert_yaml_to_json,
    convert_yaml_to_toml,
    convert_toml_to_json,
    convert_toml_to_yaml,
    load_json,
    load_yaml,
    load_toml,
    save_output
)

app = typer.Typer()

@app.command()
def main(
    f: str = typer.Option(..., help="Input file"),
    o: str = typer.Option(..., help="Output file"),
    t: str = typer.Option(..., help="Output file format (json, yaml, toml)"),
    p: bool = typer.Option(False, help="Use pretty formatting for JSON/YAML output")
):
    """
    Convert files between JSON, YAML y TOML.
    by: dropper-d
    """
    if t == "yaml":
        if f.endswith(".json"):
            data = load_json(f)
            result = convert_json_to_yaml(data)
        elif f.endswith(".toml"):
            data = load_toml(f)
            result = convert_toml_to_yaml(data)
        else:
            typer.echo("Format is not supported to YAML.")
            raise typer.Exit(1)

    elif t == "toml":
        if f.endswith(".json"):
            data = load_json(f)
            result = convert_json_to_toml(data)
        elif f.endswith(".yaml"):
            data = load_yaml(f)
            result = convert_yaml_to_toml(data)
        else:
            typer.echo("Format is not supported to TOML.")
            raise typer.Exit(1)

    elif t == "json":
        if f.endswith(".yaml"):
            data = load_yaml(f)
            result = convert_yaml_to_json(data)
        elif f.endswith(".toml"):
            data = load_toml(f)
            result = convert_toml_to_json(data)
        else:
            typer.echo("Format is not supported to JSON.")
            raise typer.Exit(1)

    else:
        typer.echo("Output format is not supported.")
        raise typer.Exit(1)

    if p and t in ["json", "yaml"]:
        if t == "json":
            result = json.dumps(json.loads(result), indent=4)
        elif t == "yaml":
            result = yaml.dump(yaml.safe_load(result), default_flow_style=False)

    save_output(o, result)
    typer.echo(f"File converted and saved in {o}")

if __name__ == "__main__":
    app()