import common as m

test = ("MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX")

# 0 - back up diagonal
# 1, up
# 2, forward up diagonal
# 3 back
# 4 forward
# 5 back down diagonal
# 6 down
# 7 forward down diagonal
directions = [0, 1, 2, 3, 4, 5, 6, 7]
x_directions = [0, 2, 5, 7]


def create_matrix():
    out = []
    f = open("wordsearch.txt", "r")
    letters = f.read().splitlines()
    for i in letters:
        out.append(m.make_string_list(i))
    return out


def move_direction(direction, ij_list, nrows, ncolumns):
    if direction == 0:
        ij_list[0] -= 1
        ij_list[1] -= 1
    elif direction == 1:
        ij_list[1] -= 1
    elif direction == 2:
        ij_list[0] += 1
        ij_list[1] -= 1
    elif direction == 3:
        ij_list[0] -= 1
    elif direction == 4:
        ij_list[0] += 1
    elif direction == 5:
        ij_list[0] -= 1
        ij_list[1] += 1
    elif direction == 6:
        ij_list[1] += 1
    elif direction == 7:
        ij_list[0] += 1
        ij_list[1] += 1
    else:
        print("not valid")
        return False

    if ij_list[0] < 0 or ij_list[1] < 0 or ij_list[0] >= nrows or ij_list[1] >= ncolumns:
        return False
    return True


def check_letter(search, i, j, val, direction):
    if val == 'S' and search[i][j] == val:
        return True

    new_index = [i, j]
    if not move_direction(direction, new_index, len(search), len(search[0])):
        return False

    if val == 'A' and search[i][j] == val:
        return check_letter(search, new_index[0], new_index[1], 'S', direction)
    elif val == 'M' and search[i][j] == val:
        return check_letter(search, new_index[0], new_index[1], 'A', direction)
    elif val == 'X' and search[i][j] == val:
        return check_letter(search, new_index[0], new_index[1], 'M', direction)
    return False


def check_letter_x(search, i, j, val):
    if val == search[i][j] and val != 'A':
        return True
    elif search[i][j] == 'A':

        x_values = []
        for d in x_directions:
            new_index = [i, j]
            if not move_direction(d, new_index, len(search), len(search[0])):
                return False
            x_values.append(new_index)
        diagonals = [False, False]

        if search[x_values[0][0]][x_values[0][1]] == 'M':
            if search[x_values[3][0]][x_values[3][1]] == 'S':
                diagonals[0] = check_letter_x(search, x_values[3][0], x_values[3][1], 'S') and check_letter_x(search, x_values[0][0], x_values[0][1], 'M')

        elif search[x_values[0][0]][x_values[0][1]] == 'S':
            if search[x_values[3][0]][x_values[3][1]] == 'M':
                diagonals[0] = check_letter_x(search, x_values[3][0], x_values[3][1], 'M') and check_letter_x(search, x_values[0][0], x_values[0][1], 'S')

        if search[x_values[1][0]][x_values[1][1]] == 'M':
            if search[x_values[2][0]][x_values[2][1]] == 'S':
                diagonals[1] = check_letter_x(search, x_values[2][0], x_values[2][1], 'S') and check_letter_x(search, x_values[1][0], x_values[1][1], 'M')

        elif search[x_values[1][0]][x_values[1][1]] == 'S':
            if search[x_values[2][0]][x_values[2][1]] == 'M':
                diagonals[1] = check_letter_x(search, x_values[2][0], x_values[2][1], 'M') and check_letter_x(search, x_values[1][0], x_values[1][1], 'S')

        if False in diagonals:
            return False
        else:
            return True
    else:
        return False


def find_xmas(search, find_x=True):
    xmas_count = 0
    for row in range(0, len(search)):
        for column in range(0, len(search[0])):
            if find_x:
                if check_letter_x(search, row, column, 'A'):
                    xmas_count += 1
            else:
                for d in directions:
                    if check_letter(search, row, column, 'X', d):
                        xmas_count += 1

    return xmas_count


print(find_xmas(create_matrix()))
