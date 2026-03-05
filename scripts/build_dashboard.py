import os
import json
import pandas as pd

ACCOUNTS_FOLDER = "../outputs/accounts"

rows = []

for account in os.listdir(ACCOUNTS_FOLDER):

    v1_path = os.path.join(ACCOUNTS_FOLDER, account, "v1", "memo.json")

    if os.path.exists(v1_path):

        with open(v1_path) as f:
            memo = json.load(f)

        rows.append({
    "account_id": memo.get("account_id"),
    "company_name": memo.get("company_name"),
    "services": ", ".join(memo.get("services_supported") or []),
    "emergency_definition": ", ".join(memo.get("emergency_definition") or [])
})

df = pd.DataFrame(rows)

output_path = "../outputs/dashboard.csv"

df.to_csv(output_path, index=False)

print("Dashboard created:", output_path)