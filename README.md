Basics with DICOM and NIfTI files using Pydicom and Nibabel
===============================

This repesotory contains scripts that demonstrate the basics of managing DICOM and NIfTI files.

1.  `Read_dicom.py`: How to read DICOM files with pydicom, write header information to the console and show them with Matplotlib.

2.  `Convert_dicom_to_png.py`: This script converts an entire directory of DICOM files to PNG files.

3.  `Read_NIfti.py `: The script is for reading NIfTI files with the nibabel library, writing the header information to the console, converting them to ndarray and showing them with Matplotlib.

4.  `Filter_NIfTI.py`: Reads, converts NIfTI files to numpy array, and applies mask.

5.  `First_order_statistics.py`: After every preprocessing step this script calculates first order statistics of the NIfTI files.

6.  `GLCM.py`: This script calculates the GLCM (Gray-Level Co-Occurrence Matrix) of the masked NIfTI image. It uses the [0, 1, 0] positional operator.

Dataset
-------
For testing, I used the IBSI (Image Biomarker Standardisation Initiative) dataset, which contains both DICOM and NIfTI datasets.
The dataset is available [here](https://github.com/theibsi/data_sets).


