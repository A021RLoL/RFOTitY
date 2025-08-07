# 代码生成时间: 2025-08-07 23:57:12
import numpy as np
import json
import os
import sys

"""
Test Report Generator

This program generates a test report based on the test results in a specified CSV file.
The report includes the number of tests run, the number of tests passed,
the number of tests failed, and detailed information about each test.
"""

class TestReportGenerator:

    def __init__(self, test_results_file):
        """
        Initialize the TestReportGenerator with the test results file.
        
        Args:
        test_results_file (str): The path to the CSV file containing test results.
        """
        self.test_results_file = test_results_file
        self.test_results = None

    def load_test_results(self):
        """
        Load the test results from the CSV file.
        
        Returns:
        None
        """
        try:
            self.test_results = np.genfromtxt(self.test_results_file, delimiter=',', dtype=None, encoding='utf-8')
        except FileNotFoundError:
            print(f"Error: The file {self.test_results_file} does not exist.")
            sys.exit(1)
        except Exception as e:
            print(f"Error: An error occurred while loading test results - {e}")
            sys.exit(1)

    def generate_report(self):
        """
        Generate the test report based on the loaded test results.
        
        Returns:
        str: The generated test report in JSON format.
        """
        if self.test_results is None:
            print("Error: Test results have not been loaded.")
            sys.exit(1)

        report = {
            "total_tests": len(self.test_results),
            "passed_tests": len([row for row in self.test_results if row[1] == 'PASS']),
            "failed_tests": len([row for row in self.test_results if row[1] == 'FAIL']),
            "test_details": []
        }

        for i, row in enumerate(self.test_results):
            test_detail = {
                "test_name": row[0],
                "test_result": row[1],
                "test_message": row[2],
                "test_id": i + 1
            }
            report["test_details"].append(test_detail)

        return json.dumps(report, indent=4)

if __name__ == '__main__':
    test_results_file = 'test_results.csv'
    generator = TestReportGenerator(test_results_file)
    generator.load_test_results()
    report = generator.generate_report()
    print(report)
    
    # Save the report to a file
    with open('test_report.json', 'w') as report_file:
        report_file.write(report)
