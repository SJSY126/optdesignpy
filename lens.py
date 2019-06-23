from surface import Surface
import paraxial_approximation


class Lens():
    surface_list = []

    def __init__(self):
        self.Fno = []
        self.wavelength_list = []

    def add_surface(self, number, radius, thickness, glass):
        Surface.add(self, number, radius, thickness, glass)

    def paraxial_amount(self):
        self.focal_length = paraxial_approximation.get_focal_length(
            self, 1, len(self.surface_list)-1)
        self.total_tarck = paraxial_approximation.get_total_track(
            self, 1, len(self.surface_list)-1)
