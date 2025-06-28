import importlib.metadata

project = "lazywrapper"
version = importlib.metadata.version(project)
copyright = "2025, ttk-adm"
author = "ttk-adm"
docstitle = f"{project} {version}"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
]
templates_path = ["_templates"]
exclude_patterns = []

always_document_param_types = True

autosummary_generate = True
autodoc_default_flags = [
    "members",
    "undoc-members",
    "show-inheritance",
]

html_theme = "pydata_sphinx_theme"
html_static_path = []
html_theme_options = {
    "icon_links": [
        {
            "name": "pypi",
            "url": "https://pypi.org/project/lazywrapper",
            "icon": "fa-brands fa-python",
        },
    ],
    "github_url": "https://github.com/ttk-adm/lazywrapper",
    "navbar_start": ["navbar_start"],
    "footer_start": ["copyright"],
    "footer_end": ["footer_end"],
}
