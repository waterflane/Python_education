
def smart_tourist(kg):
    things = {
        'зажигалка': 20, 
        'компас': 100, 
        'фрукты': 500, 
        'рубашка': 300,
        'термос': 1000, 
        'аптечка': 200, 
        'куртка': 600, 
        'бинокль': 400, 
        'удочка': 1200,
        'салфетки': 40, 
        'бутерброды': 820, 
        'палатка': 5500, 
        'спальный мешок': 2250, 
        'жвачка': 10
        }

    def key(el):
        return el[1]

    res = []
    kg = kg * 1000
    things = dict(sorted(things.items(), key=key, reverse=True))

    for keys, items in things.items():
        if items <= kg:
            kg -= items
            res.append(keys)
    return res

assert smart_tourist(1) == ['термос'], smart_tourist(1)
assert smart_tourist(2) == ['удочка', 'куртка', 'аптечка'], smart_tourist(2)
assert smart_tourist(3) == ['спальный мешок', 'куртка', 'компас', 'салфетки', 'жвачка'], smart_tourist(3)

