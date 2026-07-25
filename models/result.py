from dataclasses import dataclass

@dataclass
class PasswordResult:

    password: str

    score: int

    level: str

    entropy: float

    dictionary_match: bool
