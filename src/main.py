import os
import shutil
import sys
from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from parser import *
from converter import *

IMAGES_EXTENSIONS = ['png', 'jpg', 'jpeg', 'svg']
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    copy_to_public()
    generate_pages_recursive('content/','template.html','docs/', basepath)
    

def copy_to_public(path='static/'):
    files = os.listdir(path)
    if path =='static/':
        if os.listdir("docs/") != []:
            shutil.rmtree('docs/')
            os.mkdir('docs/')
            os.mkdir('docs/images')

    if not(os.path.exists("static/")):
        os.mkdir('static/') 
    if not(os.path.exists("docs/")):
        os.mkdir('docs/')
    if not(os.path.exists("docs/images")):
        os.mkdir('docs/images')

    
    if files != []:
        for file in files:
            if '.' not in file:
                copy_to_public(path+file+'/')
            if os.path.isfile(os.path.join(path, file)):
                print(file)
                if file.split('.')[1] in IMAGES_EXTENSIONS:
                    shutil.copy(os.path.join(path, file), 'docs/images')
                else:
                    shutil.copy(os.path.join(path, file), 'docs/')

def generate_page(from_path, template_path, dest_path, basepath):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    try:
        markdown = open(from_path, 'r').read()
        template = open(template_path, 'r').read()

        html_from_markdown = markdown_to_html_node(markdown).to_html()
        page_title = extract_title(markdown)
        template = template.replace('{{ Title }}', page_title)
        template = template.replace('{{ Content }}', html_from_markdown)
        template = template.replace('href="/', 'href="' + basepath)
        template = template.replace('src="/', 'src="' + basepath)
        if not(os.path.exists(os.path.dirname(dest_path))):
            os.makedirs(os.path.dirname(dest_path))
        if not(os.path.exists(dest_path)):
            os

        with open(dest_path, 'w') as f:
            f.write(template)
            f.close()
    except Exception as e:
        print(e)
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    entries = os.listdir(dir_path_content)
    
    for entry in entries:
        entry_path = os.path.join(dir_path_content, entry)
        
        if os.path.isdir(entry_path):
            new_dest_dir = os.path.join(dest_dir_path, entry)
            if not os.path.exists(new_dest_dir):
                os.makedirs(new_dest_dir)
            
            generate_pages_recursive(entry_path + '/', template_path, new_dest_dir + '/', basepath)
        
        elif entry.endswith('.md'):
            if entry == 'index.md':
                dest_file_path = os.path.join(dest_dir_path, 'index.html')
            else:
                dest_file_path = os.path.join(dest_dir_path, entry.replace('.md', '.html'))
            
            generate_page(entry_path, template_path, dest_file_path, basepath)
main()
