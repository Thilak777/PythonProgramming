a=int(input())
temp=a
s=0
while a!=0:
  r=a%10
  s=s*10+r
  a=a/10
if s==temp:
  print("Palindrome")
else:
  print("Not a Palindrome")
