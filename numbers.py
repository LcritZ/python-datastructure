count = 0
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if ( i != k) and (i != j ) and (j != k):
				count = count+1
				print (i*100+j*10+k)

print(count)
