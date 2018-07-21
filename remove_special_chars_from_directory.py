import os, random, string

# pasta raiz
rootdir = 'c:/novosdocumentos'

# arquivo de log 
fname = 'debug_pastas.log'
debug = False   # True para gerar log/ False para executar os renomeios

# substituir espaco por:
c_esp = ' '

# substituir caractere desconhecido por:
c_des = ""

# tamanho maximo real do nome de cada pasta
t_max_real = 128

# tamanho maximo intermediario do nome de cada pasta
t_max_int = 50

# tamanho maximo do path
# url     = 400
# arquivo = 128
# tamanho maximo = 400 - 128 = 272
t_max_path = 272

# sufixo para o nome das pastas
sufixo = 0

# numero sugerido de pastas que serao processadas Quando Debug for True, colocar valor 100 em ntotal
ntotal = 502200
natual = 0

# numero de letras randomicas
numero_letrinhas = 4


with open(fname, 'w') as arquivo:
    # provavelmente é o crawler das pastas
    for dirpath, dirnames, filenames in os.walk(rootdir, topdown=False):
        # itera entre as pastas
        for dirname in dirnames:
            
            # nome da pasta
            original_name = dirname.lower()
            
            # ----------------------------------------------------------
            # subtituicoes conhecidas
            # ----------------------------------------------------------
            
            # espaco
            original_name = original_name.replace(" ", c_esp)

            # cedilha
            original_name = original_name.replace("ç", "c")
            
            # n acentuado
            original_name = original_name.replace("ñ", "n")
            
            # vogais acentuadas
            for character in ["á", "ã", "à", "â", "ä"]:
                original_name = original_name.replace(character, "a")
            
            for character in ["é", "è", "ê", "ë"]:
                original_name = original_name.replace(character, "e")
            
            for character in ["í", "ì", "î", "ï"]:
                original_name = original_name.replace(character, "i")
            
            for character in ["ó", "õ", "ò", "ô", "ö"]:
                original_name = original_name.replace(character, "o")
            
            for character in ["ú", "ù", "û", "ü"]:
                original_name = original_name.replace(character, "u")
            
            for character in ["~", "\"", "#", "%", "&", "*", ":", "<", ">", "?", "/", "\\", "{", "|", "}", "."]:
                original_name = original_name.replace(character, " ")

            # ----------------------------------------------------------
            # substituicoes de caracteres desconhecidos
            # ----------------------------------------------------------
            
            # caractes conhecidos
            letras = "abcdefghijklmnopqrstuvwxyz"
            numeros = "0123456789"
            simbolos = "-_."
            conhecidos = f"{letras}{numeros}{simbolos}"
            new_name = ""

            for character in original_name:
                if character not in conhecidos:
                    character = c_des
                        
                new_name = f'{new_name}{character}'

            original_path = os.path.join(dirpath, dirname)
            new_path = os.path.join(dirpath, new_name)

            original_path = original_path.replace('\\', '/')
            new_path = new_path.replace('\\', '/')

            if original_path.lower() != new_path.lower():
                if os.path.isdir(new_path):
                    letrinhas = ''.join(random.choices(string.ascii_lowercase + string.digits, k=numero_letrinhas)) 
                    new_path = f'{new_path}_{letrinhas}'
                
                if debug:
                    arquivo.write(f'{original_path}\n')
                    arquivo.write(f'{new_path}\n')
                else:
                    os.rename(original_path, new_path)
