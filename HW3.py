distance = int(input("How many miles are you traveling? "))

limit = int(input("What is the speed limit? "))

speed = int(input("What speed ar you traveling at? "))

limitm = limit / 60
speedm = speed / 60

limittime = distance / limitm
yourtime = distance / speedm

saved = limittime - yourtime

print(f'You saved {saved:,.0f} minutes')
