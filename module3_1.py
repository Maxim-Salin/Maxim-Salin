import string

calls = 0

def count_calls():
    global calls
    calls +=1

def string_info(mStr):
    cort=(len(mStr),mStr.lower(),mStr.upper())
    count_calls()
    print(cort)

def is_contains(keyF, *args):
        listM = args
        key = str(keyF)
        compareM = False
        i=0
        for i in range(len(listM)):
            if key.lower()==str(listM[i]).lower():
                compareM = True
        count_calls()
        print(compareM)

string_info("Capibara")
string_info("Argument")


is_contains('Urban', 'ban', 'BaNaN', 'urBAN')
is_contains('cycle', 'recycling', 'cyclic')
print(calls)