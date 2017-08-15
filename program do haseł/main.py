import pyperclip

class PassMaster:
    
    pass_file = 'pass_base.txt'
    
    def __init__(self, passwords = {}):
        self.passwords = passwords
        self.keys = self.passwords.keys
        self.values = self.passwords.values
        print('''What do you want to do ?
                1- See all domains that are in database?
                2- Get password for specific domain?
                3- Add password to database?
                4- Replace password in databas?
                5- Remove domain from database?''')
        
    def func_choice(self, choice):
        if choice == '1':
            self.file_open()
            self.give_keys()
        elif choice == '2':
            domain = input('Please give a domain name\n')
            self.file_open()
            self.get_pass(domain)
        elif choice == '3':
            domain = input('Please give a domain name\n')
            password = input('Please give a password for this domain\n')
            self.file_open()
            self.add_pass(domain, password)
            self.file_save()
        elif choice == '4':
            domain = input('Please give a domain name\n')
            password = input('Please give a password for this domain\n')
            self.file_open()
            self.replace_pass(domain, password)
            self.file_save()
        elif choice == '5':
            domain = input('Please give a domain name\n')
            self.file_open()
            self.remove_domain(domain)
            self.file_save()
        else:
            print('Please choose option from the list\n')

    def file_open(self):
        with open(self.pass_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                x = line.split(':')
                self.passwords[x[0]] = x[1]
        file.close()

    def file_save(self):
        with open(self.pass_file, 'w') as file:
            for key in self.keys():
                file.write('{}:{}'.format(key,self.passwords.get(key)))                
        file.close()
      
    def give_keys(self):
        for key in self.keys():
            print(key)
        
    def get_pass(self, domain):
        if domain in self.keys():
            pyperclip.copy(self.passwords.get(domain))
            print('Password was copied and is ready to be pasted.')
        else:
            print('Password for this domain is not in database yet.')
            
    def add_pass(self, domain, password):
        if domain not in self.keys():
            self.passwords[domain] = password
        else:
            print('Password for domain "{}" is already in database'.format(domain))
            answer = input('Do you want to replace password for this domain?(yes/no)\n')
            if answer == 'yes':
                self.passwords[domain] = password + '\n'
            else:
                pass
            
    def replace_pass(self, domain, password):
        self.passwords[domain] = password

    def remove_domain(self, domain):
        if domain in self.keys():
            del self.passwords[domain]
            print('Deletion complete!!')
        else:
            print('This domain "{}" is not in database.'.format(domain))

haslo1 = PassMaster()
choice = input()
haslo1.func_choice(choice)


        
