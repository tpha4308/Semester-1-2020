"""
Alien Invasion
--------------
Your job is to help write the required algorithms to perform these tasks and
save the human race, before all hope is lost! Good luck!
The fate of humanity rests on your shoulders...
--------------

This module will contain all functions that you must implement. It will serve
as the main file to be created during testing.

Usage:
    - Contains functions that will be implemented to stop the Alien Invasion!
"""

import random

class AlienInvasion:
    """
    Alien Invasion Class
    Contains three functions to be implemented:

    1. `is_sorted(A)` - returns whether the array is sorted.
    2. `count_markers(A, c)` - returns the number of indices `i` such that
                                | A[i] - i | <= c.
    3. `break_control(A, c)` - returns a "random" index that satisfies
                               |A[i] - i | <= c.
    """

    @staticmethod
    def is_sorted(A: list) -> bool:
        """
        Checks whether the given list of genetic code is sorted in
        increasing order.

        If the array (A) is None, return None.
        :param A: A list of indices.
        :return: True if sorted, else False.
        """

        if A is None:
            return None

        i = 1
        n = len(A)
        while i < n:
            if A[i] < A[i - 1]:
                return False
            i += 1
        return True

    def small(self, A, l, h, c, min_value):
        if l >= h:
            #if current value satisfy, return l
            #if not, return min
            if abs(A[l] - l) <= c:
                return l
            else:
                return min_value

        mid = int((l+h)/2) # this is the value
        mid_value = A[mid]
        val = abs(mid_value - mid)

        if val <= c: #satisfy the condition
            min_value = mid
            return self.small(A, l, mid-1, c, min_value)

        else:
            value = mid_value - mid
            if value > 0:
                return self.small(A, l, mid-1, c, min_value)
            elif value < 0:
                return self.small(A, mid+1, h, c, min_value)

    def large(self, A, l, h, c, max_value):
        if l >= h:
            if abs(A[l] - l) <= c:
                return l
            else:
                return max_value

        mid = int((l + h) / 2)  # this is the value
        mid_value = A[mid]
        val = abs(mid_value - mid)

        if val <= c:  # satisfy the condition
            max_value = mid
            return self.large(A, mid+1, h, c, max_value)
        else:
            value = mid_value - mid
            if value > 0:
                return self.large(A, l, mid - 1, c, max_value)
            elif value < 0:
                return self.large(A, mid + 1, h, c, max_value)

    def min_max(self, A, c):
        low, high = 0, len(A) - 1
        min_index = self.small(A, low, high, c, None)
        max_index = self.large(A, low, high, c, None)
        return min_index, max_index

    def count_markers(self, A: list, c: int) -> int:
        if A is None:
            return None
        if len(A) == 0:
            return 0

        min_, max_ = self.min_max(A, c)

        if min_ is None or max_ is None:
            return 0
        return max_ - min_ + 1

    def break_control(self, A: list, c: int) -> int:

        if A is None or len(A) == 0:
            return None

        min_, max_ = self.min_max(A, c)
        if min_ is None or max_ is None:
            return None
        return random.randint(min_, max_)