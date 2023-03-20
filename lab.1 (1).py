def find_min(arr):

    min_val = arr[0]


    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]

            return min_val


tablica = [5, 3, 7, 1, 8, 2, 9]
minimalna_wartosc = find_min(tablica)
print("Minimalna wartość w tablicy to:", minimalna_wartosc)
