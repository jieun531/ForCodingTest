for i in range(int(input())):
    case_num = int(input())
    scores_num = [0]*101 #0점부터 100점 범위
    scores = list(map(int, input().split()))

    for j in range(1000):
        scores_num[scores[j]] += 1

    fre_sco = max(scores_num) #가장 많은 점수의 개수
    li_fre = [] #가장 많은 점수 자체를 저장하는 리스트

    for j in range(101):
        if scores_num[j] == fre_sco :
            li_fre.append(j)

    print("#%d %d" % (case_num, max(li_fre)))
