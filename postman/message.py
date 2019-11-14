from jinja2 import Template

class Message:
    _to = []
    _is_html = False

    def __init__(self, to=None, subject=None, body=None):
        self._subject = subject
        if to:
            self._to = [to]
        self._body = body

    def to(self, to):
        self._to.append(to)
        return self

    def subject(self, subject:str):
        self._subject = subject
        return self

    def body(self, body:str):
        self._body = body
        return self

    def html(self, html:str):
        self._html = html
        self._is_html = True
        return self

    def template(self, path:str, args:dict):
        self._template = path
        self._template_args = args
        self._is_html = True
        return self

    def is_html(self):
        return self._is_html

    def render(self):
        if self._body:
            return self._body
        elif self._template:
            with open(self._template) as file:
                template = Template(file.read())
                return template.render(self._template_args)
        return None

