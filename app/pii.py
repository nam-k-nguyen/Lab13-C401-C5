from __future__ import annotations

import hashlib
import re

PII_PATTERNS: dict[str, str] = {
    "email": r"[\w\.-]+@[\w\.-]+\.\w+",
    "phone_vn": r"(?:\+84|0)[ \.-]?\d{3}[ \.-]?\d{3}[ \.-]?\d{3,4}", # Matches 090 123 4567, 090.123.4567, etc.
    "cccd": r"\b\d{12}\b",
    "credit_card": r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b",
    # Vietnamese passport (CMT/HC): 8 or 9 digits, or format B<7 digits>
    "passport_vn": r"\b([A-C]\d{7}|\d{8,9})\b",
    # Vietnamese address keywords (street, ward, district, city in Vietnamese)
    "address_vn": r"\b(?:duong|đường|phuong|phường|quan|quận|huyen|huyện|tp\.?|thành phố)\b[\w\s]*",
    # Date of birth (DOB): dd/mm/yyyy or dd-mm-yyyy
    "dob": r"\b\d{2}[/-]\d{2}[/-]\d{4}\b",
}


def scrub_text(text: str) -> str:
    safe = text
    for name, pattern in PII_PATTERNS.items():
        safe = re.sub(pattern, f"[REDACTED_{name.upper()}]", safe)
    return safe


def summarize_text(text: str, max_len: int = 80) -> str:
    safe = scrub_text(text).strip().replace("\n", " ")
    return safe[:max_len] + ("..." if len(safe) > max_len else "")


def hash_user_id(user_id: str) -> str:
    return hashlib.sha256(user_id.encode("utf-8")).hexdigest()[:12]
