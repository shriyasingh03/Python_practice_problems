# Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
# Salary(Lakhs) : Tax(%)

# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%

def calculate_in_hand_salary(ctc_lakhs):
    #convert ctc to annual salary in inr
    ctc = ctc_lakhs*100000

    #deductions
    hra = 0.1*ctc
    da = 0.05*ctc
    pf = 0.03*ctc
    taxable_income = ctc - (hra+da+pf)

    #tax calculation
    if ctc_lakhs < 5:
        tax = 0
    elif 5<= ctc_lakhs <10:
        tax = 0.1*taxable_income
    elif 10 <= ctc_lakhs < 20:
        tax = 0.2* taxable_income
    else:
        tax = 0.3*taxable_income

    #inand annual salary
    inhand_annual_salary = taxable_income -tax

    #inhand monthly salary 
    inhand_monthly_salary = inhand_annual_salary /12

    return round(inhand_monthly_salary,2)               




ctc_lakhs = float(input("enter your CTC in lakhs: "))
inhand_salary = calculate_in_hand_salary(ctc_lakhs)

print(f"your final salary is: RS {inhand_salary}")

