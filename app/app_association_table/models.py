#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime

from app.database import db, CRUDMixin

#

project_user_association_table = db.Table(
    'project_user_association',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('project_id', db.Integer, db.ForeignKey('tbl_sqlalchemy_project.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('tbl_sqlalchemy_user.id')))


class VSProject(CRUDMixin, db.Model):
    """"
    项目模型
    """
    __tablename__ = 'tbl_sqlalchemy_project'

    # 项目访问权限  open: 公开  private: 私有
    access = db.Column(db.String(20), default='open')
    # 创建时间
    created_ts = db.Column(
        db.DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )
    # 更新时间
    updated_ts = db.Column(
        db.DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )
    # 激活状态
    active = db.Column(db.Boolean(), default=True)
    # many to many
    users = db.relationship("VSUser",
                            # 默认userlist=false为一对多关系,userlist=true为多对多关系
                            uselist=True,
                            secondary=project_user_association_table,
                            backref="projects",
                            # 关联的user表记录也会删除
                            cascade="save-update, merge, delete")

    def __init__(self, **kwargs):
        super(VSProject, self).__init__(**kwargs)


class VSUser(CRUDMixin, db.Model):
    """"
    账户模型
    """
    __tablename__ = 'tbl_sqlalchemy_user'

    account = db.Column(db.String(56))
    created_ts = db.Column(
        db.DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )
    updated_ts = db.Column(
        db.DateTime(timezone=True),
        default=datetime.datetime.utcnow
    )
    active = db.Column(db.Boolean(), default=True)

    def __init__(self, **kwargs):
        super(VSUser, self).__init__(**kwargs)


class VSBlog(CRUDMixin, db.Model):
    __tablename__ = 'tbl_sqlalchemy_blog'
    title = db.Column(db.String(128))

    commits = db.relationship("VScommit", backref="blog")

    def __init__(self, **kwargs):
        super(VSBlog, self).__init__(**kwargs)


class VSCommit(CRUDMixin, db.Model):
    __tablename__ = 'tbl_sqlalchemy_commit'
    content = db.Column(db.String(256))
    blog_id = db.Column(db.Integer, db.ForeignKey('tbl_sqlalchemy_blog.id'))

    def __init__(self, **kwargs):
        super(VSCommit, self).__init__(**kwargs)
