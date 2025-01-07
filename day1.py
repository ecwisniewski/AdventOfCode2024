import common as m

test1 = [3, 4, 2, 1, 3, 3]
test2 = [4, 3, 5, 3, 9, 3]


def setup_input():
    l1 = []
    l2 = []
    f = open("input.txt", "r")
    for i in f:
        element = i.split()
        l1.append(element[0])
        l2.append(element[1])

    return l1, l2


def get_dist_btw_lists(l1, l2):
    distance = 0

    # Compare lists
    a1 = m.separate_string_list(l1)
    a2 = m.separate_string_list(l2)
    if len(a1) != len(a2):
        raise "Error with comparison"
    for i in range(0, len(a1)):

        # Find Smallest Numbers
        s1 = min(a1)
        s2 = min(a2)

        # Remove From List
        a1.remove(s1)
        a2.remove(s2)

        # Add Distance
        distance += abs(s1 - s2)

    return distance


def get_similarity_score(l1, l2):
    similarity = 0
    for i in range(0, len(l1)):
        similarity += int(l1[i]) * l2.count(l1[i])
    return similarity


def run_day1_answers():
    list1, list2 = setup_input()
    d = get_dist_btw_lists(list1, list2)
    print(f'Distance {d}')
    s = get_similarity_score(list1, list2)
    print(f'Similarity Score {s}')
