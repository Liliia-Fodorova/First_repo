import requests
from datetime import date

URL = "https://raw.githubusercontent.com/lod-db/orc-losses/main/russian-losses.json"


def main():
    try:
        response = requests.get(URL, timeout=15)
        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list) or not data:
            print("Данные отсутствуют")
            return

        latest = max(data, key=lambda item: item["date"])

        categories = {
            "personnel": "Личный состав",
            "tanks": "Танки",
            "apvs": "Бронетехника",
            "artillery": "Артиллерия",
            "airDefense": "ПВО",
            "aircraft": "Самолёты",
            "helicopters": "Вертолёты",
            "uavs": "Беспилотники",
            "cruiseMissiles": "Крылатые ракеты",
        }

        print("\n" + "=" * 48)
        print("СТАТИСТИКА ПОТЕРЬ РОССИЙСКОЙ АРМИИ")
        print("=" * 48)
        print(f"Дата данных: {latest['date']}")
        print(f"Сегодня: {date.today()}")
        print("-" * 48)

        for key, name in categories.items():
            value = latest.get(key)

            if value is not None:
                print(f"{name:<25} {value:>12,}")

        print("=" * 48)
        print("Источник: Генеральный штаб ВСУ")
        print("Данные обновляются при запуске программы")

    except requests.RequestException as error:
        print("Ошибка подключения:", error)


if __name__ == "__main__":
    main()
