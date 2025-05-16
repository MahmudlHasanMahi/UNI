def main():
    
    n, k = input().split(" ")
    k = int(k)
    strs = input().split(" ")
    print(" ".join(strs[k-1::-1]))


if __name__ == '__main__':
    main()