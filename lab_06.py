""" Lab_6
    - Answer the questions:
        1) Рядки мають наступні важливі властивості:
            - довжина може бути змінною, проте алфавіт - фіксований.
            - у більшості випадків упорядкованість послідовності є важливішою
            за індексацію.
            - частіше метою доступа до рядку є не окремий її елемент(проте це також можливо),
            а деяка послідовність символів у рядку.

        2) Можна виділити такі базові операції над рядками:
            - знаходження довжини
            - присвоювання
            - конкатенація
            - пошук входження

        3) Алгоритм порівняння рядків:
            - зліва на право попарно порівнюють символи, той рядок, в котрого символ іде раніше
            у алфавіті - молодший.
            - при досягненні кінця одного з рядків, рядок в з меншою довжиною - молодший.
            - рядки однієї довжини з однаковими послідовностями симвлолів - рівні.

        4) Конкатенація - це поєднання рядків у один, шлахом дописування другого у кінець першного.

        5) Способи подання рядків у пам'яті:
            - векторне
            - символьно-зв'язне
            - блочно-зв'язне
        6) Алгоритм видалення частини рядка:
            - Визначити границі рядка починаючи від п1 до п2.
            - Виділити з початкового рядка підрядок від 1 до п1 - 1 елементу.
            - Виділити з початкового рядка підрядок від п2 + 1 до до останнього елементу.
            - Зконкатенувати отримані два рядки.

        7) Дескриптор створюється задля того, щоб зберігати деякі властивості рядка та легко їх отримувати.

        8) Переваги та Недоліки рядка як масива:
            - Переваги:
                * легко звертатись до окремих символів.
                * зберігається у статичній пам'яті.
                * ефективно займає місце у пам'яті.
            - Недоліки:
                * неефективна змінність рядку.

        9) Переваги та недоліки рядка як однозв'язного списку:
            - Переваги:
                * Гнучке для модифікації
            - Недоліки:
                * додаткові затрати пам'яті.
                * логічно сусідні елементи не є фізичними сусідами.

        10) Переваги та недоліки рядка як двозв'язного списку:
            - Переваги:
                * реалізує рух у двох напрямках.
            - Недоліки:
                * такі самі як і в однозв'язного.
                * займає ще більше пам'яті.

        11) Блоки дозволяють працювати з цілими словами як окремими одиницями, та робити операції на їх рівні.
"""
