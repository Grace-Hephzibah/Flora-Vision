import os
import numpy as np
import shutil
import random

root_dir = 'full/'
classes = os.listdir(root_dir)
first_split = 0.50
for cls in classes:
    os.makedirs('val/' + cls)
    os.makedirs('test/' + cls)
    
## creating partition of the data after shuffeling

for cls in classes:
    src = root_dir + cls # folder to copy images from
    print(src)

    allFileNames = os.listdir(src)
    np.random.shuffle(allFileNames)
 
    train_FileNames,val_FileNames = np.split(np.array(allFileNames),
                        [int(len(allFileNames)*first_split)])

    # #Converting file names from array to list

    train_FileNames = [src+'/'+ name for name in train_FileNames]
    val_FileNames = [src+'/' + name for name in val_FileNames]

    print('Total images  : '+ cls + ' ' +str(len(allFileNames)))
    print('Training : '+ cls + ' '+str(len(train_FileNames)))
    print('Validation : '+ cls + ' ' +str(len(val_FileNames)))

    ## Copy pasting images to target directory

    for name in train_FileNames:
        shutil.copy(name, 'val/'+cls )


    for name in val_FileNames:
        shutil.copy(name, 'test/'+cls )
