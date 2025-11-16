import pandas as pd


def read_csv_file(csv_file) -> list[dict]:
    """Преобразует файл csv в список словарей"""
    csv_file = pd.read_csv(csv_file, sep=";")
    csv_file_list = csv_file.to_dict("records")
    return csv_file_list


def read_excel(xlsx_file) -> list[dict]:
    """Преобразует файл xlsx в список словарей"""
    excel_file = pd.read_excel(xlsx_file)
    excel_file_list = excel_file.to_dict("records")
    return excel_file_list


if __name__ == "__main__":
    print(read_csv_file('data/transactions.csv'))