

co , cod , err = '' ,'' ,''

def Process_Cards(message , types):
    #print(types)
    if types == 'am':
        cod ,error =  Amzon_us(message)
        #print(cod)
        #print(error)
    if types == 'it':
        cod ,error =  Apples(message)
        #print(cod)
        #print(error)
    if types == 'uk':
        cod ,error = Amzon_Uk_or_De(message)

    if types == 'ni':
        cod ,error = Nintendo_Or_Uber(message)
    

    co , err = Convert_List_to_Text(cod , error)     
    return cod , co , err

def Apples(message):
    code = ''
    codes = []
    error = []
    skip = ''
    for i in message:
        skip +=i
        for j in i:
            if j == ' ':
                continue
            if j == '\n' or j == '/':
                break
            if code[0:1] == '/' or code[0:1] == '0' or code[0:2] == '10' or code[0:1] == '5' or code[0:1] == '.' or code[0:2] == '15' or code[0:2] == '20' or code[0:2] == '25':
                code = ''
            code += j
            if len(code) == 15 and (message[len(code)] ==' ' or message[len(code)] == '/' or message[len(code)] == '\n' or message[len(code)] == None):
                error.append(code)
                #print(code)
                code = ''
                break
            if len(code) % 16 == 0:
                if code[0:1] == 'X':
                    codes.append(code)
                   # print(code)
                    code = ''
                    break
            if len(code) == 15:
                if code[0:1] !='X':
                    error.append(code)
                   # print(code)
                    code = ''
                    break
            if len(code) == 15:
                #print(len(skip))
                if code[0:1] == 'X' and (message[len(skip)] == '' or message[len(skip)] == ' ' or message[len(skip)] == '\n' or message[len(skip)] == '/' ):
                    error.append(code)
                   # print(code)
                    code = ''
                    break
           

    return codes ,error      



def Nintendo_Or_Uber(message):
    code = ''
    codes = []
    error = []
    skip = ''
    for i in message:
        skip +=i
        for j in i:
            if j == ' ':
                continue
            if j == '\n' or j == '/':
                break
            if code[0:1] == '/'  or code[0:2] == '10' or code[0:1] == '5' or code[0:1] == '.' or code[0:2] == '15' or code[0:2] == '20' or code[0:2] == '25':
                code = ''
            code += j
            if len(code) == 15 and (message[len(code)] ==' ' or message[len(code)] == '/' or message[len(code)] == '\n' or message[len(code)] == None):
                error.append(code)
                # print(code)
                code = ''
                break
            if len(code) % 16 == 0:
                if code[0:1] == 'E' or code[0:1] == 'N':
                    if 'O' in code or 'I' in code :
                        error.append(code)
                        # print(code)
                        code = ''
                        break
                    else:
                        codes.append(code)
                        # print(code)
                        code = ''
                        break

            


            if len(code) == 15:
                if code[0:1] !='E' and code[0:1] !='N':
                    error.append(code)
                    # print(code)
                    code = ''
                    break
            if len(code) == 15:
                print(len(skip))
                if (code[0:1] == 'E' or code[0:1] == 'N') and (message[len(skip)] == '' or message[len(skip)] == ' ' or message[len(skip)] == '\n' or message[len(skip)] == '/' ):
                    error.append(code)
                    # print(code)
                    code = ''
                    break
           

    return codes ,error  



def Amzon_us(message):
    code = ''
    codes = []
    error = []
    skip = ''
    for i in message:
        skip +=i
        for j in i:
            if j == ' ' or j == '\n':
                continue
            code += j
            if len(code) % 16 == 0 and code[4:5] == '-' and code[11:12] == '-' and code[14:15] == 'A':
                codes.append(code)
                #print(code)
                code = ''
                break

            if (len(code) % 16 == 0 and (code[4:5] != '-' or code[11:12] != '-' or code[14:15] != 'A')):
                error.append(code)
                # print(code)
                code = ''
                break  

            if (len(code) % 16 == 0 and code[4:5] == '-' and code[11:12] == '-' and code[14:15] != 'A') or (len(code) % 16 == 15 and code[4:5] != '-' and code[11:12] != '-' and code[14:15] != 'A') or (len(code) % 16 == 15 and code[4:5] == '-' and code[11:12] != '-' and code[14:15] != 'A' and (message[len(skip)] == ' ' or message[len(skip)] == '\n' or message[len(skip)] == '' )) or (len(code) % 16 == 15 and code[4:5] == '-' and code[11:12] == '-' and code[14:15] != 'A' and (message[len(skip)] == ' ' or message[len(skip)] == '\n' or message[len(skip)] == '' )):
                #print(len(skip))
                error.append(code)
                # print(code)
                code = ''
                break 

            if (len(code) % 16 == 15 and code[4:5] == '-' and code[11:12] == '-' and code[14:15] == 'A') and  (message[len(skip)] == ' ' or message[len(skip)] == '\n' or message[len(skip)] == '' ):
                error.append(code)
                # print(code)
                code = ''
                break 


    return codes ,error

def Amzon_Uk_or_De(message):
    code = ''
    codes = []
    error = []
    skip = ''
    for i in message:
        skip +=i
        for j in i:
            if j == ' ' or j == '\n':
                continue
            code += j
            if len(code) % 16 == 0 and code[4:5] == '-' and code[11:12] == '-' and code[14:15] == 'B':
                codes.append(code)
                #print(code)
                code = ''
                break

            if (len(code) % 16 == 0 and (code[4:5] != '-' or code[11:12] != '-' or code[14:15] != 'B')):
                error.append(code)
                # print(code)
                code = ''
                break

            if(len(code) % 16 == 0 and code[4:5] == '-' and code[11:12] == '-' and code[14:15] != 'B') or (len(code) % 16 == 15 and code[4:5] != '-' and code[11:12] != '-' and code[14:15] != 'B') or (len(code) % 16 == 15 and code[4:5] == '-' and code[11:12] != '-' and code[14:15] != 'B' and (message[len(skip)] == ' ' or message[len(skip)] == '\n' or message[len(skip)] == '' )) or (len(code) % 16 == 15 and code[4:5] == '-' and code[11:12] == '-' and code[14:15] != 'B' and (message[len(skip)] == ' ' or message[len(skip)] == '\n' or message[len(skip)] == '' )):
                #print(len(skip))
                error.append(code)
                #print(code)
                code = ''
                break  
            
            if (len(code) % 16 == 15 and code[4:5] == '-' and code[11:12] == '-' and code[14:15] == 'B') and  (message[len(skip)] == ' ' or message[len(skip)] == '\n' or message[len(skip)] == '' ):
                error.append(code)
                # print(code)
                code = ''
                break 


    return codes ,error



def Rezer_Gold(message):
    code = ''
    codes = []
    error = []
    skip = ''
    for i in message:
        skip +=i
        for j in i:
            if j == ' ' or j == '\n':
                continue
            code += j
            if len(code) ==14 :
                codes.append(code)
                #print(code)
                code = ''
                break
            if len(code) % 14 == 13 and  (message[len(skip)] == ' ' or message[len(skip)] == '\n' or message[len(skip)] == '' ):
                error.append(code)
                # print(code)
                code = ''
                break 

    return codes ,error


def Convert_List_to_Text(codes , errors):
    co = ''
    err = ''
    for i in codes:
        co+=i +'\n'
    for i in errors:
        err+=i +'\n'

    return co , err

def Convert_List(codes):
    co = ''
    for i in codes:
        co+=i +'\n'
    return co

def most_redundant_element(lst):
    ree= []
    count_dict = {}
    for element in lst:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    max_count = 2
    for element, count in count_dict.items():
        if count == max_count:
            ree.append(element)
        if count > max_count:
            for i in range(count -1):
                ree.append(element)
    return ree



    
def Verified_Errors(message , codes):
    msg = Fixed_Message(message)
    # print(msg)
    errors = []
    for i in msg:
        # print(i)
        if i in codes:
            continue
        else:
            errors.append(i)
    return errors




def Fixed_Message(message):
    msg = []
    mess = ''
    for i in message:
        if i == '\n':
            continue
        mess+=i
        if len(mess) == 16:
            msg.append(mess)
            mess = ''
    return msg


##################################for amaon us
        
def append_sort_codes_am_us(codes):
    with open( "prjapp/test_file/amazon_us.text","a") as f:
            for code in codes:
                f.writelines(code)
                f.writelines("\n")



def get_code_from_text_file_am_us():
    transactions=[]
    f = open("prjapp/test_file/amazon_us.text","r")
    for line in f.readlines():
        # line = .strip()
        # print(line)
        transactions.append(line)
    code = ''
    codes = []
    for i in transactions:
        for j in i:
            if j == ' ':
                continue
            code += j
            if len(code) % 16 == 0:
                codes.append(code)
                code = ''
                break  
  
    return codes


##################################for Apple

def append_sort_codes_apple(codes):
    with open( "prjapp/test_file/apple.text","a") as f:
            for code in codes:
                f.writelines(code)
                f.writelines("\n")



def get_code_from_text_file_apple():
    transactions=[]
    f = open("prjapp/test_file/apple.text","r")
    for line in f.readlines():
        # line = .strip()
        # print(line)
        transactions.append(line)
    code = ''
    codes = []
    for i in transactions:
        for j in i:
            if j == ' ':
                continue
            code += j
            if len(code) % 16 == 0:
                codes.append(code)
                code = ''
                break  
  
    return codes

##################################for amaon uk or de


def append_sort_codes_am_uk_de(codes):
    with open( "prjapp/test_file/amazon_uk_de.text","a") as f:
            for code in codes:
                f.writelines(code)
                f.writelines("\n")



def get_code_from_text_file_am_uk_de():
    transactions=[]
    f = open("prjapp/test_file/amazon_uk_de.text","r")
    for line in f.readlines():
        # line = .strip()
        # print(line)
        transactions.append(line)
    code = ''
    codes = []
    for i in transactions:
        for j in i:
            if j == ' ':
                continue
            code += j
            if len(code) % 16 == 0:
                codes.append(code)
                code = ''
                break  
  
    return codes

##################################for nintendo


def append_sort_codes_nin(codes):
    with open( "prjapp/test_file/nintendo.text","a") as f:
            for code in codes:
                f.writelines(code)
                f.writelines("\n")



def get_code_from_text_file_nin():
    transactions=[]
    f = open("prjapp/test_file/nintendo.text","r")
    for line in f.readlines():
        # line = .strip()
        # print(line)
        transactions.append(line)
    code = ''
    codes = []
    for i in transactions:
        for j in i:
            if j == ' ':
                continue
            code += j
            if len(code) % 16 == 0:
                codes.append(code)
                code = ''
                break  
  
    return codes
