from schema import AccountMemo

test = AccountMemo(
    account_id="ACCT_TEST",
    company_name="Test Fire Protection",
    services_supported=["sprinkler repair", "fire alarm inspection"]
)

print(test.model_dump_json(indent=2))