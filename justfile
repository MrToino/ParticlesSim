set shell := ["cmd.exe", "/c"]


clear-venv:
    rm -r venv

build-venv:
    python -m venv venv
    pip install -r requirements.dev.txt

pygame:
    venv\Scripts\activate && python pygame.py

tkinter:
    venv\Scripts\activate && python tkinter.py