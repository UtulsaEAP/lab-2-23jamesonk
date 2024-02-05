#Kai Jameson
#Thursday @ 2pm

def telephone():
    phone_number = int(input())

    finalFour = phone_number%10000
    phone_number = phone_number//10000
    middleThree = (phone_number%1000)
    phone_number = phone_number//1000
    areaCode = phone_number%1000
    
    

    print('(' + str(areaCode) + ')' + ' ' + str(middleThree) + "-" + str(finalFour))
    ''' Type your code here. '''
if __name__ == "__main__":
    telephone()