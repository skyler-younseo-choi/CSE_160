# Name: Skyler Choi
# CSE 160
# Homework 5

import utils  # noqa: F401, do not remove if using a Mac
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter


###
#  Problem 1a
###

def get_practice_graph():
    """Builds and returns the practice graph
    """
    practice_graph = nx.Graph()
    letters = ["A", "B", "C", "D", "E", "F"]
    for letter in letters:
        practice_graph.add_node(letter)

    practice_graph.add_edge("A", "B")
    practice_graph.add_edge("A", "C")
    practice_graph.add_edge("B", "C")
    practice_graph.add_edge("B", "D")
    practice_graph.add_edge("C", "D")
    practice_graph.add_edge("C", "F")
    practice_graph.add_edge("D", "F")
    practice_graph.add_edge("D", "E")

    return practice_graph


def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()


###
#  Problem 1b
###

def get_romeo_and_juliet_graph():
    """Builds and returns the romeo and juliet graph
    """
    rj = nx.Graph()
    people = ["Nurse", "Juliet", "Tybalt", "Capulet", "Friar Laurence",
              "Romeo", "Benvolio", "Montague", "Escalus", "Mercutio", "Paris"]
    for person in people:
        rj.add_node(person)
    rj.add_edge("Juliet", "Nurse")
    rj.add_edge("Juliet", "Tybalt")
    rj.add_edge("Juliet", "Capulet")
    rj.add_edge("Juliet", "Friar Laurence")
    rj.add_edge("Juliet", "Romeo")
    rj.add_edge("Tybalt", "Capulet")
    rj.add_edge("Capulet", "Paris")
    rj.add_edge("Capulet", "Escalus")
    rj.add_edge("Friar Laurence", "Romeo")
    rj.add_edge("Romeo", "Benvolio")
    rj.add_edge("Romeo", "Montague")
    rj.add_edge("Romeo", "Mercutio")
    rj.add_edge("Escalus", "Montague")
    rj.add_edge("Escalus", "Paris")
    rj.add_edge("Escalus", "Mercutio")
    rj.add_edge("Paris", "Mercutio")
    rj.add_edge("Benvolio", "Montague")
    return rj


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()


###
#  Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


def friends_of_friends(graph, user):
    """Find and return the friends of friends of the given user.

    Arguments:
        graph: the graph object that contains the user and others
        user: unique identifier

    Returns: a set containing the names of all of the friends of
    friends of the user. The set should not contain the user itself
    or their immediate friends.
    """
    user_friends = friends(graph, user)
    total_fyfof = set()
    for friend in user_friends:
        friend_y_fof = friends(graph, friend)
        total_fyfof = total_fyfof | friend_y_fof
    user_friends.add(user)
    fof = total_fyfof - user_friends
    return fof


def common_friends(graph, user1, user2):
    """
    Finds and returns the set of friends that user1
    and user2 have in common.

    Arguments:
        graph:  the graph object that contains the users
        user1: a unique identifier representing one user
        user2: a unique identifier representing another user

    Returns: a set containing the friends user1 and user2 have in common
    """
    # user1_friends = friends(graph, user1)
    # user2_friends = friends(graph, user2)
    # set_cf = user1_friends & user2_friends
    return friends(graph, user1) & friends(graph, user2)


def common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }

    Arguments:
        graph: the graph object that contains the user and others
        user: unique identifier

    Returns: a dictionary mapping each person to the number of (non-zero)
    friends they have in common with the user
    """
    com_friends_map_d = {}
    for person in friends_of_friends(graph, user):
        num_com_friends = len(common_friends(graph, user, person))
        com_friends_map_d[person] = num_com_friends
    return com_friends_map_d


def num_map_to_sorted_list(map_with_number_vals):
    """Given a dictionary, return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.

    Arguments:
        map_with_number_vals: a dictionary whose values are numbers

    Returns: a list of keys, sorted by the values in map_with_number_vals
    """
    sorted_alph_list = sorted(map_with_number_vals.items(), key=itemgetter(0))
    sorted_num_list = sorted(sorted_alph_list, key=itemgetter(1), reverse=True)
    sorted_key_list = []
    for tuple_pair in sorted_num_list:
        alphabet = itemgetter(0)(tuple_pair)
        sorted_key_list.append(alphabet)
    return sorted_key_list


def recs_by_common_friends(graph, user):
    """
    Returns a list of friend recommendations for the user, sorted
    by number of friends in common.

    Arguments:
        graph: the graph object that contains the user and others
        user: a unique identifier

    Returns: A list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    recs_of_com_f = num_map_to_sorted_list(common_friends_map(graph, user))
    return recs_of_com_f


###
#  Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """
    initial_dict = common_friends_map(graph, user)
    # common_friends_map(rj, Benvolio) == {'Benvolio': 1, 'Capulet': 2,
    # 'Friar Laurence': 1, 'Juliet': 1, 'Montague': 2}
    influence_score = 0
    for person_key in initial_dict:  # Capulet
        set_A = common_friends(graph, user, person_key)
        # common_friends(rj, Mercutio, Capulet) = [Escalus, Paris]
        for common_friend_person in set_A:  # 1) common_friend_person=[Escalus]
            numfriends_person_key = len(friends(graph, common_friend_person))
            # 1) numfriends_person_key = len(friends(graph, Escalus))
            # 1) friends(graph, Escalus) = [Capulet, Montague, Mercutio, Paris]
            # 1) len(friends) = 4
            reciprocal = 1 / numfriends_person_key
            # 1) reciprocal = 1 / 4 = 0.25
            influence_score = influence_score + reciprocal
            initial_dict[person_key] = influence_score
            # I think this is the problem
        influence_score = 0
    return initial_dict


def recs_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    influence_recs_lst = num_map_to_sorted_list(influence_map(graph, user))
    return influence_recs_lst


###
#  Problem 5
###

def get_facebook_graph(filename):
    """Builds and returns the facebook graph
    Arguments:
        filename: the name of the datafile
    """
    facebook = nx.Graph()
    fb_file = open(filename)
    for line in fb_file:
        split_string = line.split()
        int_0 = int(split_string[0])
        int_1 = int(split_string[1])
        facebook.add_edge(int_0, int_1)
    return facebook


def test_get_facebook_graph(facebook, filename):
    if (filename == "facebook-links-small.txt"):
        pass
    else:
        assert len(facebook.nodes()) == 63731
        assert len(facebook.edges()) == 817090


def main():
    # practice_graph = get_practice_graph()
    # Make sure to comment out this line after you have visually verified
    # your practice graph. Otherwise, the picture will pop up every time
    # that you run your program.
    # draw_practice_graph(practice_graph)

    rj = get_romeo_and_juliet_graph()
    # Make sure to comment out this line after you have visually verified
    # your rj graph and created your PDF file. Otherwise, the picture will
    # pop up every time that you run your program.
    # draw_rj(rj)

    ###
    #  Problem 4
    ###

    print("Problem 4:")
    print()

    Unchanged_Rec = []
    Changed_Rec = []
    rj_list = list(rj.nodes)
    for character in rj_list:
        # print(character)
        # print(recs_by_common_friends(rj, character))
        # print(recs_by_influence(rj, character))
        if (recs_by_common_friends(rj, character) ==
                recs_by_influence(rj, character)):
            Unchanged_Rec.append(character)
        else:
            Changed_Rec.append(character)
    Unchanged_Rec.sort()
    Changed_Rec.sort()
    print("Unchanged Recommendations:", Unchanged_Rec)
    print("Changed Recommendations:", Changed_Rec)

    ###
    #  Problem 5
    ###

    # (replace this filename with "facebook-links-small.txt" for testing)
    fb_filename = "facebook-links-small.txt"

    facebook = get_facebook_graph(fb_filename)

    test_get_facebook_graph(facebook, fb_filename)

    ###
    #  Problem 6
    ###
    print()
    print("Problem 6:")
    print()
    # Creating a list that is sorted & div by 1000
    users_list = list(facebook.nodes)
    divisible_by_1000 = []
    for user_ID in users_list:
        if user_ID % 1000 == 0:
            divisible_by_1000.append(user_ID)
    sorted_users_list = sorted(divisible_by_1000)
    # solving for prob 6
    final_comp_com_list = []
    for user_ID in sorted_users_list:
        rec_com_list = recs_by_common_friends(facebook, user_ID)
        final_rec_com_list = rec_com_list[0:10]
        final_comp_com_list.append(final_rec_com_list)
        print(user_ID, "(by num_common_friends):", final_rec_com_list)

    ###
    #  Problem 7
    ###
    print()
    print("Problem 7:")
    print()
    final_comp_inf_list = []
    for user_ID in sorted_users_list:
        rec_inf_list = recs_by_influence(facebook, user_ID)
        final_rec_inf_list = rec_inf_list[0:10]
        final_comp_inf_list.append(final_rec_inf_list)
        print(user_ID, "(by influence):", final_rec_inf_list)

    ###
    #  Problem 8
    ###
    print()
    print("Problem 8:")
    print()

    Same_count = 0
    Different_count = 0
    for num in range(len(final_comp_inf_list)):
        if final_comp_inf_list[num] == final_comp_com_list[num]:
            Same_count += 1
        else:
            Different_count += 1
    print("Same:", Same_count)
    print("Different:", Different_count)


if __name__ == "__main__":
    main()


###
#  Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").
