#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Blueprint

vs_association = Blueprint(
    'vs_association',
    __name__,
    static_folder='../../static',
    template_folder='../../templates')

from .views import index
