"""
* Name: Skyler Choi
* Date: Feb 5th
* CSE 160, Autumn 2024
* Homework 4
* Description:
* Collaboration:
"""


from utils import (
    converged, plot_2d, plot_centroids, plot_fig, read_data,
    load_centroids, write_centroids_with_key
    )  # noqa: F401
import math  # noqa: F401
import os


def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two data points.

    Arguments:
        point1: a non-empty list of floats representing a data point
        point2: a non-empty list of floats representing a data point

    Returns: the Euclidean distance between two data points

    Example:
        Code:
            point1 = [1.1, 1, 1, 0.5]
            point2 = [4, 3.14, 2, 1]
            print(euclidean_distance(point1, point2))
        Output:
            3.7735394525564456
    """

    distance = 0
    sums = 0
    first_calc = 0
    n2 = 0  # variable for assigning (n2)th number in point2 list
    for num_pt_1 in point1:
        first_calc = ((num_pt_1) - (point2[n2])) ** 2
        n2 = n2 + 1
        sums = sums + first_calc
    distance = math.sqrt(sums)
    return distance
    pass


def get_closest_centroid(point, centroids_dict):
    """
    Given a data point, finds the closest centroid. You should use
    the euclidean_distance function (that you previously implemented).

    Arguments:
        point: a list of floats representing a data point
        centroids_dict: a dictionary representing the centroids where the keys
                        are strings (centroid names) and the values are lists
                        of centroid locations

    Returns: a string as the key name of the closest centroid to the data point

    Example:
        Code:
            point = [0, 0, 0, 0]
            centroids_dict = {"centroid1": [1, 1, 1, 1],
                            "centroid2": [2, 2, 2, 2]}
            print(get_closest_centroid(point, centroids_dict))
        Output:
            centroid1
    """
    # function will first calculate eucl.dist of pt & 1st centroid in the dict
    # Then it will for loop through the dict and calculate eucl.dist for
    # each centroids.
    # final_centroid is a variable that will be returned & printed.
    # final_centroid is set initially as first centroid in dict.
    # but if the next cent has smaller eucl.dist, it will change to
    # the corresponding centroid.

    test_distance = euclidean_distance(point, list(centroids_dict.values())[0])
    final_centroid = list(centroids_dict.keys())[0]

    for centroid_name in centroids_dict.keys():
        test_centroid2 = centroids_dict[centroid_name]
        test_distance2 = euclidean_distance(point, test_centroid2)
        if test_distance2 < test_distance:
            final_centroid = centroid_name
            test_distance = test_distance2
    return final_centroid
    pass


def assign_points_to_centroids(list_of_points, centroids_dict):
    """
    Assign all data points to the closest centroids. You should use
    the get_closest_centroid function (that you previously implemented).

    This function should return a new dictionary, not modify any
    passed in parameters.

    Arguments:
        list_of_points: a list of lists representing all data points
        centroids_dict: a dictionary representing the centroids where the keys
                        are strings (centroid names) and the values are lists
                        of centroid locations

    Returns: a new dictionary whose keys are the centroids' key names and
             values are lists of points that belong to the centroid. If a
             given centroid does not have any data points closest to it,
             do not include the centroid in the returned dictionary

    Example:
        Code:
            list_of_points = [[1.1, 1, 1, 0.5], [4, 3.14, 2, 1], [0, 0, 0, 0]]
            centroids_dict = {"centroid1": [1, 1, 1, 1],
                            "centroid2": [2, 2, 2, 2]}

            print(assign_points_to_centroids(list_of_points, centroids_dict))
        Output:
            {'centroid1': [[1.1, 1, 1, 0.5], [0, 0, 0, 0]],
             'centroid2': [[4, 3.14, 2, 1]]}
    """
    output_dict = {}
    for test_point in list_of_points:
        close_centroid = get_closest_centroid(test_point, centroids_dict)
        if close_centroid in output_dict:
            output_dict[close_centroid].append(test_point)
        else:
            output_dict[close_centroid] = [test_point]
    return output_dict
    pass


def mean_of_points(list_of_points):
    """
    Calculate the mean of a given group of data points. You should NOT
    hard-code the dimensionality of the data points).

    Arguments:
        list_of_points: a list of lists representing a group of data points

    Returns: a list of floats as the mean of the given data points

    Example:
        Code:
            list_of_points = [[1.1, 1, 1, 0.5], [4, 3.14, 2, 1], [0, 0, 0, 0]]
            print(mean_of_points(list_of_points))
        Output:
            [1.7, 1.3800000000000001, 1.0, 0.5]
    """

    mean_points_list = []
    for i in range(len(list_of_points[0])):
        sum = 0
        # sum for num of same index of num_list's
        for num_list in list_of_points:
            sum += num_list[i]
        mean_point = sum / len(list_of_points)
        mean_points_list.append(mean_point)
    return mean_points_list
    pass


def update_centroids(assignment_dict):
    """
    Update centroid locations as the mean of all data points that belong
    to the cluster. You should use the mean_of_points function (that you
    previously implemented).

    This function should return a new dictionary, not modify any
    passed in parameters.

    Arguments:
        assignment_dict: a dictionary whose keys are the centroids' key
                         names and values are lists of points that belong
                         to the centroid. It is the dictionary
                         returned by assign_points_to_centroids function.

    Returns: A new dictionary representing the updated centroids. If a
             given centroid does not have any data points closest to it,
             do not include the centroid in the returned dictionary.

    Example:
        Code:
            assignment_dict = {'centroid1': [[1.1, 1, 1, 0.5], [0, 0, 0, 0]],
                               'centroid2': [[4, 3.14, 2, 1]]}
            print(update_centroids(assignment_dict))
        Output:
          {'centroid1': [0.55, 0.5, 0.5, 0.25],
           'centroid2': [4.0, 3.14, 2.0, 1.0]}
    """

    updated_dict = {}
    for centroid in assignment_dict:
        updated_dict[centroid] = mean_of_points(assignment_dict[centroid])
    return updated_dict
    pass


def main(data, init_centroids, dataset):
    #########################################################################
    # You do not need to change anything in this function.
    # However it is HIGHLY RECOMMENDED to read through and understand what it
    # does. Particularly, the first few lines of the `while` loop show the
    # general flow of the k-means algorithm and how the data flows through
    # the functions you will implement for this assignment.
    #########################################################################
    if dataset == "2d":
        plot_steps, plot_init, plot_final = True, False, False
    elif dataset == "mnist":
        plot_steps, plot_init, plot_final = False, True, True

    centroids = init_centroids
    old_centroids = None
    step = 0

    if plot_init:
        # plot initial centroids
        plot_centroids(centroids, "init")

    while not converged(centroids, old_centroids):
        # save old centroid
        old_centroids = centroids
        # new assignment
        assignment_dict = assign_points_to_centroids(data, old_centroids)
        # update centroids
        centroids = update_centroids(assignment_dict)
        step += 1

        if plot_steps:
            # plot centroid
            fig = plot_2d(assignment_dict, centroids)
            results_dir = os.path.join("results", "2D")
            plot_fig(fig, results_dir, f"step{step}")

    print(f"K-means converged after {step} steps.")

    if plot_final:
        # plot final centroids
        plot_centroids(centroids, "final")

    return centroids


if __name__ == "__main__":
    dataset = "mnist"

    data, label = read_data("data/" + dataset + ".csv")
    init_c = load_centroids("data/" + dataset + "_init_centroids.csv")
    final_c = main(data, init_c, dataset)
    write_centroids_with_key(dataset + "_final_centroids.csv", final_c)
