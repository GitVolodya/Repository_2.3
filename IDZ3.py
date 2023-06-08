text = "Число 123, не состоит из цифры 4 и не состоит из цифры 9."

digits = [int(d) for d in text if d.isdigit()]

print(digits)

