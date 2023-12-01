from dataclasses import dataclass
from datetime import datetime

@dataclass
class TodoDomain:
    id: int
    title: str
    description: str
    priority: str
    due_date: datetime
