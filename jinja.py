from jinja2 import Template, Environment, PackageLoader, select_autoescape
env = Environment(
    loader = PackageLoader('library', 'templates'),
    autoescape= select_autoescape(['html', 'xml'])
)

template = env.get_template('test_jinja.html')
x = template.render()
print(x)
