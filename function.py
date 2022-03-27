#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 22:45:04 2022

@author: reejungkim
"""


from keras.layers import Input, Dense
from keras.models import Model
 
encoding_dim = 32
 
def create_encoder():
	input = Input(shape=(784,)) # 28x28
	encoder = Model(input, encoded)
    
    return encoder
 
def create_decoder():
	encoded_input = Input(shape=(encoding_dim,))
	decoder_layer = autoencoder.layers[-1]
	decoder = Model(encoded_input, decoder_layer(encoded_input))
    
    return decoder
    
def create_autoencoder():
	input = Input(shape=(784,)) # 28x28
    encoded = Dense(encoding_dim, activation='relu')(input)
    decoded = Dense(784, activation='sigmoid')(encoded)
    autoencoder = Model(input, output)
    
    return autoencoder