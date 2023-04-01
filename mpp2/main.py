from Flower import Flower
import random
class Perceptron:

    def __init__(self, flower):
        self.weights = []
        # initialize weights with random values between 0 and 1
        for i in range(len(flower.attributes)):
            self.weights.append(random.random())
        self.weights.append(random.random())

    def calculate_new_weights(self, flower_attributes: list) -> None:
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + ((-1) * flower_attributes[i])


def which_path(chosen_file):
    if chosen_file == 1:
        return r"data/iris_test.txt"
    elif chosen_file == 2:
        return r"data/iris_training.txt"


def read_from_file(chosen_file) -> list:
    list_of_flowers_to_return = []
    path = which_path(chosen_file)

    with open(path, "r") as file:
        read_content = file.read()
        data_in_lines = read_content.split("\n")
        for line in data_in_lines:
            line_as_list = line.split("\t")
            if len(line_as_list) == 1:
                continue
            for i in range(len(line_as_list)):
                line_as_list[i] = line_as_list[i].strip()  # removing white spaces cause University decided to gives us data not only with spaces but also with tabulators :))))
            list_of_flowers_to_return.append(
                Flower(line_as_list[:len(line_as_list) - 1], line_as_list[len(line_as_list) - 1]))  # We know that the last in the list will always be flower type rest is attributes

    return list_of_flowers_to_return

def reformat_data_commas_to_dots(data):
    for flower in data:
        flower.change_commas_to_dots()


def main():
    training_data = read_from_file(2)
    test_data = read_from_file(1)
    reformat_data_commas_to_dots(training_data)
    reformat_data_commas_to_dots(test_data)
    for flower in training_data:
        flower.to_string()
    print("TEST DATA NOW")
    for flower in test_data:
        flower.to_string()


if __name__ == '__main__':
    main()