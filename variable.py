import csv
import os

# ============================================
# 1. VARIABLES & FILE HANDLING
# ============================================
def read_numerical_data(filename):
    """Read numerical data from a CSV or text file"""
    data = []
    try:
        with open(filename, 'r') as file:
            # Check if file is CSV or plain text
            if filename.endswith('.csv'):
                reader = csv.reader(file)
                for row in reader:
                    if row:  # Skip empty rows
                        for value in row:
                            if value.strip():  # Skip empty strings
                                data.append(value.strip())
            else:
                # Plain text file - one value per line
                for line in file:
                    value = line.strip()
                    if value:  # Skip empty lines
                        data.append(value)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{filename}' not found")
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")

def read_categorical_data(filename):
    """Read categorical data from a file"""
    categories = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                category = line.strip()
                if category:  # Skip empty lines
                    categories.append(category)
        return categories
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{filename}' not found")

# ============================================
# 2. ERROR HANDLING
# ============================================
def validate_numerical_data(data):
    """Validate and convert data to floats"""
    validated_data = []
    if not data:
        raise ValueError("Error: File is empty")
    
    for i, value in enumerate(data, 1):
        try:
            num = float(value)
            validated_data.append(num)
        except ValueError:
            raise ValueError(f"Error: Invalid non-numeric value '{value}' at position {i}")
    
    return validated_data

# ============================================
# 3. FUNCTIONS
# ============================================
def calculate_total(data):
    """Calculate the total of numerical data"""
    total = 0
    for value in data:
        total += value
    return total

def calculate_average(data):
    """Calculate the average of numerical data"""
    if not data:
        return 0
    total = calculate_total(data)
    return total / len(data)

def calculate_minimum(data):
    """Find the minimum value in numerical data"""
    if not data:
        return None
    minimum = data[0]
    for value in data[1:]:
        if value < minimum:
            minimum = value
    return minimum

def calculate_maximum(data):
    """Find the maximum value in numerical data"""
    if not data:
        return None
    maximum = data[0]
    for value in data[1:]:
        if value > maximum:
            maximum = value
    return maximum

# ============================================
# 4. OPERATORS & LOOPS (Already implemented in functions above)
# Using arithmetic operators and loops in:
# - calculate_total: uses + operator and for loop
# - calculate_average: uses / operator
# - calculate_minimum/maximum: uses comparison operators and for loops
# ============================================

# ============================================
# 5. CONDITIONAL STATEMENTS
# ============================================
def evaluate_performance(average, threshold=75):
    """Evaluate performance based on average score"""
    if average >= threshold:
        return "High Performance"
    else:
        return "Needs Improvement"

# ============================================
# 6. SETS
# ============================================
def get_unique_categories(categories):
    """Extract unique categories using sets"""
    unique_categories = set(categories)
    return unique_categories, len(unique_categories)

# ============================================
# 7. OBJECT-ORIENTED PROGRAMMING
# ============================================
class DataSet:
    def __init__(self, numerical_file=None, categorical_file=None):
        self.numerical_file = numerical_file
        self.categorical_file = categorical_file
        self.numerical_data = []
        self.categorical_data = []
        self.statistics = {}
        self.unique_categories = set()
        
    def load_data(self):
        """Load data from both numerical and categorical files"""
        try:
            # Load numerical data
            if self.numerical_file:
                raw_data = read_numerical_data(self.numerical_file)
                self.numerical_data = validate_numerical_data(raw_data)
                print(f" Loaded {len(self.numerical_data)} numerical records")
            
            # Load categorical data
            if self.categorical_file:
                self.categorical_data = read_categorical_data(self.categorical_file)
                print(f"Loaded {len(self.categorical_data)} categorical records")
                
        except Exception as e:
            print(f" Error loading data: {str(e)}")
            raise
    
    def calculate_statistics(self, threshold=75):
        """Calculate all statistics"""
        if self.numerical_data:
            self.statistics = {
                'total': calculate_total(self.numerical_data),
                'average': calculate_average(self.numerical_data),
                'minimum': calculate_minimum(self.numerical_data),
                'maximum': calculate_maximum(self.numerical_data),
                'count': len(self.numerical_data),
                'performance': evaluate_performance(
                    calculate_average(self.numerical_data), 
                    threshold
                )
            }
        
        if self.categorical_data:
            self.unique_categories, unique_count = get_unique_categories(self.categorical_data)
            self.statistics['unique_categories'] = unique_count
    
    def display_results(self):
        """Display analysis results"""
        print("\n" + "="*50)
        print("DATASET ANALYSIS REPORT")
        print("="*50)
        
        if self.numerical_data:
            print("\nNUMERICAL DATA ANALYSIS:")
            print(f"  • Data Points: {self.statistics.get('count', 0):,}")
            print(f"  • Total: {self.statistics.get('total', 0):.2f}")
            print(f"  • Average: {self.statistics.get('average', 0):.2f}")
            print(f"  • Minimum: {self.statistics.get('minimum', 0):.2f}")
            print(f"  • Maximum: {self.statistics.get('maximum', 0):.2f}")
            print(f"  • Performance: {self.statistics.get('performance', 'N/A')}")
        
        if self.categorical_data:
            print("\nCATEGORICAL DATA ANALYSIS:")
            print(f"  • Total Categories: {len(self.categorical_data)}")
            print(f"  • Unique Categories: {self.statistics.get('unique_categories', 0)}")
            if self.unique_categories:
                print(f"  • Unique Values: {', '.join(sorted(self.unique_categories))}")
        
        print("\n" + "="*50)

# ============================================
# 8. SAVING RESULTS
# ============================================
def save_report(statistics, unique_categories, filename="analysis_report.txt"):
    """Save analysis results to a report file"""
    try:
        with open(filename, 'w') as file:
            file.write("DATASET ANALYSIS REPORT\n")
            file.write("="*50 + "\n\n")
            
            if 'count' in statistics:
                file.write("NUMERICAL DATA STATISTICS:\n")
                file.write("-"*30 + "\n")
                file.write(f"Total Data Points: {statistics.get('count', 0):,}\n")
                file.write(f"Sum: {statistics.get('total', 0):.2f}\n")
                file.write(f"Average: {statistics.get('average', 0):.2f}\n")
                file.write(f"Minimum: {statistics.get('minimum', 0):.2f}\n")
                file.write(f"Maximum: {statistics.get('maximum', 0):.2f}\n")
                file.write(f"Performance: {statistics.get('performance', 'N/A')}\n\n")
            
            if 'unique_categories' in statistics:
                file.write("CATEGORICAL DATA ANALYSIS:\n")
                file.write("-"*30 + "\n")
                file.write(f"Unique Categories: {statistics.get('unique_categories', 0)}\n")
                if unique_categories:
                    file.write("List of Unique Categories:\n")
                    for category in sorted(unique_categories):
                        file.write(f"  - {category}\n")
            
            file.write("\n" + "="*50 + "\n")
            file.write("Report generated by Dataset Management System\n")
        
        print(f"Report saved to '{filename}'")
        return True
    except Exception as e:
        print(f" Error saving report: {str(e)}")
        return False

# ============================================
# MAIN PROGRAM EXECUTION
# ============================================
def main():
    print("DATASET MANAGEMENT AND BASIC ANALYSIS SYSTEM")
    print("="*50)
    
    # File names (you can change these to your actual file names)
    NUMERICAL_FILE = "sample_data.csv"  # Change to your file
    CATEGORICAL_FILE = "categories.txt"  # Change to your file
    
    # Create sample data files if they don't exist
    if not os.path.exists(NUMERICAL_FILE):
        print(f"\nCreating sample numerical file: {NUMERICAL_FILE}")
        sample_data = """85,92,78,65,88,91,76,82,95,70
                        73,89,81,67,94,79,86,90,68,84"""
        with open(NUMERICAL_FILE, 'w') as f:
            f.write(sample_data)
    
    if not os.path.exists(CATEGORICAL_FILE):
        print(f"Creating sample categorical file: {CATEGORICAL_FILE}")
        sample_categories = """Mathematics
        Physics
        Chemistry
        Biology
        Mathematics
        Physics
        Computer Science
        Mathematics
        Biology
        Chemistry
        Physics
        Mathematics"""
        with open(CATEGORICAL_FILE, 'w') as f:
            f.write(sample_categories)
    
    # Create DataSet object
    dataset = DataSet(NUMERICAL_FILE, CATEGORICAL_FILE)
    
    try:
        # 1. Load data
        print("\n1. LOADING DATA...")
        dataset.load_data()
        
        # 2. Calculate statistics with threshold of 75
        print("\n2. CALCULATING STATISTICS...")
        dataset.calculate_statistics(threshold=75)
        
        # 3. Display results
        print("\n3. ANALYSIS RESULTS:")
        dataset.display_results()
        
        # 4. Save report
        print("\n4. SAVING REPORT...")
        save_report(
            dataset.statistics, 
            dataset.unique_categories, 
            "dataset_analysis_report.txt"
        )
        
        print("\n" + "="*50)
        print("ANALYSIS COMPLETED SUCCESSFULLY!")
        
    except Exception as e:
        print(f"\n Program terminated with error: {str(e)}")

# ============================================
# RUN THE PROGRAM
# ============================================
if __name__ == "__main__":
    main()