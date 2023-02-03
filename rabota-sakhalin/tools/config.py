from typing import NamedTuple


class __Settings(NamedTuple):
    HOST: str
    PORT: str
    USER: str
    PASSWORD: str
    DATABASE: str

settings = __Settings(
    HOST="127.0.0.1",
    PORT="5432",
    USER="rosya",
    PASSWORD="888",
    DATABASE="edwica"
)
TABLE_NAME = "vacancies_rabota_sakhalin"

CreateVacanciesTableQuery = f"""CREATE TABLE IF NOT EXISTS {TABLE_NAME}(
    id text not null,
    title text not null,
    region text,
    min_salary integer,
    max_salary integer,
    specialization text,
    experience_in_years integer,
    employment varchar(255),
    skills text[],
    create_date date,
    url text,
    
    PRIMARY KEY (id)
);"""
