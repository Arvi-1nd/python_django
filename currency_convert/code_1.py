history = []
def conversion(amount,enteredCurrency,modifyCurrency):
        if (enteredCurrency == 'USD' and modifyCurrency == 'EUR'):
            convertedEur = amount * 0.85
            history.append(f"{convertedEur:.2f}EUR")
            return f"{convertedEur:.2f}EUR"
        elif (enteredCurrency == 'EUR' and modifyCurrency == 'USD'):
            convertedUsd = amount *  1.08 
            history.append(f"{convertedUsd:.2f}USD")
            return f"{convertedUsd:.2f}USD"
        elif (enteredCurrency == 'CAD' and modifyCurrency == 'USD'):
            converted_1USD = amount * 0.72
            history.append(f"{converted_1USD:.2f}USD")
            return f"{converted_1USD:.2f}USD"
        elif (enteredCurrency == 'USD' and modifyCurrency == 'CAD'):
            convertedCan = amount * 1.35
            history.append(f"{convertedCan:.2f}CAD")
            return f"{convertedCan:.2f}CAD"
        elif (enteredCurrency == 'EUR' and modifyCurrency == 'CAD'):
            converted_1Can = amount * 1.63
            history.append(f"{converted_1Can:.2f}CAD")
            return f"{converted_1Can:.2f}CAD"
        elif (enteredCurrency == 'CAD' and modifyCurrency == 'EUR'):
            converted_1Eur = amount * 0.612
            history.append(f"{converted_1Eur:.2f}EUR")
            return f"{converted_1Eur:.2f}EUR"   
        else:
            print("Invalid input")
            
amount = float(input("Enter  the amount: "))
enteredCurrency = input("Source Currency (USD/EUR/CAD): ").upper()
modifyCurrency = input("Target Currency (USD/EUR/CAD): ").upper()
result = conversion(amount,enteredCurrency,modifyCurrency)
print(f"{amount} in {enteredCurrency} is equal to {result}")

for transact in history:
    print(f"Last transaction converted is {transact[-1]}")