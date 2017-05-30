import inventory.model as models
from inventory.service.base import BasedService


class Inventory(BasedService):
    def __init__(self):
        self._raw_ivt = '{}'

    def reload(self):
        # TODO: construct the ansible inventory of type json from DB
        pass

    def start(self):
        pass

    def stop(self):
        pass
