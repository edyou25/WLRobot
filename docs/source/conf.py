"""Sphinx configuration for WLRobot guide."""

project = "WLRobot 使用说明"
copyright = "2025, Hong Kong Polytechnic University"
author = "Imitation Learning Research | PolyU"
release = "0.1.0"

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
]

templates_path = ["_templates"]
exclude_patterns = []
language = "zh_CN"

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_extra_path = ["assets/wl.mp4"]
html_title = "WLRobot 使用说明"
html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "style_external_links": True,
}

autosectionlabel_prefix_document = True
todo_include_todos = False
