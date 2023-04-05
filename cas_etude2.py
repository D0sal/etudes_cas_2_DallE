# -*- coding: utf-8 -*-
"""Cas_etude2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/114UKE79Om2kShjTua_wPT2_ulx0xuPGW
"""

import os
import zipfile
from PIL import Image
import requests
from transformers import CLIPProcessor, CLIPModel, CLIPTokenizer,AutoTokenizer, CLIPImageProcessor
import pathlib
import numpy
import torch
import sys

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

tokenizer = AutoTokenizer.from_pretrained("openai/clip-vit-base-patch32")

imageprocess = CLIPImageProcessor.from_pretrained("openai/clip-vit-base-patch32")

path = pathlib.Path('/dataset/') 
#search = "a cat on a newspaper"
search = sys.argv[1]

if sys.argv[2] :
  top_k = 10
else:
  top_k = 1

size = (100,100)


image = {}
image["path"] = []
image["data"] = []
score = []
res= []

text = tokenizer([search], padding=True, return_tensors="pt")
text_emb = model.get_text_features(**text).detach().numpy()

for image_path in path.iterdir():
  image["data"].append(Image.open(str(image_path)).resize(size))
  image["path"].append(image_path)
  
  if len(image["data"]) > 50:
    
    inputs = processor(images=image["data"], return_tensors="pt", padding=True) 
    image_vectors = model.get_image_features(**inputs).detach().numpy()
    score = image_vectors / numpy.linalg.norm(image_vectors, axis=0)
    break

for i in range(len(score)):
  res.append(numpy.dot(text_emb,score[i]))

ids = sorted(range(len(res)), key=lambda i: res[i])[-top_k:]

for id in ids:
  print(image['path'][id])

