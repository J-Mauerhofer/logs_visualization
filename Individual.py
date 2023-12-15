import re


class Individual:

    def __init__(self, inputString):
        self.rawString = inputString


        dictionary = self.extract_Data_from_individuals_String(self.rawString)
        self.id = dictionary["id"]
        self.rank = dictionary["rank"]
        self.fitness = dictionary["fitness"]
        self.distance = dictionary["distance"]
        self.code = dictionary["code"]




    def extract_Data_from_individuals_String(self, input_string):
        pattern = r'\"id\": ([\w-]+), \"rank\": (\d+), \"fitness\": ([\d.]+), \"distance\": ([\d.]+), \"code\":\{(.*?)\}'

        match = re.search(pattern, input_string, re.DOTALL)

        #assert match
        id_value, rank_value, fitness_value, distance_value, code_value = match.groups()
        return {
            "id": id_value,
            "rank": int(rank_value),
            "fitness": float(fitness_value),
            "distance": float(distance_value),
            "code": code_value
            }