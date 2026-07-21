# boolean operators: and, not, or

is_raining = True
is_windy = False
# and operator: both conditions must be true
stay_inside = is_raining and is_windy

print("Should I stay inside?", stay_inside)

# or operator: at least one condition must be true
take_coat = is_raining or is_windy
print("Should I take a coat?", take_coat)


# not operator: negates the condition
is_sunny = not is_raining
print("Is it sunny?", is_sunny)