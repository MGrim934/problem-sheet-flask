print("Hello World")
a=1
b=2
c=a+b
s="Hel'l'o"
t=", world!"
print(a,b,c,s,t)

if a == 1:
	print("a is 1")
	a = 0
else:
	print("a is not 1")
	a =1
	
print(a)

l = [1,2,3,4]
for i in range(2,10,2):
	print(i)
	
#comment


def square(n):
	m=n*n
	return m

print(square(10))