from setuptools import setup, find_packages
import re

with open('README.md') as f:
    long_description = f.read()

version = ''
with open('pyext/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Version is not set')

def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements



setup(
    name='py-ext',
    version=version,
    author='LyQuid',
    author_email='lyquidpersonal@gmail.com',
    description = 'Python extension to help make your project easier',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT License',
    url='https://github.com/LyQuid12/py-ext',
    project_urls={
        "Discord": "https://discord.gg/qpT2AeYZRN",
        "Issue tracker": "https://github.com/LyQuid12/py-ext/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    keywords=["Python extensions", "extensions"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python'
    ]
)
