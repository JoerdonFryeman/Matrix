from random import choice, random

from .visualisation import Visualisation


class Matrix(Visualisation):

    @staticmethod
    def generate_symbol(*args: bool) -> str:
        """Этот метод возвращает случайный символ из списка булевых значений."""
        generated_symbol = (
            *(i for i in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9') if args[0]),
            *(i for i in ('!', '@', '#', '%', '&', '§', '№', '~', '/', '?') if args[1]),
            *(i for i in ('₿', '₽', '€', '$', '₩', 'ƒ', '¥', '₹', '₫', '£') if args[2]),
            *(i for i in ('π', 'λ', 'β', 'γ', 'Ω', 'θ', 'Σ', 'Ψ', 'ξ', 'ω') if args[3]),
            *(i for i in ('X', 'Y', 'Z', 'x', 'y', 'z', 'r', 'd', 'f', 'l') if args[4]),
            *(i for i in ('Ё', 'ё', 'Э', 'э', 'Ф', 'ф', 'Ъ', 'ъ', 'Я', 'я') if args[5]),
            *(i for i in ('小', '女', '体', '里', '字', '书', '永', '甲', '人', '是') if args[6])
        )
        try:
            return choice(generated_symbol)
        except IndexError:
            return choice(('0', '1'))

    def validate_speed_bounds(self) -> None:
        """Проверяет корректность self.min_speed и self.max_speed."""
        try:
            min_s = int(self.min_speed)
            max_s = int(self.max_speed)
        except Exception:
            raise ValueError("min_speed и max_speed должны быть целыми числами.")

        if min_s <= 0:
            raise ValueError("min_speed должен быть > 0.")
        if max_s <= 0:
            raise ValueError("max_speed должен быть > 0.")
        if min_s >= max_s:
            raise ValueError("min_speed должен быть меньше max_speed.")
        if max_s > 100:
            raise ValueError("max_speed не может быть больше 100.")

        self.min_speed = min_s
        self.max_speed = max_s

    def calculate_bold_probability(self, init_speed: float) -> bool:
        """Вычисляет вероятность жирного символа для заданной скорости и возвращает True."""
        return random() < max(0.02, min(0.9, self.bold_symbols_rate / init_speed))
