from surface import Surface


class Lens():
    surface_list = []

    def __init__(self):
        self.Fno = []
        self.wavelength_list = []

    def add_surface(self, number, radius, thickness, glass):
        Surface.add(self, number, radius, thickness, glass)
