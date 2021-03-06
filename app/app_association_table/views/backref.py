#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import request, json, jsonify
from app.app_association_table import vs_association
from app.app_association_table.models import VSBlog, VSCommit
from sqlalchemy.orm import subqueryload


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
        # 通过backref建立的表关系,可以获取到commits集合
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
        commit = VSCommit.create(**args_data)
    else:
        return "blog is not existed now!"

    return jsonify(commit.to_dict())


@vs_association.route('/blog/<string:b_id>/commit/<string:c_id>', methods=['GET'])
def blog_commit_info(b_id, c_id):
    blog = VSBlog.query.filter_by(id=b_id).first_or_404()
    if blog:
        commit = VSCommit.query.filter_by(id=c_id).first_or_404()
    else:
        return "commit is not existed now!"

    return jsonify(commit.to_dict())
