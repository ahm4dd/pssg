import os
import shutil
from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from parser import *
from converter import *

def main():
    copy_to_public()

def copy_to_public():
    if not(os.path.exists("static/")):
        os.mkdir('static/') 
    if not(os.path.exists("public/")):
        os.mkdir('public/')

    if os.listdir("public/") != []:
        shutil.rmtree('public/')
        os.mkdir('public/')
    if os.listdir('static/') != []:
        for file in os.listdir("static/"):
            if os.path.isfile(os.path.join('static/', file)):
                shutil.copy(os.path.join('static/', file), 'public/') 
main()