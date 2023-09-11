class Constants:
    """Класс Constants предоставляет списки индексов для копирования данных из разных категорий.

    Атрибуты:
        capex (list): Список индексов для данных CAPEX.
        production (list): Список индексов для данных Production.
        opex (list): Список индексов для данных OPEX.
        market (list): Список индексов для данных Market.
        tax (list): Список индексов для данных Tax.
        npv (list): Список индексов для данных NPV.
        elastic (list): Список индексов для данных Elastic.
        credits (list): Список индексов для данных Credits.
        montecarlo (list): Список индексов для данных MonteCarlo.
    """

    # Excel part:
    COPY_DICT = {
        "CAPEX": [1, 3, 5, 10, 11, 13, 15, 10, 21, 23, 25, 10, 31, 33, 35, 10, 41, 43, 45, 10, 51, 53, 55, 10, 61, 63,
                  65, 10, 71, 73, 75, 10, 81, 83, 85, 10, 91, 93, 95, 10, 101, 103, 105, 10, 10, 10],
        "Production": [1, 2, 6, 6, 6],
        "OPEX": [1, 3, 6, 7, 8, 10, 13, 7, 15, 17, 20, 7, 22, 24, 27, 7, 29, 31, 34, 7, 36, 38, 41, 7, 43, 45, 48, 7,
                 50, 52, 55, 7, 57, 59, 62, 7,
                 64, 66, 69, 7, 7, 7],
        "Market": [1, 2, 3, 7, 8, 10, 11, 12, 13, 14, 17, 18, 19, 20, 21, 23, 11, 11, 11],
        "Tax": [1, 4, 5, 6, 9, 5, 11, 14, 5, 16, 19, 5, 21, 25, 5, 27, 30, 5, 5, 5],
        "NPV": [1, 7, 9, 10, 11, 13, 14, 17, 18, 19, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
        "Elastic": [55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55,
                    55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55,
                    55, 55, 55],
        "Credits": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                    28, 29],
        "MonteСarlo": [],
    }

    MERGE_HEAD_DICT = {
        "CAPEX": ['A4:A6', 'A8:A10', 'A12:A14', 'A16:A18', 'A20:A22', 'A24:A26', 'A28:A30', 'A32:A34', 'A36:A38',
                  'A40:A42', 'A44:A46'] + ['B4:C4', 'B8:C8', 'B12:C12', 'B16:C16', 'B20:C20', 'B24:C24', 'B28:C28',
                                           'B32:C32', 'B36:C36', 'B40:C40'],
        "Production": ['A50:A51'] + ['B50:C50'],
        "OPEX": ['A55:A57', 'A59:A61', 'A63:A65', 'A67:A69', 'A71:A73', 'A75:A77', 'A79:A81', 'A83:A85', 'A87:A89',
                 'A91:A93'] + ['B55:C55', 'B59:C59', 'B63:C63', 'B67:C67', 'B71:C71', 'B75:C75', 'B79:C79', 'B83:C83',
                               'B87:C87', 'B91:C91'],
        "Market": ['A97:A102', 'A104:A112'] + ['B97:C97', 'B104:C104'],
        "Tax": ['A116:A117', 'A119:A120', 'A122:A123', 'A125:A126', 'A128:A129', 'A131:A132'] + ['B116:C116',
                                                                                                 'B119:C119',
                                                                                                 'B122:C122',
                                                                                                 'B125:C125',
                                                                                                 'B128:C128',
                                                                                                 'B131:C131'],
        "NPV": ['A136:A139', 'A141:A145'] + ['B136:C136', 'B143:C143'],
        "Elastic": [],
        "Credits": ['A219:A223', 'A233:A237'] + ['A212:B212', 'C212:D212', 'B219:C219', 'A226:B226', 'C226:D226',
                                                 'B233:C233'],
        "MonteСarlo": [],
    }

    GRAPH_DICT = {
        "NPV": {
            "index": [0],
            "place": ['I141'],
            "attributes": [
                {
                    "title": "График сроков окупаемости",
                    "width": 25.4
                }
            ]
        },
        "Elastic": {
            "index": [0, 1, 2],
            "place": ['A160', 'A177', 'A194'],
            "attributes": [
                {
                    "title": "График общей чувствительности",
                    "width": 23.7,
                    'height': 7.6
                },
                {
                    "title": "График общей чувствительности по CAPEX",
                    "width": 23.7,
                    'height': 7.6
                },
                {
                    "title": "График общей чувствительности по OPEX",
                    "width": 23.7,
                    'height': 7.6
                }
            ]
        },
        "MonteСarlo": {
            "index": [0],
            "place": ['A241'],
            "attributes": [
                {
                    "title": "Анализ рисков применения инновационных технологий",
                    "width": 22,
                    'height': 7.1
                }
            ]

        },
    }
    TITLE_LIST = ['A3:C3', 'A49:C49', 'A54:C54', 'A96:C96', 'A115:C115', 'A135:C135', 'A158:C158', 'A211:C211',
                  'A240:C240']

    ROTATE_LIST = ['A4', 'A8', 'A12', 'A16', 'A20', 'A24', 'A28', 'A32', 'A36', 'A40', 'A44', 'A50', 'A55', 'A59',
                   'A63', 'A67', 'A71', 'A75', 'A79', 'A83', 'A87', 'A91', 'A97', 'A104', 'A116', 'A119', 'A122',
                   'A125', 'A128', 'A131', 'A136', 'A141', 'A219', 'A233']

    HEIGHT_DICT = {'109': 10, '110': 10, '111': 10, '138': 10, '139': 10, '144': 10, '145': 10}
