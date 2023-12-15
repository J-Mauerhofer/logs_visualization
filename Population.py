import re
from Individual import Individual


class Population:

    def __init__(self, inputString):
        self.rawString = inputString

        self.individuals = []
        for individualString in self.parseStringFromPopulationStringToIndividualsStringList(self.rawString):
            individual = Individual(individualString)
            self.individuals.append(individual)

    def parseStringFromPopulationStringToIndividualsStringList(self, log_string):
        # Regular expression pattern to match the individuals
        pattern = r"\{ \"id\":.*?\}\ \},"

        # re.DOTALL flag is used to make the '.' special character match any character at all, including a newline
        individuals = re.findall(pattern, log_string, re.DOTALL)

        return individuals

    def get_fronts(self):
        allFronts = []

        # get the largest rank
        largestRank = -1
        for individual in self.individuals:
            if largestRank < individual.rank:
                largestRank = individual.rank

        # create all fronts and add them to the fronts list
        for i in range(largestRank + 1):
            currentFront = []
            for individual in self.individuals:
                if individual.rank == i:
                    currentFront.append(individual)
            allFronts.append(currentFront)

        return allFronts

    def get_number_of_fronts(self):
        return len(self.get_fronts())
