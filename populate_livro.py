#!/usr/bin/env python3

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'bibliotefast.settings')
import django

django.setup()
from estante.models import livro


def populate():
    livros = open('populate_l.csv').readlines()
    print('Populating %d categories...' % len(categories))
    for livro in livros:
        isbn, titulo, autor, editora,ano, dono = livro.rstrip().split(',')
        add_livro(isbn, titulo, autor, editora, ano, dono)

def show():
    # Print out the categories we have added.
    print('Showing pages...')
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_livro(isbn=0, titulo='', autor='', editora='', ano =0 dono=''):
    c = Livro.objects.get_or_create(name=name)[0]
    if not c.views:
        c.views = views
    if not c.likes:
        c.likes = likes
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print("starting populat books")
    populate()
    show()