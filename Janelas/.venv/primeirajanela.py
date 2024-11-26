# A bibliotecqa sys(sistema) nos ajuda a gerenciar
# a janela do sistema operacional. Biblioteca
# nativa do Python
import sys
# importar as bibliotecas do pyqt para criar a
# janela e os elementos gráficos, tais como:
#label, caixas de textos, botôes e outros
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton

# Para construir a nossa janela, iremos
# montar uma classe que terá todos 
# os itens da janela. Essa classe será chamada
# para executar a janela e exibi-la em tela
class janela(QWidget):
    #  função __int__ faz referência da janela, ou seja,
    # faz a janela executar. Inicia a janela
    #  o parâmetri self, faz referêcia a própia janela
    def __init(self):
    # O comando super faz refêrencia ao QWidget
    # que foi chamado na construção da janela
    # e inicia uma cópia ára a classse janela
        super().__init__()
    # definindo a posição de X e Y e também o tamanho da janela.
    # O comando setGeometry pede os seguintes valores:
    # x = posição horizontal da abertura da janela
    # y = posição vertical de abertura da janela
    # w = largura da janela
    # x = altura da janela
        self.setGeometry(50,100,600,500)   
    # Vamos fazer a chamada do layout vertical para
    # para adicionar os controles: label, editline e button
        self.v_layout = QVBoxLayout()
        # Vamos criar uma label para o nome do cliente
        self.label_nome = QLa("Nome do Cliente")

app = QApplication(sys.argv)
jan = janela()
jan.show()
app.exec_()

