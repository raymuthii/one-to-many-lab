class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to store all instances of Pet

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.validate_pet_type(pet_type)
        Pet.all.append(self)  # Add the pet instance to the class variable
        
        if owner:  # If an owner is provided, add the pet to the owner's list
            owner.add_pet(self)

    def validate_pet_type(self, pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Private variable to store pets

    def pets(self):
        return self._pets  # Return the list of owner's pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added.")
        pet.owner = self  # Set the owner for the pet
        self._pets.append(pet)  # Add pet to the owner's list

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)  # Sort pets by their names
