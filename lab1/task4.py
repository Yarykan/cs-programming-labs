time = int(input())
minute = (time // 60) % 60 
hour = (time // 60) // 60
print(f'{hour:02d}:{minute:02d}:{time%60:02d}')
