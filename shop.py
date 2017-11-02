suppliers = [['Johnson', 'Johnson@mail.com']]
companies = ['Johnson', 'Semirenko', 'Chiliwilly', 'Friends', 'Craftfood']

products = [['Pineapple', 4, 2.5, 'Johnson'], ['Banana', 5, 2.0, 'Chiliwilly']]


def sort_col(array):
    return array[index]


def print_products():
    global product
    print('-' * the_longest_word * 4 + '-' * 5)
    print('|{0}|{1}|{2}|{3}|'.format('title'.center(the_longest_word), 'price'.center(the_longest_word),
                                     'quantity'.center(the_longest_word), 'company'.center(the_longest_word)))
    print('-' * the_longest_word * 4 + '-' * 5)
    for product in products:
        print('|{title}|{price}|{quantity}|{company}|'.format(title=product[0].center(the_longest_word),
                                                              price=str(product[2]).center(the_longest_word),
                                                              quantity=str(product[1]).center(the_longest_word),
                                                              company=product[3].center(the_longest_word)))


def filter_products(sequence):
    return [i for i in products if sequence in i[0] or sequence in i[3]]


welcome = ' '

print('Hello, Employee!')


while welcome != 'Q':
    welcome = input(
        '''What do you like to do?
Input 0 to add supplier;
Input 1 to add product;
Input 2 to see all items;
Press Q to Quit\n''').capitalize()

    if welcome == '0':
        name = input('Enter the Name \n').lower()
        email = input('Enter the e-mail \n').lower()
        name_email = [name, email]
        if name_email not in suppliers:
            suppliers.append(name_email)
            print('Contacts were successfully added! \n')
            print(suppliers)
        else:
            print('Those contacts already have been added!')
            print(name.capitalize())
            print(email)

    elif welcome == '1':
        title = ''
        while len(title) < 5:
            title = input('Enter title \n')
            print('Title length must be longer then 3')  # <--print even if title correct !!!
            continue
        amount = ''
        price = ''
        while amount.isdigit() == False and price.isdigit() == False:
            amount = input('Enter number \n')
            price = input('Enter price \n')
            print('Amount and price should be digit!')  # <--print even if type of amount and price correct !!!
            continue
        if amount.isdigit() and price.isdigit():
            amount = int(amount)
            price = float(price)
        for a, b in enumerate(companies, 1):
            print('{} {}'.format(a, b))
        firm = int(input('Enter the number of company \n')) - 1  # index in companies
        producer = companies[firm]
        product = [title, amount, price, producer]
        products.append(product)
        print('Product info was successfully added')
        print(products)

    elif welcome == '2':

        items = []
        for product in products:
            for i in product:
                items.append(str(i))
        the_longest_word = len(max(items, key=len))
        # -----------------------------
        # |title|price|quantity|company|
        # -----------------------------
        print_products()

        filter_or_sort = input('What do you like to do? '
                               'Press 0 to Sort;'
                               'Press 1 to Filter \n')

        if filter_or_sort == '0':

            sort_items = input(
                'If you want to sort by title press 0, '
                'by price press 1, '
                'by company press 2, '
                'press any key to quite \n')
            if sort_items == '0':
                products.sort()
                print_products()
            elif sort_items == '1':
                index = int(sort_items) + 1
                products.sort(key=sort_col)
                print_products()
            elif sort_items == '2':
                index = int(sort_items) + 1
                products.sort(key=sort_col)
                print_products()
        elif filter_or_sort == '1':
            filter_option = input('What do you want to find? Enter here: \n').capitalize()
            print('-' * the_longest_word * 4 + '-' * 5)
            print('|{0}|{1}|{2}|{3}|'.format('title'.center(the_longest_word), 'price'.center(the_longest_word),
                                             'quantity'.center(the_longest_word), 'company'.center(the_longest_word)))
            print('-' * the_longest_word * 4 + '-' * 5)
            for i in filter_products(filter_option):
                print('|{0}|{1}|{2}|{3}|'.format(i[0].center(the_longest_word),
                                                 str(i[1]).center(the_longest_word),
                                                 str(i[2]).center(the_longest_word),
                                                 i[3].center(the_longest_word)))

    else:
        print('Good buy, Employee!')
