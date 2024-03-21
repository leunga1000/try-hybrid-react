from socketify import App, sendfile
import json
from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions


class MakoTemplate:
    def __init__(self, **options):
        self.lookup = TemplateLookup(**options)
        # You can also add caching and logging strategy here if you want ;)
    def render(self, templatename, **kwargs):
        try:
            template = self.lookup.get_template(templatename)
            return template.render(**kwargs)
        except Exception as err:
            return exceptions.html_error_template().render()

async def home(res, req):
    res.render('index.html')
    #await sendfile(res, req, './public/template.html')


def run(app: App):
    app.template( 
            MakoTemplate(
                #directories=["./templates"], output_encoding='utf-8', encoding_errors="replace" 
                directories=["./public"], output_encoding='utf-8', encoding_errors="replace" 
                )
    )
    app.get("/", home)
    app.get("/hw", lambda res, req: res.end("Hello World!"))
    app.static('/', './public')

#\k🤣🤣🤣

if __name__ == '__main__':
    app = App()
    run(app)
    app.listen(8000)
    app.run()
