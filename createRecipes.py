#!/usr/bin/python3

import os 
import sys

# Ensure correct argument passing
if len(sys.argv) > 1:
    # Open 'README.md' and write a markdown link to the file
    with open('README.md', 'w+') as file:
        file.write(f"[{sys.argv[1]}](https://timcharlier6.github.io/recipes/recipes/{sys.argv[1]})\n")
    
    # Check if 'recipes' directory exists, if not create it
    if not os.path.exists('recipes'):
        os.makedirs('recipes')
    
    # Change to 'recipes' directory
    os.chdir('recipes')
    
    # Create the file with the name passed in the argument
    with open(f'{sys.argv[1]}.md', 'w+'):
        pass  # Creating an empty file

