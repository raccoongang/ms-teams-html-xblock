"""Setup for html XBlock."""

import os

from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='ms-teams-html-xblock',
    version='0.1.3',
    description='HTML XBlock will help creating and using a secure and easy-to-use HTML blocks',
    license='AGPL v3',
    packages=[
        'html_xblock',
    ],
    install_requires=[
        'XBlock',
        'bleach',
    ],
    entry_points={
        'xblock.v1': [
            'ms_teams_xblock = html_xblock:HTML5XBlock',
            'ms_teams_excluded_html5 = html_xblock:ExcludedHTML5XBlock',
        ]
    },
    package_data=package_data("html_xblock", ["static", "public"]),
)
