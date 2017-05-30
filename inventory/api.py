from flask import Blueprint, request


__all__ = [
    'api'
]


api = Blueprint('api', __name__)


@api.record_once
def init():
    pass


@api.route('/namespace/<namespace>')
def dump_inventory(namespace):
    pass


@api.route('/groups/create')
def create_group():
    pass


@api.route('/groups/update')
def update_group():
    pass


@api.route('/groups/list')
def list_group():
    pass


@api.route('/hosts/upsert')
def upsert_hosts():
    pass


@api.route('/hosts/get/<host>')
def get_host(host):
    pass
