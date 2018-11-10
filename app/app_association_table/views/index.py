#!/usr/bin/python3
# -*- coding: utf-8 -*-

from app.app_association_table import vs_association


@vs_association.route('/', methods=['GET'])
def index():
    return 'vsppm application vs_association module!'
