from flask import Blueprint, request


__all__ = [
    'api'
]


api = Blueprint('api', __name__)


@api.record_once
def init():
    pass


@api.route('/inventory/<namespace>')
def dump_inventory(namespace):
    pass
