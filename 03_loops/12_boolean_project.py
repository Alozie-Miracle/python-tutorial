"""

Write a program that asks the user three questios.

Ask the user:
1. Are you a student?
2. Do you have a pet?
3. Do you smoke?


The program automatically decides whether a property you've applied to rent is available to you.

It should print an appropriate response, like "Property availble" or "Property not available".

The program applies these criteria:

- if you're a student, you can only rent the property if you don't have a pet and don't smoke.
- if you're not a student, you can rent the property if you smoke or have a pet, but not if
you both smoke and have a pet.
"""


# Get user input
is_student = input("Are you a student? (yes/no): ").strip().lower() == "yes"
has_pet = input("Do you have a pet? (yes/no): ").strip().lower() == "yes"
smokes = input("Do you smoke? (yes/no): ").strip().lower() == "yes"


# Determine property availability based on the criteria
if is_student:
    if not has_pet and not smokes:
        print("Property available")
    else:
        print("Property not available")
else:
    if smokes or has_pet:
        if not (smokes and has_pet):
            print("Property available")
        else:
            print("Property not available")
    else:
        print("Property not available")


# alternative approach using boolean operators

student_can_rent = is_student and not has_pet and not smokes
non_student_can_rent = not is_student and (smokes or has_pet) and not (smokes and has_pet)

can_rent = student_can_rent or non_student_can_rent
print("Property available" if can_rent else "Property not available")