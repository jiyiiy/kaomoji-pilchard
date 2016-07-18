import random
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))


class WebBase:
    def _template(self, name, vars={}):
        tmpl = env.get_template(name)
        return tmpl.render(**vars)


    def _add_random(self, mc, map):
        out = []
        for key, occurences in mc:
            print key, map[key]
            out.append((
                key, occurences,
                random.choice(map[key])
            ))
        return out

