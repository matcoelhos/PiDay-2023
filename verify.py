file = open('solution.txt','r')
sol_line = file.readlines()[0]
file.close()

file = open('pi-10million.txt','r')
tru_line = file.readlines()[0]
file.close()

n = -1

for i in range(len(sol_line)):
	if sol_line[i] == tru_line[i]:
		n+=1
		#print(sol_line[i],end='')
	else:
		#print(sol_line[i])
		break

print('Places: %d'%(n))