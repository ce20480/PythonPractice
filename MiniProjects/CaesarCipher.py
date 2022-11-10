import random
import re
class Cryptography:
    def __init__(self,mode,RotVal,message):
        self.mode = mode
        self.RotVal = RotVal
        self.message = message
        self.Check()

    def __repr__(self):
        '''
        controls the output of the print 
        '''
        return "You have " + str(self.mode) + 'ed your message: ' + str(self.message)
    
    def encrypt(self):
        '''
        encrytpion
        '''
        message = self.message
        char = list(message)
        char = [ord(c.upper()) for c in char]
        for count,c in enumerate(char):
            if c >= 65 and c <= 90:
                if c >= (90-self.RotVal):
                    Rot = self.RotVal - (90-c)
                    c = ord('A') + Rot
                else:
                    c += self.RotVal
            char[count] = c
        # RotChar = [c+self.RotVal for c in char] cant use this because if the ascii value is close to z then the rotation will send the ascii towards none alphabet characters
        EncrList = [chr(c) for c in char]
        self.message  = ''.join(EncrList)
        return self.message # dont actually need the return
    
    def decrypt(self):
        message = self.message
        char = list(message)
        char = [ord(c.upper()) for c in char]# ord makes integer
        for count,c in enumerate(char):
            if c >= 65 and c <= 90:
                if c <= (65+self.RotVal):
                    Rot =  self.RotVal - (c - 65)
                    c = ord('Z') - Rot
                c -= self.RotVal
            char[count] = c
        # RotChar = [c-self.RotVal for c in char]
        EncrList = [chr(c) for c in char]
        self.message = ''.join(EncrList)
        return self.message

    def Check(self):
        if self.mode in ['E', 'encrypt', 'Encrypt','e']:
            self.encrypt()
        elif self.mode in ['D', 'd', 'Decrypt', 'decrypt']:
            self.decrypt()
    
    # def Inputs(self):
    # tried to 
    #     self.mode = input('What mode do you want the program in: Encrypt(E)/Decrypt(D)')  
    #     x = False
    #     y = False
    #     while x == False:
    #         try:
    #             self.RotVal = int(input('What rotation value do you want: '))%26
    #             x = True
    #         except ValueError:     
    #             print('please input a number')
    #     self.message = input('What message do you want to '+ self.mode +'ed')
    #     while y == False:
    #         if self.message.isalpha():
    #             y == True
    #         else:
    #             print('Make sure there are only letters in your message')
    #             self.message = input('What message do you want to '+ self.mode +'ed')
    #     return self.mode, self.RotVal, self.message
        







if __name__ == '__main__':
    # mode, RotVal, message = Cryptography.Inputs() 
    x = False
    y = False
    t = False
    q = False
    while x == False:
        # try:
        CheckRan = input('Do you want a random rotation value:(Yes(Y)/No(N)) ')
        if CheckRan in ['Yes', 'y', 'Y', 'yes']: 
            RotVal = random.randint(0,26)
            x = True
        elif CheckRan in ['No','n','N','no']:
            while q == False:
                try:
                    RotVal = int(input('What rotation value do you want: '))%26
                    q = True
                except ValueError:     
                    print('please input a number')
            x = True
        else:
            print('Make sure that you answer Yes(Y)/No(N)')
        # except ValueError:
        #     print('Please input True/False')
    mode = input('What mode do you want the program in: Encrypt(E)/Decrypt(D) ') 
    while t == False:
        if mode in ['E', 'e', 'encrypt', 'Encrypt']:
            mode = 'encrypt'
            message = input('What message do you want to encrypted: ')
            t = True
        elif mode in ['D', 'd', 'decrypt', 'Decrypt']:
            mode = 'decrypt'
            message = input('What message do you want to decrypted: ')
            t = True
        else:
            print('Please input the mode correctly either as Encrypt/Decrypt, encrypt/decrypt, E/D or e/d')
            mode = input('What mode do you want the program in: Encrypt(E)/Decrypt(D) ') 
    while y == False:
        if re.findall(r'[A-Za-z,\s\d]', message) == list(message):
            y = True
        else:
            print('Make sure your message was in the correct format(only containing letters numbers or punctuation.')
            message = input('What message do you want to '+ mode +'ed ')
            break
    print(Cryptography(mode, RotVal, message))
    








