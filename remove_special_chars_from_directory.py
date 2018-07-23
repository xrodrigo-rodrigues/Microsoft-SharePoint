import os, random, string

# pasta raiz
rootdir = 'c:/novosdocumentos'

# arquivo de log 
fname = 'debug_pastas.log'
debug = False   # True para gerar log/ False para executar os renomeios

# substituir espaco por:
character_espaco = ""

# substituir caractere desconhecido por:
character_desconhecido = " "

with open(fname, 'w') as arquivo:

    for dirpath, dirnames, filenames in os.walk(rootdir, topdown=False):

        for dirname in dirnames:
            
            # nome da pasta
            original_name = dirname.lower()
            
            # ----------------------------------------------------------
            # subtituicoes conhecidas
            # ----------------------------------------------------------
            
            # nomes com espaco
            original_name = original_name.replace("", character_espaco)

            # nomes com cedilha
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
                
            for character in ["@"]:
                original_name = original_name.replace(character, "a")
            
            for character in ["$"]:
                original_name = original_name.replace(character, "s")
            
            for character in ["~", "\"", "#", "%", "&", "*", ":", "<", ">", "?", "/", "\\", "{", "|", "}", "."]:
                original_name = original_name.replace(character, " ")

            # ----------------------------------------------------------
            # substituicoes de caracteres desconhecidos
            # ----------------------------------------------------------
            
            # caracteres conhecidos
            letras = "abcdefghijklmnopqrstuvwxyz"
            numeros = "0123456789"
            simbolos = "-_."
            conhecidos = f"{letras}{numeros}{simbolos}"
            new_name = ""

            for character in original_name:
                if character not in conhecidos:
                    character = character_desconhecido
                        
                new_name = f'{new_name}{character}'

            original_path = os.path.join(dirpath, dirname)
            new_path = os.path.join(dirpath, new_name)

            original_path = original_path.replace('\\', '/')
            new_path = new_path.replace('\\', '/')

            if original_path.lower() != new_path.lower():
                if os.path.isdir(new_path):
                    letrinhas = ''.join(random.choices(string.ascii_lowercase + string.digits, k=numero_letrinhas)) 
                    new_path = f'{new_path}_{letrinhas}'
                
                #cria arquivo debug com informacoes do processo
                if debug:
                    arquivo.write(f'{original_path}\n')
                    arquivo.write(f'{new_path}\n')
                else:
                    os.rename(original_path, new_path)
