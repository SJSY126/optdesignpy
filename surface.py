import glass_db


class Surface():
    def __init__(self, wavelength_list, number, radius, thickness, glass):
        self.wavelength_list = wavelength_list
        self.number = number
        self.radius = radius
        self.glass = glass_db.Glass(glass)
        self.thickness = thickness
        self.indexlist = {
            wavelength_list[0]: self.glass.getRefractiveIndex(wavelength_list[0])}

    def add(self, number, radius, thickness, glass):
        New_Surface = Surface(wavelength_list=self.wavelength_list,
                              number=number, radius=radius, thickness=thickness, glass=glass)
        self.surface_list.append(New_Surface)
