import keyboard
from PIL import ImageGrab

# PARTE LOGICA DE UM SISTEMA DE BANCO DIGITAL

def menu_de_transferencias():
    opções = input('Opções de pagamentos : \n | [1] - PIX | [2] - TED | [3] - PAGAMENTO BANCARIO | [4] - QRCODE | [5] - PIX AGENDADO | \nSelecione uma opção: ')

# PAGAMENTO VIA PIX
    if opções == '1':
        tipos_de_chave = input("Tipos de chave pix : \n| [e] - EMAIL | [c] - CHAVE ALEATORIA | [n] - NUMERO DE TELEFONE | [c] - CPF | \nSelecione uma opção: ")
        
        # CHAVE PIX EMAIL
        if tipos_de_chave == "e":
            nome_destinatario_email = str(input("Coloque o nome do destinatario: "))
            email = str(input("Coloque a chave: "))
            confirm_email = str(input("Confirme chave: "))

            if email != confirm_email:
                print("Chave pix não se coincidem. Tente novamente")
                return menu_de_transferencias()
            else:
                print("Pix enviado com sucesso.")
                print_tela = input("Pressione [s] para obter o comprovante: ")

                def capture_tela():
                     print_da_tela = ImageGrab.grab()
                     print_da_tela.save('screenshot.png')

                def on_print(event):
                    if event.name == 's':
                     capture_tela()

            keyboard.on_press(on_print)
            keyboard.wait()

        # CHAVE ALEATORIA
        elif tipos_de_chave == "c":
            nome_destinatario_chaveAleatoria = str(input("Coloque o nome do destinatario: "))
            chave_aleatoria = input("Coloque a chave: ")
            confirm_chave_aleatoria = input("Confirme a chave")

            if chave_aleatoria != confirm_chave_aleatoria:
                print("Chave pix não se coincidem. Tente novamente")
                return menu_de_transferencias()
            else:
                print("Pix enviado com sucesso.")
                print_tela = input("Pressione [s] para obter o comprovante: ")

                def capture_tela():
                     print_da_tela = ImageGrab.grab()
                     print_da_tela.save('screenshot.png')

                def on_print(event):
                    if event.name == 's':
                     capture_tela()

            keyboard.on_press(on_print)
            keyboard.wait()

        # CHAVE NUMERO
        elif tipos_de_chave == "n":
            nome_destinatario_numero = str("Nome do destinatario: ")
            numero_pix = input("LEMBRANDO NÃO SÃO ACEITO CARACTERES ESPECIAIS \nColoque a chave pix: ")
            confirm_numero_pix = input("Confirme a chave pix: ")

            if numero_pix != confirm_numero_pix:
                print("Chave pix não se coincidem. Tente novamente")
                return menu_de_transferencias()
            else:
                print("Pix enviado com sucesso.")
                print_tela = input("Pressione [s] para obter o comprovante: ")

                def capture_tela():
                     print_da_tela = ImageGrab.grab()
                     print_da_tela.save('screenshot.png')

                def on_print(event):
                    if event.name == 's':
                     capture_tela()

            keyboard.on_press(on_print)
            keyboard.wait()

        # CHAVE CPF
        elif tipos_de_chave == "c":

            nome_destinatario_cpf = str("Nome do destinatario: ")
            cpf_pix = input("LEMBRANDO NÃO SÃO ACEITO CARACTERES ESPECIAIS \nColoque a chave pix: ")
            confirm_cpf_pix = input("Confirme a chave pix: ")

            if cpf_pix != confirm_cpf_pix:
                print("Chave pix não se coincidem. Tente novamente")
                return menu_de_transferencias()
            else:
                print("Pix enviado com sucesso.")
                print_tela = input("Pressione [s] para obter o comprovante: ")

                def capture_tela():
                     print_da_tela = ImageGrab.grab()
                     print_da_tela.save('screenshot.png')

                def on_print(event):
                    if event.name == 's':
                     capture_tela()

            keyboard.on_press(on_print)
            keyboard.wait()

# PAGAMENTO VIA TED
    elif opções == '2':
        pagamento_ted = input("Você escolheu o metodo de pagamento TED [a] Para avançar e [0] para retorna o menu principal: ")

        if pagamento_ted == 'a':
            banco_do_destinatario = str(input("Nome do banco: "))
            agencia_do_destino = int(input("Agencia: "))
            numero_da_conta = input("Numero da conta: ")
            nome_do_beneficiario = str(input("Nome do beneficiario: "))
            cpf_cnpj = str(input("CPF/CNPJ: "))
            confirme_cpf_cnpj = str(input("Confirme o CPF/CNPJ: "))

            if cpf_cnpj != confirme_cpf_cnpj:
                print("Os dados não se coincidem")
                return pagamento_ted
            else:
                data_de_pagamento = str(input("Data de pagamante: "))
                descrição_do_pagamento = str(input("Descrição do pagamento: "))

            print(f"\n DESCRIÇÃO DO PAGAMENTO : \nNome do banco: {banco_do_destinatario} \nAgencia: {agencia_do_destino} \nNumero da conta: {numero_da_conta} \nNome do beneficiario: {nome_do_beneficiario} \nCPF/CNPJ {confirme_cpf_cnpj} \nDescrição do pagamento {descrição_do_pagamento}")

            print("Pix enviado com sucesso.")
            print_tela = input("Pressione [s] para obter o comprovante: ")

            def capture_tela():
                print_da_tela = ImageGrab.grab()
                print_da_tela.save('screenshot.png')

            def on_print(event):
                if event.name == 's':
                    capture_tela()

            keyboard.on_press(on_print)
            keyboard.wait()
        
        elif pagamento_ted == '0':
            return menu_de_transferencias()
                
# PAGAMENTO VIA TRANSFERENCIA BANCARIA 
    elif opções == '3':
        pagamento_transferencia_bancaria = input("Você escolheu tranferencia bancaria [a] Para avançar e [0] para retorna ao menu principal:")

        if pagamento_transferencia_bancaria == 'a':
            banco_destinatario_tb = str(input("Nome do banco: "))
            agencia_do_destino_tb = int(input("Agencia: "))
            numero_da_conta_tb = input("Numero da conta: ")
            nome_do_beneficiario_tb = str(input("Nome do beneficiario: "))
            cpf_cnpj_tb = str(input("CPF/CNPJ: "))
            confirme_cpf_cnpj_tb = str(input("Confirme o CPF/CNPJ: "))

            if cpf_cnpj_tb != confirme_cpf_cnpj_tb:
                print("Os dados não se coincidem!")
                return pagamento_transferencia_bancaria
            else:
                descrição_do_pagamento_tb = str(input("Descrição do pagamento."))
                print(f"\n DESCRIÇÃO DO PAGAMENTO : \nNome do banco: {banco_destinatario_tb} \nAgencia: {agencia_do_destino_tb} \nNumero da conta: {numero_da_conta_tb} \nNome do beneficiario: {nome_do_beneficiario_tb} \nCPF/CNPJ {confirme_cpf_cnpj_tb} \nDescrição do pagamento {descrição_do_pagamento_tb}")

            print("Pix enviado com sucesso.")
            print_tela = input("Pressione [s] para obter o comprovante: ")

            def capture_tela():
                print_da_tela = ImageGrab.grab()
                print_da_tela.save('screenshot.png')

            def on_print(event):
                if event.name == 's':
                    capture_tela()

            keyboard.on_press(on_print)
            keyboard.wait()
        elif pagamento_transferencia_bancaria == '0':
            return menu_de_transferencias()

# PAGAMENTO VIA QRCODE 
    elif opções == '4':
        print("")

# PAGAMENTO VIA PIX AGENDADO
    if opções == '5':
        pix_agendado = input("Você escolheu a opção de Pix agendado. [a] Para avançar e [0] para retornar ao menu principal: ")
        escolher_pixagnd = None  # Valor padrão

        if pix_agendado == 'a':
            escolher_pixagnd = input("Selecione um modo de transferência pix.\nOpções: [e] - EMAIL | [k] - CHAVE ALEATORIA | [n] - NUMERO DE TELEFONE | [c] - CPF |")

        if escolher_pixagnd == 'e':
            pix_agnd_email = input("Coloque o email do destinatário: ")
            confirm_email_pix_agnd = input("Confirme o email: ")

            if pix_agnd_email != confirm_email_pix_agnd:
                print("Os emails não coincidem.")
                return menu_de_transferencias()
            else:
                valor_pix_agnd = input("Coloque o valor do pix: ")
                confirm_valor_pix_agnd = input("Confirme o valor do pix: ")

                if valor_pix_agnd != confirm_valor_pix_agnd:
                    print("Os valores não coincidem.")
                    return menu_de_transferencias()
                else:
                    selecione_data_pix_agnd = input("Coloque a data: ")
                    confirm_data_pix_agnd = input("Confirme a data: ")

                    if selecione_data_pix_agnd != confirm_data_pix_agnd:
                        print("As datas não coincidem.")
                        return menu_de_transferencias()
                    else:
                        enviar_email = input("Pressione 'enter' para realizar o pagamento")
                        def on_event(event):
                            if event.name == 'enter':
                                print("Pix enviado com sucesso")
                        print_tela = input("Pressione [s] para obter o comprovante: ")

                        def capture_tela():
                            print_da_tela = ImageGrab.grab()
                            print_da_tela.save('screenshot.png')

                        def on_print(event):
                            if event.name == 's':
                                capture_tela()

                        keyboard.on_press(on_print)
                        keyboard.wait()

        elif pix_agendado == '0':
            return menu_de_transferencias()
        
    # PIX AGENDADO NUMERO
        elif escolher_pixagnd == 'n':
            numero_pix = input("Coloque o numero do destinatario: ")
            confirm_numero_pix = input("Confirme o numero: ")

            if numero_pix != confirm_numero_pix:
                print("Os numeros não se coincidem.")
                return menu_de_transferencias()
            else:
                valor_pix = input("coloque o valor do pix: ")
                confirm_valor_pix = input("Confirme o valor do pix: ")

                if valor_pix != confirm_valor_pix:
                    print("Os valores não se coincidem.")
                    return menu_de_transferencias()
                else:
                    data_pix = input("Selecione a data: ")
                    confirm_data_pix = input("COnfirme a data do pix: ")

                    if data_pix != confirm_data_pix:
                        print("As datas não se coincidem.")
                        return menu_de_transferencias()
                    else:
                        enviar_numero = input("Pressione 'enter' para realizar o pagamento")

                def on_event(event):
                    if event.name == 'enter':
                        print("Pix enviado com sucesso")

                        print_tela = input("Pressione [s] para obter o comprovante: ")

                    def capture_tela():
                        print_da_tela = ImageGrab.grab()
                        print_da_tela.save('screenshot.png')

                    def on_print(event):
                        if event.name == 's':
                            capture_tela()

                        keyboard.on_press(on_print)
                        keyboard.wait()

       #  CHAV ALEATORIA AGENDADA
        elif escolher_pixagnd == 'k':
            key_ale_agend = input("Coloque a chave: ")
            valor_key = input("Coloque o valor do pix: ")
            confirm_valor_key = input("COnfirme o valor: ")

            if valor_key != confirm_valor_key:
                print("Os valores não se coincidem.")
                return menu_de_transferencias()
            else:
                enviar_key = input("Pressione 'enter' para realizar o pagamento")

                def on_event(event):
                    if event.name == 'enter':
                        print("Pix enviado com sucesso")
                input("Pressione [s] para realizar o print do pagamento: ")

                def capture_tela():
                    print_da_tela = ImageGrab.grab()
                    print_da_tela.save('screenchot.png')

                def on_print(event):
                    if event.name == 's':
                        capture_tela()

                    keyboard.on_press(on_print)
                    keyboard.wait()

        # PIX CPF AGENDADO
        elif escolher_pixagnd == 'c':
            cpf = input("Digite o CPF: ")
            valor_cpf = input("Digite o valor do pix: ")
            confirm_valor_cpf = input("Confirme o valor: ")

            if valor_cpf != confirm_valor_cpf:
                print("Os valores não coincidem.")
                return menu_de_transferencias()
            else:
                enviar_cpf = input("Pressione 'enter' para realizar o pagamento")

                def on_event(event):
                    if event.name == 'enter':
                        print("Pix enviado com sucesso")

                    keyboard.on_press(on_event)
                    input("Pressione [s] para realizar o print do pagamento: ")

                def capture_tela():
                    print_da_tela = ImageGrab.grab()
                    print_da_tela.save('screenshot.png')

                def on_print(event):
                    if event.name == 's':
                        capture_tela()

                keyboard.on_press(on_print)
                keyboard.wait()
            
menu_de_transferencias()