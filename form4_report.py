from dataclasses import dataclass
from datetime import datetime

@dataclass
class Form4Report:
    insider_name: str
    company_name: str
    transaction_date: datetime
    shares_bought: int
