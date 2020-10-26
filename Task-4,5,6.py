class Storage:
    storage = {}
    title = ['ID', 'Developer', 'Model', 'Price', 'Format', 'Pr_PPI', 'Pr_speed', 'Pr_color', 'Sc_PPI', 'Sc_speed',
             'Sc_color']

    def add_equip(self, quantity, equipment):
        if self.storage.get(equipment) is None:
            self.storage.update({equipment: quantity})
        else:
            self.storage.update({equipment: self.storage.pop(equipment) + quantity})
        print(f'Added {quantity} {equipment.inf[1]} {equipment.inf[2]}')

    def remove_equip(self, quantity, equipment):
        if self.storage.get(equipment) is None:
            print('Вы не можете передать несуществий товар')
        elif self.storage[equipment] - quantity == 0:
            self.storage.pop(equipment)
        else:
            self.storage.update({equipment: self.storage.pop(equipment) - quantity})
        print(f'Removed {quantity} {equipment.inf[1]} {equipment.inf[2]}')
        print('Now we got 0' if self.storage.get(equipment) is None else f'Now we got {self.storage.get(equipment)}')

    def __str__(self):
        print(f'Quantity|' + '|'.join(f'{el:10}' for el in self.title) + '|')
        for key in self.storage.keys():
            print('-' * 130)
            print(f'{self.storage.get(key):8}|', end='')
            print(key)
        return ''


class OfficeEquipment:
    inf = []

    def __str__(self):
        return '|'.join(f'{el:10}' if el is not None else f'{"None":10}' for el in self.inf) + '|'

    def validate(self):
        if not isinstance(self.inf[3], (int, float)):
            print(f'Передана некорректная стоимость товара {self.inf[1]} {self.inf[2]}')
            self.inf[3] = None
        if not isinstance(self.inf[5], (int, float, type(None))):
            print(f'Передано некорректное значение чёткости печати {self.inf[1]} {self.inf[2]}')
            self.inf[5] = None
        if not isinstance(self.inf[7], (int, float, type(None))):
            print(f'Передано некорректное значение скорости печати {self.inf[1]} {self.inf[2]}')
            self.inf[7] = None
        if not isinstance(self.inf[8], (int, float, type(None))):
            print(f'Передано некорректное значение чёткости сканирования {self.inf[1]} {self.inf[2]}')
            self.inf[8] = None
        if not isinstance(self.inf[10], (int, float, type(None))):
            print(f'Передано некорректное значение скорости сканирования {self.inf[1]} {self.inf[2]}')
            self.inf[10] = None


class Printer(OfficeEquipment):
    def __init__(self, equip_id, price, developer, model, print_ppi, print_speed, print_color=False, sheet_type='A4'):
        self.inf = [equip_id, developer, model, price, sheet_type, print_ppi, print_color, print_speed, None, None,
                    None]
        super().validate()


class Scanner(OfficeEquipment):
    def __init__(self, equip_id, price, developer, model, scan_ppi, scan_speed, scan_color=False, sheet_type='A4'):
        self.inf = [equip_id, developer, model, price, sheet_type, None, None, None, scan_ppi, scan_color, scan_speed]
        super().validate()


class MFP(OfficeEquipment):
    def __init__(self, equip_id, price, developer, model, print_ppi, print_speed, scan_ppi, scan_speed,
                 print_color=False, scan_color=False, sheet_type='A4'):
        self.inf = [equip_id, developer, model, price, sheet_type, print_ppi, print_color, print_speed, scan_ppi,
                    scan_color, scan_speed]
        super().validate()


p_1 = Printer('01', 'fd', 'hp', 'mx350', 320, 3, True)
s_1 = Scanner('02', 125, 'Xerox', 'i10', 220, 2.5, True)
m_1 = MFP('03', 300, 'hp', 'mp76ex', 320, 3.5, 220, 2, False, True, 'A3')
s = Storage()
s.add_equip(3, p_1)
s.add_equip(10, s_1)
s.add_equip(7, m_1)
print(s)
p_1.inf[3] = 200
s.remove_equip(2, p_1)
s.remove_equip(8, s_1)
s.remove_equip(7, m_1)
print(s)
