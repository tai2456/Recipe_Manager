import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read the existing csv file or create a new one if it does not exist
try:
    recipes_df = pd.read_csv("recipes.csv")
except FileNotFoundError:
    recipes_df = pd.DataFrame(columns=["name", "ingredients", "instructions", "cooking_time", "serving_size", "cuisine_type", "meal_type", "dietary_preferences"])

# Function to add new recipes
def add_recipe():
    # add global to avoid UnboundLocalError issue
    global recipes_df
    
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
def search_recipe():
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
def visualize_recipe():
    # Visualize recipes by cuisine type
    cuisines = recipes_df["cuisine_type"].value_counts()
    cuisines.plot(kind="bar", title="Recipes by Cuisine Type")

    # Visualize recipes by meal type
    meals = recipes_df["meal_type"].value_counts()
    meals.plot(kind="pie", title="Recipes by Meal Type")

    # Visualize recipes by dietary preferences
    dietary_preferences_counts = recipes_df["dietary preferences"].value_counts()
    dietary_preferences_counts.plot(kind="bar", title="Recipes by Dietary Preferences")

# Analyze most common ingredients
def analyze_most_common_ingredients():
    ingredients = recipes_df["ingredients"].str.lower().str.split(',')
    all_ingredients = []
    for ingredients_list in ingredients:
        all_ingredients += ingredients_list
    ingredients = pd.Series(all_ingredients).str.strip().value_counts()
    print("Most common ingredients:")
    print(ingredients.head())

    # show plots
    plt.show()

# main loop
while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        add_recipe()
        print("Recipe added to your collection!")
    elif choice == "2":
        search_recipe()
        print("Found the item you are looking for!")
    elif choice == "3":
        visualize_recipe()
    elif choice == "4":
        analyze_most_common_ingredients()
    elif choice == "5":
        print("Enjoy cooking!!!")
        break
    else:
        print("Invalid choice. Please try again.")
