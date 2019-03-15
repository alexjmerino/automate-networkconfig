# Imports Jinja2
from jinja2 import Environment, FileSystemLoader

# Import YAML
import yaml

# Create Jinja2 environment
environment = Environment(loader=FileSystemLoader('./'))

with open("dictionary.yaml") as _:
    dictionary =  yaml.load(_)

# Render template and print generated config to file
template = environment.get_template("baseline_config.j2")
print (template.render(config=dictionary), file=open("output_config.txt", "w") )
