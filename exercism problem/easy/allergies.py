#copy-paste from ai...

allergies = {
    1: "eggs", 2: "peanuts", 4: "shellfish", 8: "strawberries",
    16: "tomatoes", 32: "chocolate", 64: "pollen", 128: "cats"
}

score = int(input("Enter score: "))

# Find all keys that exist inside the score using bitwise AND
result = [allergies[key] for key in allergies if score & key]

print(result)

#solution...

class Allergies:

    ingredients = {"eggs": 1, "peanuts": 2, "shellfish": 4, "strawberries": 8, "tomatoes": 16,
        "chocolate": 32, "pollen": 64, "cats": 128}
    
    def __init__(self, score):
        self.score = score
        

    def allergic_to(self, item):
        self.item = item
        # Boolean to check if score and allergy item is in ingredients
        return bool(self.score & Allergies.ingredients[item])

    @property
    def lst(self):
        list = []
        # Loop through ingredients, if allergic_to function True, append to list
        for allergy in Allergies.ingredients:
            if self.allergic_to(allergy):
                list.append(allergy)
        return list
