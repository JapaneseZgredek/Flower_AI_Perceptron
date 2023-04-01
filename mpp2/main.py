from Flower import Flower
import random
class Perceptron:

    def __init__(self, flower):
        self.weights = []
        # initialize weights with random values between 0 and 1
        for i in range(len(flower.attributes)):
            self.weights.append(random.random())
        self.weights.append(random.random())

    def calculate_new_weights(self, flower_attributes: list, real_output: int, should_output: int) -> bool:
        copy_of_flower_attributes = flower_attributes
        copy_of_flower_attributes.append(1)
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + ((real_output - should_output) * copy_of_flower_attributes[i])
        return False

    def calculate_output(self, flower: Flower) -> bool:
        output = 0.0
        for i in range(len(self.weights) - 1):
            output = output + self.weights[i] * flower.attributes[i]
        output = output + self.weights[len(self.weights) - 1] * 1
        return output > 0


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

def teaching_perceptron(training_data, perceptron):
    git = 0
    nie_git = 0
    obrot_po_calej_dacie = 0
    # teaching perceptron
    while not git == 120:
        obrot_po_calej_dacie = obrot_po_calej_dacie + 1
        git = 0
        for flower in training_data:
            if flower.flower_type == 'Iris-setosa':
                expected_output = True
            else:
                expected_output = False
            if not expected_output == perceptron.calculate_output(flower=flower):
                if expected_output:
                    copy_of_attributes = flower.attributes.copy()
                    perceptron.calculate_new_weights(copy_of_attributes, 1, 0)
                else:
                    copy_of_attributes = flower.attributes.copy()
                    perceptron.calculate_new_weights(copy_of_attributes, 0, 1)
                nie_git = nie_git + 1
            else:
                git = git + 1


def checking_perceptron_on_test_data(test_data, perceptron):
    correct = 0
    for flower in test_data:
        if flower.flower_type == 'Iris-setosa':
            expected_output = True
        else:
            expected_output = False
        if expected_output == perceptron.calculate_output(flower):
            correct = correct + 1
    print("Correctness: " + str(correct/len(test_data) * 100) + "%")
def main():
    training_data = read_from_file(2)
    test_data = read_from_file(1)
    reformat_data_commas_to_dots(training_data)
    reformat_data_commas_to_dots(test_data)
    perceptron = Perceptron(training_data[0])
    teaching_perceptron(training_data=training_data, perceptron=perceptron)
    checking_perceptron_on_test_data(test_data=test_data, perceptron=perceptron)
    does_user_continue = int(input("If you want to input your own values input 0 if not 1: "))
    while does_user_continue == 0:
        user_input = input("Give me values separated by spaces, and with dots as number pointer,"
                           " NOT COMMAS LIKE IN DATA GIVEN BY FABULOUS UNIVERSITY, in this program version required number of attributes is "
                           + str(len(training_data[0].attributes)) + ": ").split(" ")
        user_input = [float(x) for x in user_input]
        flower = Flower(user_input, "?")
        print(perceptron.calculate_output(flower=flower))
        does_user_continue = int(input("If you want to input your own values input 0 if not 1: "))


if __name__ == '__main__':
    main()