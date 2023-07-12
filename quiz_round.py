#!/usr/bin/env python
"""
This file defines a class that encapsulates all the features
of a quiz round.
"""


class Round:
    '''
    This class encapsulates a quiz round, it allows rounds to be
    created, questions to be associated, difficulty levels to be
    associated and questions to be asked. The round will have a
    name to begin with but it might change.
    '''

    def _init__(self, name):
        # Add some initisation here
        self.name = name
