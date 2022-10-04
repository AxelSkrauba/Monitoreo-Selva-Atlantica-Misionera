import cv2
import os
import numpy as np


input_images_path = "input"
files_names = os.listdir(input_images_path)
print(files_names)
output_images_path = "output"
if not os.path.exists(output_images_path):
    os.makedirs(output_images_path)
    print("Directorio creado: ", output_images_path)


def img_to_grid(img, row,col):
    ww = [[i.min(), i.max()] for i in np.array_split(range(img.shape[0]),row)]
    hh = [[i.min(), i.max()] for i in np.array_split(range(img.shape[1]),col)]
    grid = [img[j:jj,i:ii,:] for j,jj in ww for i,ii in hh]
    return grid, len(ww), len(hh)



row, col = 9, 12

for file_name in files_names:
    #print(file_name)
    '''
    if file_name.split(".")[-1] not in ["jpeg", "png"]:
        continue
    '''
    image_path = input_images_path + "/" + file_name
    print(image_path)
    image = cv2.imread(image_path)
    if image is None:
        continue

    # Dimensiones
    ancho = image.shape[1] #columnas
    alto = image.shape[0] # filas

    grid, r, c = img_to_grid(image, row, col)

    count = 0
    os.makedirs(output_images_path + "/" + file_name[:-4])
    for img in grid:
        cv2.imwrite(output_images_path + "/" + file_name[:-4]+ "/" + file_name[:-4] + "_" + str(count) + ".jpg", img)
        count += 1
