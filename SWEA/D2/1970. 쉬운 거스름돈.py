num_of_try = int(input().rstrip())

for i in range(num_of_try):
   changes = [0] * 8
   money = int(input().rstrip())
   changes[1] = money // 10000
   changes[3] = (money % 10000) // 1000
   changes[-3] = (money % 1000) // 100
   changes[-1] = (money % 100) // 10

   if changes[1] >= 5 :
      changes[0] += money // 50000
      changes[1] = changes[1] - 5 * changes[0]

   if changes[3] >= 5:
      changes[2] += (money % 10000) // 5000
      changes[3] = changes[3] - 5 * changes[2]

   if changes[5] >= 5 :
      changes[4] += (money % 1000) // 500
      changes[5] = changes[5] - 5 * changes[4]

   if changes[7] >= 5 :
      changes[6] += (money % 100) // 50
      changes[7] = changes[7] - 5 * changes[6]

   print("#%d" % (i + 1))
   print(*changes, sep=' ')
