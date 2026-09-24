class utils:

    @staticmethod
    def reversed(number):
        if isinstance(number, bool) or not isinstance(number, int):
            raise TypeError("reversed() expects an int, got " + type(number).__name__)
        sign = -1 if number < 0 else 1
        digits = str(abs(number))
        flipped = digits[::-1]
        return sign * int(flipped)

    @staticmethod
    def formatter(number):
        if isinstance(number, bool) or not isinstance(number, int):
            raise TypeError("formatter() expects an int, got " + type(number).__name__)
        return format(number, "b"), format(number, "o")
