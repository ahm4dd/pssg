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
    if os.path.exists("static/"):
        if os.path.exists("public/"):
          if os.listdir("public/") != []:
              shutil.rmtree('public/')
              os.mkdir('public/')
          for file in os.listdir("static/"):
              shutil.copy(os.path.join('static/', file), 'public/')

main()