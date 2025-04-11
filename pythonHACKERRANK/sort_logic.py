def sort_logic(x):
    method_1_list = x.copy()
    print(sorted(method_1_list))
    method_2 = x.copy()
    new_method_2 = []
    while method_2:
        smallest = min(method_2)
        new_method_2.append(smallest)
        method_2.remove(smallest)
    print(new_method_2)
    method_3= x.copy()
    length = len(method_3)
    for i in range(length):
        for j in range(0, length - i - 1):
            if method_3[j] > method_3[j + 1]:
                method_3[j], method_3[j + 1] = method_3[j + 1], method_3[j]
    print(method_3)

list2 = [4,8,5,5,4,5,4,8,65,48,46,84,68,15,54]
sort_logic(list2)