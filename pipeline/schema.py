from typing import Optional, List
from pydantic import BaseModel, Field

class ExtractedKYCDocument(BaseModel):
    """Structured entity extracted from unstructured KYC/policy scans."""
    doc_type: str = Field(description="Document type: pan, aadhaar_front, aadhaar_back, cheque, motor_policy, health_policy")
    holder_name: Optional[str] = Field(None, description="Full legal name of the document holder")
    pan: Optional[str] = Field(None, description="10-digit Indian Permanent Account Number")
    aadhaar_last4: Optional[str] = Field(None, description="Last 4 digits of Aadhaar (unmasked for verification)")
    dob: Optional[str] = Field(None, description="Date of birth in YYYY-MM-DD or DD/MM/YYYY")
    gender: Optional[str] = Field(None, description="Male / Female / Other")
    father_name: Optional[str] = Field(None, description="Father or Spouse name if present")
    
    # Financial & Banking details (Cheque)
    bank_account_number: Optional[str] = Field(None, description="Bank account number extracted from cheque")
    ifsc_code: Optional[str] = Field(None, description="11-character Indian Financial System Code")
    bank_name: Optional[str] = Field(None, description="Bank name")

    # Insurance specific details
    insurer_name: Optional[str] = Field(None, description="Underwriting insurer name (e.g. HDFC ERGO, ICICI Lombard)")
    policy_number: Optional[str] = Field(None, description="Unique policy identifier")
    gross_premium: Optional[float] = Field(None, description="Gross premium amount")
    net_premium: Optional[float] = Field(None, description="Net premium amount")
    idv_amount: Optional[float] = Field(None, description="Insured Declared Value for motor policies")
    expiry_date: Optional[str] = Field(None, description="Policy expiry date")
    nominee_name: Optional[str] = Field(None, description="Nominee legal name")
    nominee_relationship: Optional[str] = Field(None, description="Relationship with policy holder")
    vehicle_registration: Optional[str] = Field(None, description="Vehicle registration number")
    engine_number: Optional[str] = Field(None, description="Engine serial number")
    chassis_number: Optional[str] = Field(None, description="Chassis serial number")

    confidence_score: float = Field(default=1.0, description="Extraction confidence score (0.0 to 1.0)")
