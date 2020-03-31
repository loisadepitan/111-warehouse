def print_menu():
    print('-' * 30)
    print(' Pythouse - Welcome')
    print('-' * 30)

    print('[1] Register new Item')
    print('[2] Display Catalog')
    print('[3] Display Items with no Stock')
    print('[4] Update Stock manually')
    print('[5] Print stock value')
    print('[6] Remove item from stock')
        

    print('[x] Exit')

def print_header(title):
    print('\n\n') # 2 blank lines
    print('-' * 80)
    print(title)
    print('-' * 80)