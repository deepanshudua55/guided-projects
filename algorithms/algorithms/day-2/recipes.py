
# What is the smallest result from divided every value in the ingredients dictionary by its corresponding value in the recipe dictionary?

# Loop through the ingredients dictionary
# Keep a variable for the smallest result - initialize it as None
# Divide each value by its counterpart in the ingredient dictionary, round down the result
# If it is the first pair, then set that to be the smallest, otherwise compare the current result to the smallest result and set that to be the smallest if it is smaller
# O(n)

# { 'milk': 100, 'butter': 50, 'flour': 5 },
#  { 'milk': 138, 'butter': 48, 'flour': 51 }
# 1. 138 // 100 = 1, our current smallest
# 2. 48 // 50 = 0, our new smallest and stop since it's 0


def recipe_batches(recipe, ingredients):
    # variable for the smallest result of division
    smallest = None
    # loop
    for key in recipe:
        # check if key is in ingredients
        if key not in ingredients:
            return 0
        # divide the ingredient by its requirement
        result = ingredients[key] // recipe[key]
        # check if result == 0
        if result == 0:
            # we can't make any batches, so return 0
            return 0
        # check if smallest is None or result < smallest
        elif smallest is None or result < smallest:
            smallest = result
    return smallest