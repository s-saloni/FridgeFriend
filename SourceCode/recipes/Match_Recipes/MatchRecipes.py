#!/usr/bin/python3
# Saloni Sharma

#Script: matching ingredients in kitchen with recipes

#Get absolute path to current directory
import os
import sys
import pathlib
abs_path = os.getcwd()
abs_path = os.path.join(abs_path, "recipes", "Match_Recipes")

#INGREDIENTS 
def StoreIngredients(PantryList):
    #Combine path to directory and file name
    PantryList_Path = os.path.join(abs_path, PantryList)
    ingredients_file = open(PantryList_Path) #open file with ingredients
    ingredients_file.readline() #moving read to third line where ingredients start

    #read in each line with ingredient name and store in list
    ingredients = []
    for ing in ingredients_file.readlines():
        if (ing == '\n' or ing == 'Staple Items:\n'):
            break
        else:
            ingredients.append(ing[3:-1]) #removing ' -' and '/n' to get word only

    #OUTPUT 1
    #print('\033[44m' + '\nCurrent ingredients in your kitchen:' + '\033[0m')
    i_string = ' '
    for i in ingredients:
        i_string += i + ", "
    #print('\033[94m' + i_string[:-2] + '\033[0m')
    
    #return list of ingredients (items in kitchen)
    return ingredients

#RECIPES
def StoreRecipeFilenames(RecipesDir):
    #takes relative path to directory with recipe files
    import os
    RecipesDir_Path = os.path.join(abs_path, RecipesDir)
    #Names of all recipe files
    recipes = os.listdir(RecipesDir_Path)
    return recipes

#MATCHING
import re
def IngredientToRecipe(ingredient, RecipeFilenames):
    #Search each ingredient in each recipe file
    matched_recipes = []
    #remove 's' for any plural suffixes of ingredients
    #print("User searched for:", ingredient)
    if ingredient[-1:] == 's':
        ingredient = ingredient[:-1]
    elif ingredient[-3:] == 'oes':
        ingredient = ingredient[:-2]
    #takes ingredient string as regex pattern
    item = re.compile(ingredient, re.IGNORECASE)
    #search through all recipes
    for current_recipe in RecipeFilenames:
        #Get path to current_recipe file
        Curr_Recipe_Path = os.path.join(abs_path, 'Recipes', current_recipe)
        #open each recipe file and read in recipe name
        r = open((Curr_Recipe_Path), 'r')
        recipe_name = (r.readline())[8:-1] #slice 'Recipe:' from line to get name
        recipe_url = (r.readline()) #slice 'Recipe:' from line to get name
        
        r.seek(0) #brings read cursor back to start of file
        
        #match ingredient name regex in recipe file
        if item.search(r.read()):
            #check if recipe name has already been added to list
            if recipe_name not in matched_recipes:
                matched_recipes.append([recipe_name, recipe_url]) #add recipe name to options
        r.close() #close each recipe file when done

    
    #OUTPUT 2
    '''
    if len(matched_recipes) == 0: #when no recipes matched the ingredient
        print("\nOh no! No recipes in the library include this ingredient. ")
    if len(matched_recipes) == 1:
        print('\nYou can try out this recipe!')
        print('-' + matched_recipes[0])
    else:
        print('\033[44m' + "\nHere are recipes you can try:" + '\033[0m')
        for option in matched_recipes:
            print('\033[94m' + '- ' + option + '\033[0m')
    print("\n")
    '''
    #returns list with recipes that match ingredients
    return matched_recipes


#RUN PROGRAM
#PantryList = StoreIngredients('ItemsInKitchen.txt')
RecipeFilenames = StoreRecipeFilenames('Recipes/')
print(RecipeFilenames)
print(IngredientToRecipe("Sugar", RecipeFilenames))

