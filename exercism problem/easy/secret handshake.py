#it took almost 1 hour 30 min to completed... took help of duck ai for string method...

user=str(input("Enter the number: "))
a=[]
if user[4]=="1":
    a.append("wink")
if user[3]=="1":
    a.append("double blink")
if user[2]=="1":
    a.append("close your eyes")
if user[1]=="1":
    a.append("jump")
if user[0]=="1":
    a.reverse()

print(*a,sep=",")

#solution..

CMDS = ('wink', 'double blink', 'close your eyes', 'jump')

def commands(number):
  number = int(number, 2)
  c = []
  for i, j in enumerate(CMDS):
    if number & 1 << i:
      c.append(j)
  if number & 1 << 4:
    c.reverse()
  return c