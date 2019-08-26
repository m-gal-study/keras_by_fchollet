# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:56:35 2019

@author: mikhail.galkin
"""
# Chart #2
from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images.shape
len(train_labels)
train_labels

test_images.shape
len(test_images)
test_labels

from keras import models
from keras import layers
ner