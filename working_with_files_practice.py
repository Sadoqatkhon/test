#1. working with files
with open ( 'input.txt', 'r') as rf:
    a, b = rf.readline().split()

a = int(a)
b = int(b)
if b >= a:
    result = f'{ b-a+1}'

with open('output.txt', 'w') as wf:
    wf.write(result)


# Homework:Robocontestdan masalalar
# h1 Azimjonning bir poda qo‘ylari bor. 
# U sizga qo‘ylarining jami oyoqlari sonini aytadi. 
# Siz esa podadagi qo‘ylarda jami bo‘lib nechta quloq borligini topishingiz kerak.

with open ('input.txt', 'r') as f:
    n = f.read()
n = int(n)
if n%4 == 0:
    result = f'{n/2} \n'
else:
    result = '-1 \n'

with open (' output. txt', 'a') as f:
    f.write(result )
    
# Robocontestda qabul qilingan varianti
# with open ('input.txt', 'r') as f:
#     n = f.read()
# n = int(n)
# if n%4 == 0:
#     result = n/2
# else:
#     result =-1 
  
# result = str(int(result))
# with open ('output.txt', 'w') as f:
#     f.write(result)
    
# h2 Shaxboz yaqinda sanashni o'rgandi. 
# U har bir sonni gapairishga 10 soniya vaqt sarflaydi.
#  U N dan M gacha sanashi uchun qancha vaqt sarflashini toping.

with open ('input.txt','r') as f:
    N, M = f.readline().split()

n = int(N)
m = int(M)

result = f'{(m-n+1)*10} '

with open ('output.txt', 'a') as f:
    f.write(result)


