class Flower:
    def __init__(self, list_of_attributes, flower_type):
        self.attributes = list_of_attributes
        self.flower_type = flower_type

    def change_commas_to_dots(self):
        for i in range(len(self.attributes)):
            self.attributes[i] = float(str(self.attributes[i]).replace(",", "."))

    def to_string(self):
        print(str(self.attributes) + " " + self.flower_type)
