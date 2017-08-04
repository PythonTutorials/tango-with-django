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
            'url': 'http://docs.python.org/2/tutorial/'
        },
        {
            'title': 'How to Think like a Computer Scientist',
            'url': 'http://www.greenteapress.com/thinkpython/'
        },
        {
            'title': 'Learn Python in 10 Minutes',
            'url': 'http://www.korokithakis.net/tutorials/python/'
        }
    ]

    django_pages = [
        {
            'title': 'Official Django Tutorial',
            'url': 'https://docs.djangoproject.com/en/1.9/intro/tutorial01/'
        },
        {
            'title': 'Django Rocks',
            'url': 'http://www.djangorocks.com/'
        },
        {
            'title': 'How to Tango with Django',
            'url': 'http://www.tangowithdjango.com/'
        }
    ]

    other_pages = [
        {
            'title': 'Bottle',
            'url': 'http://bottlepy.org/docs/dev/'
        },
        {
            'title': 'Flask',
            'url': 'http://flask.pocoo.org'
        }
    ]

    categories = {
        'Python': python_pages,
        'Django': django_pages,
        'Other Frameworks': other_pages
    }

    for category_name, pages in categories.items():
        c = Category.objects.get_or_create(name=category_name)[0]
        c.save()

        for page in pages:
            _ = dict(title=page['title'], url=page['url'], category=c)
            p = Page.objects.get_or_create(**_)[0]
            p.save()


if __name__ == '__main__':
    populate()
