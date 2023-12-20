a,b=map(int,input().split())
print(('==','>','<')[2*(a<b)+1*(a>b)])