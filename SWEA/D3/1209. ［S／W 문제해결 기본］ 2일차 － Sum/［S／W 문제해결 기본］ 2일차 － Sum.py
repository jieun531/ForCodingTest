for _ in range(10):
   list_num = int(input().rstrip())
   num_list = []
   max_list = [[],[],[0,0]]

   for _ in range(100) :
      num_list.append(list(map(int, input().rstrip().split(' '))))

   for i in range(100):
         max_list[0].append(sum(row for row in num_list[i]))
         max_list[1].append(sum(row[i] for row in num_list))
         max_list[2][0] += num_list[i][i]
         max_list[2][1] += num_list[-i-1][-i-1]

   print("#%d" % list_num, end=' ')
   print(max(max(max_list[0]), max( max_list[1]), max( max_list[2])))