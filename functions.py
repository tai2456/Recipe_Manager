import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class RecipeFunctions:
# Function to add new recipes
    def add_recipe(self,recipes_df):
        # add global to avoid UnboundLocalError issue
        
        
        name = input("Enter recipe name: ")
        ingredients = input("Enter ingredients (comma-separated list): ")
        instructions = input("Enter instructions: ")
        cooking_time = int(input("Enter cooking time (minutes): "))
        serving_size = int(input("Enter serving size: "))
        cuisine_type = input("Enter cuisine type: ")
        meal_type = input("Enter meal type: ")
        dietary_preferences = input("Enter dietary preferences: ")

        # add new recipe information to dataframe
        new_recipe = pd.DataFrame({"name": [name], "ingredients": [ingredients], "instructions": [instructions], "cooking_time": [cooking_time], "serving_size": [serving_size], "cuisine_type": [cuisine_type], "meal_type": [meal_type], "dietary_preferences": [dietary_preferences]})
        recipes_df = pd.concat([recipes_df, new_recipe], ignore_index=True)

        # save updated dataframe as csv file
        recipes_df.to_csv("recipes.csv", index=False)


    # Function to search recipes
    def search_recipe(self,recipes_df):
        # get search query from user input
        query = input("Enter keyword, ingredient or category to search for: ")

        # search for matching recipes
        matches = recipes_df[recipes_df.apply(lambda row: query.lower() in row.astype(str).str.lower().str.cat(sep=" "), axis=1)]

        # display matching recipes
        if len(matches) > 0:
            print(f"Found {len(matches)} matching recipe(s):")
            print(matches)
        else:
            print("No matching recipe found.")

    # Function to visualize recipes by cuisine type, meal type or dietary preferences
    def visualize_recipe(self,recipes_df):
        # Visualize recipes by cuisine type
        cuisines = recipes_df["cuisine_type"].value_counts()
        cuisines.plot(kind="bar", title="Recipes by Cuisine Type")

        # Visualize recipes by meal type
        meals = recipes_df["meal_type"].value_counts()
        meals.plot(kind="pie", title="Recipes by Meal Type")

        # Visualize recipes by dietary preferences
        dietary_preferences_counts = recipes_df["dietary_preferences"].value_counts()
        dietary_preferences_counts.plot(kind="bar", title="Recipes by Dietary Preferences")
        plt.show() 

    # Analyze most common ingredients
    def analyze_most_common_ingredients(self,recipes_df):
        ingredients = recipes_df["ingredients"].str.lower().str.split(',')
        all_ingredients = []
        for ingredients_list in ingredients:
            all_ingredients += ingredients_list
        ingredients = pd.Series(all_ingredients).str.strip().value_counts()
        print("Most common ingredients:")
        print(ingredients.head())

        # show plots
        plt.show()
    # Function to update a recipe
    def update_recipe(self,recipes_df):
        

        name = input("Enter the name of the recipe you want to update: ")
        recipe = recipes_df.loc[recipes_df["name"] == name]

        if not recipe.empty:
            print("Enter the new details for the recipe:")
            # Get the new details for the recipe
            for column in recipes_df.columns:
                new_value = input(f"Enter new {column}: ")
                if new_value:
                    recipes_df.loc[recipes_df["name"] == name, column] = new_value
            recipes_df.to_csv("recipes.csv", index=False)
            print("Recipe updated.")
        else:
            print("Recipe not found.")

    # Function to delete a recipe
    def delete_recipe(self,recipes_df):
        

        name = input("Enter the name of the recipe you want to delete: ")
        recipe = recipes_df.loc[recipes_df["name"] == name]

        if not recipe.empty:
            recipes_df = recipes_df[recipes_df["name"] != name]
            recipes_df.to_csv("recipes.csv", index=False)
            print("Recipe deleted.")
        else:
            print("Recipe not found.")
