print(*(f"Case #{i+1}: {(lambda x,y:f'{x} + {y} = {x+y}')(*map(int,input().split()))}"for i in range(int(input()))))