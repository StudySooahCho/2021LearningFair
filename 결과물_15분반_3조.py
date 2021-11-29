goal=int(input("목표로 하는 금액을 입력하세요: "))
count=int(input("알바 개수를 입력하세요: "))
total=0
income=0
for i in range(count):
    print("==========================================")
    week=int(input("1주일 근무 시간을 입력하세요: "))
    money=int(input("시급을 입력하세요: "))

    if week >14:
        day=int(input("하루 근무 시간을 입력하세요: "))
        total=(week+day)*money*4

    else:
        total=week*money*4

    tax=input("세금 납부 여부를 입력하세요(Y/N): ")

    if tax=='Y' or tax=='y':
        total=total*0.967

    else:
        total=total*1
    income = income+total
    
print()

print("월급은", int(income),"원", "입니다")

month=(goal/income-0.5)+1
print( int(month), "개월 후에 목표금액에 도달합니다.")
