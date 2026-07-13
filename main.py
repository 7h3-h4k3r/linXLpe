from libs.run import SCAnning
from os import makedirs

from libs import make_table , worker ,status , status_lock ,console ,Live ,threading
import time

if __name__ == "__main__":

    methods = []
    for name in dir(SCAnning):
        if name.startswith("_"):
            continue
        method = getattr(SCAnning, name)
        if callable(method):
            scan = method()
            status[name] = {
                "title": scan["title"],
                "state": "[red]Waiting[/red]",
                "current": "-"
            }
            methods.append((name, method))
    makedirs("Enum", exist_ok=True)
    with Live(make_table(), refresh_per_second=10) as live:
        threads = []
        for name, method in methods:
            t = threading.Thread(
                target=worker,
                args=(name, method),
                daemon=True
            )
            t.start()
            threads.append(t)

        while any(t.is_alive() for t in threads):
            live.update(make_table())
            time.sleep(0.1)

        for t in threads:
            t.join()

        live.update(make_table())

    console.print("\n[bold green]✓ Scan Finished[/bold green]")