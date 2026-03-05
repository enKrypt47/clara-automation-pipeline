import json
import os
from schema import AccountMemo


def extract_from_transcript(transcript):

    memo = AccountMemo(
        account_id="ACCT_001"
    )

    transcript_lower = transcript.lower()

    services = []

    if "sprinkler" in transcript_lower:
        services.append("sprinkler repair")

    if "fire alarm" in transcript_lower:
        services.append("fire alarm inspection")

    if services:
        memo.services_supported = services

    if "emergency" in transcript_lower or "sprinkler leak" in transcript_lower:
        memo.emergency_definition = [
            "sprinkler leak",
            "fire alarm triggered"
        ]

    memo.notes = "Generated from demo transcript"

    return memo
def process_file(path):

    with open(path, "r", encoding="utf-8") as f:
        transcript = f.read()

    memo = extract_from_transcript(transcript)

    return memo
def save_memo(memo):

    account_folder = f"../outputs/accounts/{memo.account_id}/v1"

    os.makedirs(account_folder, exist_ok=True)

    output_path = os.path.join(account_folder, "memo.json")

    with open(output_path, "w") as f:
        json.dump(memo.model_dump(), f, indent=2)

    print(f"Memo saved to {output_path}")

def save_memo(memo):

    account_folder = f"../outputs/accounts/{memo.account_id}/v1"

    os.makedirs(account_folder, exist_ok=True)

    output_path = os.path.join(account_folder, "memo.json")

    with open(output_path, "w") as f:
        json.dump(memo.model_dump(), f, indent=2)

    print(f"Memo saved to {output_path}")


if __name__ == "__main__":

    transcript_path = "../dataset/demo_calls/demo1.txt"

    memo = process_file(transcript_path)

    print(memo.model_dump_json(indent=2))

    save_memo(memo)