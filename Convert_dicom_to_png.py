import pydicom
import os
from PIL import Image
import numpy as np
import cv2

images_folder = 'data/data_sets-master/ibsi_1_ct_radiomics_phantom/dicom/image'
output_folder = 'output_images/'
os.makedirs(output_folder, exist_ok=True)

images = os.listdir(images_folder)

for i, image in enumerate(images):

    if image.endswith('.dcm'):
        dcm_file = pydicom.dcmread(os.path.join(images_folder, image))

        img = dcm_file.pixel_array
        img = ((img - np.min(img)) / np.ptp(img) * 255.0).astype(np.uint8)

        cv2.imwrite(os.path.join(output_folder, str(i) + '.png'), img)



