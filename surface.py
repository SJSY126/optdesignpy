class Surface():
    def __init__(self, number, radius, thickness, glass):
        self.number = number
        self.radius = radius
        self.glass = glass
        self.thickness = thickness

    def add(self, number, radius, thickness, glass):
        New_Surface = Surface(number=number, radius=radius,
                              thickness=thickness, glass=glass)
        self.surface_list.append(New_Surface)
