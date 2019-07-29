def find_order(alpha_list):
    # function has as an input a list of ordered word strings and calculates the alphabetical rules for this ordering
    # system.

    letters = "abcdefghijklmnopqrstuvwxyz"
    num_letters = 26
    num_elements = len(alpha_list)
    if num_elements == 1:
        print(letters)
    adjacency = [[]] * 26
    in_edge = [0]*num_letters
    base = alpha_list[0]
    for i in list(range(1, num_elements)):
        compare = alpha_list[i]
        min_length = min(len(base), len(compare))
        for j in list(range(0, min_length)):
            if base[j] != compare[j]:
                break
        if j < min_length:
            adjacency[letters.find(base[j])].append(letters.find(compare[j]))
            in_edge[letters.find(compare[j])] += 1
            base = compare
            continue
        if len(base) > len(compare):
            print("Not possible to order")
        base = compare
    stack = []
    for i in list(range(num_letters)):
        if in_edge[i] == 0:
            stack.append(i)
    output = []
    nodes_visited = [False]*num_letters
    while stack:
        item = stack.pop()
        nodes_visited[item] = True
        output.append(item)
        for i in list(range(len(adjacency[item]))):
            if nodes_visited[adjacency[item][i]]:
                continue
            in_edge[adjacency[item][i]] -= 1
            if in_edge[adjacency[item][i]] == 0:
                stack.append(adjacency[item][i])
    for i in list(range(num_letters)):
        if not nodes_visited[i]:
            return "Not possible to order"
    for i in output:
        print(letters[output[i]])
