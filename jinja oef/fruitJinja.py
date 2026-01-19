from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("fruitTemplate.txt")


print(template.render(fruits=["appel","peer","banaan"]))