import os
import json
from extract_memo import process_file
from generate_agent import generate_agent_spec
import logging

DATASET_FOLDER = "../dataset/demo_calls"
OUTPUT_FOLDER = "../outputs/accounts"


def run_demo_pipeline():

    files = [f for f in os.listdir(DATASET_FOLDER) if f.endswith(".txt")]

    for i, file in enumerate(files, start=1):

        account_id = f"ACCT_{i:03d}"

        transcript_path = os.path.join(DATASET_FOLDER, file)

        memo = process_file(transcript_path)

        memo.account_id = account_id

        account_folder = os.path.join(OUTPUT_FOLDER, account_id, "v1")

        os.makedirs(account_folder, exist_ok=True)

        memo_path = os.path.join(account_folder, "memo.json")

        with open(memo_path, "w") as f:
            f.write(memo.model_dump_json(indent=2))

        agent_spec = generate_agent_spec(json.loads(memo.model_dump_json()))

        agent_path = os.path.join(account_folder, "agent_spec.json")

        with open(agent_path, "w") as f:
            json.dump(agent_spec, f, indent=2)

        print(f"Processed {file} → {account_id}")


if __name__ == "__main__":
    run_demo_pipeline()