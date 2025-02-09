import typer
from .converter import convert_file

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
    By: dropper-d
    """
    supported_formats = ["json", "yaml", "toml"]
    
    input_fmt = f.split('.')[-1]
    output_fmt = t.lower()

    if input_fmt not in supported_formats or output_fmt not in supported_formats:
        typer.echo("Both input and output formats must be one of json, yaml, or toml.")
        raise typer.Exit(1)
    
    try:
        convert_file(f, input_fmt, o, output_fmt)
        typer.echo(f"File converted and saved in {o}")
    except Exception as e:
        typer.echo(f"Error: {str(e)}")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()