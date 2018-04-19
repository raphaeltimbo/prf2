"""Module to define impeller class."""
import numpy as np
from collections import UserList
from prf2 import check_units


class Impeller(UserList):
    """Impeller class.

    Impeller instance is initialized with the list of points.
    The created instance will hold the dimensional points used in instantiation
    non dimensional points generated from the given dimensional points and
    another list of dimensional points based on current suction condition.
    Curves will be generated from points close in similarity.

    """
    @check_units
    def __init__(self, points, b=None, D=None):
        super().__init__(points)

        self.b = b
        self.D = D
        self.points = points

        self._suc = None

    @property
    def suc(self):
        return self._suc

    @suc.setter
    def suc(self, new_suc):
        self._suc = new_suc

    def tip_speed(self, point):
        """Impeller tip speed."""
        speed = point.speed

        u = speed * self.D / 2

        return u

    def phi(self, point):
        """Flow coefficient."""
        flow_v = point.flow_v

        u = self.tip_speed(point)

        phi = (flow_v * 4 /
               (np.pi * self.D ** 2 * u))

        return phi.to('dimensionless')

    def psi(self, point):
        """Head coefficient."""
        head = point.head

        u = self.tip_speed(point)

        psi = 2 * head / u ** 2

        return psi.to('dimensionless')

    def mach(self, point):
        """Mach number."""
        suc = point.suc

        u = self.tip_speed(point)
        a = suc.speed_sound()

        mach = u / a

        return mach.to('dimensionless')

    def s(self, point):
        """Work input factor."""
        pass


