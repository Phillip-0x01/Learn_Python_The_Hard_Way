try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Project ex48 - Lexicon',
    'author': 'Phillip Henkels',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'phenkels@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'project_ex48'
}

setup(**config)
