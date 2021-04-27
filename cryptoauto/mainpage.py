import pyupbit
access = "37w9Ple15Epe5AxRkhaMOp7ZyiuDkYwjQt69rlgd"          # 본인 값으로 변경
secret = "9ttdPjuolevVIkmGsLYPdHXe9dh7wH2Nx15u0I1c"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

myMED=upbit.get_balance("KRW-MED")
myMVL=upbit.get_balance("KRW-MVL")
myBTC=upbit.get_balance("KRW-BTC")
myKRW=upbit.get_balance("KRW")

correntMED=pyupbit.get_current_price("KRW-MED")
correntMVL=pyupbit.get_current_price("KRW-MVL")
correntBTC=pyupbit.get_current_price("KRW-BTC")


print()
print("MED 보유량 : %f개 MED 현재가 : %f원 평가금액 : %f원" %(myMED,correntMED,myMED*correntMED) )
print()
print("MVL 보유량 : %f개 MVL 현재가 : %f원 평가금액 : %f원" %(myMVL,correntMVL,myMVL*correntMVL) )
print()

print("BTC 보유량 : %f개 BTC 현재가 : %f원 평가금액 : %f원" %(myBTC,correntBTC,myBTC*correntBTC) )

print()

print("보유 현금: %f원 " %myKRW)

print("총보유량: %f원 " %(myKRW+myMED*correntMED+myMVL*correntMVL+myBTC*correntBTC))




