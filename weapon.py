from math import sqrt


class NoAmmunitionError(Exception):
    pass
class OutOfRangeError(Exception):
    pass

class Weapon:
    def __init__(self,ammunitions,range) -> None:
        self.ammunations = ammunitions
        self.range = range
    def fire_at(self,x,y,z):
        if self.ammunations == 0:
            raise NoAmmunitionError
        self.ammunations -= 1
        if sqrt(x**2 + y**2) > self.range:
            raise OutOfRangeError
        

class LMAS(Weapon):
    """Lance missile antisurface"""
    def __init__(self) -> None:
        super().__init__(40, 30)
    def fire_at(self,x, y, z):
        super().fire_at(x,y,z)
        if z != 0:
            raise OutOfRangeError

class LMAR(Weapon):
    """Lance missile anti-air"""
    def __init__(self) -> None:
        super().__init__(50, 40)
    def fire_at(self,x, y,z):
        super().fire_at(x,y,z)
        if z <= 0:
            raise OutOfRangeError

class LT(Weapon):
    """Lance torpilles"""
    def __init__(self) -> None:
        super().__init__(15, 20)
    def fire_at(self,x, y,z):
        super().fire_at(x,y,z)
        if z > 0:
            raise OutOfRangeError


if __name__ == "__main__":
    LMAS = LMAS()
    LMAR = LMAR()
    LT = LT()
    LMAS.fire_at(0,0,0)
    assert LMAS.ammunations == 39
    try:
        LMAS.fire_at(0,0,1)
    except:
        assert LMAS.ammunations == 38
    LMAR.fire_at(0,0,1)
    assert LMAR.ammunations == 49
    try:
        LMAR.fire_at(0,0,0)
    except:
        assert LMAR.ammunations == 48
    LT.fire_at(0,0,0)
    assert LT.ammunations == 14
    LT.fire_at(0,0,-1)
    assert LT.ammunations == 13
    try:
        LT.fire_at(0,0,1)
    except:
        assert LT.ammunations == 12
