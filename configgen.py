import jinja2
import json

template_file = "rrtemplate.j2"
json_parameter_file = "rrconfig.json"

config_parameters = json.load(open(json_parameter_file))

env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."),
                         trim_blocks=True,
                         lstrip_blocks=True)
template = env.get_template(template_file)

result = ''
for parameter in config_parameters:
    result = template.render(parameter)

print(result)
