import datetime

import aiof.config as config

from aiof.data.asset import Asset
from aiof.data.liability import Liability

from pydantic import BaseModel, typing, validator
from typing import List, Optional


_settings = config.get_settings()
_event_types = _settings.LifeEventTypes

class LifeEventRequest(BaseModel):
    """
    Life event request class. This is used to request specific event
    """
    assets: List[Asset]
    liabilities: Optional[List[Liability]]
    type: str
    amount: Optional[float]
    plannedDate: Optional[datetime.datetime]

    # Contributions
    monthlyCashContribution: Optional[float]
    monthlyInvestmentContribution: Optional[float]
    monthlyStockContribution: Optional[float]

    # Car
    carLoanAmount: Optional[float]
    carDownPayment: Optional[float]
    carInterest: Optional[float]
    carYears: Optional[int]


    @validator("type")
    def type_must_be_valid(cls, t):
        if t not in _event_types:
            raise ValueError("Invalid type. Please use one of the following {0}".format(", ".join(str(x) for x in _event_types)))
        return t.title()


class LifeEventResponse(BaseModel):
    """
    Life event response class. This is used to return specific response
    """
    assets: Optional[List[Asset]]
    liabilities: Optional[List[Liability]]
    event: Optional[typing.Any]
