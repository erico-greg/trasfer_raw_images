'''
Script for moving raw photo files
to .jpg files directory after the
selection of the good .jpg pictures.

Step one:
    Separete raw and .jpg files in
    differente directories:
    |File Type | Dir. Name |
    |  .jpg    |  'Fotos'  |
    |   raw    |   'raw'   |

Step two:
    Select the best images on .jpg 
    directory
    
Step three:
    Run script
    
Step four:
    Feel Free for moving files to
    the most convenient location
    
Step five:
    Have fun with the time saved ;D
'''
import os

#change raw extention type
raw_ext = 'CR2'

cwd = os.getcwd()


# Name 'fotos' the photos folder
fotos_path = os.path.join(cwd,'fotos')

# Name 'raw' the raw directory
raw_path = os.path.join(cwd,'raw')

if os.path.isdir(fotos_path):
    if os.path.isdir(raw_path):
        fotos = os.listdir(fotos_path)
        raw = os.listdir(raw_path)

        for foto in fotos:
            raw_name = foto.split(".")[0] + '.' + raw_ext
            src = os.path.join(raw_path,raw_name)
            if os.path.isfile(src):
                dst = os.path.join(fotos_path,raw_name)
                os.rename(src,dst)
            else:
                pass
    else:
        print("The 'raw' folder is named wrong or wasn't created.")
else:
    print("The 'Fotos' folder is named wrong or wasn't created.")