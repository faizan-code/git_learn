def migratoryBirds(arr):

    dic = dict()

    for bird in arr:
        if bird in dic:
            dic[bird] = dic[bird] + 1
        else:
            dic[bird] = 1


    bigcount = 0
    bigno = 0

    for name, val in dic.items():
        if bigcount == 0 or bigcount < val:
            bigcount = val
            bigno = name

    return bigno



arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

print(migratoryBirds(arr))
