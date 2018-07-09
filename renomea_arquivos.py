import os, random, string

# pasta raiz
rootdir = 'c:/novosdocumentos'

# arquivo de log
fname = 'debug_arquivos.log'
debug = False  # True para gerar log/ False para executar os renomeios

# substituir espaco por:
c_esp = '_'

# substituir caractere desconhecido por:
c_des = '_'

# tamanho maximo intermediario do nome de cada arquivo
t_max_int = 100

# tamanho maximo real do nome de cada arquivo
t_max_real = 128

# tamanho maximo do path
t_max_path = 400

# sufixo para o nome dos arquivos
sufixo = 0

# numero sugerido de arquivos que serao processados. Quando Debug for True, colocar valor 100 em ntotal
ntotal = 5369100
natual = 0

# numero de letras randomicas
numero_letrinhas = 4

with open(fname, 'w') as arquivo:
    for dirpath, dirnames, filenames in os.walk(rootdir, topdown=False):
        for filename in filenames:
            
            # nome do arquivo
            n1 = filename.lower()
            
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
            # testa o tamanho intermediario do nome do arquivo
            # ----------------------------------------------------------
            n3 = ''
            if len(n2) > t_max_int:
                
                # pega a extensao do arquivo
                f = os.path.join(dirpath, filename)
                _, extensao = os.path.splitext(f)
                extensao = extensao.lower()
                
                # pega a parte inicial do nome do arquivo
                n2 = n2[:t_max_int]
                
                # atualiza o sufixo
                sufixo += 1
                
                # adiciona um sufixo e a extensao
                n3 = f'{n2}_{sufixo}'
                n2 = f'{n2}_{sufixo}{extensao}'

            # ---------------------------------------------------------
            # testa o tamanho real
            # ----------------------------------------------------------
            t = len(n2)
            if t > t_max_real:
                msg1 = f'ERRO: arquivo possuira um nome muito grande ({t} caracteres)'
                msg2 = f'antes de renomear:\n{filename}'
                msg3 = f'depois de renomear:\n{n2}'
                exit(f'{msg1}\n{msg2}\n{msg3}')
            
            # ----------------------------------------------------------
            # testa o tamanho do path final
            # ----------------------------------------------------------
            p1 = os.path.join(dirpath, filename)
            p2 = os.path.join(dirpath, n2)
            p3 = os.path.join(dirpath, n3)
            
            p1 = p1.replace('\\', '/')
            p2 = p2.replace('\\', '/')
            p3 = p3.replace('\\', '/')
            
            # tipo de codificacao
            #p1 = p1.encode('utf-8')
            #p2 = p2.encode('utf-8')
            #p3 = p3.encode('utf-8')
                        
            t = len(p2)
            if t > t_max_path:
                exit(f'ERRO: Path muito grande ({t} caracteres):\n{p2}')
            
            # informa o andamento
            natual += 1
            porcentagem = (natual / ntotal) * 100
            print('{:.1%}'.format(porcentagem)) 
            
            # ----------------------------------------------------------
            # renomeia o arquivo
            # ----------------------------------------------------------

            if p1.lower() != p2.lower():
                if os.path.isfile(p2):
                    letrinhas = ''.join(random.choices(string.ascii_lowercase + string.digits, k=numero_letrinhas)) 
                    p2 = f'{p3}_{letrinhas}{extensao}'
                    
                if debug:    
                    arquivo.write(f'{p1}\n')
                    arquivo.write(f'{p2}\n')
                else:    
                    os.rename(p1, p2)
            
