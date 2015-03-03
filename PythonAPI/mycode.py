from pycocotools.coco import COCO
from write_xml import write_to_file
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import os
import shutil

dataDir='..'
dataType='val2014'
annFile='%s/annotations/instances_%s.json'%(dataDir,dataType)

coco=COCO(annFile)	# load database
cats=coco.loadCats(coco.getCatIds())
print cats

foodCategory = []
foodCategoryId = []
foodImageId = []

for cat in cats:
	if cat['supercategory'] == 'food':
		foodCategory.append(cat['name'])
		print cat['name']

foodCategoryId = coco.getCatIds(foodCategory)
foodImageId = coco.getImgIds(catIds=foodCategoryId) #must add catIds=

dstdir = './JPEGImages/'

# Get all food images and copy them to JPEGImages folders.(#JPEGImage#)
for cat in range(0, len(foodImageId)):
	img = coco.loadImgs(foodImageId[cat])[0]
	img_name = '%s/images/%s/%s'%(dataDir,dataType,img['file_name'])
	#print img_name
	shutil.copy(img_name, dstdir)


# Generate the SegmentationObject/SegmentationClass (#Segmentation#)
dstdir = './SegmentationClass'
dstdir_2 = './SegmentationObject'

# Generate the configuration files for Annotation folders(#Annotation#)
# Move to the above the share the loop of image_names.
for cat in range(0, len(foodImageId)):
	img = coco.loadImgs(foodImageId[cat])[0]
	img_name = os.path.splitext(img['file_name'])[0]
	img_annotation_xml_name ='./Annotations/%s.xml'%(img_name)
	print img_annotation_xml_name
	file = open(img_annotation_xml_name, "wb")
	file.close()

### ?????? 

# Generat the configuration for ImageSet


img = coco.loadImgs(foodImageId[5])[0]
img_name = '%s/images/%s/%s'%(dataDir,dataType,img['file_name'])
I = io.imread(img_name)
plt.figure()
plt.imshow(I)
plt.show()

# JUST FOR DEBUGGING
print foodCategory
print foodCategoryId	
print foodImageId
print img_name
