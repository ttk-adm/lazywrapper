

# -- Project information -----------------------------------------------------
project = 'lazywrapper'
version = "0.1.0"
copyright = '2025, ttk-adm'
author = 'ttk-adm'
docstitle = "lazywrapper"

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    "sphinx.ext.autosummary",
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

always_document_param_types = True

autodoc_default_flags = [
    "members",
    "undoc-members",
    "show-inheritance",
]


# -- HTML output -------------------------------------------------------------
html_theme = 'alabaster'
html_static_path = []