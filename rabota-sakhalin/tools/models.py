from typing import NamedTuple
from datetime import date


class SakhalinData(NamedTuple):
    Title:str
    MinSalary:str
    MaxSalary:str
    Url: str

class TrudVsemData(NamedTuple):
    Id: str
    Date: date
    Specialization: str
    Region: str
    Employment: str
    Skills: list[str]
    ExperienceInYears: int

class Vacancy(NamedTuple):
    Sakhalin: SakhalinData
    TrudVsem: TrudVsemData
