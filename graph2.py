import random


n = int(input())
j = [ random.randint(0, 10)  for i in range(2*n)]
#j = [7, 6, 5, 6, 8, 6]
x_pts = [j[i] for i in range(0,len(j), 2)]
y_pts = [j[i] for i in range(1, len(j), 2)]

x_max = max(x_pts) + 2
y_max = max(y_pts) + 2
pts = list(zip(x_pts, y_pts))
pts = sorted(pts, key = lambda x: x[1], reverse = True)

print(j)
#print(x_pts)
#print(y_pts)
#print(x_max)
#print(y_max)
#print(pts)


last = 10000
count = 0
list1 = []
k = []

for i in pts:
	if(last == i[1] or count == 0):
		k.append(count)
		if(count == len(pts) - 1):
			list1.append(k)
			k = []
	else:
		list1.append(k)
		k = []
		k.append(count)
		if(count == len(pts) - 1):
			list1.append(k)
		
	
	last = i[1]
	count += 1

#print(list1)

list2 = []
for i in list1:
	if(len(i) > 1):
		beg = i[0]
		end = i[len(i) - 1] + 1
		list2 += sorted(pts[beg:end], key = lambda x : x[0])
	else:
		list2.append(pts[i[0]])

pts = list2
print(list2)

count = 0 
pt = pts[count]

for i in range(y_max, 0, -1):
	print("\n%2d"%i, end = '')
	last = 0
	if(pt[1] == i):
		prev = (-1, -1)
		while(pt[1] == i):		
			temp = pt[0] - last
			spacing = ' ' * (temp * 4 - 1)
			if(pt[0] != 0 and (prev[0] != pt[0] or prev[1] != pt[1])):
				print(spacing + '*' , end = '')
				last = pt[0]
				prev = pt
			if(count < len(pts) - 1):
				count += 1
				pt = pts[count]
			else:
				pt = (-1, -1)
		print()
		
	else:
		print()
print("\n%2d"%0, end = '')
for i in range(1,x_max):
	print("%4d"%i, end = '')
print()

