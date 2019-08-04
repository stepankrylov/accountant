from application.salary import calculate_salary
from db.people import get_employees

def main():
    print('main.py запущен')

if __name__ == '__main__':
    main()
    calculate_salary()
    get_employees()