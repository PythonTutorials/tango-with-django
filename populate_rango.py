import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    """Popoluate database."""
    python_pages = [
        {
            'title': 'Official Python Tutorial',
            'url': 'http://docs.python.org/2/tutorial/',
            'views': 13
        },
        {
            'title': 'How to Think like a Computer Scientist',
            'url': 'http://www.greenteapress.com/thinkpython/',
            'views': 33
        },
        {
            'title': 'Learn Python in 10 Minutes',
            'url': 'http://www.korokithakis.net/tutorials/python/',
            'views': 3
        }
    ]

    django_pages = [
        {
            'title': 'Official Django Tutorial',
            'url': 'https://docs.djangoproject.com/en/1.9/intro/tutorial01/',
            'views': 66
        },
        {
            'title': 'Django Rocks',
            'url': 'http://www.djangorocks.com/',
            'views': 34
        },
        {
            'title': 'How to Tango with Django',
            'url': 'http://www.tangowithdjango.com/',
            'views': 28
        }
    ]

    other_pages = [
        {
            'title': 'Bottle',
            'url': 'http://bottlepy.org/docs/dev/',
            'views': 12
        },
        {
            'title': 'Flask',
            'url': 'http://flask.pocoo.org/',
            'views': 43
        }
    ]

    categories = {
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16},
    }

    for category_name, category_attr in categories.items():
        c = Category.objects.get_or_create(name=category_name)[0]
        c.views, c.likes = category_attr['views'], category_attr['likes']
        c.save()

        for page in category_attr['pages']:
            _ = dict(title=page['title'], url=page['url'])
            p = Page.objects.get_or_create(**_)[0]
            p.category, p.views = c, page['views']
            p.save()


if __name__ == '__main__':
    populate()
