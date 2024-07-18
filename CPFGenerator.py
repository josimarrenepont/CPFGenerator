import random

nineDigits = ''

for i in range(9):
    nineDigits += str(random.randint(0, 9))

countdownTimerFirst = 10

result_digit_first = 0

for digitirst in nineDigits:
    result_digit_first += int(digitirst) * countdownTimerFirst
    countdownTimerFirst -= 1
    
digitFirst = (result_digit_first * 10) % 11
digitFirst = digitFirst if digitFirst < 10 else 0
print(digitFirst)
    
#GeneratingSecondDigit
tenDigits = nineDigits + str(digitFirst)
countdownTimerSecond = 11

result_digit_second = 0

for digitSecond in tenDigits:
    result_digit_second += int(digitSecond) * countdownTimerSecond
    countdownTimerSecond -= 1
digitSecond = (result_digit_second * 10) % 11
digitSecond = digitSecond if digitSecond < 10 else 0
print(digitSecond)

#Verify CPF is valid
cpf = (f'{nineDigits}{digitFirst}{digitSecond}')

print(cpf)
