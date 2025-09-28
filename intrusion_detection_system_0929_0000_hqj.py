# 代码生成时间: 2025-09-29 00:00:43
import numpy as np

"""
Intrusion Detection System using Python and NumPy.
This system assumes that there is a dataset available for training.
The dataset should be labeled with 'normal' and 'intrusion'.
"""

def load_dataset(file_path):
    """
    Load the dataset from a file.
    Args:
        file_path (str): The path to the dataset file.
    Returns:
        numpy.ndarray: The loaded dataset.
    Raises:
        FileNotFoundError: If the file does not exist.
    """
    try:
        dataset = np.loadtxt(file_path)
        return dataset
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        raise


def preprocess_data(dataset):
    """
    Preprocess the dataset by scaling features.
    Args:
        dataset (numpy.ndarray): The dataset to preprocess.
    Returns:
        numpy.ndarray: The preprocessed dataset.
    """
    # Assuming the last column is the label
    features = dataset[:, :-1]
    labels = dataset[:, -1]

    # Scale the features
    features = (features - np.mean(features, axis=0)) / np.std(features, axis=0)

    return np.hstack((features, labels.reshape(-1, 1)))


def train_model(X_train, y_train):
    """
    Train a simple logistic regression model.
    Args:
        X_train (numpy.ndarray): The features for training.
        y_train (numpy.ndarray): The labels for training.
    Returns:
        model: A trained model.
    """
    # Using a simple logistic regression for demonstration purposes
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(solver='liblinear')
    model.fit(X_train, y_train)
    return model


def detect_intrusion(model, features):
    """
    Detect intrusions using the trained model.
    Args:
        model: The trained model.
        features (numpy.ndarray): The features to test.
    Returns:
        numpy.ndarray: Predictions ('normal' or 'intrusion').
    """
    # Predict the labels
    predictions = model.predict(features)
    return predictions


def main():
    """
    Main function to run the Intrusion Detection System.
    """
    # Load the dataset
    file_path = 'dataset.txt'  # Replace with your dataset file path
    dataset = load_dataset(file_path)

    # Preprocess the dataset
    dataset = preprocess_data(dataset)

    # Split the dataset into training and testing sets
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        dataset[:, :-1], dataset[:, -1], test_size=0.2, random_state=42
    )

    # Train the model
    model = train_model(X_train, y_train)

    # Detect intrusions on the test set
    predictions = detect_intrusion(model, X_test)

    # Print the results
    print('Test predictions:', predictions)

if __name__ == '__main__':
    main()