'''
Landon Pack
IS 303-A04

Reciple scaler program:
This program will take a recipe, look at the amount of ingredients
needed to feed one person and run calculations to scale the recipe upwards to feed (X) people.

Inputs:
-Amount of people to feed
-Recipe name
-Ingredients needed for recipe to feed one person

Processes:
-get_amount_of_ppl() Input validation on the amount of people to feed to ensure that it is a valid integer
-get_ingredients() Create a list of ingredients needed to feed one person and the amount of each ingredient needed for a specific recipe
-calculate_ingredients() Scale the amount of each ingredient needed to feed one person up to the amount needed
 to feed (X) people
- generate_report() Generates a report outlining the information

Outputs: 
-A report detailing the recipe name, the amount of people to feed, the ingredients needed to feed one person and the amount of each ingredient needed to feed (X) people


'''

from datetime import datetime

def get_amount_of_ppl():
    while True:
        try:
            ppl = int(input("How many people will you be feeding?: "))
            return ppl
        except ValueError:
            print("Error: Unexpected value. Please enter a whole number.")

def get_recipe_name():
    recipe_name = input("What is the name of the recipe?: ").title()
    return recipe_name

def get_ingredients(recipe_name):
    ingredients = []
    print(f"Enter the ingredients needed to feed one person for the {recipe_name} recipe. Type 'done' when finished.")
    while True:
        ingredient_name = input("Ingredient name (or 'done' to finish): ")
        if ingredient_name.lower() == 'done':
            break
        try:
            amount_needed = float(input(f"Amount of {ingredient_name} needed to feed one person: "))
            ingredients.append({"ingredient":ingredient_name, "amount": amount_needed})
        except ValueError:
            print("Error: Unexpected value. Please enter a valid number for the amount.")
    return ingredients

def calculate_ingredients(ingredients, ppl):
    scaled_ingredients = []
    for ingredient in ingredients:
        scaled_amount = ingredient["amount"] * ppl 
        scaled_ingredients.append({"ingredient": ingredient["ingredient"], "amount": scaled_amount})
    return scaled_ingredients

def generate_report(recipe_name, ppl, ingredients, scaled_ingredients):
    print("\nRecipe Scaling Report")
    print("---------------------")
    print(f"Generated on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}")
    print(f"Recipe Name: {recipe_name}")
    print(f"Number of People to Feed: {ppl}\n")
    print("Ingredients needed to feed one person:")
    for ingredient in ingredients:
        print(f"- {ingredient['ingredient']}: {ingredient['amount']}")
    print(f"\nIngredients needed to feed {ppl} people:")
    for ingredient in scaled_ingredients:
        print(f"- {ingredient['ingredient']}: {ingredient['amount']}")
    print("\nThank you for using the recipe scaler program!")


ppl = get_amount_of_ppl()
recipe_name = get_recipe_name()
ingredients = get_ingredients(recipe_name)
scaled_ingredients = calculate_ingredients(ingredients, ppl)
generate_report(recipe_name, ppl, ingredients, scaled_ingredients)

