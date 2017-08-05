import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django.settings')

import django
django.setup()

import csv
from rango.models import Category, Page


def output():
    """Output dabase data to csv files."""
    with open('category.csv', 'w') as f:
        w = csv.DictWriter(f, ['name', 'views', 'likes', 'slug'])
        w.writeheader()
        for c in Category.objects.all():
            row = {'name': c.name, 'views': c.views, 'likes': c.likes, 'slug': c.slug}
            w.writerow(row)

    with open('page.csv', 'w') as f:
        w = csv.DictWriter(f, ['category', 'title', 'url', 'views'])
        w.writeheader()
        for p in Page.objects.all():
            row = {'category': p.category, 'title': p.title, 'url': p.url, 'views': p.views}
            w.writerow(row)


if __name__ == '__main__':
    output()
