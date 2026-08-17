# reports.py

def generate_transaction_summary(transaction, fee, total):
    return f"ID: {transaction['id']} | Subtotal: ${transaction['amount']:.2f} | Fee: ${fee:.2f} | Total: ${total:.2f}"