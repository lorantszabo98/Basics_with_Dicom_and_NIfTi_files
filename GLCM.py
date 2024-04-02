import nibabel as nib
import numpy as np
# import matplotlib.pyplot as plt


image_path = r'C:\Users\pc-l\PycharmProjects\cv_venv\medical_images\data\data_sets-master\ibsi_1_digital_phantom\nifti\image\phantom.nii.gz'
img = nib.load(image_path)
# data = img.get_fdata()
mask = nib.load(
    r'C:\Users\pc-l\PycharmProjects\cv_venv\medical_images\data\data_sets-master\ibsi_1_digital_phantom\nifti\mask\mask.nii.gz'
)
img_data = img.get_fdata()
mask_data = mask.get_fdata()

img_data[mask_data == 0] = np.nan  # Set the values of the image to NaN where the mask is 0
img_data = np.pad(img_data, 1, mode="constant", constant_values=np.nan)  # Pad the image with NaN values


glcm = np.zeros(
    (int(np.nanmax(img_data)) - int(np.nanmin(img_data)) + 1, int(np.nanmax(img_data)) - int(np.nanmin(img_data)) + 1)
)
print(glcm)

# x, y, z
pos_op = [0, 1, 0]

for i in range(1, img_data.shape[0] - 2):
    for j in range(1, img_data.shape[1] - 2):
        for k in range(1, img_data.shape[2] - 2):
            if ~(np.isnan(img_data[i, j, k]) or np.isnan(img_data[i + pos_op[0], j + pos_op[1], k + pos_op[2]])):
                glcm[int(img_data[i, j, k] - 1), int(img_data[i + pos_op[0], j + pos_op[1], k + pos_op[2]] - 1)] += 1


print(glcm)
