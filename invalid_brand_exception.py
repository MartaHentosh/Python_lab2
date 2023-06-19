"""
This module provides invalid brand exception
"""


class InvalidBrandException(Exception):
    """
    Exception appears when brand of fridge is incorrect
    """

    def __init__(self, message="Invalid brand"):
        self.message = message
        super().__init__(self.message)
