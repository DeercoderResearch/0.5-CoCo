from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt

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



img = coco.loadImgs(foodImageId[5])[0]
img_name = '%s/images/%s/%s'%(dataDir,dataType,img['file_name'])
I = io.imread(img_name)
plt.figure()
plt.imshow(I)
plt.show()

print foodCategory
print foodCategoryId	
print foodImageId
print img_name
