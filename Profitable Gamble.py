def profitable_gamble(prob, prize, pay):
    if prob*prize > pay:
        return True
    else:
        return False
print(profitable_gamble(0.2, 50, 9))
#op:-True