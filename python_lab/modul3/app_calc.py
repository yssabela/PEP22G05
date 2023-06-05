'''- if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of
the income minus 556 thalers and 2 cents
  - if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents,plus 32% of the
surplus over 85,528 thalers.

It should accept one floating-point value: the income.
Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do
the rounding for you - you'll find it in the skeleton code in the editor.

Note: If the calculated tax is less than zero,it only means no tax at all (the tax is equal to zero).
Take this into consideration during your calculations.

Your task is to write a tax calculator.'''

income = float(input("Enter the annual income: "))

if income < 85528:
    tax = income * 0.18 - 556.02
    if tax < 0: tax = 0
else:
    tax = (income - 85528) * 0.32 - 14839.02

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
