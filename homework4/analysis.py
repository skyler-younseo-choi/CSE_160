"""
* Name: Skyler Choi
* Date:
* CSE 160, Autumn 2024
* Homework 4
* Description:
* Collaboration:
"""

from utils import load_centroids, read_data
from kmeans import get_closest_centroid  # noqa: F401


# ----------------------------------------------------------
# PROBLEMS FOR STUDENTS
def assign_labels(list_of_points, labels, centroids_dict):
    """
    Assign all data points to the closest centroids and keep track of their
    labels. The i-th point in "data" corresponds to the i-th label in "labels".

    Arguments:
        list_of_points: a list of lists representing all data points
        labels: a list of strings representing all data labels
                labels[i] is the label of the point list_of_points[i]
        centroids_dict: a dictionary representing the centroids where the keys
                        are strings (centroid names) and the values are lists
                        of centroid locations

    Returns: a new dictionary whose keys are the centroids' key names and
             values are a list of labels of the data points that are assigned
             to that centroid.

    Example:
        Code:
            list_of_points = [[1.1, 1, 1, 0.5], [4, 3.14, 2, 1], [0, 0, 0, 0]]
            labels = ['N', 'M', 'W']
            centroids_dict = {"centroid1": [1, 1, 1, 1],
                              "centroid2": [2, 2, 2, 2]}
            print(assign_labels(list_of_points, labels, centroids_dict))
        Output:
            {'centroid1': ['M', 'N'], 'centroid2': ['W']}
    """

    output_dict = {}
    n = 0
    for test_point in list_of_points:
        close_centroid = get_closest_centroid(test_point, centroids_dict)
        label = labels[n]
        if close_centroid in output_dict:
            output_dict[close_centroid].append(label)
        else:
            output_dict[close_centroid] = [label]
        n += 1
    return output_dict
    pass


def majority_count(labels):
    """
    Return the count of the majority label in the label list.

    Arguments:
        labels: a list of labels

    Returns: the count of the majority labels in the list

    Example:
        Given labels = ['M', 'M', 'N']
        majority_count(labels) returns 2
    """

    letter_count_dict = {}
    for letter in labels:
        if letter in letter_count_dict:
            # letter_count += 1
            letter_count_dict[letter] += 1  # letter_count
        else:
            letter_count_dict[letter] = 1
    max_letter_count = 0
    for letter in letter_count_dict:
        if max_letter_count < letter_count_dict[letter]:
            max_letter_count = letter_count_dict[letter]
            # max_letter = letter
    # print(max_letter)
    return max_letter_count
    pass


def accuracy(list_of_points, labels, centroids_dict):
    """
    Calculate the accuracy of the algorithm. You should use assign_labels and
    majority_count (that you previously implemented)

    Arguments:
        list_of_points: a list of lists representing all data points
        labels: a list of ints representing all data labels
                labels[i] is the label of the point list_of_points[i]
        centroids_dict: a dictionary representing the centroids where the keys
                        are strings (centroid names) and the values are lists
                        of centroid locations

    Returns: a float representing the accuracy of the algorithm
    """
    assign_output = assign_labels(list_of_points, labels, centroids_dict)
    total_num = 0
    for key in assign_output:
        # listvalues = assign_output[key]  # Returns the value of key
        # total_labels = len(listvalues)  # length=total # of labels each pt
        num = majority_count(assign_output[key])
        # calculate accuracty for each centroids
        # indiv_accuracy = num / total_labels
        total_num = total_num + num
        # print(key, indiv_accuracy)
    accuracy = total_num / len(labels)
    return accuracy
    pass


if __name__ == "__main__":
    centroids = load_centroids("mnist_final_centroids.csv", with_key=True)
    # Consider exploring the centroids data here

    data, label = read_data("data/mnist.csv")
    print(accuracy(data, label, centroids))
    print(list(centroids.keys()))
