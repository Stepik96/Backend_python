# Практические задания Python

Решения лекций 1 и 2. Python 3.11.

## Окружение

Окружение находится в `Лекция 2/calculator/.venv`.
Из корневой папки проекта в PowerShell:

```powershell
& ".\Лекция 2\calculator\.venv\Scripts\python.exe" -m pip install -r requirements-dev.txt
& ".\Лекция 2\calculator\.venv\Scripts\python.exe" -m unittest discover -s tests -v
& ".\Лекция 2\calculator\.venv\Scripts\python.exe" -m unittest discover -s "Лекция 2/calculator" -p test_calculator.py -v
& ".\Лекция 2\calculator\.venv\Scripts\python.exe" "Лекция 2/calculator/test_numpy.py"
```

Если окружение отсутствует, сначала выполните:
`python -m venv "Лекция 2/calculator/.venv"`.

Скрипты заданий запускаются тем же интерпретатором с указанием пути.
Римский конвертер принимает канонические числа от I до MMMCMXCIX.
Для N < 2 решето возвращает пустой список.
