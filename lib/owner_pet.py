class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.name = name
        self.pet_type = pet_type
        self._owner = None
        Pet.all.append(self)
        if owner:
            self.owner = owner

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner.")
        self._owner = owner


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Must add instance of Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
