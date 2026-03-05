import json
import os


def generate_agent_spec(memo):

    agent = {
        "agent_name": f"{memo['account_id']} Clara Assistant",

        "version": "v1",

        "voice_style": "professional and calm",

        "variables": {
            "timezone": "unknown",
            "business_hours": memo.get("business_hours"),
            "office_address": memo.get("office_address")
        },

        "system_prompt": f"""
You are Clara, an AI phone assistant for a service trade company.

Your job is to answer inbound calls and route them correctly based on the company’s operational rules.

BUSINESS HOURS FLOW
1. Greet the caller politely.
2. Ask how you can help them today.
3. Collect the caller's name and phone number.
4. Determine whether the request is an emergency or non-emergency.
5. Route or transfer the call according to the routing rules.
6. If the transfer fails, apologize and inform the caller someone will follow up.
7. Ask if they need anything else.
8. If not, close the call politely.

AFTER HOURS FLOW
1. Greet the caller and inform them the office is currently closed.
2. Ask the purpose of the call.
3. Confirm whether the situation is an emergency.
4. If it is an emergency:
   - Immediately collect the caller's name, phone number, and service address.
   - Attempt to transfer the call to emergency dispatch.
5. If the transfer fails:
   - Apologize and assure the caller that someone will contact them shortly.
6. If the issue is not an emergency:
   - Collect details about the service request.
   - Inform the caller the office will follow up during business hours.
7. Ask if the caller needs anything else.
8. Close the call politely.

Do not mention internal tools or system processes to the caller.
""",

        "call_transfer_protocol": {
            "timeout_seconds": 60,
            "retries": 2,
            "fallback_message": "I couldn't connect you, but someone will call you shortly."
        },

        "tools": [
            "create_ticket_placeholder",
            "dispatch_notification_placeholder"
        ]
    }

    return agent


if __name__ == "__main__":

    memo_path = "../outputs/accounts/ACCT_001/v2/memo.json"

    with open(memo_path) as f:
        memo = json.load(f)

    agent_spec = generate_agent_spec(memo)

    output_path = "../outputs/accounts/ACCT_001/v2/agent_spec.json"

    with open(output_path, "w") as f:
        json.dump(agent_spec, f, indent=2)

    print("Agent spec v2 created")