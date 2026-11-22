from datetime import date

estimates = [
    {
        "source": "Президент Украины",
        "date": "2026-02",
        "category": "Погибшие военнослужащие",
        "min": 55000,
        "max": 55000,
        "url": "https://www.russiamatters.org/news/russia-ukraine-war-report-card/russia-ukraine-war-report-card-nov-18-2026",
    },
    {
        "source": "CSIS",
        "date": "2026-07",
        "category": "Погибшие, раненые и пропавшие",
        "min": 525000,
        "max": 625000,
        "url": "https://www.russiamatters.org/news/russia-ukraine-war-report-card/russia-ukraine-war-report-card-nov-18-2026",
    },
]


def main():
    print("=" * 55)
    print("ОПУБЛИКОВАННЫЕ ОЦЕНКИ ПОТЕРЬ УКРАИНСКОЙ АРМИИ")
    print("=" * 55)
    print(f"Дата запуска: {date.today()}")
    print("Это исторические оценки, не данные за сегодня.")

    for item in estimates:
        print("\n" + "-" * 55)
        print("Источник:", item["source"])
        print("Дата оценки:", item["date"])
        print("Категория:", item["category"])

        minimum = item["min"]
        maximum = item["max"]

        if minimum == maximum:
            print(f"Оценка: {minimum:,}")
        else:
            print(f"Оценка: {minimum:,} - {maximum:,}")

        print("Ссылка:", item["url"])

    print("\nДанные разных источников нельзя напрямую сравнивать.")


if __name__ == "__main__":
    main()