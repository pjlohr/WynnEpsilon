#!/usr/bin/env python3
"""tests for wynnpi.py"""

from subprocess import getstatusoutput
import re

prg = "./wynnpi.py"


# --------------------------------------------------
def test_usage():
    """usage"""
    rv1, out1 = getstatusoutput('{} {}'.format(prg, '-h'))
    assert rv1 == 0
    assert re.match("usage", out1, re.IGNORECASE)


# --------------------------------------------------
def test_bad_input():
    """bad_input"""
    for n in [0, 23]:
        rv, out = getstatusoutput('{} -n {}'.format(prg, n))
        assert rv > 0
        assert out.strip(
        ) == '-n Number of terms "{}" must be between 1 and 24, inclusive'.format(n)


# --------------------------------------------------
def test_good_input():
    rv, out = getstatusoutput('{}'.format(prg))

    assert rv == 0
    assert out == '{}{}{}{}'.format(
        '\nSeries approximation for π (10 terms):      3.041839618929403\n',
        'Wynn Epsilon accelerated result (10 terms): 3.141593311879928\n',
        'Actual Value:                               3.141592653589793\n',
        'Relative Error:                             2.0954025804051612e-07\n')
