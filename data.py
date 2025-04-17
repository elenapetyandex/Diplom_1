class Data:
    bun_list = [
        ['black bun', 100],
        ['white bun', 75.3],
        ['red bun', 0]
    ]
    ingredients_for_burger = [
        ['SAUCE', 'hot sauce', 200],
        ['FILLING', 'cutlet', 115.75],
        ['FILLING', 'dinosaur', 0 ]
    ]

    bun_list_from_database = [
        ["black bun", 100],
        ['white bun', 200],
        ['red bun', 300]
    ]

    ingredient_list_from_database = [
        ['SAUCE', 'hot sauce', 100],
        ['SAUCE', 'sour cream', 200],
        ['SAUCE', 'chili sauce', 300],
        ['FILLING', 'cutlet', 100],
        ['FILLING', 'dinosaur', 200],
        ['FILLING', 'sausage', 300]
    ]


    bun_and_ingredient_price_valid = [
        [0, 1000000],
        [215.11111111, 0],
        [300, 215.11111111],
        [1000000, 300],
        [0, 0]
    ]

    bun_and_ingredient_price_invalid = [
        [200, -0.01],
        [-1000, 200],
        [-0.01, -1000]
    ]