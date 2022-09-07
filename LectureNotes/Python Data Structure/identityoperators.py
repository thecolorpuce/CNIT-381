"""

Keyword	Operator
is	evaluates if both sides have the same identity
is not	evaluates if both sides have different identities
You can check if a key returned None with the is operator. You can check for the opposite using is not.
"""

elements = {'hydrogen' : 1, 'helium': 2, 'carbon': 6}

n = elements.get("dilithium")

print(n is None)
print(n is not None)