from surface import Surface
from paraxial_approximation import ABCD_cal


class Lens():
    surface_list = []

    def __init__(self):
        self.Fno = []
        self.wavelength_list = []

    def add_surface(self, number, radius, thickness, glass):
        Surface.add(self, number, radius, thickness, glass)

    def paraxial_approximation_cal(self):
        self.A, self.B, self.C, self.D = ABCD_cal(self, 0, 1)


if __name__ == "__main__":
    test_lens = Lens()
    test_lens.Fno = 1.4
    test_lens.wavelength_list = [587.562]

    test_lens.add_surface(number=1, radius=100, thickness=1, glass='BK7')
    test_lens.add_surface(number=2, radius=-100, thickness=1, glass='1')

    test_lens.paraxial_approximation_cal()
