class Html:
    def __init__(self):
        pass
    def doctype(self):
        return '<!DOCTYPE html>'
    def html(self , content):
        content = str(content)
        return f'<html>{content}</html>'
    def title(self , title):
        tilte = str(title)
        return f'<title>{title}</title>'
    def body(self , content):
        content = str(content)
        return f'<body>{content}</body>'
    def head(self , content):
        content = str(content)
        return f'<head>{content}</head>'
    def h(self, heading , level):
        heading = str(heading)
        level = int(level)
        if level < 1 or level > 6:
            level = ''
        return f'<h{level}>{heading}</h{level}>'
    def p(self , text , level):
        text = str(text)
        level = int(level)
        if level < 1 or level > 6:
            level = ''
        return f'<p{level}>{text}</p{level}>'
    def a(self , href , text):
        href = str(href)
        text = str(text)
        return f'<a href="{href}">{text}</a>'
    def img(path , alt , width , height):
        path = str(path)
        alt = str(alt)
        width = int(width)
        height = int(height)
        return f'<img src="{path}" alt="{alt}" width="{width}" height="{height}">'
    def div(self , content):
        content = str(content)
        return f'<div>{content}</div>'
    def br(self):
        return '<br>'
    def b(self , text):
        text = str(text)
        return f'<b>{text}</b>'
    def strong(self , text):
        text = str(text)
        return f'<strong>{text}</strong>'
    def i(self , text):
        text = str(text)
        return f'<i>{text}</i>'
    def small(self , text):
        text = str(text)
        return f'<small>{text}</small>'
    def mark(self , text):
        text = str(text)
        return f'<mark>{text}</mark>'
    def dele(self , text):
        text = str(text)
        return f'<del>{text}</del>'
    def ins(self , text):
        text = str(text)
        return f'<ins>{text}</ins>'
    def sub(self , text):
        text = str(text)
        return f'<sub>{text}</sub>'
    def sup(self , text):
        text = str(text)
        return f'<sup>{text}</sup>'
whtml = Html()