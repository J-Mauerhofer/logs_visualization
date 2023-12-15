import re
from Iteration import Iteration


class TestGeneration:

    def __init__(self, path_to_log_file):
        # declaration of instance variables
        # open log file and set rawString to its contents
        with open(path_to_log_file, 'r') as file:
            self.rawString = file.read()

        # defining the instance variable ""iterations"
        self.iterations = []
        itSave = self.parseRawStringFromLogFileToIterations(self.rawString)
        for element in itSave:
            # creating a new Iteration object which is added to the iterations instance variable.
            iteration = Iteration(element)
            self.iterations.append(iteration)

    def parseRawStringFromLogFileToIterations(self, entireLogFileString):
        """
        This method takes a string which contains the contents of the log file
        as an input and returns a list of all iterations in the file.

        Parameters:
        entireLogFileString (string): The log file content as a string.

        Returns:
        list of strings: A list of all iterations in the file.
        """
        # Pattern to match each iteration block
        # The pattern looks for the starting "population": {"iteration": and the ending }}]}

        #old pattern is above
        pattern = r'("population": \{"iteration":.*?\}\}\]\})'
        #pattern = r'"Crossovers": \{"iteration":(.*?)\s*"Archive": \[(.*?)\]\s*\}'

        # Using re.findall to find all occurrences of the iteration blocks
        iterations = re.findall(pattern, entireLogFileString, re.DOTALL)

        #print("anzahl der iterationen: ", len(iterations))

        return iterations
