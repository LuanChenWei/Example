
def find_min(num):
    result = num[0]
    for i in num:
        if i <= result:
            result = i

    return result

info = [3,67,34,12,67,89,23,12,45,3,6]

getmin = find_min(info)

print(getmin)


