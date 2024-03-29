import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

NIfTI_path = 'data/data_sets-master/ibsi_1_ct_radiomics_phantom/nifti/image/phantom.nii.gz'
image = nib.load(NIfTI_path)
print(type(image))

print(image.header)
print(image.shape)
print(image.get_data_dtype())
print(image.affine.shape)

data = image.get_fdata()
print(type(data))

plt.imshow(data[50], cmap='bone')
plt.axis('off')
plt.show()



