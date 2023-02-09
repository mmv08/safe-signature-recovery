# safe-signature-recovery
Small script to recover an address from a signature the way Gnosis Safe does it

Uses [poetry](https://python-poetry.org/)

## Installation

```
poetry install
```

## Running the script

Edit the signature and signed hash in `main.py` and run

```
poetry run python main.py
```

and you should see the recovered address in the output
