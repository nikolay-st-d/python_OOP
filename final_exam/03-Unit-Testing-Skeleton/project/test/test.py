import unittest
from collections import deque

from project.railway_station import RailwayStation


class TestRailwayStation(unittest.TestCase):

    def setUp(self):
        self.station = RailwayStation("Test Station")

    def test_init_valid_station_name(self):
        self.assertEqual(self.station.name, "Test Station")
        self.assertEqual(self.station.arrival_trains, deque([]))
        self.assertEqual(self.station.departure_trains, deque([]))

    def test_init_station_name_less_than_3_chars(self):
        with self.assertRaises(ValueError) as err:
            self.station.name = "**"
        self.assertEqual("Name should be more than 3 symbols!", str(err.exception))

    def test_init_station_name_3_chars(self):
        with self.assertRaises(ValueError) as err:
            self.station.name = "***"
        self.assertEqual("Name should be more than 3 symbols!", str(err.exception))

    def test_new_arrival_on_board(self):
        self.assertEqual(self.station.arrival_trains, deque([]))
        self.station.new_arrival_on_board("Train 1")
        self.assertEqual(self.station.arrival_trains, deque(["Train 1"]))

    def test_train_has_arrived(self):
        self.station.new_arrival_on_board("Test Train")
        result = self.station.train_has_arrived("Test Train")
        self.assertEqual(result, "Test Train is on the platform and will leave in 5 minutes.")
        self.assertEqual(self.station.arrival_trains, deque([]))
        self.assertEqual(self.station.departure_trains, deque(["Test Train"]))

    def test_train_has_arrived_with_other_trains(self):
        self.station.new_arrival_on_board("Train 1")
        self.station.new_arrival_on_board("Train 2")
        result = self.station.train_has_arrived("Train 2")
        self.assertEqual(result, "There are other trains to arrive before Train 2.")
        self.assertEqual(self.station.arrival_trains, deque(["Train 1", "Train 2"]))
        self.assertEqual(self.station.departure_trains, deque([]))

    def test_train_has_left(self):
        self.station.new_arrival_on_board("Test Train")
        self.station.train_has_arrived("Test Train")
        result = self.station.train_has_left("Test Train")
        self.assertTrue(result)
        self.assertEqual(self.station.arrival_trains, deque([]))
        self.assertEqual(self.station.departure_trains, deque([]))

    def test_train_has_left_nonexistent_train(self):
        result = self.station.train_has_left("Nonexistent Train")
        self.assertFalse(result)
        self.assertEqual(self.station.arrival_trains, deque([]))
        self.assertEqual(self.station.departure_trains, deque([]))


if __name__ == '__main__':
    unittest.main()
