"""
Documentation is used to make your code easier to understand and use. Functions are especially readable because they often use documentation strings, or docstrings.
Docstrings are a type of comment used to explain the purpose of a function, and how it should be used. Here's a function for population density with a docstring.
"""

#I've been making use of docstrings in several of these notes

def population_density(population, land_area):
    """Calculate the population density of an area:
    
        INPUT:
        population: int. The population of that area.
        land_area: int or float. This function is  unit-agnostic, if you pass
        in values in terms of square or km or square miles, the function will
        return a density in those units.
        
        OUTPUT:
        population_density: population / land_area. The population density of a 
        particular area."""
    return population / land_area

print("St.Paul size: 56.1 mi^2")
print("StPaul population: 305,877")

print(f"Population density: {population_density( 305877, 56.1)} per mi^2.")
