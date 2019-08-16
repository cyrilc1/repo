#Import modules
import math

#Initial Investment value/amount
share_vlu = float((input("Share Value cost = $")))
share_amt = float((input("Share amount : ")))

#print standing stock at purchase
share_cst = share_vlu * share_amt
print (("share cost = ") + str(share_cst) )

#Broker Commission calcs
brk_cmssn = share_cst*0.02

print (("Broker Commission : $") + str(brk_cmssn))

#Joe's Remaining account Balance
Balance = share_cst + brk_cmssn
print (("Joes current ballance: $") + str(Balance))

print("####SELL STOCK####")

share_vlu2 = (float(input("New Share Value cost : $")))
share_amt2 = (float(input("Share amount : ")))

#Print New stock profit/loss
share_cst2 = share_vlu2 * share_amt2
print (("New share cost = ") + str(share_cst2))

#New Broker Commission after sell
brk_cmssn2 = share_cst2*0.02
print (("Broker Commission : $") + str(brk_cmssn2))

#Joe's Remaining account Balance
Balance2 = share_cst2 - brk_cmssn2
print (("Joes current ballance: $") + str(Balance2))

#Result Profit/Stagnant/Loss
if Balance2 == Balance:
    print(("profit of : $0"))
elif Balance2 > Balance:
    print(("profit of : $") + str(round(Balance2 - Balance,2)))
else:
    print(("loss of : $") + str(round(Balance2 - Balance,2)))
