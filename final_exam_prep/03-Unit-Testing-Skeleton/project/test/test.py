import unittest

from project.trip import Trip


class TextTrip(unittest.TestCase):

    def setUp(self):
        self.t1f = Trip(10000, 1, False)
        self.t2t = Trip(10000, 2, True)
        self.t2f = Trip(10000, 2, False)

    def test_trip_init(self):
        self.assertEqual(10000, self.t1f.budget)
        self.assertEqual(1, self.t1f.travelers)
        self.assertFalse(self.t1f.is_family)
        self.assertEqual({}, self.t1f.booked_destinations_paid_amounts)

    def test_setter_travelers(self):
        with self.assertRaises(ValueError) as err:
            self.t1f.travelers = 0
        self.assertEqual('At least one traveler is required!', str(err.exception))

    def test_setter_is_family(self):
        self.t1f.is_family = True
        self.assertFalse(self.t1f.is_family, False)
        self.assertTrue(self.t2t.is_family)

    def test_book_a_trip_invalid_destination(self):
        self.assertEqual('This destination is not in our offers, please choose a new one!',
                         self.t1f.book_a_trip('Moon'))

    def test_book_a_trip_budget_not_enough(self):
        self.assertEqual('Your budget is not enough!', self.t2t.book_a_trip('New Zealand'))

    def test_book_a_trip_budget_enough_with_family_discount(self):
        self.t2t.budget = 100_000
        result = self.t2t.book_a_trip('New Zealand')
        self.assertEqual('Successfully booked destination New Zealand! Your budget left is 86500.00', result)

    def test_book_a_trip_budget_enough_no_family_discount(self):
        self.t2f.budget = 100_000
        result = self.t2f.book_a_trip('New Zealand')
        self.assertEqual('Successfully booked destination New Zealand! Your budget left is 85000.00', result)

    def test_booking_status_no_destinations(self):
        self.assertEqual('No bookings yet. Budget: 10000.00', self.t1f.booking_status())

    def test_booking_status_with_booked_destinations(self):
        self.t2f.book_a_trip('Bulgaria')
        expected = """Booked Destination: Bulgaria
Paid Amount: 1000.00
Number of Travelers: 2
Budget Left: 9000.00"""
        self.assertEqual(expected, self.t2f.booking_status())


if __name__ == "__main__":
    unittest.main()
