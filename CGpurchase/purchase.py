import pandas as pd

SteellTOupdate =[]

class Steel:
    def __init__(self , length, dia):
        # self.s8 = s8 
        # self.s10 = s10
        self.length = float(length)
        self.bal_length  =  12 - float(length)
        self.dia = float(dia)
    def Steel8mm(self):
        return (self.length / .18)*6.28*((self.dia/100)/2) * .394
    def Steel10mm(self):
        return 0

    def Steel12mm(self):
        return (self.length / 1.5)*6.28*((self.dia/100)/2) *.88
        
    def Steel16mm(self):
        try:
            if self.dia == 60:
                return 12*6*1.58
            elif self.dia == 70:
                return 12*8*1.58
            elif self.dia == 80:
                return 12*10*1.58
        except:
            return 0

    def Steel20mm(self):
        try:
            if self.dia == 90:
                return 12*10*2.46
        except:
            return 0
    def Steel25mm(self):
        return 0
    
    
    
print('#'*125)
print('Enter your choice -- p for existing data c for contineue:')
choice = input()
if choice == 'p': 
    dataToPrint = pd.read_csv('WhiteberryPilingSteelQty.csv', index_col=0)
    print(dataToPrint)
    print('Df name is dataToPrint')	
elif choice == 'c':
    print('Enter date:\n')
    date = input()
    print('Enter pile no:\n')
    pileno = input()
    print('Enter Dia in cm:\n')
    dia = input()
    print('Enter length of the pile \n')
    length_pile = input()

    if float(length_pile) < 12:
        length = 12
    elif float(length_pile) > 12:
        length = length_pile
    elif float(length_pile) < 9:
        lenth = 12 - length_pile


    steelQty = Steel(length,dia)


    print('8mm Steel used for this pile:--',steelQty.Steel8mm())
    print('10mm Steel used for this pile:--',steelQty.Steel10mm())
    print('12mm Steel used for this pile:--',steelQty.Steel12mm())
    print('16mm Steel used for this pile:--',steelQty.Steel16mm())
    print('20mm Steel used for this pile:--',steelQty.Steel20mm())

    SteellTOupdate = {
        'Date': [date],
        'Pile No': [pileno],
        '8mm Steel': [steelQty.Steel8mm()],
        '10mm Steel': [steelQty.Steel10mm()],
        '12mm Steel': [steelQty.Steel12mm()],
        '16mm Steel': [steelQty.Steel16mm()],
        '20mm Steel': [steelQty.Steel20mm()]
        }
    # df = pd.DataFrame(list(SteellTOupdate.items()),columns = ['Steel ','Qty')
    df = pd.DataFrame(SteellTOupdate, columns = ['Date','Pile No','8mm Steel', '10mm Steel','12mm Steel','16mm Steel','20mm Steel'])

    print(df)
    print('Do you want to update records?')  
    print('y/n')
    ans = input()
    try:
        if ans =='y':
            # df.to_csv('WhiteberryPilingSteelQty.csv')
            df.to_csv('WhiteberryPilingSteelQty.csv', mode='a', header=False)
            # with open('WhiteberryPilingSteelQty.csv', 'a') as f:
            #     df.to_csv(f, header=f.tell()==0)
            print('Document updated')
        elif ans == 'n':
            print('Not updated ...Thanks')
    except:
        print('Something went wrong ')
    present_data = pd.read_csv('WhiteberryPilingSteelQty.csv', index_col=0)

    print(present_data)
