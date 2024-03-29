import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

image_path = 'data/data_sets-master/ibsi_1_ct_radiomics_phantom/nifti/image/phantom.nii.gz'
image = nib.load(image_path)
data = image.get_fdata()
np.nanmean(data)

mask_path = 'data/data_sets-master/ibsi_1_ct_radiomics_phantom/nifti/mask/mask.nii.gz'
mask = nib.load(mask_path)

data[mask.get_fdata().astype(bool) == False] = np.nan
np.nanmean(data)
print(data[:, :, 0])

