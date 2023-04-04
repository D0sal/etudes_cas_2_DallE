# Cas_etude2.ipynb


!pip install transformers


import os
import zipfile

local_zip = '/tmp/cats_and_dogs_filtered.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/content')
zip_ref.close()

base_dir = '/content/cats_and_dogs_filtered'
train_dir = os.path.join(base_dir, 'val')

# Directory with our training cat pictures
train_cats_dir = os.path.join(train_dir)

# Directory with our training dog pictures
train_dogs_dir = os.path.join(train_dir)

from PIL import Image
import requests
from transformers import CLIPProcessor, CLIPModel, CLIPTokenizer,AutoTokenizer, CLIPImageProcessor
import pathlib
import numpy
import torch

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

tokenizer = AutoTokenizer.from_pretrained("openai/clip-vit-base-patch32")

imageprocess = CLIPImageProcessor.from_pretrained("openai/clip-vit-base-patch32")

path = pathlib.Path('/content/cats_and_dogs_filtered/train/cats') 

top_k = 10
size = (224,224)

image = []
score = []
res= []

text = tokenizer(["A black cat"], padding=True, return_tensors="pt")
text_emb = model.get_text_features(**text).detach().numpy()

for image_path in path.iterdir():
  
  image.append(Image.open(str(image_path)).resize(size))

  if len(image) > 50:
    
    inputs = processor(images=image, return_tensors="pt", padding=True) 
    image_vectors = model.get_image_features(**inputs).detach().numpy()
    score = image_vectors / numpy.linalg.norm(image_vectors, axis=0)
    break

for i in range(len(score)):
  res.append(numpy.dot(text_emb,score[i]))

ids = sorted(range(len(res)), key=lambda i: res[i])[-top_k:]

for id in ids:
  image[id].show()

'''
    outputs = model(**inputs).logits_per_image
  
  
    if len(res) < 10:
      res.append(image)
      value.append(outputs)
    else :
      if outputs > min(value):
        id = value.index(min(value))
        res[id] = image
        value[id] = outputs


for i in range(len(res)):

  res[i].show()
'''