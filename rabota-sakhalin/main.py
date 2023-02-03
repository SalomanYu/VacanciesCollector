from tools.decoding import get_json
import tools.database as database
import trudvsem
import rabota_sakhalin
from tools.models import *

def parse_vacancies():
    err = database.create_table()
    if err != None: exit(err)
    next_page = f"https://back-stage.traektoria.website/api/external_vacancies/search?page=1"
    while next_page != None:        
        page_data = get_json(next_page)
        next_page = page_data["links"]["next"]
        vacancies = get_vacancies_from_page(page_data)
        database.add_multiple_rows(vacancies)


def get_vacancies_from_page(data: dict) -> list[Vacancy]:
    vacancies: list[Vacancy] = []
    for item in data["external_vacancies"]:
        if item["platform"] != "trudvsem.ru":
            print(f"Внимание! Вакансия из другого ресурса:\nUrl:{item['link']}\n-----------------\n")
            continue
        vacancy = Vacancy(
            Sakhalin=rabota_sakhalin.parse_vacancy(item),
            TrudVsem=trudvsem.parse_vacancy(item["link"]))
        if vacancy.TrudVsem is not None: 
            vacancies.append(vacancy)
    return vacancies



if __name__ == "__main__":
    parse_vacancies()
    