from tools.models import SakhalinData


def parse_vacancy(data: dict) -> SakhalinData:
    return (SakhalinData(
        Title=data["name"],
        MaxSalary=data["max_salary"],
        MinSalary=data["min_salary"],
        Url=data["link"]
    ))