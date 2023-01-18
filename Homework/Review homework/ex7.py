n = float(input())
if n <= 10000:
    hra = 20
    da = 80
elif 10001<=n<=20000:
    hra = 25
    da = 90
else:
    hra = 30
    da = 95
daa = n*(da/100)
hraa = n*(hra/100)
gross = n + daa + hraa
print("%.2f"%(gross))