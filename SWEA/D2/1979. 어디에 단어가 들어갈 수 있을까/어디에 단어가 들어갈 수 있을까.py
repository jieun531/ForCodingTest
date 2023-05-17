test_case = int(input())

for i in range(1, test_case+1):
    length, w_len = map(int, input().split())
    board = [[0]*(length+2)] #단어가 들어갈 수 있는 부분은 1, 외곽을 0으로 감쌀 예정
    to_find = [0]+[1]*w_len+[0]
    w_avail = 0
    for _ in range(length) :
        board.append([0]+list(map(int, input().split()))+[0])
    board.append([0]*(length+2))

    for j in range(length+2):
        for k in range(1,length-w_len+2):
            if board[j][k-1:k+w_len+1] == to_find :
                w_avail += 1
            if list(x[j] for x in board[k-1:k+w_len+1]) == to_find :
                w_avail += 1

    print("#%d %d" % (i, w_avail))