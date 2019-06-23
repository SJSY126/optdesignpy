import matplotlib.pyplot as plt

import lens
import draw

sample_lens = lens.Lens()
sample_lens.Fno = 1.4
sample_lens.wavelength_list = [587.60, 486.10, 656.30]

sample_lens.add_surface(number=0, radius=10000000000, thickness=1, glass='1')
sample_lens.add_surface(number=1, radius=4.25, thickness=0.7, glass='S-BSM16')
sample_lens.add_surface(number=2, radius=-31.73, thickness=1.2, glass='1')
sample_lens.add_surface(number=3, radius=-4.05, thickness=0.3, glass='S-TIM2')
sample_lens.add_surface(number=4, radius=3.86, thickness=1.2, glass='1')
sample_lens.add_surface(number=5, radius=28.25, thickness=0.7, glass='S-BSM16')
sample_lens.add_surface(number=6, radius=-3.5, thickness=8.59, glass='1')
sample_lens.add_surface(number=7, radius=100000000, thickness=0, glass='1')

sample_lens.paraxial_amount()

x = 0
for i in range(len(sample_lens.surface_list)):
    draw.draw_surf(
        sample_lens.surface_list[i].radius, 1.8, x)
    x += sample_lens.surface_list[i].thickness
plt.show()
