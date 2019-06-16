class Surface():
    def __init__(self, wavelength_list, number, radius, thickness, glass):
        self.wavelength_list = wavelength_list
        self.number = number
        self.radius = radius
        self.glass = glass
        self.thickness = thickness
        self.indexlist = {wavelength_list[0]: 1.5}

    def add(self, number, radius, thickness, glass):
        New_Surface = Surface(wavelength_list=self.wavelength_list, number=number, radius=radius,
                              thickness=thickness, glass=glass)
        self.surface_list.append(New_Surface)
