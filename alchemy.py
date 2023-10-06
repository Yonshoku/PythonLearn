import re
from enum import Enum
from enum import auto


# Parent enum to autoname Elements
class ElementAutoName(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return name.capitalize()


# Enum with elements
class Element(ElementAutoName):
    WATER = auto()
    FIRE = auto()
    SOIL = auto()
    AIR = auto()
    LAVA = auto()
    ROCK = auto()
    DIRT = auto()
    HURRICANE = auto()
    SAND = auto()
    DUST = auto()
    POWDER = auto()
    EXPLOSION = auto()


unlocked_elements = {Element.WATER, Element.FIRE, Element.SOIL, Element.AIR}
recipes = [[Element.FIRE, Element.SOIL], [Element.LAVA, Element.WATER], [Element.WATER, Element.SOIL],
           [Element.AIR, Element.AIR], [Element.ROCK, Element.AIR], [Element.AIR, Element.SOIL],
           [Element.DUST, Element.FIRE], [Element.FIRE, Element.POWDER]]

elements = [Element.LAVA, Element.ROCK, Element.DIRT, Element.HURRICANE,
            Element.SAND, Element.DUST, Element.POWDER, Element.EXPLOSION]


# Function gets input and return elements from it
def get_input(message: str):
    lst = list(map(lambda s: s.strip(), input(message).split(" ")))
    return list(map(lambda s: s.capitalize(), lst))


# Function validate input and return error message
def check_input(given_inp):
    # Check if there is two words or more
    if len(given_inp) < 2:
        return "Choose the only two elements to join \n"

    # Check if given strings are words with only letters
    for i in range(2):
        if not re.fullmatch(r"[a-zA-Z]+", given_inp[i]):
            return "You need to choose two elements to join and to get a new element \n"

    return None


# Function checks if the two given elements unlock a new element
def check_recipe(elem1: str, elem2: str):
    # Check if given elements exists
    if elem1 not in [elem.value for elem in Element]:
        return None
    if elem2 not in [elem.value for elem in Element]:
        return None

    # Return recipe if its exists
    recipe1 = [Element(elem1), Element(elem2)]
    recipe2 = [Element(elem2), Element(elem1)]
    if recipe1 in recipes:
        return elements[recipes.index(recipe1)]
    elif recipe2 in recipes:
        return elements[recipes.index(recipe2)]
    else:
        return None


# Game cycle
print("This is demo alchemy game. Try to join two elements together to get new one. Unlock all 12 elements.",
      end="\n\n")

new_element = None
while True:
    print("Unlocked elements:")
    print(" ".join(map(lambda elem: str(elem), unlocked_elements)))
    inp = get_input("Choose two elements \n")
    error_message = check_input(inp)

    while error_message is not None:
        inp = get_input(check_input(inp))
        error_message = check_input(inp)

    new_element = check_recipe(inp[0], inp[1])
    if new_element is None:
        print("There is no such recipe.")
    else:
        unlocked_elements.add(new_element)
        print(f"Element unlocked: {new_element}")

    if len(unlocked_elements) >= len(Element):
        print("Congratulations! You unlocked every element.")
        break
