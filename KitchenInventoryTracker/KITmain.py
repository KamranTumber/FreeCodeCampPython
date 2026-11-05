# Initial kitchen stock (global variables)
available_eggs = 1
available_flour = 2
available_sugar = 3


def check_kitchen_stock():
    """Prints the current inventory of kitchen items and the total count."""
    total_items = available_eggs + available_flour + available_sugar
    print(f"The kitchen has {total_items} total items:")
    print(f"- {available_eggs} eggs")
    print(f"- {available_flour} flour")
    print(f"- {available_sugar} sugar")


# Display the initial kitchen stock
print("--- Initial Stock ---")
check_kitchen_stock()
print()


def use_eggs(current_eggs, eggs_to_use):
    """Decreases the egg count if enough eggs are available.

    Returns the updated egg count.
    """
    if eggs_to_use > current_eggs:
        print("The kitchen does not have enough eggs.")
        return current_eggs

    print(f"{eggs_to_use} egg(s) used out of {current_eggs} available.")
    return current_eggs - eggs_to_use


# Example call: Note that the return value isn't assigned back here,
# so the global 'available_eggs' variable remains 1.
use_eggs(available_eggs, 1)
print(f"Global available_eggs remains: {available_eggs}\n")


def make_fried_egg(current_eggs):
    """Attempts to make a fried egg if at least 1 egg is available.

    Updates and returns the new egg count.
    """
    has_enough_eggs = current_eggs >= 1

    if has_enough_eggs:
        current_eggs = use_eggs(current_eggs, 1)
        print("Made a fried egg. Yummy!")
    else:
        print("Could not make a fried egg. Not enough eggs!")

    return current_eggs


# Make a fried egg and update the global available_eggs variable with the result
print("--- Cooking ---")
available_eggs = make_fried_egg(available_eggs)
print()

# Display the final kitchen stock
print("--- Final Stock ---")
check_kitchen_stock()