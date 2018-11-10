#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import request, json, jsonify
from app.app_association_table import vs_association
from app.app_association_table.models import VSBlog, VSCommit


@vs_association.route('/blog', methods=['POST'])
def blog_create():
    if request.is_json:
        args_data = request.get_json()
    else:
        args_data = json.loads(request.data)

    blog = VSBlog.create(**args_data)

    return jsonify(blog.to_dict())


@vs_association.route('/blog/<string:id>', methods=['GET'])
def blog_info(id):
    blog = VSBlog.query.filter_by(id=id).first_or_404()
    if blog:
        for cc in blog.commits:
            print(cc.to_dict())

    return jsonify(blog.to_dict())


@vs_association.route('/blog/<string:id>', methods=['DELETE'])
def blog_del(id):
    blog = VSBlog.query.filter_by(id=id).first_or_404()
    if blog:
        blog.delete()
    else:
        return 'False'

    return 'True'


@vs_association.route('/blog/<string:id>', methods=['PUT'])
def blog_update(id):
    if request.is_json:
        args_data = request.get_json()
    else:
        args_data = json.loads(request.data)

    blog = VSBlog.query.filter_by(id=id).first_or_404()
    if blog:
        blog.update(**args_data)
    else:
        return 'False'

    return 'True'


@vs_association.route('/blog/<string:id>/commit', methods=['POST'])
def blog_commit_create(id):
    if request.is_json:
        args_data = request.get_json()
    else:
        args_data = json.loads(request.data)

    blog = VSBlog.query.filter_by(id=id).first_or_404()
    if blog:
        blog.commits.append(VSCommit(**args_data))
        blog.save()

    return jsonify(blog.to_dict())



