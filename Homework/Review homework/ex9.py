typ = int(input())
hour = float(input())
if typ==1:
    if hour <3:
        print("%.2f"%(0.7*hour))
    else:
        print("%.2f"%(0.7*3+2.50*(hour-3)))
elif typ==2:
    if hour <3:
        print("%.2f"%(1.5*hour))
    else:
        print("%.2f"%(1.5*3+2.0*(hour-3)))
else:
    if hour <3:
        print("%.2f"%(2.5*hour))
    else:
        print("%.2f"%(2.5*2+3.25*(hour-2)))