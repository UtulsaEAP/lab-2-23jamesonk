#Kai Jameson
#Thursday @ 2pm

def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''
    sixHrCaffeine = caffeine_mg/2
    twelveHrCaffeine = caffeine_mg/4
    twentyFourHrCaffeine = caffeine_mg/16

    print('After 6 hours: ' + f'{sixHrCaffeine:.2f} ' + 'mg' + '\n' 'After 12 hours: ' + f'{twelveHrCaffeine:.2f} ' + 'mg' + '\n' + 'After 24 hours: ' + f'{twentyFourHrCaffeine:.2f} ' + 'mg')

if __name__ == "__main__":
    caffeine()