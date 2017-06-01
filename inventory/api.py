import json

from flask import Blueprint, request


__all__ = [
    'api'
]


'''
Convention:
    1. all the method must has a return value
'''


api = Blueprint('api', __name__)


def rsp_json(func):
    def internal(*args, **kwargs):
        wrapper = dict()
        try:
            rsp = func(*args, **kwargs)
            wrapper['code'] = 0
            wrapper['data'] = rsp
        except Exception as e:
            wrapper['code'] = 1
            wrapper['error'] = e.message
        return json.dumps(wrapper)
    return internal


@api.record_once
def init():
    pass


@api.route('/namespace/<namespace>')
@rsp_json
def dump_inventory(namespace):
    return True


@api.route('/groups/create')
@rsp_json
def create_group():
    payload = {
        'name': 'group_name',
        'hosts': ['h1', 'h2'],
        'variables': {
        },
        'children': ['g1', 'g2']
    }
    name = payload['name']
    if name == 'all':
        pass


@api.route('/groups/update')
@rsp_json
def update_group():
    return True


@api.route('/groups/list')
@rsp_json
def list_group():
    return True


@api.route('/hosts/upsert')
@rsp_json
def upsert_hosts():
    return True


@api.route('/hosts/get/<host>')
@rsp_json
def get_host(host):
    return True
