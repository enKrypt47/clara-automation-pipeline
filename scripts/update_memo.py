import json
import os
from deepdiff import DeepDiff


def load_json(path):
    with open(path) as f:
        return json.load(f)


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def extract_updates(transcript):

    updates = {}

    text = transcript.lower()

    if "8 am" in text and "5 pm" in text:
        updates["business_hours"] = {
            "days": ["Mon", "Tue", "Wed", "Thu", "Fri"],
            "start": "08:00",
            "end": "17:00",
            "timezone": "unknown"
        }

    if "sprinkler leak" in text or "fire alarm" in text:
        updates["emergency_definition"] = [
            "sprinkler leak",
            "fire alarm triggered"
        ]

    if "westfield" in text:
        updates["office_address"] = "2145 Westfield Rd Houston"

    return updates


def generate_changelog(old, new):

    diff = DeepDiff(old, new, ignore_order=True)

    return diff.pretty()


if __name__ == "__main__":

    memo_v1_path = "../outputs/accounts/ACCT_001/v1/memo.json"
    onboarding_path = "../dataset/onboarding_calls/onboard1.txt"

    memo_v1 = load_json(memo_v1_path)

    with open(onboarding_path) as f:
        transcript = f.read()

    updates = extract_updates(transcript)

    memo_v2 = memo_v1.copy()

    memo_v2.update(updates)

    save_json("../outputs/accounts/ACCT_001/v2/memo.json", memo_v2)

    changelog = generate_changelog(memo_v1, memo_v2)

    with open("../outputs/accounts/ACCT_001/changes.md", "w") as f:
        f.write(changelog)

    print("v2 memo created")