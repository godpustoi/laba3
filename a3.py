prev = int(input())
curr = int(input())

if curr >= prev:
    used = curr - prev
else:
    used = 10000 - prev + curr

if used <= 300:
    pay = 21.0
elif used <= 600:
    pay = 21.0 + (used - 300) * 0.06
elif used <= 800:
    pay = 21.0 + 300 * 0.06 + (used - 600) * 0.04
else:
    pay = 21.0 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025

avg_price = pay / used

print("Предыдущее Текущее Использовано К оплате Ср. цена m^3")
print(f"{prev} {curr} {used} {pay:.3f} {avg_price:.2f}")