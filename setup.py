from setuptools import setup


setup(
    name='lektor-rstfile',
    description='Adds reStructuredText support to Lektor (as standalone files).',
    version='0.2',
    author=u'Amit Aronovitch',
    author_email='aronovitch@gmail.com',
    url='http://github.com/AmitAronovitch/lektor-rstfile',
    license='MIT',
    install_requires=[
        'Pygments',
        'docutils'],
    py_modules=['lektor_rstfile'],
    entry_points={
        'lektor.plugins': [
            'rstfile = lektor_rstfile:RstFilePlugin']})
