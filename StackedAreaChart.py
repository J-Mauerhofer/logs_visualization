from TestGeneration import TestGeneration
import matplotlib.pyplot as plt


class StackedAreaChart:

    def __init__(self, file_path):
        self.log_file_path = file_path
        self.test_generation = TestGeneration(file_path)

    def generate_stacked_area_chart(self):
        print("yet to implement this function")

    def create_stacked_area_chart(self):
        """
        Create a stacked area chart from a list of lists of integers.

        Args:
        all_iterations (list of list of int): List of lists where each sublist represents a series of data points.
        """
        all_iterations = self.get_list_of_lists_of_size_of_fronts()
        # Transpose the list of lists if necessary to ensure that each list represents a different series
        all_iterations = list(map(list, zip(*all_iterations)))

        # Create the area plot
        plt.stackplot(range(len(all_iterations[0])), *all_iterations)

        # Add labels and title if needed
        plt.title("Stacked Area Chart")
        plt.xlabel("Iterations")
        plt.ylabel("Size of the fronts")

        # Show the plot
        plt.show()

    def get_preprocessed_fronts(self):
        """
        This method returns a list. Every entry stands for an iteration in the genetic algorithm.
        Every entry is a list of all the fronts of this iteration. The special thing is that every
        entry in the outermost list has exactly the same amount of entries. Normally, it could be
        that for example there are 5 fronts in one iteration but only 3 in another one. In this case,
        the iteration with only 3 fronts would get filled up with 2 empty fronts.
        :return:
        """
        # get number of fronts of the population with the largest amount of fronts
        length_of_longest_front = - 1
        for iteration in self.test_generation.iterations:
            number_of_fronts = iteration.population.get_number_of_fronts()
            if length_of_longest_front < number_of_fronts:
                length_of_longest_front = number_of_fronts

        # fill up return list of fronts
        preprocessed_iterations = []
        for iteration in self.test_generation.iterations:
            fronts_of_current_population = iteration.population.get_fronts()

            while len(fronts_of_current_population) < length_of_longest_front:
                empty_front = []
                fronts_of_current_population.append(empty_front)
            preprocessed_iterations.append(fronts_of_current_population)

        return preprocessed_iterations

    def get_list_of_lists_of_size_of_fronts(self):
        iterations = self.get_preprocessed_fronts()

        output = []
        for current_iteration in iterations:
            sizes_of_fronts = []
            for front in current_iteration:
                sizes_of_fronts.append(len(front))
            output.append(sizes_of_fronts)

        return output
