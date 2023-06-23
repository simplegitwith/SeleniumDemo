

import pytest


class Test_py02:
    def test_sum_005(self):
        a = 2
        b = 8
        sum = a + b
        print("sum -- >" + str(sum))
        if sum == 10:
            assert True
        else:
            assert False

