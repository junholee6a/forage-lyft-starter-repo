from abc import ABC

from engines.engine import Engine


class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_is_on):
        self._warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self._warning_light_is_on:
            return True
        else:
            return False
