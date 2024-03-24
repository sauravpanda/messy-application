from utils import calculate_average, filter_data

class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    def process_data(self):
        processed_data = []
        for item in self.data:
            item['value'] = float(item['value'])
            processed_data.append(item)
        
        categories = []
        for item in processed_data:
            if item['category'] not in categories:
                categories.append(item['category'])
        
        for category in categories:
            category_data = filter_data(processed_data, 'category', category)
            values = [item['value'] for item in category_data]
            avg_value = calculate_average(values)
            
            for item in category_data:
                item['avg_value'] = avg_value
                item['diff_from_avg'] = item['value'] - avg_value
        
        sorted_data = sorted(processed_data, key=lambda x: x['value'], reverse=True)
        
        return sorted_data
