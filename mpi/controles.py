syracuse_list = []


def syracuse(current, index):
    if index == 0:
        syracuse_list.append(current)
        syracuse(current, index + 1)
    else:
        if current == 1:
            syracuse_list.append(1)
        else:
            if current % 2 == 0:
                next_value = int(current / 2)
            else:
                next_value = int(3 * current) + 1
            syracuse_list.append(next_value)
            if next_value != 1:
                syracuse(next_value, index + 1)


syracuse(5, 0)
print(syracuse_list)
