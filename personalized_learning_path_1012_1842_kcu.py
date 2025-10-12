# 代码生成时间: 2025-10-12 18:42:56
import numpy as np

"""
Personalized Learning Path program using Python and NumPy.
This program allows the creation of a learning path tailored to the user's needs.
It includes error handling, appropriate documentation, and follows Python best practices.
"""

# Define the learning materials available for each topic
learning_materials = {
    "Mathematics": ["Algebra", "Geometry", "Calculus"],
    "Science": ["Physics", "Chemistry", "Biology"],
    "Programming": ["Python", "Java", "C++"]
}


# Custom exception for invalid user choices
class InvalidChoiceError(Exception):
    pass


def get_user_choice(topic):
    """
    Get a valid choice from the user.

    Parameters:
        topic (str): The topic for which the user needs to choose a material.

    Returns:
        str: The chosen material.
    """
    materials = learning_materials.get(topic, [])
    if not materials:
        raise ValueError(f"No materials available for topic: {topic}")

    print(f"Available materials for {topic}: {materials}")
    while True:
        try:
            choice = input(f"Enter your choice ({', '.join(materials)}): ")
            if choice in materials:
                return choice
            else:
                print("Invalid choice. Please try again.")
        except KeyboardInterrupt:
            print("
User interrupted the program.")
            exit()
        except Exception as e:
            print(f"An error occurred: {e}")
            raise


def personalized_learning_path():
    """
    Generate a personalized learning path based on user's choices.

    This function iterates over each topic and uses get_user_choice to get the user's choice
    for the learning material.
    """
    topics = list(learning_materials.keys())
    learning_path = []

    for topic in topics:
        try:
            material = get_user_choice(topic)
            learning_path.append((topic, material))
        except InvalidChoiceError:
            print(f"Invalid choice for topic: {topic}")
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print("
User interrupted the program.")
            exit()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    return learning_path


def main():
    """
    Main function to run the personalized learning path program.
    """
    try:
        learning_path = personalized_learning_path()
        print("
Your personalized learning path is: ")
        for topic, material in learning_path:
            print(f"{topic}: {material}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()