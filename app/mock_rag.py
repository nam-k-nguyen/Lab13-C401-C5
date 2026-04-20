from __future__ import annotations

import time

from .incidents import STATE

CORPUS = {
    "london": ["London is the capital of England. Top attractions: Big Ben, Tower of London, British Museum, Buckingham Palace."],
    "visa": ["Vietnamese citizens need a UK Standard Visitor Visa. Apply online at least 3 weeks before travel."],
    "transport": ["UK has extensive rail, bus and Underground networks. Oyster card covers all zones in London."],
    "scotland": ["Scotland offers stunning highlands, Edinburgh Castle, and whisky distillery tours. Best visited May-September."],
    "weather": ["UK weather is mild but unpredictable. Carry a raincoat year-round. Summer averages 18-22°C in London."],
}


def retrieve(message: str) -> list[str]:
    if STATE["tool_fail"]:
        raise RuntimeError("Vector store timeout")
    if STATE["rag_slow"]:
        time.sleep(2.5)
    if STATE["quality_drop"]:
        return []
    lowered = message.lower()
    for key, docs in CORPUS.items():
        if key in lowered:
            return docs
    return ["No domain document matched. Use general fallback answer."]
