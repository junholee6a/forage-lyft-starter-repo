import unittest

from engines.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced_when_warning_light_is_on(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced_when_warning_light_is_off(self):
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()