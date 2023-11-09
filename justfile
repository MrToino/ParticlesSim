set shell := ["cmd.exe", "/c"]


clear-venv:
    rm -r venv

build-venv:
    python -m venv venv
    pip install -r requirements.dev.txt

run:
    venv\Scripts\activate && python simulate.py
