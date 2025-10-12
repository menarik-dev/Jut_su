import random
import string

class TestGenerateData():
    @staticmethod
    def random_string(size: int, lower_case: bool = False) -> str:
        # Используем string.ascii_uppercase (A-Z)
        chars = string.ascii_uppercase

        # Генерация строки
        random_str = ''.join(random.choice(chars) for _ in range(size))

        if lower_case:
            return random_str.lower()
        return random_str

    @staticmethod
    def random_email(domain_name: str, size: int = 10) -> str:
        # Генерируем случайную строку и добавляем домен
        random_part = TestGenerateData.random_string(size, lower_case=True)
        # Убедимся, что domain_name начинается с '@'
        if not domain_name.startswith('@'):
            domain_name = '@' + domain_name

        return random_part + domain_name

    @staticmethod
    def random_data(size: int) -> str:
        # Диапазон символов от ! (33) до ~ (126) [Python's randint включает верхнюю границу]
        data = ''.join(chr(random.randint(33, 126)) for _ in range(size))
        return data

    @staticmethod
    def random_password(size: int) -> str:
        # Генерирует случайный пароль (просто псевдоним для random_data).
        return TestGenerateData.random_data(size)

    @staticmethod
    def generate_random_number(min_value: int, max_value: int) -> int:
        # В Python's random.randrange(min, max) max - не включительно, как в C# random.Next.
        return random.randrange(min_value, max_value)

    @staticmethod
    def random_phone_number(country_code: str, digit_count: int) -> str:
        digits = ''.join(random.choice(string.digits) for _ in range(digit_count))
        return country_code + digits