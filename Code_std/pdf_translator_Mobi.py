#pip install PyPDF2
#pip install calibre

import os
import sys
from ebooklib import epub
from PyPDF2 import PdfFileReader
from ebooklib.utils import debug

def pdf_to_epub(file):
    # read pdf
    pdf = PdfFileReader(open(file, "rb"))

    # create epub
    book = epub.EpubBook()
    book.set_identifier('id123456')
    book.set_title(os.path.splitext(os.path.basename(file))[0])
    book.set_language('pt')

    # add metadata
    book.add_author('Seu Nome Aqui')
    book.add_metadata('DC', 'description', 'Converter PDF para MOBI')

    # add chapters
    chapters = []
    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        text = page.extractText()
        chapters.append(epub.EpubHtml(title='Página %d' % (i+1), file_name='page%d.xhtml' % (i+1), lang='pt'))
        chapters[-1].content = u'<html><head></head><body>%s</body></html>' % text

    # add chapters to book
    for chapter in chapters:
        book.add_item(chapter)
    
    # define Table Of Contents
    book.toc = tuple(chapters)

    # add navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # define CSS style
    style = 'p { text-align: justify; }'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)

    # write epub file
    epub_file = os.path.splitext(file)[0] + '.epub'
    epub.write_epub(epub_file, book, {})
    return epub_file

def epub_to_mobi(file):
    os.system('ebook-convert "%s" "%s" --output-profile=kindle' % (file, os.path.splitext(file)[0] + '.mobi'))

def pdf_to_mobi(file):
    epub_file = pdf_to_epub(file)
    epub_to_mobi(epub_file)
    os.remove(epub_file)

