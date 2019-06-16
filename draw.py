import numpy as np
import matplotlib.pyplot as plt

from surface import Surface
from lens import Lens


def draw_surf(r, d, x0):
    surf_spot = []
    y = np.linspace(0, d/2, 20)
    for y_ in y:
        if r > 0:
            x = r - np.sqrt(r**2-y_**2)
        else:
            x = r + np.sqrt(r**2-y_**2)
        surf_spot.append(x+x0)

    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.plot(surf_spot, y, color='000000')
    ax.plot(surf_spot, -y, color='000000')


if __name__ == "__main__":
    test_lens = Lens()
    test_lens.Fno = 1.4
    test_lens.wavelength_list = 587.562

    test_lens.add_surface(number=1, radius=10, thickness=1, glass='BK7')

    draw_surf(test_lens.surface_list[0].radius,
              10, 0)
    plt.show()
