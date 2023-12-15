import re
from Population import Population


class Iteration:
    def __init__(self, inputString):
        self.rawString = inputString

        self.population = Population(self.parseRawStringFromIterationToPopulation(self.rawString))

    def parseRawStringFromIterationToPopulation(self, iterationString):
        """
        This method takes a string which is one iteration in the log file and returns
        a list of the population in this iteration.

        Returns:
        string: the string of the iteration
        """
        # Regular expression pattern to match the desired iteration block
        pattern = r'popStart\[.*?\]popEnd'

        # Find all occurrences of the pattern in the iteration
        matches = re.findall(pattern, iterationString, re.DOTALL)

        # the length has to be exactly one because exactly one population exists per iteration
        #print(iterationString)
        assert (len(matches) == 1)

        return matches[0]
