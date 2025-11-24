from utils import json_read_file
from read_csv_excel import read_csv_file, read_excel
from processing import filter_by_state, sort_by_date
from generators import filter_by_currency
from process_bank import process_bank_search
from widget import get_date, mask_account_card


def main():
    """Основная функция проекта, связывающая все функциональности"""
    global choice, choice_list, sort_date, sort_currency, filter_transactions, amount, currency_name
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    answer = input("Введите номер интересующей информации:  ")
    if answer == "1":
        print("Для обработки выбран JSON-файл.")
        choice = json_read_file(r"../data/operations.json")
    elif answer == "2":
        print("Для обработки выбран CSV-файл.")
        choice = read_csv_file(r"../data/transactions.csv")
    elif answer == "3":
        print("Для обработки выбран XLSX-файл.")
        choice = read_excel(r"../data/transactions_excel.xlsx")

    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы:")
    print("EXECUTED")
    print("CANCELED")
    print("PENDING")
    status = input()
    status_list = ["EXECUTED", "CANCELED", "PENDING"]
    while status.upper() not in status_list:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы:")
        print("EXECUTED")
        print("CANCELED")
        print("PENDING")
        status = input()
    else:
        choice_list = filter_by_state(choice, status.upper())

    print("Отсортировать операции по дате? Да/Нет")
    answer_date = input()
    while answer_date.title() != "Да" and answer_date.title() != "Нет":
        print("Неверный ввод данных!")
        print("Отсортировать операции по дате? Да/Нет")
        print('Введите пожалуйста "Да" или "Нет"')
        answer_date = input()
    if answer_date.title() == "Да":
        print("Отсортировать по возрастанию или по убыванию?")
        sort_reverse = input()
        while (
            sort_reverse.lower() != "по убыванию"
            and sort_reverse.lower() != "по возрастанию"
        ):
            print("Неверный ввод данных!")
            print("Отсортировать по возрастанию или по убыванию?")
            print('Введите пожалуйста "по убыванию" или "по возрастанию"')
            sort_reverse = input()
        if sort_reverse.lower() == "по убыванию":
            sort_date = sort_by_date(choice_list)
        elif sort_reverse.lower() == "по возрастанию":
            sort_date = sort_by_date(choice_list, False)
    elif answer_date.title() == "Нет":
        sort_date = choice_list

    print("Выводить только рублевые транзакции? Да/Нет")
    choice_rub = input()
    while choice_rub.title() != "Да" and choice_rub.title() != "Нет":
        print("Неверный ввод данных!")
        print("Выводить только рублевые транзакции? Да/Нет")
        print('Введите пожалуйста "Да" или "Нет"')
        choice_rub = input()
    if choice_rub.title() == "Да":
        sort_currency = filter_by_currency(sort_date, "RUB")
    elif choice_rub.title() == "Нет":
        sort_currency = sort_date

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    filter_words = input()
    while filter_words.title() != "Да" and filter_words.title() != "Нет":
        print("Неверный ввод данных!")
        print(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет"
        )
        print('Введите пожалуйста "Да" или "Нет"')
        filter_words = input()
    if filter_words.title() == "Да":
        words_input = input("Напишите слова для фильтра: ")
        filter_transactions = process_bank_search(sort_currency, words_input)
    elif filter_words.title() == "Нет":
        filter_transactions = sort_currency

    print("\nРаспечатываю итоговый список транзакций")
    print(f"\nВсего банковских операций в выборке: {len(filter_transactions)}")

    if len(filter_transactions) > 0:
        for transaction in filter_transactions:
            if transaction.get("operationAmount") is not None:
                amount = transaction.get("operationAmount").get("amount")
            if transaction.get("operationAmount") is not None:
                if transaction.get("currency") is None:
                    currency_name = (
                        transaction.get("operationAmount").get("currency").get("name")
                    )
            else:
                amount = transaction.get("amount")
                currency_name = transaction.get("currency_name")
            date = get_date(transaction.get("date"))
            sender_card = mask_account_card(str(transaction.get("from")))
            recipient = mask_account_card(str(transaction.get("to")))
            print(f"\n{date} {transaction.get('description')}")
            print(f"{sender_card} -> {recipient}")
            print(f"Сумма: {amount} {currency_name}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    return


if __name__ == "__main__":
    print(main())
