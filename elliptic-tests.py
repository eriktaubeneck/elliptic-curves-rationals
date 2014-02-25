from elliptic import *
from fractions import Fraction as frac
from unittest import TestCase

C = EllipticCurve(a=frac(-2), b=frac(4))
P = Point(C, frac(3), frac(5))
Q = Point(C, frac(-2), frac(0))
zero = Ideal(C)

class EllipticTestCase(TestCase):
    def test_addition(self):
        self.assertEquals(P + Q, Point(C,frac(0,1),frac(-2,1)))

    def test_addition_commutivity(self):
        self.assertEquals(Q + P, P + Q)

    def test_multiplicatoin(self):
        self.assertEquals(5*P, P+P+P+P+P)

    def test_composition(self):
        self.assertEquals(Q - 3*P, Point(C, frac(240,1), frac(3718,1)))

    def test_equals(self):
        self.assertTrue(zero == Ideal(C))
        self.assertTrue(P == Point(C, frac(3), frac(5)))
        self.assertTrue(Q == Point(C, frac(-2), frac(0)))
        self.assertFalse(zero == P)
        self.assertFalse(zero == Q)
        self.assertFalse(P == zero)
        self.assertFalse(P == Q)
        self.assertFalse(Q == zero)
        self.assertFalse(Q == P)

    def test_less_than(self):
        self.assertFalse(zero < zero)
        self.assertFalse(P < zero)
        self.assertTrue(zero < P)

        self.assertFalse(Q < Q)
        self.assertFalse(Q < zero)
        self.assertTrue(zero < Q)

        self.assertFalse(P < P)
        self.assertFalse(P < Q)
        self.assertTrue(Q < P)

    def test_greater_than(self):
        self.assertFalse(zero > zero)
        self.assertFalse(zero > P)
        self.assertTrue(P > zero)

        self.assertFalse(Q > Q)
        self.assertFalse(zero > Q)
        self.assertTrue(Q > zero)

        self.assertFalse(P > P)
        self.assertFalse(Q > P)
        self.assertTrue(P > Q)

    def test_less_than_or_equal(self):
        self.assertTrue(zero <= zero)
        self.assertFalse(P <= zero)
        self.assertTrue(zero <= P)

        self.assertTrue(Q <= Q)
        self.assertFalse(Q <= zero)
        self.assertTrue(zero <= Q)

        self.assertTrue(P <= P)
        self.assertFalse(P <= Q)
        self.assertTrue(Q <= P)

    def test_greater_than(self):
        self.assertTrue(zero >= zero)
        self.assertFalse(zero >= P)
        self.assertTrue(P >= zero)

        self.assertTrue(Q >= Q)
        self.assertFalse(zero >= Q)
        self.assertTrue(Q >= zero)

        self.assertTrue(P >= P)
        self.assertFalse(Q >= P)
        self.assertTrue(P >= Q)

    def test_points_on_different_curves(self):
        C1 = EllipticCurve(3,4)
        C2 = EllipticCurve(5,4)
        self.assertFalse(C1 == C2)
        P1 = Point(C1,frac(0), frac(2))
        P2 = Point(C2,frac(0), frac(2))

        with self.assertRaises(Exception):
            #I don't think it makes sense to compare points on different curves
            #but correct me if I'm wrong.
            P1 == P2

        with self.assertRaises(Exception):
            P1 < P2

        with self.assertRaises(Exception):
            P1 > P2

        with self.assertRaises(Exception):
            P1 <= P2

        with self.assertRaises(Exception):
            P1 >= P2

        with self.assertRaises(Exception):
            P1 + P2

        with self.assertRaises(Exception):
            P1 - P2
