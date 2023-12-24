from dataclasses import dataclass

@dataclass
class TodoDomain:
    id: int
    title: str
    description: str
    priority: str
    dueDate: str