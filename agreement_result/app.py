import json
from jinja2 import Environment, FileSystemLoader, StrictUndefined

def pln(x):
    return f"{x:,.2f}".replace(",", " ").replace(".", ",") + " zł"

dane = json.load(open("dane.json", encoding="utf-8"))

env = Environment(loader=FileSystemLoader("."), undefined=StrictUndefined)
env.globals["pln"] = pln

html = env.get_template("szablon_umowy.html").render(**dane)
open("umowa_wynik.html", "w", encoding="utf-8").write(html)