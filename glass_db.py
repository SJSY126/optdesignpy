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
    def __init__(self, glass_name):
        if glass_name == '1':
            glass_name = 'air'
            self.glass_name = glass_name
        else:
            glass_data_filepath = getGlassFilePath(
                'glass', 'ohara', glass_name)
            self.glass_name = glass_name
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
        if self.glass_name == 'air':
            return 1
        else:
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
