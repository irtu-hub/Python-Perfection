# main.py

import validation,calculations,report


def run():

    transaction = {"id": "TX100", "amount": 49.99}    
    
    if not validation.validate_transaction(transaction):
        print("Invalid transaction data!")
        return

    
    amount = transaction["amount"]
    fee = calculations.calculate_processing_fee(amount)
    total = calculations.calculate_final_total(amount, fee)

   
    out = report.generate_transaction_summary(transaction, fee, total)

    print(out)
if __name__ == "__main__":
    run()