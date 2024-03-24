from utils import *
from data_processor import DataProcessor
from report_generator import ReportGenerator

def main():
    data = load_data('data.csv')
    processor = DataProcessor(data)
    processed_data = processor.process_data()
    
    report_data = []
    for item in processed_data:
        if item['value'] > 10:
            report_data.append(item)
    
    generator = ReportGenerator(report_data)
    report = generator.generate_report()
    
    print(report)

if __name__ == '__main__':
    main()
