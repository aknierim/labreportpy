#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import datetime

from configparser import ConfigParser

import labreportpy

# -- Project information -----------------------------------------------------
setup_cfg = ConfigParser()
setup_cfg.read([os.path.join(os.path.dirname(__file__), "..", "setup.cfg")])
setup_metadata = dict(setup_cfg.items("metadata"))
setup_options = dict(setup_cfg.items("options"))

project = setup_metadata["name"]
author = setup_metadata["author"]
copyright = "{}.  Last updated {}".format(
    setup_metadata["author"], datetime.datetime.now().strftime("%d %b %Y %H:%M")
)
python_requires = setup_options["python_requires"]

version = labreportpy.__version__
# The full version, including alpha/beta/rc tags.
release = version

print(python_requires)

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx_automodapi.automodapi",
    "sphinx_automodapi.smart_resolver",
    "numpydoc",
    "sphinx_design",
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_theme_options = {
    "github_url": "https://github.com/aknierim/labreportpy",
    "use_edit_page_button": True,
}

html_context = {
    "default_mode": "light",
    "github_user": "aknierim",
    "github_repo": "labreportpy",
    "github_version": "main",
    "doc_path": "docs",
}

html_title = f"{project} v{release}"
htmlhelp_basename = project + "doc"


intersphinx_mapping = {
    "python": ("https://docs.python.org/3.11", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
}
