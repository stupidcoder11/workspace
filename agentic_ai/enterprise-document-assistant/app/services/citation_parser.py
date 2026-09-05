import re

def extract_citations(answer: str) -> list[int]:
    matches = re.findall(
        r"\[(\d+)\]",
        answer
    )

    return sorted(set(int(m) for m in matches))
