import markdown
from weasyprint import HTML, CSS

# 生成带双栏CSS的HTML
css = CSS(string='''
    @page { size: A4; margin: 1cm; }
    body {
        column-count: 2;
        column-gap: 2em;
        /* 关键：指定一个安全的字体栈 */
        font-family: "DejaVu Sans", Arial, Helvetica, sans-serif;
    }
    h1, h2, h3 { break-after: avoid; }
''')

html = markdown.markdown(open("未命名.md", encoding='utf-8').read())
HTML(string=html).write_pdf("output.pdf", stylesheets=[css], optimize_size=None)