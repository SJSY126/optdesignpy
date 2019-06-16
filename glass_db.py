import yaml
import os
import numpy as np

cwd = os.getcwd()
referencePath = cwd + '/database/data'


def getGlassFilePath(shelf, book, page):
    glass_catalog = book
    filename = page + '.yml'
    for root, subFolders, files in os.walk(referencePath, topdown=True):
        if root.endswith(glass_catalog):
            break
    for f in files:
        if f == filename:
            filepath = os.path.join(referencePath, root, filename)
            break
    return filepath


class Glass:
    def __init__(self, lass_data_filepath):
        with open(glass_data_filepath, 'r') as f:
            glass_data = yaml.safe_load(f)

        for data in glass_data['DATA']:
            if data['type'].split()[0] == 'formula':
                self.formula_type = int(data['type'].split()[1])
                self.wavelangth_range_min = float(
                    data['wavelength_range'].split()[0])
                self.wavelangth_range_max = float(
                    data['wavelength_range'].split()[1])
                self.coefficients = [float(s)
                                     for s in data['coefficients'].split()]
                break
            else:
                print("Can not load glass data.")

    def getRefractiveIndex(self, wavelength):
        wavelength /= 1000
        if self.wavelangth_range_min <= wavelength and wavelength <= self.wavelangth_range_max:
            formula_type = self.formula_type
            coefficients = self.coefficients
            if formula_type == 1:  # database/doc/Dispersion formulas.pdf
                n2 = 1 + coefficients[0]

                def x(wavelength, c1, c2):
                    return c1 * (wavelength ** 2) / (wavelength ** 2 - c2 ** 2)
                for i in range(1, len(coefficients), 2):
                    n2 += x(wavelength, coefficients[i], coefficients[i+1])
                n = np.sqrt(n2)
            if formula_type == 2:  # database/doc/Dispersion formulas.pdf
                n2 = 1 + coefficients[0]

                def x(wavelength, c1, c2):
                    return c1 * (wavelength ** 2) / (wavelength ** 2 - c2)
                for i in range(1, len(coefficients), 2):
                    n2 += x(wavelength, coefficients[i], coefficients[i+1])
                n = np.sqrt(n2)
        return n


glass_maker = 'ohara'
glass_name = 'S-BSM18'

glass_index = {}

wavelength_list = [546.07, 435.835, 656.27]
glass_data_filepath = getGlassFilePath('glass', glass_maker, glass_name)
glass = Glass(glass_data_filepath)
for wavelength in wavelength_list:
    n = glass.getRefractiveIndex(wavelength)
    glass_index[wavelength] = np.round(n, 5)

print(glass_index)
