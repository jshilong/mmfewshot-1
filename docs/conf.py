# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

import pytorch_sphinx_theme

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'mmfewshot'
copyright = '2018-2021, OpenMMLab'
author = 'MMFewShot Author'
version_file = '../mmfewshot/version.py'


def get_version():
    with open(version_file, 'r') as f:
        exec(compile(f.read(), version_file, 'exec'))
    return locals()['__version__']


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'recommonmark',
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton',
    'sphinx_markdown_tables',
]

autodoc_mock_imports = ['matplotlib', 'mmfewshot.version', 'mmcv.ops']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pytorch_sphinx_theme'
html_theme_path = [pytorch_sphinx_theme.get_html_theme_path()]
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'menu': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/open-mmlab/mmfewshot'
        },
        {
            'name':
            'Projects',
            'children': [{
                'name':
                'MMCV',
                'url':
                'https://mmcv.readthedocs.io/en/latest/',
                'description':
                'Foundational library for computer vision'
            }, {
                'name':
                'MMDetection',
                'url':
                'https://mmdetection.readthedocs.io/en/latest/',
                'description':
                'Object detection toolbox and benchmark'
            }, {
                'name':
                'MMAction2',
                'url':
                'https://mmaction2.readthedocs.io/en/latest/',
                'description':
                'Action understanding toolbox and benchmark'
            }, {
                'name':
                'MMClassification',
                'url':
                'https://mmclassification.readthedocs.io/en/latest/',
                'description':
                'Image classification toolbox and benchmark'
            }, {
                'name':
                'MMSegmentation',
                'url':
                'https://mmsegmentation.readthedocs.io/en/latest/',
                'description':
                'Semantic segmentation toolbox and benchmark'
            }, {
                'name': 'MMDetection3D',
                'url': 'https://mmdetection3d.readthedocs.io/en/latest/',
                'description': 'General 3D object detection platform'
            }, {
                'name': 'MMEditing',
                'url': 'https://mmediting.readthedocs.io/en/latest/',
                'description': 'Image and video editing toolbox'
            }, {
                'name':
                'MMOCR',
                'url':
                'https://mmocr.readthedocs.io/en/latest/',
                'description':
                'Text detection, recognition and understanding toolbox'
            }, {
                'name':
                'MMTracking',
                'url':
                'https://mmtracking.readthedocs.io/en/latest/',
                'description':
                'Video perception toolbox and benchmark'
            }, {
                'name': 'MMGeneration',
                'url': 'https://mmgeneration.readthedocs.io/en/latest/',
                'description': 'Generative model toolbox'
            }, {
                'name': 'MMFlow',
                'url': 'https://mmflow.readthedocs.io/en/latest/',
                'description': 'Optical flow toolbox and benchmark'
            }, {
                'name':
                'MMFewShot',
                'url':
                'https://mmfewshot.readthedocs.io/en/latest/',
                'description':
                'FewShot learning toolbox and benchmark'
            }, {
                'name':
                'MMHuman3D',
                'url':
                'https://mmhuman3d.readthedocs.io/en/latest/',
                'description':
                '3D human parametric model toolbox and benchmark.'
            }]
        },
        {
            'name':
            'OpenMMLab',
            'children': [{
                'name': 'Homepage',
                'url': 'https://openmmlab.com/'
            }, {
                'name': 'GitHub',
                'url': 'https://github.com/open-mmlab/'
            }, {
                'name': 'Twitter',
                'url': 'https://twitter.com/OpenMMLab'
            }, {
                'name': 'Zhihu',
                'url': 'https://zhihu.com/people/openmmlab'
            }]
        },
    ]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/readthedocs.css']

# -- Extension configuration -------------------------------------------------
# Ignore >>> when copying code
copybutton_prompt_text = r'>>> |\.\.\. '
copybutton_prompt_is_regexp = True
