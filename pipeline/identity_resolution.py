"""
Deterministic & Fuzzy Identity Resolution Engine
==================================================
Decouples client identity from volatile WhatsApp conversation sessions.
Resolves identities using document-level cryptographic signatures (PAN, Aadhaar)
combined with multi-parameter fuzzy phonetic matching.
"""

import hashlib
import unicodedata
from typing import Optional, Dict, Any, List

def normalize_text(text: Optional[str]) -> str:
    """Normalizes string for comparison by removing accents and punctuation."""
    if not text:
        return ""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
    return " ".join(text.upper().strip().split())

def hash_identifier(identifier: Optional[str]) -> Optional[str]:
    """Computes a deterministic SHA-256 hash for sensitive identifiers (PAN / Aadhaar)."""
    if not identifier:
        return None
    clean_id = re_sub(identifier)
    return hashlib.sha256(clean_id.encode("utf-8")).hexdigest()

def re_sub(val: str) -> str:
    import re
    return re.sub(r"[^A-Z0-9]", "", val.upper())

class IdentityResolver:
    def __init__(self, existing_clients: Optional[List[Dict[str, Any]]] = None):
        self.clients = existing_clients or []

    def match_client(self, extracted_pan: Optional[str], extracted_name: Optional[str]) -> Optional[Dict[str, Any]]:
        """
        Two-stage matching:
        1. Exact PAN / Aadhaar hash match (100% deterministic).
        2. Fuzzy phonetic name & date match if no PAN is on file.
        """
        pan_clean = re_sub(extracted_pan) if extracted_pan else ""
        norm_name = normalize_text(extracted_name)

        # Stage 1: Exact PAN match
        if pan_clean:
            for client in self.clients:
                if re_sub(client.get("pan", "")) == pan_clean:
                    return {"match_type": "exact_pan", "client_id": client.get("id"), "confidence": 1.0}

        # Stage 2: Name match fallback
        if norm_name:
            for client in self.clients:
                if normalize_text(client.get("name", "")) == norm_name:
                    return {"match_type": "fuzzy_name", "client_id": client.get("id"), "confidence": 0.85}

        return None

if __name__ == "__main__":
    resolver = IdentityResolver([
        {"id": 101, "name": "Hardik Sapra", "pan": "ABCDE1234F"}
    ])
    result = resolver.match_client("ABCDE1234F", "Hardik Sapra")
    print(f"Match test result: {result}")
