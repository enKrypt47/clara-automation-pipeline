# clara-automation-pipeline
# Clara Automation Pipeline

## Overview
This project implements an automation pipeline that converts unstructured customer conversations into structured configurations for an AI voice assistant.

The system processes demo call transcripts and onboarding conversations to generate and update Retell agent configurations.

## Architecture

Demo Transcript → Account Memo (v1)  
Account Memo → Agent Configuration  
Onboarding Transcript → Updated Memo (v2)  
v1 vs v2 → Change Log  
All Accounts → Dashboard Summary

## Project Structure

dataset/
  demo_calls/
  onboarding_calls/

scripts/
  extract_memo.py
  generate_agent.py
  update_memo.py
  run_pipeline.py
  schema.py
  build_dashboard.py

outputs/
  accounts/
  dashboard.csv

## How to Run

cd scripts

python run_pipeline.py  
python update_memo.py  
python build_dashboard.py

## Outputs

Each account produces:

- v1 memo and agent configuration
- v2 updated configuration
- change log showing differences

## Limitations

- Rule-based extraction
- No real-time API integrations
- Mock Retell configuration

## Future Improvements

- LLM-based extraction
- Direct Retell API integration
- Real-time orchestration using n8n
