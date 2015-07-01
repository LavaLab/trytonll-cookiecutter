# -*- coding: utf-8 -*-
"""
    {{ cookiecutter.module_name }}

    :copyright: (c) The file COPYRIGHT at the top level of this
    :repository contains the full copyright notices.
    :license: , see LICENSE for more details.
"""
from trytond.pool import Pool


def register():
    Pool.register(
        module='{{ cookiecutter.module_name }}', type_='model'
    )
