import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
# fits_image_filename =r"C:\Users\aarus\Downloads\hlsp_phangs-hst_hst_wfc3-uvis_ngc1365_multi_v1_drc-bundle\ngc1365\hlsp_phangs-hst_hst_wfc3-uvis_ngc1365_f336w_v1_exp-drc-sci.fits"
# #fits_image_filename = r"C:\Users\aarus\Downloads\hlsp_phangs-cat_hst_acs-uvis_ngc1365_multi_v1_cats\catalogs\hlsp_phangs-cat_hst_uvis_ngc1365_multi_v1_obs-human-cluster-class12.fits"
# hdul = fits.open(fits_image_filename)

# # For getting file structure
# #hdul.info()

# #print(hdul[1].header)
# hdrtab = hdul[1].data
# print(hdul[0].header['PHOTFNU']) 

# # column_data = hdrtab['CD1_1']  # Replace with actual column name
# # print(column_data)
# # column_data = hdrtab['CD1_2']  # Replace with actual column name
# # print(column_data)
# # column_data = hdrtab['CD2_1']  # Replace with actual column name
# # print(column_data)
# # column_data = hdrtab['CD2_2']  # Replace with actual column name
# # print(column_data)


# # column_data = hdrtab['PHANGS_F814W_VEGA']
# # print(column_data)

# hdul.close()

gas = fits.open(r'C:\Users\aarus\Downloads\ngc1365_gas_distribution.fits')
distribution = gas[0].data
print(distribution)