#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Implementation of Cipolla's algorithm from rosettacode.org
# modified to work with Python 3


# Converts n to base b as a list of integers between 0 and b-1
# Most-significant digit on the left
def convertToBase(n, b, output, add_output, k=100):
    if n < 2:
        add_output(output, ("branch 4T", (0 if n - 2 < 0 else n - 2 + k)))
        return [n]
    temp = n
    ans = []
    while temp != 0:
        ans = [temp % b] + ans
        temp /= b
    add_output(output, ("branch 4F", (0 if n - 2 < 0 else n - 2 + k)))
    return ans


# Helper funcion called from cipolla
def cipollaMult(a, b, c, d, w, p):
    return ((a * c + b * d * w) % p, (a * d + b * c) % p)


# Takes integer n and odd prime p
# Returns both square roots of n modulo p as a pair (a,b)
# Returns () if no root
def cipolla(n, p, output, add_output, k=100):
    n %= p
    if n == 0 or n == 1:
        add_output(output, ("branch 1T", (0 if abs(n - 1) == 0 else abs(n - 1) + k)))
        return (n, -n % p)
    phi = p - 1
    add_output(output, ("branch 1F", (0 if abs(n - 1) == 0 else abs(n - 1) + k)))
    if pow(int(n), int(phi / 2), int(p)) != 1:
        add_output(
            output,
            (
                "branch 2T",
                (0 if abs(pow(int(n), int(phi / 2), int(p)) - 1) != 0 else k),
            ),
        )
        return ()
    add_output(
        output,
        ("branch 2F", (0 if abs(pow(int(n), int(phi / 2), int(p)) - 1) != 0 else k)),
    )
    if p % 4 == 3:
        ans = pow(int(n), int((p + 1) / 4), int(p))
        add_output(
            output, ("branch 3T", (0 if abs(p % 4 - 3) == 0 else abs(p % 4 - 3) + k))
        )
        return (ans, -ans % p)
    aa = 0
    for i in range(1, p):
        temp = pow(int((i * i - n) % p), int(phi / 2), int(p))
        if temp == phi:
            aa = i
            break
    exponent = convertToBase((p + 1) / 2, 2, output, add_output, k=100)
    x1 = (aa, 1)
    x2 = cipollaMult(*x1, *x1, aa * aa - n, p)
    for i in range(1, len(exponent)):
        if exponent[i] == 0:
            x2 = cipollaMult(*x2, *x1, aa * aa - n, p)
            x1 = cipollaMult(*x1, *x1, aa * aa - n, p)
        else:
            x1 = cipollaMult(*x1, *x2, aa * aa - n, p)
            x2 = cipollaMult(*x2, *x2, aa * aa - n, p)
    add_output(
        output, ("branch 3F", (0 if abs(p % 4 - 3) == 0 else abs(p % 4 - 3) + k))
    )
    return (x1[0], -x1[0] % p)


# print(f"Roots of 2 mod 7: {cipolla(2, 7)}")
# print(f"Roots of 8218 mod 10007: {cipolla(8218, 10007)}")
# print(f"Roots of 56 mod 101: {cipolla(56, 101)}")
# print(f"Roots of 1 mod 11: {cipolla(1, 11)}")
# print(f"Roots of 8219 mod 10007: {cipolla(8219, 10007)}")
