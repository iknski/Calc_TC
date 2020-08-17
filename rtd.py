class RTD:
    """Создаем термопреобразователь сопротивления"""

    def __init__(self, nominal, material):
        """Инициализируем параметры ТС"""
        self.nominal = nominal
        self.material = material

    def type(self):
        """Определяем градуировку ТС"""
        type_tc = str(self.nominal) + self.material
        return type_tc
