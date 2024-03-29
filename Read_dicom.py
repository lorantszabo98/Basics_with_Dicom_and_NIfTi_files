import pydicom
import matplotlib.pyplot as plt

image_path = 'data/data_sets-master/ibsi_1_ct_radiomics_phantom/dicom/image/DCM_IMG_00000.dcm'

dcm_file = pydicom.dcmread(image_path)
print(dcm_file)

plt.imshow(dcm_file.pixel_array, cmap=plt.cm.gray)
plt.show()