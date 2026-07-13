import subprocess 
import threading
from os import path
from rich.live import Live
from rich.table import Table
from rich.console import Console
import time
import json
from datetime import datetime


class LPEAException(Exception):
    pass

console = Console()
status = {}
status_lock = threading.Lock()


def make_table():
    table = Table(title="LPE Scanner")
    table.add_column("Category", style="cyan", width=25)
    table.add_column("State", style="green", width=12)
    table.add_column("Current Function", style="yellow")

    with status_lock:
        for _, info in status.items():
            table.add_row(
                info["title"],
                info["state"],
                info["current"]
            )

    return table

def worker(name, scanner):

    scan = scanner()

    functions = scan["functions"]
    category = scan["title"]

    with status_lock:
        status[name]["state"] = "[yellow]Running[/yellow]"

    total = len(functions)

    results = {}

    for index, func in enumerate(functions, start=1):

        with status_lock:
            status[name]["current"] = f"{func.__name__} ({index}/{total})"

        try:

            value, title = func()

            results[title] = value

        except Exception as e:

            results[func.__name__] = {
                "error": str(e)
            }

    report = {
        name: {                   
            "title": category,   
            "results": results
        }
    }

    filename = f"{name}.json"

    with open(path.join("Enum", filename), "w") as f:
        json.dump(report, f, indent=4)

    with status_lock:
        status[name]["state"] = "[green]Done[/green]"
        status[name]["current"] = f"{total}/{total} checks"

   