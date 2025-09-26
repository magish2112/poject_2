import requests
from bs4 import BeautifulSoup
from sqlmodel import Session
from src.database import engine
from src.models.medication import Medication

def parse_fullscript_catalog():
    url = "https://fullscript.com/catalog/supplements"  # пример, возможно потребуется другая ссылка
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Пример парсинга: найди нужные теги/классы на странице
    items = []
    for product in soup.select(".product-card"):  # примерный CSS-селектор
        name = product.select_one(".product-card__title").text.strip()
        brand = product.select_one(".product-card__brand").text.strip()
        form = product.select_one(".product-card__form").text.strip() if product.select_one(".product-card__form") else None
        price = None  # Цена может быть скрыта для неавторизованных
        items.append(Medication(name=name, brand=brand, form=form, price=price))
    return items

def save_to_db(items):
    with Session(engine) as session:
        for med in items:
            session.add(med)
        session.commit()

if __name__ == "__main__":
    meds = parse_fullscript_catalog()
    print(f"Найдено {len(meds)} БАДов")
    save_to_db(meds)
    print("Данные сохранены в базу")
