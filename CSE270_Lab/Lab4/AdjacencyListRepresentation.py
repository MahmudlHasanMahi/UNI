def main():

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


    v,e = map(int, input().split(" "))
    arr = [None] * v
    v1 = list(map(int, input().split(" ")))
    v2 = list(map(int, input().split(" ")))
    w = list(map(int, input().split(" ")))
    for i in range(e):
        if arr[v1[i]-1] == None:
            arr[v1[i]-1] = Node((v2[i], w[i]))
        else:
            temp = arr[v1[i]-1]
            while temp.next != None:
                temp = temp.next
            temp.next = Node((v2[i], w[i]))


    for i in range(v):
        node = arr[i]
        print(i+1,end=": ")
        while(node != None ):
            print(node.data, end =" ")
            node = node.next
        print()
    

        
    

if __name__ == "__main__":
    main()