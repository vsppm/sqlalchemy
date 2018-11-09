#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os


class base_config(object):
    """Default configuration options."""
    SITE_NAME = os.environ.get('APP_NAME', 'SQLALCHEMY')

    SERVER_HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    SERVER_PORT = os.environ.get('SERVER_PORT', '5555')
    MYSQL_HOST = os.environ.get('MYSQL_HOST', '47.104.184.107')
    MYSQL_PORT = os.environ.get('MYSQL_PORT', 8096)
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASS = os.environ.get('MYSQL_PASS', 'Red198594#')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sqlalchemy_test')

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (
        MYSQL_USER,
        MYSQL_PASS,
        MYSQL_HOST,
        MYSQL_PORT,
        MYSQL_DB
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class dev_config(base_config):
    """Development configuration options."""
    ASSETS_DEBUG = True
