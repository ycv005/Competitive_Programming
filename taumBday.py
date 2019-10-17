# https://www.hackerrank.com/challenges/taum-and-bday/problem

for t in range(int(input())):
	b,w=input().split()
	bc,wc,z=input().split()
	bc,wc,z=int(bc),int(wc),int(z)
	r=0
	if abs(bc-wc)>z:
		if bc<wc:
			r=int(b)*bc+int(w)*bc+z*int(w)
		else:
			r=z*int(b)+int(b)*wc+int(w)*wc
	else:
		r=int(b)*bc+int(w)*wc
	print(r)