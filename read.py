data = []
count = 0

with open ('reviews.txt', 'r') as c:
	for line in c:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0: # % 用來求餘數, 1000的餘數是0 = 1000的倍數
			print(len(data))

print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)

print('每筆留言的平均長度為', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])