def diagonalDifference(arr):
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    for index1 in range(len(arr)):
        for index2 in range(len(arr[0])):
            if index1 == index2:
                primary_diagonal_sum += arr[index1][index2]
            if index1+index2 == len(arr)-1:
                secondary_diagonal_sum += arr[index1][index2]
    return abs(primary_diagonal_sum - secondary_diagonal_sum) 
            