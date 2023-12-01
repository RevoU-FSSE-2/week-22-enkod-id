from dataclasses import dataclass
from enum import Enum

@dataclass
class TodoDomain:
    id: int
    title: str
    description: str
    priority: 'Priority'
    due_date: datetime

class Priority(Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
