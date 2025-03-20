import os
import shutil
from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from parser import *
from converter import *

IMAGES_EXTENSIONS = ['png', 'jpg', 'jpeg', 'svg']

def main():
    copy_to_public()

def copy_to_public(path='static/'):
    files = os.listdir(path)
    if path =='static/':
        if os.listdir("public/") != []:
            shutil.rmtree('public/')
            os.mkdir('public/')
            os.mkdir('public/images')

    if not(os.path.exists("static/")):
        os.mkdir('static/') 
    if not(os.path.exists("public/")):
        os.mkdir('public/')
    if not(os.path.exists("public/images")):
        os.mkdir('public/images')

    
    if files != []:
        for file in files:
            if '.' not in file:
                copy_to_public(path+file+'/')
            if os.path.isfile(os.path.join(path, file)):
                print(file)
                if file.split('.')[1] in IMAGES_EXTENSIONS:
                    shutil.copy(os.path.join(path, file), 'public/images')
                else:
                    shutil.copy(os.path.join(path, file), 'public/')
main()