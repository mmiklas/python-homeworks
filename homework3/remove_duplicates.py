# Napisz funkcję, która pozbędzie się z listy powtarzających się elementów.

def remove_duplicates(list_with_duplicates):
    result = []
    for e in list_with_duplicates:
        if e not in result:
            result.append(e)
    return result

def show_result(list):
    print("lista z duplikatami:", list)
    print("lista bez duplikatów:", remove_duplicates(list))

show_result([3, 3, 2, 1, 5, 3, 6, 7, 9, 9])
show_result(["Ala", "Adam", "Ada", "Karol", "Karol"])
