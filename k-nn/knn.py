from genericItem import generic_item

class knn:

    def __init__(self, k, items: generic_item):
        self.k = k
        self.items = items
    
    def categorize_item(self, categorizable_item: generic_item, strategy = 'euclidian'):
        knn = self._get_k_nears_neighboors(categorizable_item, strategy)
        categories: dict = {}
        for item in map(lambda knn: knn[0], knn):
            categories[item.category] = categories.get(item.category, 0) + 1
        
        return max(categories, key=categories.get)

    def get_categorize_distance_function(item: generic_item, strategy: str):
        return item.calculate_euclidian_distance if strategy == 'euclidian' else item.calculate_manhattan_distance
    
    def _get_k_nears_neighboors(self, new_item: generic_item, strategy: str):
        items_distance = []
        for item in self.items:
            distance_function = knn.get_categorize_distance_function(item, strategy)
            items_distance.append((item, distance_function(new_item.features)))
        
        items_distance.sort(key=lambda item_groud: item_groud[1], reverse=True)
        return items_distance[0:self.k]