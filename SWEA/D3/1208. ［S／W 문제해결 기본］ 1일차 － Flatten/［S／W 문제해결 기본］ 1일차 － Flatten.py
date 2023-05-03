for i in range(10):
   num_of_dmp = int(input().rstrip())
   b_list = list(map(int, input().rstrip().split(' ')))
   b_max = max(b_list)
   b_min = min(b_list)

   for j in range(num_of_dmp) :
      if b_max - b_min <= 1 :
         break
      else :
         b_list[b_list.index(b_max)] -= 1
         b_list[b_list.index(b_min)] += 1
         b_max = max(b_list)
         b_min = min(b_list)

   print("#%d %d" % (i + 1 , b_max - b_min))