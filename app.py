from flask import Flask, request, jsonify

app = Flask(__name__)

ACCOUNTS = {
    "TR1001": {"balance": 5000.0, "currency": "TRY", "status": "ACTIVE"},
    "TR1002": {"balance": 150.0, "currency": "TRY", "status": "BLOCKED"},
}

@app.route('/api/v1/pay', methods=['POST'])
def process_payment():
    data = request.get_json()

    # 1.Kontrol
    if not data or 'account_number' not in data or 'amount' not in data:
        return jsonify({"status": "REJECTED", "reason": "Missing parameters"}), 400

    account_id = data['account_number']
    try:
        amount = float(data['amount'])
    except (TypeError, ValueError):
        return jsonify({"status": "REJECTED", "reason": "Invalid amount format"}), 400

    # 2.Kontrol
    if account_id not in ACCOUNTS:
        return jsonify({"status": "REJECTED", "reason": "Account not found"}), 404

    account = ACCOUNTS[account_id]

    # 3.Kontrol
    if account['status'] != 'ACTIVE':
        return jsonify({"status": "REJECTED", "reason": "Account is not active"}), 403

    # 4.Kontrol
    if account['balance'] < amount:
        return jsonify({"status": "REJECTED", "reason": "Insufficient funds"}), 422

    # Kontroller Bitti - Ödemeyi Onayla
    account['balance'] -= amount

    return jsonify({
        "status": "APPROVED",
        "transaction_id": "TXN-" + account_id + "-2026",
        "remaining_balance": account['balance']
    }), 200

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)
