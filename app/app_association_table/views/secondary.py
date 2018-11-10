#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import request, json, jsonify
from app.app_association_table import vs_association
from app.app_association_table.models import VSProject, VSUser


@vs_association.route('/project', methods=['POST'])
def project_create():
    if request.is_json:
        args_data = request.get_json()
    else:
        args_data = json.loads(request.data)

    project = VSProject.create(**args_data)

    return jsonify(project.to_dict())


@vs_association.route('/project/<string:id>', methods=['GET'])
def project_info(id):
    project = VSProject.query.filter_by(id=id).first_or_404()
    if project:
        for uu in project.users:
            print(uu.to_dict())

    return jsonify(project.to_dict())


@vs_association.route('/project/<string:id>', methods=['DELETE'])
def project_del(id):
    project = VSProject.query.filter_by(id=id).first_or_404()
    if project:
        project.delete()
    else:
        return 'False'

    return 'True'


@vs_association.route('/project/<string:id>', methods=['PUT'])
def project_update(id):
    if request.is_json:
        args_data = request.get_json()
    else:
        args_data = json.loads(request.data)

    project = VSProject.query.filter_by(id=id).first_or_404()
    if project:
        project.update(**args_data)
    else:
        return 'False'

    return 'True'


@vs_association.route('/project/<string:id>/user', methods=['POST'])
def project_user_create(id):
    if request.is_json:
        args_data = request.get_json()
    else:
        args_data = json.loads(request.data)

    project = VSProject.query.filter_by(id=id).first_or_404()
    if project:
        # 中间表添加了关联记录,同时user表也会生成一条记录,
        project.users.append(VSUser(**args_data))
        project.save()

    return jsonify(project.to_dict())

