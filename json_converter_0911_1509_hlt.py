# 代码生成时间: 2025-09-11 15:09:55
import json
import numpy as np


class JSONConverter:
    """A converter class for JSON data to numpy arrays."""
    def __init__(self):
        """Initialize the JSONConverter."""
        pass

    def convert_to_numpy(self, json_data):
        """Converts JSON data to a numpy array."""
        # Load the JSON data into a Python dictionary
        try:
            data = json.loads(json_data)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON data provided: " + str(e))

        # Check if the JSON data contains a single array of numbers
        if not isinstance(data, list) or not all(isinstance(item, (int, float)) for item in data):
            raise ValueError("JSON data must be a single array of numbers.")

        # Convert the list to a numpy array
        return np.array(data)

    def convert_to_json(self, numpy_array):
        """Converts a numpy array to JSON data."""
        # Check if numpy_array is a valid numpy array
        if not isinstance(numpy_array, np.ndarray):
            raise ValueError("Input must be a numpy array.")

        # Convert the numpy array to a list
        return json.dumps(numpy_array.tolist())


# Example usage
if __name__ == '__main__':
    converter = JSONConverter()

    # Example JSON data (as a string)
    json_data = '[1, 2, 3, 4, 5]'

    # Convert JSON to numpy array
    numpy_array = converter.convert_to_numpy(json_data)
    print(f"Numpy Array: {numpy_array}
")

    # Convert numpy array back to JSON
    converted_json = converter.convert_to_json(numpy_array)
    print(f"Converted JSON: {converted_json}")