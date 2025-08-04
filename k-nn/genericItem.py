import math

class generic_item:

    def __init__(self, features: dict, category: str):
        self.features = features
        self.category = category

    def calculate_euclidian_distance(self, features: dict):
        dimensions_distance = 0
        for key in features.keys():
            dimensions_distance += math.pow((self.features[key] - features[key]), 2)
        return math.sqrt(dimensions_distance)
    
    def calculate_manhattan_distance(self, features: dict):
        dimensions_distance = 0
        for key in features.keys():
            dimensions_distance += abs(self.features[key] - features[key])
        return dimensions_distance
    
    def __str__(self):
        return f'\ncategory: {self.category}\nfeatures: {self.features}'