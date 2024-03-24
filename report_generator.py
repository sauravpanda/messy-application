class ReportGenerator:
    def __init__(self, data):
        self.data = data
    
    def generate_report(self):
        report = "Data Report\n\n"
        
        for item in self.data:
            report += f"Category: {item['category']}\n"
            report += f"Value: {item['value']}\n"
            report += f"Average Value: {item['avg_value']}\n"
            report += f"Difference from Average: {item['diff_from_avg']}\n\n"
        
        total_value = sum(item['value'] for item in self.data)
        report += f"Total Value: {total_value}\n"
        
        return report
