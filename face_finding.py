import cv2
import json 
import requests 
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

KEY = "xxxx"   

service_address = "xxxx"

address = service_address + "analyze"

parameters  = {'visualFeatures':'Faces',
               'language':'en'}

headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': KEY}

cam = cv2.VideoCapture(0)

ret, frame = cam.read()

img_name = "person.jpg"
cv2.imwrite(img_name, frame)    

path = "person.jpg"

image_data = open(path, "rb").read()

response = requests.post(address, headers=headers, params=parameters, data=image_data)

results = response.json()

cam.release()

cv2.destroyAllWindows()

im = np.array(Image.open("person.jpg"), dtype=np.uint8)
fig,ax = plt.subplots(1)

ax.set_title("Person Detected")

ax.imshow(im)

x  = results['faces'][0]['faceRectangle']['left']
y  = results['faces'][0]['faceRectangle']['top']
w  = results['faces'][0]['faceRectangle']['width']
h  = results['faces'][0]['faceRectangle']['height']

rect = patches.Rectangle((x,y),w,h,linewidth=1,edgecolor='r',facecolor='none')
ax.add_patch(rect)

plt.show()
