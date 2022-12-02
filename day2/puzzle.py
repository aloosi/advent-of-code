#print(max([sum([int(x) for x in i.split("\n")])for i in open("input.txt", "r").read()[:-1].split("\n\n")]))
#part 2
with open('input.txt','r',encoding='utf-8') as f:
    data = f.readlines()
translate = [{"A":"Rock","B":"Paper","C":"Scissors"},{"X":"Rock","Y":"Paper","Z":"Scissors"}]
FP_Me = 0
for line in data: # A Y
    line = line.replace("\n","")
    
    Opponent = translate[0][ line.split(" ")[0] ] # Rock
    Me = translate[1][ line.split(" ")[1] ] # Paper
    
    P_Opponent = list( translate[0].values() ).index(Opponent)+1 # 1
    P_Me = list( translate[1].values() ).index(Me)+1 # 2
    
    # 0 if you lost, 3 if the round was a draw, and 6 if you won
    RP = 0 # round points
    
    if ( P_Me > P_Opponent or (P_Me == 1 and P_Opponent == 3) ) and not ( P_Opponent == 1 and P_Me == 3):
            RP = 6
    
    elif P_Me == P_Opponent:
        RP = 3
    
    else:
        RP = 0
    
    FP = RP+P_Me
    FP_Me += int(FP)
        
    formatted_str = ( "%8s || %8s || %1s" % (Opponent,Me,str(FP)) ) # 25 symbols.
    print(formatted_str)
    
print("Sum: "+str(FP_Me))