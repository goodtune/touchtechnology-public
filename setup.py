from setuptools import setup, find_packages

from touchtechnology.public import __version__ as version


def pep386(v):
    import re
    regex = re.compile(r' (?:([ab])\w+) (\d+)$')
    if regex.search(v):
        base = regex.sub('', v)
        minor = ''.join(regex.search(v).groups())
        return base + minor
    return v

setup(
    name='touchtechnology-public',
    version=pep386(version),
    packages=find_packages(exclude=["test_app"]),
    author='Touch Technology Pty Ltd',
    author_email='support@touchtechnology.com.au',
    description='Publicly released components used in all Touch Technology library code.',
    url='http://www.touchtechnology.com.au/',
    install_requires=[
        'Django>=1.4.10,<1.7',
    ],
    test_suite='test_app.runtests.runtests',
    include_package_data=True,
    namespace_packages=['touchtechnology'],
    zip_safe=False,
)
