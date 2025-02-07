# CLI Format Converter

A simple command-line tool to convert between JSON, YAML, and TOML formats.

## Features

- Convert between JSON, YAML, and TOML formats
- Pretty printing support for JSON and YAML outputs
- Simple command-line interface
- Fast and lightweight

## Requirements

- Python >=3.7
- typer (included)
- pyyaml (included)
- toml (included)
- [pipx](https://github.com/pypa/pipx)

## Installation

Clone the repository and install using pip:

```bash
git clone https://github.com/dropper-d/format-converter.git
cd format-converter
pipx install .
```

## Usage

Basic usage:
```bash
fconv --f file_input.format --o file_output.format --t output format
```

### Options

- `--f`: Input file path (required)
- `--o`: Output file path (required)
- `--t`: Desired output format: json, yaml, or toml (required)
- `--p`: Use pretty formatting for JSON/YAML output (optional)

### Examples

Convert JSON to YAML:
```bash
fconv --f config.json --o config.yaml --t yaml
```

Convert YAML to TOML:
```bash
fconv --f config.yaml --o config.toml --t toml
```

Convert JSON to YAML with pretty printing:
```bash
fconv --f config.json --o config.yaml --t yaml --p
```

## Supported Conversions

- JSON → YAML
- JSON → TOML
- YAML → JSON
- YAML → TOML
- TOML → JSON
- TOML → YAML

## Development

To set up the development environment:

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .
```

## Author

Developed by dropper-d