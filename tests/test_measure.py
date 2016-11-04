import unittest
from unittest import mock

from tim.measure import Measure


class TestMeasure(unittest.TestCase):

    def setUp(self):
        self.times = list(range(1, 9))

    def stub_time(self):
        return self.times.pop(0)

    def test_measure_works_as_context_manager(self):
        with mock.patch('time.time', self.stub_time):
            m = Measure('Test {}')
            with m:
                sum([4]*1000)

        self.assertEqual(len(m.times), 1)
        self.assertEqual(m.times[0], 1)

    def test_measure_works_as_a_decorator(self):
        with mock.patch('time.time', self.stub_time):
            m = Measure('Test {}')

            @m
            def test_func():
                return sum([4]*1000)

            test_func()

        self.assertEqual(len(m.times), 1)
        self.assertEqual(m.times[0], 1)

