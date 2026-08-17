# validation.py

def validate_transaction(transaction):
   
    if "amount" not in transaction or "id" not in transaction or transaction["amount"] <= 0:

        return False 
    return True

    