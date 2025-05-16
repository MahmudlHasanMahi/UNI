def getIdx(arr, a, n):
    for i in range(n):
        if arr[i] == a:
            return i
    return None;

def getPostOrder(inorder, preorder, n):

    parent = getIdx(inorder, preorder[0], n)

    if parent != 0:
        getPostOrder(inorder[0:parent], preorder[1:], parent)

    if parent != n - 1:
        getPostOrder(inorder[parent + 1:], preorder[parent + 1:], n - parent - 1)

    print(preorder[0], end=" ")


def main():
    n = int(input())
    inorder = list(map(int, input().split(" ")))
    preorder = list(map(int, input().split(" ")))

    getPostOrder(inorder, preorder, n)


if __name__ == '__main__':
    main()