class Animal:
    def __init__(self, id, mother_id = None, father_id = None):
        self.id = id
        self.mother_id = mother_id
        self.father_id = father_id
        self.children = []

class Pedigree:
    def __init__(self, root_id):
        self.root = Animal(root_id)
