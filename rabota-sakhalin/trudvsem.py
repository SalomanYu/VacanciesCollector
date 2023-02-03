import re

from tools.models import TrudVsemData
from tools.decoding import get_json


def parse_vacancy(url: str) -> TrudVsemData | None:
    vacancy_id = url.split("card/")[-1]
    api_url = f"https://opendata.trudvsem.ru/api/v1/vacancies/vacancy/{vacancy_id}"
    json = get_json(api_url)
    try:
        vacancy_data = json["results"]["vacancies"][0]["vacancy"]
        return TrudVsemData(
            Id=vacancy_id,
            Date=vacancy_data["creation-date"],
            Region=parse_region(vacancy_data),
            Employment=vacancy_data["employment"],
            Skills=parse_skills(vacancy_data["duty"]),
            ExperienceInYears=parse_experience(vacancy_data["requirement"]),
            Specialization=vacancy_data["category"]["specialisation"])
    except:
        return None
    
def parse_region(data: dict) -> str:
    try:
        return data["addresses"]["address"][0]["location"].split(",")[0]
    except BaseException as err:
        print("Не удалось выбрать регион:", err)
        return ""

def parse_skills(text: str) -> list[str]:
    if text.count("\n") > 1:
        return text.split("\n")
    elif text.count(";") > 1:
        return text.split(";")

def parse_experience(data: dict) -> int:
    try:
        pattern = "\d+"
        experience = re.findall(pattern, str(data["experience"]))[0]
        return int(experience)
    except KeyError:
        return 0