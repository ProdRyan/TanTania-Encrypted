################################################################
#                                                              #
#                        [Creditos ]                           #
#                                                              #
################################################################
#                                                              #
#                 Codigo hecho por xNetting                    #
#                                                              #
#                Dev: xNetting / Grupo: Craka Squad            #
#                                                              #
################################################################

# CodedByxNetting
# CrakaSquad

import hashlib
import os
import sys



os.system('color a')
print('''

    ▄▄▄█████▓ ▄▄▄       ███▄    █ ▄▄▄█████▓ ▄▄▄       ███▄    █  ██▓ ▄▄▄      
    ▓  ██▒ ▓▒▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒▒████▄     ██ ▀█   █ ▓██▒▒████▄    
    ▒ ▓██░ ▒░▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▒██  ▀█▄  ▓██  ▀█ ██▒▒██▒▒██  ▀█▄  
    ░ ▓██▓ ░ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░██░░██▄▄▄▄██ 
      ▒██▒ ░  ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░  ▓█   ▓██▒▒██░   ▓██░░██░ ▓█   ▓██▒
      ▒ ░░    ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░    ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▓   ▒▒   ▓▒█░
        ░      ▒   ▒▒ ░░ ░░   ░ ▒░    ░      ▒   ▒▒ ░░ ░░   ░ ▒░ ▒ ░  ▒   ▒▒ ░
      ░        ░   ▒      ░   ░ ░   ░        ░   ▒      ░   ░ ░  ▒ ░  ░   ▒   
               ░  ░         ░                ░  ░         ░  ░        ░  ░

                       Dev: xNetting / Grupo: #CrakaSquad                                              
    ''')  

def encode_sha3_256():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │ Escriba el texto que quiere encriptar en SHA3_256   │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    sha3_256_crypt = hashlib.sha3_256()

    sha3_256_encrypted = input('''

    root@xnetting: ~# ''')

    sha3_256_crypt.update(b'sha3_256_encrypted')

    print(f'''

    root@xnetting: ~# ''' + sha3_256_crypt.hexdigest()
    
    )

def encode_blake2b():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │  Escriba el texto que quiere encriptar en blake2b   │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    blake2b_crypt = hashlib.blake2b()

    blake2b_encrypted = input('''

    root@xnetting: ~# ''')

    blake2b_crypt.update(b'blake2b_encrypted')

    print(f'''

    root@xnetting: ~# ''' + blake2b_crypt.hexdigest()
    
    )

def algoritmos():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │        Aqui tiene la lista de algoritmos            │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    print(f'{hashlib.algorithms_available}')

def encode_sha224():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │  Escriba el texto que quiere encriptar en SHA224    │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    sha224_crypt = hashlib.sha224()

    sha224_encrypted = input('''

    root@xnetting: ~# ''')

    sha224_crypt.update(b'sha224_encrypted')

    print(f'''

    root@xnetting: ~# ''' + sha224_crypt.hexdigest()
    
    )

def encode_sha256():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │  Escriba el texto que quiere encriptar en SHA265    │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    sha256_crypt = hashlib.sha256()

    sha256_encrypted = input('''

    root@xnetting: ~# ''')

    sha256_crypt.update(b'sha256_encypted')

    print(f'''

    root@xnetting: ~# ''' + sha256_crypt.hexdigest()
    
    )

def encode_sha1():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │   Escriba el texto que quiere encriptar en SHA1     │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    sha1_crypt = hashlib.sha1()

    sha1_encrypted = input('''

    root@xnetting: ~# ''')

    sha1_crypt.update(b'sha1_encrypted')

    print(f'''

    root@xnetting: ~# ''' + sha1_crypt.hexdigest()
    
    )


def encode_md5():
    print('''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │   Escriba el texto que quiere encriptar en MD5      │                      
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    md5_crypt = hashlib.md5()

    md5_encrypted = input('''

    root@xnetting: ~# ''')

    md5_crypt.update(b'md5_encrypted')

    print(f'''

    root@xnetting: ~# ''' + md5_crypt.hexdigest()
    
    )

def main():
    print('''

    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │   Eliga el metodo que quiere para su encriptacion   │                      
    │                                                     │
    │        1 - MD5                                      │
    │                                                     │
    │        2 - SHA1                                     │                     
    │                                                     │
    │        3 - SHA256                                   │
    │                                                     │
    │        4 - SHA224                                   │
    │                                                     │
    │        5 - blake2b                                  │
    │                                                     │
    │        6 - SHA3_256                                 │
    │                                                     │
    │        10 - Todos los Algoritmos                    │
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    ''')

    opcion = input('''
    
    root@xnetting: ~# ''')

    if opcion == '1':
        encode_md5()
    elif opcion == '2':
        encode_sha1()
    elif opcion == '3':
        encode_sha256()
    elif opcion == '4':
        encode_sha224()
    elif opcion == '5':
        encode_blake2b()
    elif opcion == '6':
        encode_sha3_256()
    elif opcion == '10':
        algoritmos()
    else:
        sys.exit()

main()
