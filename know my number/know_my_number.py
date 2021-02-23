from validations import how_many_attempts


print("Thought of a number between 1 and 100, do you want to try to guess?")
attempts = how_many_attempts()
print(f'You got it right in {attempts} attempts')
