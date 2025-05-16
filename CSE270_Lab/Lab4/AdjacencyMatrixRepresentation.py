def main():
    v,n = map(int,input().split(" "))
    matrix = [[0]*(v+1) for _ in range(v+1)]
    for _ in range(n):
        x,y,z = map(int,input("").split(" "))
        matrix[x][y] = z;
    for i in range(1,v+1):
        for j in range(1,v+1):
            print(matrix[i][j],end=" ")
        print()





if __name__ == "__main__":
    main()