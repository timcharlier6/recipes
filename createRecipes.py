#!/usr/bin/python3

import os 
import sys

if len(sys.argv) > 1:
    with open('README.md', 'a') as file:
        file.write(f"- [{sys.argv[1]}](https://timcharlier6.github.io/recipes/recipes/{sys.argv[1]})\n")
    
    if not os.path.exists('recipes'):
        os.makedirs('recipes')
    
    os.chdir('recipes')
    
    with open(f'{sys.argv[1]}.md', 'w+') as file:
        file.write(f"# {sys.argv[1]}\n")

