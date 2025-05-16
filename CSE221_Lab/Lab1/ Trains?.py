def bubble_sort(arr):
    for i in range(len(arr)):
        flag = True
        for j in range(0,len(arr)-i-1):

            if arr[j][0] > arr[j+1][0] :
                arr[j],arr[j+1] = arr[j+1], arr[j]
                flag = False
            elif arr[j][0] == arr[j+1][0] and arr[j][-1] < arr[j+1][-1]:
                flag = False
                arr[j],arr[j+1] = arr[j+1], arr[j]
        if flag:
            return

            


def main():
    n = int(input())
    trains = []
    for i in range(n):
        trains.append(input().split(" "))

    bubble_sort(trains)
    for i in trains:
        print(" ".join(i))



if __name__ == '__main__':
    main()