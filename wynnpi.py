#!/usr/bin/env python3
"""
Author : patricklohr
Date   : 2019-04-16
Purpose: Demonstrate Wynn Epsilon Convergence Acceleration of the Gregory-Leibniz series
"""

import argparse
import sys
import numpy as np


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Wynn Epsilon for Gregory-Leibniz series',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-n',
        '--numterms',
        help='Number of series terms (1<=n<=22)',
        metavar='INT',
        type=int,
        default=10)

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


def wynnepsilon(sn, r):
    """Perform Wynn Epsilon Convergence Algorithm"""
    r = int(r)
    n = 2 * r + 1
    e = np.zeros(shape=(n + 1, n + 1))

    for i in range(1, n + 1):
        e[i, 1] = sn[i - 1]

    for i in range(3, n + 2):
        for j in range(3, i + 1):
            e[i - 1, j - 1] = e[i - 2, j - 3] + 1 / (e[i - 1, j - 2] - e[i - 2, j - 2])

    er = e[:, 1:n + 1:2]
    return er


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    n = args.numterms
    ps = []
    s = 0

    if not 1 <= n <= 22:
        die('-n Number of terms "{}" must be between 1 and 24, inclusive'.format(n))

    for k in range(0, n):
        term = 4 * np.power(-1, k) / (2 * k + 1)
        s += term
        ps.append(s)

    er = wynnepsilon(ps, np.floor((n - 1) / 2))
    last = er[-1, -1]
    rel = abs(last - np.pi) / np.pi

    print('\nSeries approximation for π ({:02d} terms):      {:0.15f}'.format(n, s))
    print('Wynn Epsilon accelerated result ({:02d} terms): {:0.15f}'.format(n, last))
    print('Actual Value: {:47}'.format(np.pi))
    print('Relative Error: {:50}\n'.format(rel))



# --------------------------------------------------
if __name__ == '__main__':
    main()
