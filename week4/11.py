"""Restuarant"""

def main():
    """main function"""
    menu1 = int(input())
    menu2 = int(input())
    menu3 = int(input())
    menu4 = int(input())
    menu5 = int(input())
    menu6 = int(input())
    menu7 = int(input())
    menu8 = int(input())
    menu = {1:'Fish and Chips', 2:'Hamburger', 3:'Spaghetti Carbonara', 4:'Spaghetti Meatball', \
    5:'Lasagna', 6:'Garlic Bread', 7:'Water', 8:'Ice'}
    cost = {1:69, 2:79, 3:85, 4:70, 5:80, 6:40, 7:15, 8:3}
    price = cost.get(menu1)+cost.get(menu2)+cost.get(menu3)+cost.get(menu4)+\
    cost.get(menu5)+cost.get(menu6)+cost.get(menu7)+cost.get(menu8)
    total = price * 1.07
    total_menu = '%d%d%d%d%d%d%d%d'%(menu1, menu2, menu3, menu4, menu5, menu6, menu7, menu8)
    if total_menu.count('1') >= 1:
        print('%s (%d)  %d'%(menu.get(1), total_menu.count('1'), cost.get(1)*total_menu.count('1')))
    if total_menu.count('2') >= 1:
        print('%s (%d)  %d'%(menu.get(2), total_menu.count('2'), cost.get(2)*total_menu.count('2')))
    if total_menu.count('3') >= 1:
        print('%s (%d)  %d'%(menu.get(3), total_menu.count('3'), cost.get(3)*total_menu.count('3')))
    if total_menu.count('4') >= 1:
        print('%s (%d)  %d'%(menu.get(4), total_menu.count('4'), cost.get(4)*total_menu.count('4')))
    if total_menu.count('5') >= 1:
        print('%s (%d)  %d'%(menu.get(5), total_menu.count('5'), cost.get(5)*total_menu.count('5')))
    if total_menu.count('6') >= 1:
        print('%s (%d)  %d'%(menu.get(6), total_menu.count('6'), cost.get(6)*total_menu.count('6')))
    if total_menu.count('7') >= 1:
        print('%s (%d)  %d'%(menu.get(7), total_menu.count('7'), cost.get(7)*total_menu.count('7')))
    if total_menu.count('8') >= 1:
        print('%s (%d)  %d'%(menu.get(8), total_menu.count('8'), cost.get(8)*total_menu.count('8')))
    print('Subtotal %d'%(price//1))
    if total%2 == 0 or total%2 == 5:
        print('Total (VAT 7%) '+str(int(total)))
    else:
        print('Total (VAT 7%) '+str(int(total//1+1)))

main()
