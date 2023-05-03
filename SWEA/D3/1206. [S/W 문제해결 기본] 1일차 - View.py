for i in range(10):
   num_of_try = int(input().rstrip())
   b_list = list(map(int, input().rstrip().split(' ')))
   b_view = 0 #조망권 확보된 층수

   for j in range(2, num_of_try-2) :
      if max(b_list[j-2:j]) < b_list[j] and b_list[j] > max(b_list[j+1:j+3]) :
         b_view += b_list[j] - max(max(b_list[j-2:j]), max(b_list[j+1:j+3]))
         #왼쪽과 오른쪽에 인접한 두 빌딩의 최대높이 보다 해당 빌딩에 더 높은 층이 있는지 확인 후 인접한 4빌딩 중 가장 높은 빌딩 층수를 해당 빌딩 층수에서 뺀다
          
   print("#%d %d" % (i + 1 , b_view))
