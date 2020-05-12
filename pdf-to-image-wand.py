#downloading the imagemagicx don't download the static version(https://imagemagick.org/script/download.php#windows)
#downloading the ghostscript (https://www.ghostscript.com/download/gsdnld.html)
#configuring the the paths (https://stackoverflow.com/questions/3243361/how-to-install-test-convert-resize-pdf-using-imagemagick-ghostscript-window)



from wand.image import Image
import matplotlib.pyplot as plt
import numpy as np
from glob import glob 
from tqdm import tqdm

path = glob("Dataset/Train/*.pdf")

for pdf in tqdm(path):
    
    filename = pdf.split("\\")[-1].split(".")[0]
    print(filename)
    with Image(filename=pdf,resolution=250) as img: //here resolution is used to improve the quality of the image
        img.compression_quality = 100
        img.save(filename = "Dataset/Converted_Train/"+filename+".jpg")
        
