import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

# Read the NIfTi data
NIfTI_path = 'data/data_sets-master/ibsi_1_ct_radiomics_phantom/nifti/image/phantom.nii.gz'
image = nib.load(NIfTI_path)
# print(type(image))

# Print the NIfTI header
print(image.header)
print(image.shape)
# print(image.get_data_dtype())
# print(image.affine.shape)

# Extract the data to numpy array
data = image.get_fdata()
print(type(data))

# Show one slice
plt.imshow(data[50], cmap='gray')
plt.axis('off')
plt.show()

# Rotate and show one slice
plt.imshow(ndi.rotate(data[50], 90), cmap='gray')
plt.axis('off')
plt.show()

# Show series of slices
fig_rows = 3
fig_cols = 3
n_subplots = fig_rows * fig_cols
n_slice = data.shape[0]
step_size = n_slice // n_subplots
plot_range = n_subplots * step_size
start_stop = int((n_slice - plot_range) / 2)

fig, axs = plt.subplots(fig_rows, fig_cols, figsize=[10, 10])

for idx, img in enumerate(range(start_stop, plot_range, step_size)):
    axs.flat[idx].imshow(ndi.rotate(data[img, :, :], 90), cmap='gray')
    axs.flat[idx].axis('off')

plt.tight_layout()
plt.show()



