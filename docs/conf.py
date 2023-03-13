# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python Teamscale Client'
copyright = '2023, CQSE GmbH'
author = 'CQSE GmbH'
release = '9.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon', 'sphinx.ext.githubpages']

templates_path = ['_templates']
exclude_patterns = []

source_suffix = '.rst'
root_doc = 'index'

pygments_style = 'sphinx'

toc_object_entries_show_parents = 'domain'
add_module_names = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
htmlhelp_basename = 'sphinxdoc'

# -- Options for Theme 'sphinx_book_theme' -----------------------------------
# https://sphinx-book-theme.readthedocs.io/en/latest/tutorials/get-started.html
html_theme_options = {
    "use_edit_page_button": True,
    "use_source_button": True,
    "use_issues_button": True,
    "icon_links": [{
        "name": "GitHub",
        "url": "https://github.com/cqse/teamscale-client-python",
        "icon": "fa-brands fa-square-github",
        "type": "fontawesome"
    }, {
        "name": "Teamscale Documentation",
        "url": "https://docs.teamscale.com/reference/python-client/",
        "icon": "fa-solid fa-house",
        "type": "fontawesome"
    }, {
        "name": "Teamscale REST API",
        "url": "https://docs.teamscale.com/reference/rest-api/",
        "icon": "fa-sharp fa-solid fa-gears",
        "type": "fontawesome"
    }, {
        "name": "PyPi",
        "url": "https://pypi.org/project/teamscale-client/",
        "icon": "https://badge.fury.io/py/teamscale-client.svg",
        "type": "url"
    }]
}

html_context = {
    "github_url": "https://github.com",
    "github_user": "cqse",
    "github_repo": "teamscale-client-python",
    "github_version": "master",
    "doc_path": "docs",
}

# -- Options for Python ------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-python-domain
python_use_unqualified_type_names = True
