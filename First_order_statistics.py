import nibabel as nib
import numpy as np
from scipy.stats import skew

image_path = 'data/data_sets-master/ibsi_1_digital_phantom/nifti/image/phantom.nii.gz'
image = nib.load(image_path)

mask_path = 'data/data_sets-master/ibsi_1_digital_phantom/nifti/mask/mask.nii.gz'
mask = nib.load(mask_path)

data = image.get_fdata()

# Applying mask
data[mask.get_fdata().astype(bool) == False] = np.nan

# Calculate first order statistics of the filtered data
mean = np.nanmean(data.flatten())
std = np.nanstd(data.flatten())
min_val = np.nanmin(data.flatten())
max_val = np.nanmax(data.flatten())
skewness = skew(data.flatten(), nan_policy="omit")

print("Mean: ", mean)
print("Standard Deviation: ", std)
print("Minimum Value: ", min_val)
print("Maximum Value: ", max_val)
print("Skewness: ", skewness)