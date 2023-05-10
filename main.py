import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functions import RecipeFunctions
# read the existing csv file or create a new one if it does not exist
functions =  RecipeFunctions()
try:
    recipes_df = pd.read_csv("recipes.csv")
except FileNotFoundError:
    recipes_df = pd.DataFrame(columns=["name", "ingredients", "instructions", "cooking_time", "serving_size", "cuisine_type", "meal_type", "dietary_preferences"])


while True:
    choice = input("Please enter a number: 1: Adding 2: Searching 3:Visualizing 4: Analyzing 5: end this file 6 Updating 7: Deleting ")
    if choice == "1":
        functions.add_recipe(recipes_df)
        print("Recipe added to your collection!")
    elif choice == "2":
        functions.search_recipe(recipes_df)
        print("Found the item you are looking for!")
    elif choice == "3":
        functions.visualize_recipe(recipes_df)
    elif choice == "4":
        functions.analyze_most_common_ingredients(recipes_df)
    elif choice == "5":
        print("Enjoy cooking!!!")
        break
    elif choice == "6":
        functions.update_recipe(recipes_df)
        break
    elif choice == "7":
        functions.delete_recipe(recipes_df)
        break
    else:
        print("Invalid choice. Please try again.")
