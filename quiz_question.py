#!/usr/bin/env python
"""
This file defines a class that encapsulates all the features
of a question.
"""


class Question:
    """
    This class encapsulates a quiz question, it defines the difficulty
    of the question, the question,tself  what the correct answer is and what
    possible plausible wrong answers are. The class could also define
    how the question could be asked and deal with other things limiting
    the question answering to a given period for example.
    """

    def _init__(self, question="", correct_answer="", wrong_answers=[], difficulty=1):
        # Add some initisation here
        self._question = question
        self._correct_answer = correct_answer
        self._wrong_answers = wrong_answers
        self._difficulty = difficulty
