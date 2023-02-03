import psycopg2
from tools.models import Vacancy
from tools.config import settings, CreateVacanciesTableQuery, TABLE_NAME

COLUMNS_COUNT = 11

def connect() -> psycopg2.extensions.connection | None:
    try:
        connection = psycopg2.connect(database=settings.DATABASE, user=settings.USER, password=settings.PASSWORD, host=settings.HOST, port=settings.PORT)
    except BaseException as err:
        print(err)
        connection = None
    finally:
        return connection

def create_table():
    connection = connect()
    if connection is None: return f"Failed to connect to the database: {settings.DATABASE}"
    cursor = connection.cursor()
    try:
        cursor.execute(CreateVacanciesTableQuery)
        connection.commit()
    except BaseException as err:
        print("Failed to created table!", err)
    finally:
        connection.close()

def add_multiple_rows(data: list[Vacancy]):
    connection = connect()
    if connection is None: return f"Failed to connect to the database: {settings.DATABASE}"
    cursor = connection.cursor()

    try:
        rows = ",".join("%s" for _ in range(COLUMNS_COUNT))
        cursor.executemany(f"INSERT INTO {TABLE_NAME} VALUES({rows})", [(i.TrudVsem.Id, i.Sakhalin.Title, i.TrudVsem.Region, i.Sakhalin.MinSalary, i.Sakhalin.MaxSalary, i.TrudVsem.Specialization, i.TrudVsem.ExperienceInYears, i.TrudVsem.Employment, i.TrudVsem.Skills, i.TrudVsem.Date, i.Sakhalin.Url) for i in data])
        connection.commit()
        print("Succesuful")
    except BaseException as err:
        print(f"Failed to adding {len(data)} vacancies in table:", err)
    finally:
        connection.close()