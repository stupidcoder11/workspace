import re

def extract_citations(answer: str) -> list[int]:
    matches = re.findall(
        r"\[(.*?)\]",
        answer
    )

    citations: set[int] = set()

    for match in matches:
        for num in re.findall(r"\d+", match):
            citations.add(int(num))

    return sorted(citations)
