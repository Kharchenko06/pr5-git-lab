# utils.py - вспомогательные функции

def print_repo_info():
    """Выводит информацию о репозитории"""
    print("Репозиторий: pr5-git-lab")
    print("Ветка: code-branch")
    print("Файлы: main.py, utils.py, README.md и др.")

def calculate_statistics(numbers):
    """Рассчитывает статистику по списку чисел"""
    return {
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers)
    }

if __name__ == "__main__":
    print_repo_info()
    stats = calculate_statistics([1, 2, 3, 4, 5])
    print(f"Статистика: {stats}")
