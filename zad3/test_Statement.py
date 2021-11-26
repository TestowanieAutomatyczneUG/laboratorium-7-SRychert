import unittest

from Statement import statement

invoice = {
    "customer": "BigCo",
    "performances": [
        {
            "playID": "hamlet",
            "audience": 55
        },
        {
            "playID": "as-like",
            "audience": 35
        },
        {
            "playID": "othello",
            "audience": 40
        }
    ]
}

plays = {
    "hamlet": {"name": "Hamlet", "type": "tragedy"},
    "as-like": {"name": "As You Like It", "type": "comedy"},
    "othello": {"name": "Othello", "type": "tragedy"}
}


class TestStatement(unittest.TestCase):
    def test_all_plays(self):
        self.assertEqual(statement(invoice, plays),
                         "Statement for BigCo\n Hamlet: $650.00 (55 seats)\n As You Like It: $580.00 (35 seats)\n Othello: $500.00 (40 seats)\nAmount owed is $1,730.00\nYou earned 47 credits\n")

    def test_missing_plays(self):
        self.assertRaises(KeyError, statement, invoice, {})

    def test_invalid_play(self):
        self.assertRaises(ValueError, statement, invoice, {"hamlet": {"name": "Very nice play", "type": "somethingsomething"}})

    def test_small_audiences(self):
        self.assertEqual(statement({
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 4
                },
                {
                    "playID": "as-like",
                    "audience": 5
                },
                {
                    "playID": "othello",
                    "audience": 2
                }
            ]}, plays),
            "Statement for BigCo\n Hamlet: $400.00 (4 seats)\n As You Like It: $315.00 (5 seats)\n Othello: $400.00 (2 seats)\nAmount owed is $1,115.00\nYou earned 1 credits\n")
