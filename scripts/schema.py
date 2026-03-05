from pydantic import BaseModel
from typing import List, Optional


class BusinessHours(BaseModel):
    days: Optional[List[str]] = None
    start: Optional[str] = None
    end: Optional[str] = None
    timezone: Optional[str] = None


class EmergencyRouting(BaseModel):
    primary_contact: Optional[str] = None
    transfer_timeout_seconds: Optional[int] = None
    fallback: Optional[str] = None


class NonEmergencyRouting(BaseModel):
    during_hours: Optional[str] = None
    after_hours: Optional[str] = None


class CallTransferRules(BaseModel):
    timeout_seconds: Optional[int] = None
    max_retries: Optional[int] = None
    failure_message: Optional[str] = None


class AccountMemo(BaseModel):

    account_id: str

    company_name: Optional[str] = None

    business_hours: Optional[BusinessHours] = None

    office_address: Optional[str] = None

    services_supported: Optional[List[str]] = None

    emergency_definition: Optional[List[str]] = None

    emergency_routing_rules: Optional[EmergencyRouting] = None

    non_emergency_routing_rules: Optional[NonEmergencyRouting] = None

    call_transfer_rules: Optional[CallTransferRules] = None

    integration_constraints: Optional[List[str]] = None

    after_hours_flow_summary: Optional[str] = None

    office_hours_flow_summary: Optional[str] = None

    questions_or_unknowns: Optional[List[str]] = None

    notes: Optional[str] = None