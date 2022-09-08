from multiprocessing import Value


cast = {
            "jerry seinfeld": "Jerry Seinfeld",
            "Julia Louis-Dreyfus": "Elaine Benes",
            "Jason Alexander": "George Costanza",
            "Michael Richards": "Cosmo Kramer",
            }
            
for key, value in cast.items():    #The items() method allows you to itterate through both the keys and the values
    print(f"They key: {key.title()}")
    print(f"\tThe value: {value.title()}")