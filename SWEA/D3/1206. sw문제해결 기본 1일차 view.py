for i in range(10):
   num_of_try = int(input().rstrip())
   b_list = list(map(int, input().rstrip().split(' ')))
   b_view = 0 #조망권 있는 빌딩 층수 저장

   for j in range(2, num_of_try-2) :
      if max(b_list[j-2:j]) < b_list[j] and b_list[j] > max(b_list[j+1:j+3]) :
         b_view += b_list[j] - max(max(b_list[j-2:j]), max(b_list[j+1:j+3]))
         #인접한 4개의 빌딩 중 가장 큰 빌딩과 층수 비교 후 차이나는 층수 저장
   print("#%d %d" % (i + 1 , b_view))
