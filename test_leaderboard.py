# -*- coding: utf-8 -*-
import json
import unittest
import random
from gradescope_utils.autograder_utils.decorators import leaderboard


class TestLeaderboard(unittest.TestCase):
    results = None

    def setUp(self):
        try:
            with open('/autograder/results/results.json') as json_file:
                self.results = json.load(json_file)
                print(self.results)
        except:
            print("Could not load results.json file.")

    @leaderboard("high score")
    def test_leaderboard(self, set_leaderboard_value=None):
        """Sets a leaderboard value"""
        set_leaderboard_value(random.randint(0, 10))

    @leaderboard("accuracy")
    def test_leaderboard_float(self, set_leaderboard_value=None):
        """Sets a leaderboard value"""
        set_leaderboard_value(round(random.uniform(50, 100), 2))

    @leaderboard("stars")
    def test_string(self, set_leaderboard_value=None):
        """Sets a leaderboard value"""
        set_leaderboard_value("🌟" * random.randint(0, 10))

    @leaderboard("time", "asc")
    def test_time_executed(self, set_leaderboard_value=None):
        """Sets a leaderboard value that's sorted ascending (lower is better)"""
        set_leaderboard_value(round(random.gauss(7, 3), 2))
