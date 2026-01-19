from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("fruitPriceTemplate.txt")


print(template.render(market={"appel": 2,"peer":5,"banaan":7}))