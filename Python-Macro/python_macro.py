class Macro:

    # 整数Nと、N要素のリストAを入力する
    def input_list():
        N = int(input())
        A = [0] * N
        for i in range(N):
            A[i] = int(input())
        return N, A

    # 整数H, Wと、H行W列の行列を入力する
    def input_matrix():
        H, W = map(int, input().split())
        matrix = [0] * H
        for i in range(H):
            matrix[i] = list(map(int, input().split()))
        return H, W, matrix


if __name__ == "__main__":
    N, A = Macro.input_list()
    print(N)
    print(A)
    H, W, matrix = Macro.input_matrix()
    print(H)
    print(W)
    print(matrix)
