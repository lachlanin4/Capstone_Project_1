#!/usr/bin/env python
"""
This file defines a class that encapsulates all the features
of a quiz game
"""


class Game:
    """
    This class encapsulates a quiz game session, it is per player and could have many
    options. As a minimum the game will always contain a number of rounds of
    various levels of difficulty, as the player answers questions correctly
    this class will keep a track of the score as each round is completed.
    The user should be able to end the game, but its not clear if the user
    should be able to "save" their status and perhaps come back to it later.
    Since multiple players can play on the same platform it would be nice to
    keep a record of scores and have a league table. To do this something in
    this class needs to pass the result back for a given player once they have
    finished.
    """

    def _init__(self, player=""):
        # At the minute just the players name is provided, but more might be needed ...

        # Add some initisation here
        self._player = player
