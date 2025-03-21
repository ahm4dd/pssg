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
    generate_page('content/index.md','template.html','public/index.html')
    

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

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    try:
        markdown = open(from_path, 'r').read()
        template = open(template_path, 'r').read()

        html_from_markdown = markdown_to_html_node(markdown).to_html()
        page_title = extract_title(markdown)
        template = template.replace('{{ Title }}', page_title)
        template = template.replace('{{ Content }}', html_from_markdown)

        if not(os.path.exists(os.path.dirname(dest_path))):
            os.makedirs(os.path.dirname(dest_path))
        if not(os.path.exists(dest_path)):
            os

        with open(dest_path, 'w') as f:
            f.write(template)
            f.close()
    except Exception as e:
        print(e)

main()