import os, random, string

# pasta raiz
rootdir = 'c:/novosdocumentos'

# arquivo de log 
fname = 'debug_pastas.log'
debug = False   # True para gerar log/ False para executar os renomeios

# substituir espaco por:
c_esp = '_'

# substituir caractere desconhecido por:
c_des = '_'

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
    for dirpath, dirnames, filenames in os.walk(rootdir, topdown=False):
        for dirname in dirnames:
            
            # nome da pasta
            n1 = dirname.lower()
            
            # ----------------------------------------------------------
            # subtituicoes conhecidas
            # ----------------------------------------------------------
            
            # espaco
            n1 = n1.replace(" ", c_esp)

            # cedilha
            n1 = n1.replace("ç", "c")
            
            # n acentuado
            n1 = n1.replace("ñ", "n")
            
            # vogais acentuadas
            for c in ["á", "ã", "à", "â", "ä"]:
                n1 = n1.replace(c, "a")
            
            for c in ["é", "è", "ê", "ë"]:
                n1 = n1.replace(c, "e")
            
            for c in ["í", "ì", "î", "ï"]:
                n1 = n1.replace(c, "i")
            
            for c in ["ó", "õ", "ò", "ô", "ö"]:
                n1 = n1.replace(c, "o")
            
            for c in ["ú", "ù", "û", "ü"]:
                n1 = n1.replace(c, "u")
            
            # ----------------------------------------------------------
            # substituicoes de caracteres desconhecidos
            # ----------------------------------------------------------
            
            # caractes conhecidos
            letras = "abcdefghijklmnopqrstuvwxyz"
            numeros = "0123456789"
            simbolos = "-_."
            conhecidos = f"{letras}{numeros}{simbolos}"
            n2 = ""

            for c in n1:
                if c not in conhecidos:
                    c = c_des
                        
                n2 = f'{n2}{c}'
            
            # ----------------------------------------------------------
            # testa o tamanho intermediario do nome da pasta
            # ----------------------------------------------------------
            if len(n2) > t_max_int:
                
                # pega a parte inicial do nome da pasta
                n2 = n2[:t_max_int]
                
                # atualiza o sufixo
                sufixo += 1
                
                # adiciona um sufixo
                n2 = f'{n2}_{sufixo}'
            
            # ---------------------------------------------------------
            # testa o tamanho real
            # ----------------------------------------------------------
            t = len(n2)
            if t > t_max_real:
                msg1 = f'ERRO: pasta possuira um nome muito grande ({t} caracteres)'
                msg2 = f'antes de renomear:\n{dirname}'
                msg3 = f'depois de renomear:\n{n2}'
                exit(f'{msg1}\n{msg2}\n{msg3}')

            # ----------------------------------------------------------
            # testa o tamanho do path final
            # ----------------------------------------------------------
            p1 = os.path.join(dirpath, dirname)
            p2 = os.path.join(dirpath, n2)
            
            p1 = p1.replace('\\', '/')
            p2 = p2.replace('\\', '/')
            
            # tipo de codificacao
            #p1 = p1.encode('utf-8')
            #p2 = p2.encode('utf-8')
            
            t = len(p2)
            
            if t > t_max_path:
                exit(f'ERRO: Path muito grande ({t} caracteres):\n{p2}')
            
            # informa o andamento
            natual += 1
            porcentagem = (natual / ntotal) * 100
            print('{:.1%}'.format(porcentagem))
                        
            # ----------------------------------------------------------
            # renomeia a pasta
            # ----------------------------------------------------------
            if p1.lower() != p2.lower():
                if os.path.isdir(p2):
                    letrinhas = ''.join(random.choices(string.ascii_lowercase + string.digits, k=numero_letrinhas)) 
                    p2 = f'{p2}_{letrinhas}'
                
                if debug:
                    arquivo.write(f'{p1}\n')
                    arquivo.write(f'{p2}\n')
                else:        
                    os.rename(p1, p2)

