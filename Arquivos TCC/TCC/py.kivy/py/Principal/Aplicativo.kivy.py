from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
          # Defina a cor de fundo
        Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)

        layout = FloatLayout()
          
          # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.57}  # Define o topo do layout na parte superior da tela
          
          
          # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

          
          # Botão Voltar
        back_button = Button(text="",
                      font_size=7,
                      background_normal="py.kivy/py/img_wireframe\ICONS\Menu/perfil.png",
                      background_down="py.kivy/py/img_wireframe/transparent.png",
                      border=(0,0,0,0),
                      size_hint=(None, None),
                      size=(50, 50),
                      pos_hint={'x': 0, 'top': 2.0})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_login)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)
          

        # Imagem no canto superior esquerdo
        image = Image(source="py.kivy/py/img_wireframe/Imagem1.png",
                size_hint=(None, None),
                size=(50, 50))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

          # Botão "centro"
        btn5 = Button(text="", 
                        background_normal="py.kivy/py/img_wireframe/alunos.png",
                        background_down="py.kivy/py/img_wireframe/transparent.png",
                        border=(0,0,0,0),
                        size_hint=(None, None), 
                        size=(170, 170), 
                        markup=True)
        btn5.bind(on_release=self.trocar_para_tela_aluno)  # Associar a ação ao botão
        btn5.pos_hint={'center_x': 0.5, 'center_y': 0.7}  # Ajuste o valor de 'center_y'
          
        with btn5.canvas.before:

              self.rect = Rectangle(pos=btn5.pos, size=btn5.size)
              
          # Rótulo para o primeiro botão
              label1 = Label(text="[color=000000]Alunos[/color]", 
                             halign='center',
                             markup= True)
        
              layout.add_widget(btn5)
              layout.add_widget(label1)

              
          
            # Botão2 "centro"
        btn6 = Button(text="", 
                        background_normal="py.kivy/py/img_wireframe\ICONS\Menu/professor.png",
                        background_down="py.kivy/py/img_wireframe/transparent.png",
                        border=(0,0,0,0),
                        size_hint=(None, None), 
                        size=(170, 170), 
                        markup=True)
        btn6.bind(on_release=self.trocar_para_tela_professor)  # Associar a ação ao botão
        btn6.pos_hint={'center_x': 0.5, 'center_y': 0.4}  # Ajuste o valor de 'center_y'
          
        with btn6.canvas.before:

              self.rect = Rectangle(pos=btn6.pos, size=btn6.size)
              
              # Rótulo para o segundo botão
        label2 = Label(text="[color=000000]Professor[/color]", 
                         halign='center',
                         markup=True)

        layout.add_widget(btn6)
        layout.add_widget(label2)
        
        self.add_widget(layout)
        
    def trocar_para_tela_login(self, instance):
        self.manager.current = 'login'
    def trocar_para_tela_aluno(self, instance):
        self.manager.current = 'aluno'
    def trocar_para_tela_professor(self, instance):
        self.manager.current = 'professor'
    def trocar_para_tela_menu(self, instance):
              self.manager.current = 'menu'

class LoginADMScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginADMScreen, self).__init__(**kwargs)
         # Defina a cor de fundo
        Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)

          
          
          # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.67}  # Define o topo do layout na parte superior da tela
          
           # Título (no topo do layout)
        title_label = Label(text="[color=000000]Secretaria[/color]",
                              font_size=32,
                              size_hint_y=None,
                              height=30,
                              markup=True)
        layout.add_widget(title_label)
          
           # Título (no topo do layout)
        title_label = Label(text="[color=000000]Login[/color]",
                              font_size=32,
                              size_hint_y=None,
                              height=150,
                              markup=True)
        layout.add_widget(title_label)
          
          # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

          
          # Botão Voltar
        back_button = Button(text="Voltar",
                      font_size=7,
                      background_normal="py.kivy/py/img_wireframe/voltar.png",
                      background_down="py.kivy/py/img_wireframe/transparent.png",
                      border=(0,0,0,0),
                      size_hint=(None, None),
                      size=(50, 50),
                      pos_hint={'x': 0, 'top': 5.3})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_menu)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)
          

        # Imagem no canto superior direito
        image = Image(source="",
                size_hint=(None, None),
                size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=260)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
          
          # Campos de entrada
        input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=80, pos_hint={'x': 0})
        
        # Email
        input_label2 = Label(text="[color=000000]EMAIL:[/color]", 
                               font_size=14, 
                               size_hint_x=None, 
                               width=150,
                               markup=True)
        input_layout.add_widget(input_label2)

        email_input = TextInput(hint_text="Email", background_color=(0.5, 0.7, 1, 1))
        input_layout.add_widget(email_input)

          # Widget em branco para aumentar o espaço
        layout.add_widget(Widget(size=(1, 40)))  # Ajuste a altura conforme necessário
        # Senha
        input_label3 = Label(text="[color=000000]SENHA:[/color]", 
                               font_size=14, 
                               size_hint_x=None, 
                               width=150,
                               markup=True)
        input_layout.add_widget(input_label3)

        password_input = TextInput(hint_text="Senha", 
                                     background_color=(0.5, 0.7, 1, 1))
        input_layout.add_widget(password_input)

        layout.add_widget(input_layout)

         # Botão "REALIZAR LOGIN"
        btn5 = Button(text="REALIZAR LOGIN", 
                        background_color=(0.5, 0.7, 1, 1), 
                        size_hint=(None, None), 
                        size=(270, 45))
        btn5.bind(on_release=self.trocar_para_tela_secretaria)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        layout.add_widget(btn5)

        self.add_widget(layout)
    def trocar_para_tela_secretaria(self, instance):
        self.manager.current = 'secretaria' 
    def trocar_para_tela_menu(self, instance):
        self.manager.current = 'menu'
    def trocar_para_tela_login(self, instance):
        self.manager.current = 'login'
        
class SecretariaScreen(Screen):
    def __init__(self, **kwargs):
        super(SecretariaScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        
        # Título (no topo do layout)
        title_label = Label(text="[color=000000]Secretaria[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1300,
                            markup=True)
        layout.add_widget(title_label)
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        # Botão Voltar
        back_button = Button(text="",
                             font_size=20,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_login)  # Associar a ação ao botão
        voltar_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint_y=None, height=690)
        voltar_layout.add_widget(back_button)
        top_button_layout.add_widget(voltar_layout)

       # Botão "Login" ancorado no canto superior direito
        login_button = Button(text="",
                              font_size=7,
                              background_normal="py.kivy/py/img_wireframe/login.png",
                              background_down="py.kivy/py/img_wireframe/transparent.png",
                              border=(0,0,0,0),
                              size_hint=(None, None),
                             size=(60, 60))
        login_button.bind(on_release=self.trocar_para_tela_contaADM)  # Associar a ação ao botão
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=690)
        anchor_layout.add_widget(login_button)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        
        # Botão "conteudo" centro
        Adicionar_button = Button(text="",
                              font_size=0,
                              background_normal="py.kivy/py/img_wireframe/ICONS/adm.secretaria/segue.png",
                              background_down="py.kivy/py/img_wireframe/transparent.png",
                              border=(0,0,0,0),
                              size_hint=(None, None),
                             size=(175, 175))
        Adicionar_button.bind(on_release=self.trocar_para_tela_addConta)  # Associar a ação ao botão
        Adicionar_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=950)
        Adicionar_layout.add_widget(Adicionar_button)
        layout.add_widget(Adicionar_layout)
        
        # Título "CONTEUDO"
        title_label = Label(text="[color=000000]Adicionar Conta[/color]",
                            font_size=30,
                            size_hint_y=None,
                            height=730,
                            markup=True)
        layout.add_widget(title_label)
        
        # Botão "conteudo" centro
        validar_button = Button(text="",
                              font_size=0,
                              background_normal="py.kivy/py/img_wireframe/ICONS/adm.secretaria/conta-verificada.png",
                              background_down="py.kivy/py/img_wireframe/transparent.png",
                              border=(0,0,0,0),
                              size_hint=(None, None),
                             size=(175, 175))
        validar_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=475)
        validar_layout.add_widget(validar_button)
        layout.add_widget(validar_layout)
        
        # Título "CONTEUDO"
        title_label = Label(text="[color=000000]Validar Conta[/color]",
                            font_size=30,
                            size_hint_y=None,
                            height=250,
                            markup=True)
        layout.add_widget(title_label)
        
        self.add_widget(layout) 
    def trocar_para_tela_login(self, instance):
        self.manager.current = 'login'
    def trocar_para_tela_secretaria(self, instance):
        self.manager.current = 'secretaria'
    def trocar_para_tela_cadastro(self, instance):
        self.manager.current = 'cadastro' 
    def trocar_para_tela_addConta(self, instance):
        self.manager.current = 'addConta'  
    def trocar_para_tela_contaADM(self, instance):
        self.manager.current = 'contaADM'  
class CadastroScreen(Screen):
    def __init__(self, **kwargs):
        super(CadastroScreen, self).__init__(**kwargs)
        
        # Defina a cor de fundo
        Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)

        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.4}  # Define o topo do layout na parte superior da tela

        # Título (no topo do layout)
        title_label = Label(text="[color=000000]Secretaria[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=620,
                            markup=True)
        layout.add_widget(title_label)

        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        # Botão Voltar
        back_button = Button(text="",
                            font_size=7,
                            background_normal="py.kivy/py/img_wireframe/voltar.png",
                            background_down="py.kivy/py/img_wireframe/transparent.png",
                            border=(0,0,0,0),
                            size_hint=(None, None),
                            size=(50, 50),
                            pos_hint={'x': 0, 'top': 8.0})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_secretaria)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)

        # Imagem no canto superior direito
        image = Image(source="py.kivy/py/img_wireframe/Imagem1.png",
                    size_hint=(None, None),
                    size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

        # Campos de entrada
        input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=80, pos_hint={'x': 0})

        # Nome Completo
        name_layout = BoxLayout (orientation='vertical', spacing=8, padding=(0, 0, 0, 205))

        # Nome Completo
        name_label = Label(text="[color=000000]NOME COMPLETO:[/color]",
                            font_size=12,
                            markup=True)
        name_layout.add_widget(name_label)

        name_input = TextInput(hint_text="Nome Completo", background_color=(0.7, 0.87, 0.38, 1), size_hint_y=None, height=30)
        name_layout.add_widget(name_input)

        layout.add_widget(name_layout)
        
        # Layout para Email
        email_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 132))  # Adicionamos margem inferior de 20)

        email_label = Label(text="[color=000000]EMAIL:[/color]",
                              font_size=12,
                              markup=True)
        email_layout.add_widget(email_label)

        email_input = TextInput(hint_text="Email", background_color=(0.7, 0.87, 0.38, 1), size_hint_y=None, height=30)
        email_layout.add_widget(email_input)
          
        layout.add_widget(email_layout)
          
        # Layout para Senha  
        senha_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 60))  # Adicionamos margem inferior de 20)

        senha_label = Label(text="[color=000000]SENHA:[/color]",
                              font_size=12,
                              markup=True)
        senha_layout.add_widget(senha_label)

        senha_input = TextInput(hint_text="Senha", background_color=(0.7, 0.87, 0.38, 1), size_hint_y=None, height=30)
        senha_layout.add_widget(senha_input)
          
        layout.add_widget(senha_layout)

        # Botão "Finalizar Cadastro"
        btn5 = Button(text="[color=000000]FINALIZAR CADASTRO[/color]", 
                      background_color=(0.7, 0.87, 0.38, 1), 
                      size_hint=(None, None), 
                      size=(270, 75), 
                      markup=True)
        btn5.bind(on_release=self.trocar_para_tela_secretaria)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.background_normal = ''  # Removemos o fundo padrão do botão
        layout.add_widget(btn5)

        # Botão "Upload da Foto do Usuário"
        btn6 = Button(text="[color=000000]UPLOAD DA FOTO DO USUÁRIO[/color]", background_color=(0.7, 0.87, 0.38, 1), size_hint=(None, None), size=(270, 75), markup=True)
        btn6.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn6.background_normal = ''  # Removemos o fundo padrão do botão
        layout.add_widget(btn6)

        self.add_widget(layout)
    def trocar_para_tela_secretaria(self, instance):
        self.manager.current = 'secretaria'
    def trocar_para_tela_login(self, instance):
        self.manager.current = 'login'

        
class ListagemScreen(Screen):
    def __init__(self, **kwargs):
        super(ListagemScreen, self).__init__(**kwargs)
        data = [
            {"nome": "João", "email": "joao@example.com", "senha": "senha1", "autorizar": False},
            {"nome": "Maria", "email": "maria@example.com", "senha": "senha2", "autorizar": True},
            {"nome": "Pedro", "email": "pedro@example.com", "senha": "senha3", "autorizar": False},
        ]

        layout = GridLayout(cols=6, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        layout.add_widget(Label(text="Nome"))
        layout.add_widget(Label(text="Email"))
        layout.add_widget(Label(text="Senha"))
        layout.add_widget(Label(text="Autorizar"))
        layout.add_widget(Label(text="Inativar"))
        layout.add_widget(Label(text="Atualizar"))

        for row in data:
            layout.add_widget(Label(text=row["nome"]))
            layout.add_widget(Label(text=row["email"]))
            layout.add_widget(Label(text=row["senha"]))
            checkbox = CheckBox(active=row["autorizar"])
            layout.add_widget(checkbox)
            inativar_button = Button(text="Inativar", size_hint=(None, None), size=(100, 30))
            layout.add_widget(inativar_button)
            atualizar_button = Button(text="Atualizar", size_hint=(None, None), size=(100, 30))
            layout.add_widget(atualizar_button)

        tabela_scrollview = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - 100))
       
        self.add_widget(layout)
    def trocar_para_tela_listagem(self, instance):
        self.manager.current = 'listagem'
        
class ContaADMScreen(Screen):
    def __init__(self, **kwargs):
        super(ContaADMScreen, self).__init__(**kwargs)
      # Defina a cor de fundo
        Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)
        
          # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.5}  # Define o topo do layout na parte superior da tela
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        
        # Botão Voltar
        back_button = Button(text="",
                    font_size=7,
                    background_normal="py.kivy/py/img_wireframe/voltar.png",
                    background_down="py.kivy/py/img_wireframe/transparent.png",
                    border=(0,0,0,0),
                    size_hint=(None, None),
                    size=(50, 50),
                    pos_hint={'x': 0, 'top': 9.0})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_secretaria)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)
        
          # Botão "Secretaria"
        btn1 = Button(text="[color=000000]SECRETARIA[/color]", 
                      font_size=18,
                    background_color=(220/255, 220/255, 220/255, 1), 
                    size_hint=(None, None), size=(200, 35), 
                    markup=True,
                    pos_hint={'center_x': 0.5, 'center_y': 0.9})
        btn1.background_normal = ''
        with btn1.canvas.before:
          Rectangle(pos=btn1.pos, size=btn1.size)
        layout.add_widget(btn1)
        
        # Imagem no canto superior direito
        image = Image(source="py.kivy/py/img_wireframe\ICONS\Conta\Avaliacao.png",
              size_hint=(None, None),
              size=(170, 170))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        
        
        # Widget em branco para aumentar o espaço
        layout.add_widget(Widget(size=(1, 40)))  # Ajuste a altura conforme necessário


        
        # Botão "LISTAGEM"
        btn5 = Button(text="[color=000000]LISTAGEM[/color]", 
                      font_size=18,
                      background_color=(0.7, 0.87, 0.38, 1), 
                      size_hint=(None, None), 
                      size=(200, 35), 
                      markup=True)
        btn5.bind(on_release=self.trocar_para_tela_listagem)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.background_normal = ''  # Removemos o fundo padrão do botão
        with btn5.canvas.before:

            self.rect = Rectangle(pos=btn5.pos, size=btn5.size)
        layout.add_widget(btn5)
          
        self.add_widget(layout)
    def trocar_para_tela_cadastro(self, instance):
        self.manager.current = 'cadastro'
    def trocar_para_tela_listagem(self, instance):
        self.manager.current = 'listagem'
    def trocar_para_tela_contaADM(self, instance):
        self.manager.current = 'contaADM'
    def trocar_para_tela_secretaria(self, instance):
        self.manager.current = 'secretaria'    
class AlunoScreen(Screen):
    def __init__(self, **kwargs):
        super(AlunoScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        # Botão Voltar
        back_button = Button(text="",
                             font_size=20,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_menu)  # Associar a ação ao botão
        voltar_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint_y=None, height=690)
        voltar_layout.add_widget(back_button)
        top_button_layout.add_widget(voltar_layout)

       # Botão "Login" ancorado no canto superior direito
        login_button = Button(text="",
                              font_size=7,
                              background_normal="py.kivy/py/img_wireframe/login.png",
                              background_down="py.kivy/py/img_wireframe/transparent.png",
                              border=(0,0,0,0),
                              size_hint=(None, None),
                             size=(60, 60))
        login_button.bind(on_release=self.trocar_para_tela_loginAluno)  # Associar a ação ao botão
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=690)
        anchor_layout.add_widget(login_button)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        
        # Botão "conteudo" centro
        conteudo_button = Button(text="",
                              font_size=0,
                              background_normal="py.kivy/py/img_wireframe/ICONS/Aluno/escolher_atividade.png",
                              background_down="py.kivy/py/img_wireframe/transparent.png",
                              border=(0,0,0,0),
                              size_hint=(None, None),
                             size=(260, 260))
        conteudo_button.bind(on_release=self.trocar_para_tela_escolher)  # Associar a ação ao botão
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=780)
        anchor_layout.add_widget(conteudo_button)
        layout.add_widget(anchor_layout)
        
        # Título "CONTEUDO"
        title_label = Label(text="[color=000000]Escolher Atividade[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=450,
                            markup=True)
        layout.add_widget(title_label)
        
        self.add_widget(layout)
    def trocar_para_tela_loginAluno(self, instance):
        self.manager.current = 'loginAluno'
    def trocar_para_tela_escolher(self, instance):
        self.manager.current = 'escolher'    
    def trocar_para_tela_menu(self, instance):
        self.manager.current = 'menu'    
        
class EscolherScreen(Screen):
    def __init__(self, **kwargs):
        super(EscolherScreen, self).__init__(**kwargs)
         # Defina a cor de fundo
        Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)

        layout = FloatLayout()

        
          # Título 
        title_label1 = Label(text="[color=000000]Escolha sua Atividade[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1330,
                            markup=True)
        layout.add_widget(title_label1)
      
        
         # Layout superior para os botões "Voltar" 
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(50, 50),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_aluno)  # Associar a ação ao botão
        layout.add_widget(back_button)


       # Botões "Escolher"
        brn1 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 470))#posicao
        brn1.bind(on_release=self.trocar_para_tela_licaoEscolhida)  # Associar a ação ao botão
        layout.add_widget(brn1)
       
        brn2 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 240))#posicao
        brn2.bind(on_release=self.trocar_para_tela_licaoEscolhida)  # Associar a ação ao botão
        layout.add_widget(brn2)
       
        brn3 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(70, 9))
        brn3.bind(on_release=self.trocar_para_tela_licaoEscolhida)  # Associar a ação ao botão
        layout.add_widget(brn3)

        btn4 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(240, 470))#posicao
        btn4.bind(on_release=self.trocar_para_tela_licaoEscolhida)  # Associar a ação ao botão
        layout.add_widget(btn4)
       
        btn5 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(240, 240))#posicao
        btn5.bind(on_release=self.trocar_para_tela_licaoEscolhida)  # Associar a ação ao botão
        layout.add_widget(btn5)
       
        btn6 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(240, 9))
        btn6.bind(on_release=self.trocar_para_tela_licaoEscolhida)  # Associar a ação ao botão
        layout.add_widget(btn6)
        
        self.add_widget(layout)
    def trocar_para_tela_aluno(self, instance):
        self.manager.current = 'aluno'
    def trocar_para_tela_escolher(self, instance):
        self.manager.current = 'escolher'
    def trocar_para_tela_licaoEscolhida(self, instance):
        self.manager.current = 'licaoEscolhida'    
        
class LoginALUNOScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginALUNOScreen, self).__init__(**kwargs)
        # Defina a cor de fundo
        Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)

        
        
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.67}  # Define o topo do layout na parte superior da tela
        
        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Login[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=150,
                            markup=True)
        layout.add_widget(title_label)
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        
        # Botão Voltar
        back_button = Button(text="",
                    font_size=7,
                    background_normal="py.kivy/py/img_wireframe/voltar.png",
                    background_down="py.kivy/py/img_wireframe/transparent.png",
                    border=(0,0,0,0),
                    size_hint=(None, None),
                    size=(50, 50),
                    pos_hint={'x': 0, 'top': 5.3})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_Aluno)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)
        

      # Imagem no canto superior direito
        image = Image(source="",
              size_hint=(None, None),
              size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=260)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        
        # Campos de entrada
        input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=80, pos_hint={'x': 0})
      
        # Nome
        name_label2 = Label(text="[color=000000]NOME:[/color]", 
                              font_size=14, 
                              size_hint_x=None, 
                              width=150,
                              markup=True)
        input_layout.add_widget(name_label2)

        name_input = TextInput(hint_text="Email", background_color=(0.5, 0.7, 1, 1))
        input_layout.add_widget(name_input)
        
      # Email
        input_label2 = Label(text="[color=000000]EMAIL:[/color]", 
                              font_size=14, 
                              size_hint_x=None, 
                              width=150,
                              markup=True)
        input_layout.add_widget(input_label2)

        email_input = TextInput(hint_text="Email", background_color=(0.5, 0.7, 1, 1))
        input_layout.add_widget(email_input)

        # Widget em branco para aumentar o espaço
        layout.add_widget(Widget(size=(1, 40)))  # Ajuste a altura conforme necessário
      # Senha
        input_label3 = Label(text="[color=000000]SENHA:[/color]", 
                              font_size=14, 
                              size_hint_x=None, 
                              width=150,
                              markup=True)
        input_layout.add_widget(input_label3)

        password_input = TextInput(hint_text="Senha", 
                                    background_color=(0.5, 0.7, 1, 1))
        input_layout.add_widget(password_input)

        layout.add_widget(input_layout)

        # Botão "REALIZAR LOGIN"
        btn5 = Button(text="REALIZAR LOGIN", 
                      background_color=(0.5, 0.7, 1, 1), 
                      size_hint=(None, None), 
                      size=(270, 45))
        btn5.bind(on_release=self.trocar_para_tela_contaALUNO)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        layout.add_widget(btn5)
        
        self.add_widget(layout)
    def trocar_para_tela_loginAluno(self, instance):
        self.manager.current = 'loginAluno'
    def trocar_para_tela_contaALUNO(self, instance):
        self.manager.current = 'contaALUNO'
    def trocar_para_tela_Aluno(self, instance):
        self.manager.current = 'aluno'    
class ContaALUNOScreen(Screen):
    def __init__(self, **kwargs):
        super(ContaALUNOScreen, self).__init__(**kwargs)
        # Defina a cor de fundo
        Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)
        
          # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.5}  # Define o topo do layout na parte superior da tela
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        
        # Botão Voltar
        back_button = Button(text="",
                    font_size=7,
                    background_normal="py.kivy/py/img_wireframe/voltar.png",
                    background_down="py.kivy/py/img_wireframe/transparent.png",
                    border=(0,0,0,0),
                    size_hint=(None, None),
                    size=(50, 50),
                    pos_hint={'x': 0, 'top': 9.0})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_loginAluno)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)
        
        # Rótulo para o primeiro botão
        label1 = Label(text="[color=000000]André da Silva[/color]", 
                            font_size=22,
                            halign='center',
                            markup= True)
        layout.add_widget(label1)
        
        
        # Imagem no canto superior direito
        image = Image(source="py.kivy/py/img_wireframe/alunos.png",
          size_hint=(None, None),
          size=(170, 170))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)
        layout.add_widget(top_button_layout)
        
        
        
        # Widget em branco para aumentar o espaço
        layout.add_widget(Widget(size=(1, 40)))  # Ajuste a altura conforme necessário


        
        # Botão "Atividades"
        btn5 = Button(text="[color=000000]ATIVIDADES[/color]", 
                      font_size=18,
                      background_color=(0.7, 0.87, 0.38, 1), 
                      border=(0,0,0,0),
                      size_hint=(None, None), 
                      size=(200, 35), 
                      markup=True)
        btn5.bind(on_release=self.trocar_para_tela_escolher)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.background_normal = ''  # Removemos o fundo padrão do botão
        with btn5.canvas.before:

            self.rect = Rectangle(pos=btn5.pos, size=btn5.size)
        layout.add_widget(btn5)
        
        self.add_widget(layout)
    def trocar_para_tela_contaALUNO(self, instance):
        self.manager.current = 'contaALUNO'
    def trocar_para_tela_escolher(self, instance):
        self.manager.current = 'escolher'
    def trocar_para_tela_loginAluno(self, instance):
        self.manager.current = 'loginAluno'    
class licaoEscolhidaScreen(Screen):
    def __init__(self, **kwargs):
        super(licaoEscolhidaScreen, self).__init__(**kwargs)
        # Defina a cor de fundo
        Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)

        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)
        
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(50, 50),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_escolher)  # Associar a ação ao botão
        layout.add_widget(back_button)

        # Layout para imagem central
        #img_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        #image = Image(source="py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Pc.png",
        #        size_hint=(None, None),
        #        size=(260, 260))
        #anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=290)
        #nchor_layout.add_widget(image)
        #img_layout.add_widget(anchor_layout)
        #layout.add_widget(img_layout)
        
        # Botões "trocar para get com imagem selecionada"
        brn1 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(300, 500), #tamanho
              markup=True,
              pos=(50, 145))#posicao
        layout.add_widget(brn1)
        
        # Botão "download"
        btn5 = Button(text="[color=000000]Download[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#77C4FF"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 80))
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        layout.add_widget(btn5)
        
        self.add_widget(layout)
    def trocar_para_tela_licaoEscolhida(self, instance):
        self.manager.current = 'licaoEscolhida'  
    def trocar_para_tela_escolher(self, instance):
        self.manager.current = 'escolher'    
       
class ProfessorScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfessorScreen, self).__init__(**kwargs)        
        
        layout = FloatLayout()
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        # Botão Voltar
        back_button = Button(text="",
                             font_size=20,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(50, 50),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_menu)  # Associar a ação ao botão
        voltar_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint_y=None, height=690)
        voltar_layout.add_widget(back_button)
        top_button_layout.add_widget(voltar_layout)

       # Botão "Login" ancorado no canto superior direito
        login_button = Button(text="",
                              font_size=7,
                              background_normal="py.kivy/py/img_wireframe/login.png",
                              background_down="py.kivy/py/img_wireframe/transparent.png",
                              border=(0,0,0,0),
                              size_hint=(None, None),
                             size=(50, 50))
        login_button.bind(on_release=self.trocar_para_tela_loginProf)  # Associar a ação ao botão
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=690)
        anchor_layout.add_widget(login_button)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        
        # Botão "conteudo" centro
        conteudo_button = Button(text="",
                              font_size=0,
                              background_normal="py.kivy/py/img_wireframe/ICONS/Professor/Conteudo.png",
                              background_down="py.kivy/py/img_wireframe/transparent.png",
                              border=(0,0,0,0),
                              size_hint=(None, None),
                             size=(260, 260))
        conteudo_button.bind(on_release=self.trocar_para_tela_conteudo)  # Associar a ação ao botão
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=780)
        anchor_layout.add_widget(conteudo_button)
        layout.add_widget(anchor_layout)
        
        # Título "CONTEUDO"
        title_label = Label(text="[color=000000]Conteudo[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=450,
                            markup=True)
        layout.add_widget(title_label)
        
        self.add_widget(layout)
    def trocar_para_tela_professor(self, instance):
        self.manager.current = 'professor'      
    def trocar_para_tela_menu(self, instance):
        self.manager.current = 'menu'    
    def trocar_para_tela_loginProf(self, instance):
        self.manager.current = 'loginProf' 
    def trocar_para_tela_conteudo(self, instance):
        self.manager.current = 'conteudo'     
class LoginPROFScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginPROFScreen, self).__init__(**kwargs)
          # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.5}  # Define o topo do layout na parte superior da tela
          
          
           # Título (no topo do layout)
        title_label = Label(text="[color=000000]Login[/color]",
                              font_size=32,
                              size_hint_y=None,
                              height=700,
                              markup=True)
        layout.add_widget(title_label)
          
          # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

          
          # Botão Voltar
        back_button = Button(text="",
                      font_size=7,
                      background_normal="py.kivy/py/img_wireframe/voltar.png",
                      background_down="py.kivy/py/img_wireframe/transparent.png",
                      border=(0,0,0,0),
                      size_hint=(None, None),
                      size=(50, 50),
                      pos_hint={'x': 0, 'top': 8.7})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_professor)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)
          

        # Imagem no canto superior direito
        image = Image(source="",
                size_hint=(None, None),
                size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=260)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
          
         # Campos de entrada
        input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=80, pos_hint={'x': 0})

        # Nome Completo
        name_layout = BoxLayout (orientation='vertical', spacing=8, padding=(0, 0, 0, 205))

        # Nome Completo
        name_label = Label(text="[color=000000]NOME COMPLETO:[/color]",
                            font_size=12,
                            markup=True)
        name_layout.add_widget(name_label)

        name_input = TextInput(hint_text="Nome Completo", background_color=("#77C4FF"), size_hint_y=None, height=30)
        name_layout.add_widget(name_input)

        layout.add_widget(name_layout)
        
        # Layout para Email
        email_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 132))  # Adicionamos margem inferior de 20)

        email_label = Label(text="[color=000000]EMAIL:[/color]",
                              font_size=12,
                              markup=True)
        email_layout.add_widget(email_label)

        email_input = TextInput(hint_text="Email", background_color=("#77C4FF"), size_hint_y=None, height=30)
        email_layout.add_widget(email_input)
          
        layout.add_widget(email_layout)
          
        # Layout para Senha  
        senha_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 60))  # Adicionamos margem inferior de 20)

        senha_label = Label(text="[color=000000]SENHA:[/color]",
                              font_size=12,
                              markup=True)
        senha_layout.add_widget(senha_label)

        senha_input = TextInput(hint_text="Senha", background_color=("#77C4FF"), size_hint_y=None, height=30)
        senha_layout.add_widget(senha_input)
          
        layout.add_widget(senha_layout)

         # Botão "REALIZAR LOGIN"
        btn5 = Button(text="REALIZAR LOGIN", 
                        background_color=("#77C4FF"), 
                        size_hint=(None, None), 
                        size=(270, 45))
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.bind(on_release=self.trocar_para_tela_contaProf)  # Associar a ação ao botão
        layout.add_widget(btn5)

        self.add_widget(layout)
    def trocar_para_tela_secretaria(self, instance):
        self.manager.current = 'secretaria' 
    def trocar_para_tela_loginAluno(self, instance):
        self.manager.current = 'loginProf' 
    def trocar_para_tela_professor(self, instance):
        self.manager.current = 'professor'
    def trocar_para_tela_contaProf(self, instance):
        self.manager.current = 'contaProf'        
        
class ContaPROFScreen(Screen):
    def __init__(self, **kwargs):
        super(ContaPROFScreen, self).__init__(**kwargs)   
        layout = FloatLayout()
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        # Botão Voltar
        back_button = Button(text="",
                             font_size=20,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_loginProf)  # Associar a ação ao botão
        voltar_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint_y=None, height=690)
        voltar_layout.add_widget(back_button)
        top_button_layout.add_widget(voltar_layout)

        layout.add_widget(top_button_layout)
        
        #img professor
        img_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        image = Image(source="py.kivy/py/img/Jaqueline_Maciel.png",
                size_hint=(None, None),
                size=(260, 260))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=550)
        anchor_layout.add_widget(image)
        img_layout.add_widget(anchor_layout)
        
        layout.add_widget(img_layout)
        
        #titulo professor
        title_label = Label(text="[color=000000]Profª: Jaqueline Maciel[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=650,
                            markup=True)
        layout.add_widget(title_label)

       # Botão "Conteudo"
        brn = Button(text="[color=000000]Conteudo[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 200))
        brn.bind(on_release=self.trocar_para_tela_conteudo)  # Associar a ação ao botão
        brn.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(brn)
        
        self.add_widget(layout)
    def trocar_para_tela_contaProf(self, instance):
        self.manager.current = 'contaProf'
    def trocar_para_tela_loginProf(self, instance):
        self.manager.current = 'loginProf'
    def trocar_para_tela_conteudo(self, instance):
        self.manager.current = 'conteudo'
        
class AddContaScreen(Screen):
    def __init__(self, **kwargs):
        super(AddContaScreen, self).__init__(**kwargs)
        
        # Defina a cor de fundo
        Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)

        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.4}  # Define o topo do layout na parte superior da tela

        # Título (no topo do layout)
        title_label = Label(text="[color=000000]Secretaria[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=620,
                            markup=True)
        layout.add_widget(title_label)

        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        # Botão Voltar
        back_button = Button(text="",
                            font_size=7,
                            background_normal="py.kivy/py/img_wireframe/voltar.png",
                            background_down="py.kivy/py/img_wireframe/transparent.png",
                            border=(0,0,0,0),
                            size_hint=(None, None),
                            size=(55, 55),
                            pos_hint={'x': 0, 'top': 8.0})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_secretaria)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)

        # Imagem no canto superior direito
        image = Image(source="py.kivy/py/img_wireframe/Imagem1.png",
                    size_hint=(None, None),
                    size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

        # Campos de entrada
        input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=80, pos_hint={'x': 0})

        # Nome Completo
        name_layout = BoxLayout (orientation='vertical', spacing=8, padding=(0, 0, 0, 205))

        # Nome Completo
        name_label = Label(text="[color=000000]NOME COMPLETO:[/color]",
                            font_size=12,
                            markup=True)
        name_layout.add_widget(name_label)

        name_input = TextInput(hint_text="Nome Completo", background_color=(0.7, 0.87, 0.38, 1), size_hint_y=None, height=30)
        name_layout.add_widget(name_input)

        layout.add_widget(name_layout)
        
        # Layout para Email
        email_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 132))  # Adicionamos margem inferior de 20)

        email_label = Label(text="[color=000000]EMAIL:[/color]",
                              font_size=12,
                              markup=True)
        email_layout.add_widget(email_label)

        email_input = TextInput(hint_text="Email", background_color=(0.7, 0.87, 0.38, 1), size_hint_y=None, height=30)
        email_layout.add_widget(email_input)
          
        layout.add_widget(email_layout)
          
        # Layout para Senha  
        senha_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 60))  # Adicionamos margem inferior de 20)

        senha_label = Label(text="[color=000000]SENHA:[/color]",
                              font_size=12,
                              markup=True)
        senha_layout.add_widget(senha_label)

        senha_input = TextInput(hint_text="Senha", background_color=(0.7, 0.87, 0.38, 1), size_hint_y=None, height=30)
        senha_layout.add_widget(senha_input)
          
        layout.add_widget(senha_layout)

        # Botão "Finalizar Cadastro"
        btn5 = Button(text="[color=000000]FINALIZAR CADASTRO[/color]", 
                      background_color=(0.7, 0.87, 0.38, 1), 
                      size_hint=(None, None), 
                      size=(270, 75), 
                      markup=True)
        btn5.bind(on_release=self.trocar_para_tela_secretaria)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.background_normal = ''  # Removemos o fundo padrão do botão
        layout.add_widget(btn5)

        # Botão "Upload da Foto do Usuário"
        btn6 = Button(text="[color=000000]UPLOAD DA FOTO DO USUÁRIO[/color]", background_color=(0.7, 0.87, 0.38, 1), size_hint=(None, None), size=(270, 75), markup=True)
        btn6.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn6.background_normal = ''  # Removemos o fundo padrão do botão
        layout.add_widget(btn6)

        self.add_widget(layout)  
    def trocar_para_tela_secretaria(self, instance):
        self.manager.current = 'secretaria'
             
class ConteudoScreen(Screen):
    def __init__(self, **kwargs):
        super(ConteudoScreen, self).__init__(**kwargs)   
        
        layout = FloatLayout()
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        # Botão Voltar
        back_button = Button(text="",
                             font_size=20,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_contaProf)  # Associar a ação ao botão
        voltar_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint_y=None, height=690)
        voltar_layout.add_widget(back_button)
        top_button_layout.add_widget(voltar_layout)

        layout.add_widget(top_button_layout)
        
        #titulo Conteudo
        title_label = Label(text="[color=000000]Conteúdo[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1320,
                            markup=True)
        layout.add_widget(title_label)
        
        # Botao e label "atividade avaliativa"
        brn1 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/ICONS/Atividade-a/Icone.png", 
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(125, 160), #tamanho
              markup=True,
              pos=(70, 440))#posicao
        brn1.bind(on_release=self.trocar_para_tela_AtividadeA)  # Associar a ação ao botão
        layout.add_widget(brn1)
        
        label1 = Label(text="[color=000000]Atividade avaliativa[/color]",
                            font_size=20,
                            size_hint=(None, None),
                            height=835,
                            width=250,
                            markup=True)
        layout.add_widget(label1)       
       
       # Botao e label "palavras cruzadas"
        brn2 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/ICONS/Pc-Imprimir/Pc-imagem.png", 
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(125, 160), #tamanho
              markup=True,
              pos=(70, 230))#posicao
        brn2.bind(on_release=self.trocar_para_tela_PalavraCruzada)  # Associar a ação ao botão
        layout.add_widget(brn2)
        
        voltar_label = Label(text="[color=000000]Palavras\acruzadas[/color]",
                            font_size=20,
                            size_hint=(None, None),
                            height=430,
                            width=250,
                            markup=True)
        layout.add_widget(voltar_label) 
       
       # Botao e label "quebra cabeça"
        brn3 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/ICONS/quebra cabeca/quebra-cabeca.png", 
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(125, 160), 
              markup=True,
              pos=(160, 40))
        brn3.bind(on_release=self.trocar_para_tela_QuebraCabeca)  # Associar a ação ao botão
        layout.add_widget(brn3)

        voltar_label = Label(text="[color=000000]Quebra cabeça[/color]",
                            font_size=20,
                            size_hint=(None, None),
                            height=60,
                            width=430,
                            markup=True)
        layout.add_widget(voltar_label)
        
        # Botao e label "matematica"
        btn4 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/ICONS/Matematica/Matematica.png", 
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(125, 160), #tamanho
              markup=True,
              pos=(240, 440))#posicao
        btn4.bind(on_release=self.trocar_para_tela_Matematica)  # Associar a ação ao botão
        layout.add_widget(btn4)
        
        voltar_label = Label(text="[color=000000]Matemática[/color]",
                            font_size=20,
                            size_hint=(None, None),
                            height=835,
                            width=600,
                            markup=True)
        layout.add_widget(voltar_label)
        
        # Botao e label "pintura"
        btn5 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/ICONS/Pintura/Pinturap.png",  
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(125, 160), #tamanho
              markup=True,
              pos=(240, 230))#posicao
        btn5.bind(on_release=self.trocar_para_tela_Pintura)  # Associar a ação ao botão
        layout.add_widget(btn5)
       
        voltar_label = Label(text="[color=000000]Pintura[/color]",
                            font_size=20,
                            size_hint=(None, None),
                            height=430,
                            width=600,
                            markup=True)
        layout.add_widget(voltar_label)

        
        self.add_widget(layout)  
    def trocar_para_tela_conteudo(self, instance):
        self.manager.current = 'conteudo'
    def trocar_para_tela_contaProf(self, instance):
        self.manager.current = 'contaProf'
    def trocar_para_tela_QuebraCabeca(self, instance):
        self.manager.current = 'QuebraCabeca' 
    def trocar_para_tela_AtividadeA(self, instance):
        self.manager.current = 'AtividadeA'
    def trocar_para_tela_Matematica(self, instance):
        self.manager.current = 'Matematica'
    def trocar_para_tela_PalavraCruzada(self, instance):
        self.manager.current = 'PalavraCruzada'
    def trocar_para_tela_Pintura(self, instance):
        self.manager.current = 'Pintura'                  
class QuebraCabecaScreen(Screen):
    def __init__(self, **kwargs):
        super(QuebraCabecaScreen, self).__init__(**kwargs)  
         
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\quebra cabeca\Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Quebra cabeça[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1300,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_Conteudo)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Imagem no canto superior direito
        image = Image(source="py.kivy/py/img_wireframe\ICONS\quebra cabeca\quebra-cabeca.png",
                size_hint=(None, None),
                size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=690)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        

       # Botão "Upload"
        brn3 = Button(text="[color=000000]Fazer upload de\nimagem[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 220))
        brn3.bind(on_release=self.trocar_para_tela_QuebraCabecaCriar)  # Associar a ação ao botão
        brn3.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(brn3)
        
        # Botão "Imprimir"
        brn3 = Button(text="[color=000000]Pronto para imprimir[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 110))
        brn3.bind(on_release=self.trocar_para_tela_QuebraCabecaImprimir)  # Associar a ação ao botão
        brn3.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(brn3)
        
        self.add_widget(layout)  
    def trocar_para_tela_QuebraCabeca(self, instance):
        self.manager.current = 'QuebraCabeca' 
    def trocar_para_tela_QuebraCabecaCriar(self, instance):
        self.manager.current = 'QuebraCabecaCriar'   
    def trocar_para_tela_QuebraCabecaImprimir(self, instance):
        self.manager.current = 'QuebraCabecaImprimir'
    def trocar_para_tela_Conteudo(self, instance):
        self.manager.current = 'conteudo'         
class QuebraCabecaCriarScreen(Screen):
    def __init__(self, **kwargs):
        super(QuebraCabecaCriarScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\quebra cabeca\Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Quebra cabeça[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1330,
                            markup=True)
        layout.add_widget(title_label)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_QuebraCabeca)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Layout para imagem central
        img_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        image = Image(source="py.kivy/py/img_wireframe\ICONS\quebra cabeca\mao.png",
                size_hint=(None, None),
                size=(260, 260))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=290)
        anchor_layout.add_widget(image)
        img_layout.add_widget(anchor_layout)

        layout.add_widget(img_layout)
        
        
        # Botão "Upload"
        btn5 = Button(text="[color=000000]Upload[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 150))
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
         
        self.add_widget(layout) 
    def trocar_para_tela_QuebraCabecaCriar(self, instance):
        self.manager.current = 'QuebraCabecaCriar'
    def trocar_para_tela_QuebraCabeca(self, instance):
        self.manager.current = 'QuebraCabeca'    
        
class QuebraCabecaImprimirScreen(Screen):
    def __init__(self, **kwargs):
        super(QuebraCabecaImprimirScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\quebra cabeca\Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Quebra cabeça[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1300,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "logo"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_QuebraCabeca)  # Associar a ação ao botão
        layout.add_widget(back_button)
        

        # Imagem no canto superior direito
        image = Image(source="py.kivy/py/img_wireframe\ICONS\quebra cabeca\quebra-cabeca.png",
                size_hint=(None, None),
                size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=690)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

        # Layout para Texto introdutorio
        text_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        font_name_cg = Label(text="[color=000000]Estão disponiveis dois\ntipos de modelos de\nquebra-cabeça para a\nimpressão: Meio a meio\ne o quebra-cabeça.[/color]",
                            font_size=20,
                            markup=True)
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=400)
        anchor_layout.add_widget(font_name_cg)
        text_layout.add_widget(anchor_layout)
        
        
        layout.add_widget(text_layout)
        


       # Botão "Acessar"
        btn5 = Button(text="[color=000000]ACESSAR[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 170))
        btn5.bind(on_release=self.trocar_para_tela_QuebraCabecaEscolher)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
        
        self.add_widget(layout) 
    def trocar_para_tela_QuebraCabecaImprimir(self, instance):
        self.manager.current = 'QuebraCabecaImprimir'
    def trocar_para_tela_QuebraCabecaEscolher(self, instance):
        self.manager.current = 'QuebraCabecaEscolher'       
    def trocar_para_tela_QuebraCabeca(self, instance):
        self.manager.current = 'QuebraCabeca'       
class QuebraCabecaEscolherScreen(Screen):
    def __init__(self, **kwargs):
        super(QuebraCabecaEscolherScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\quebra cabeca\Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título facil
        title_label1 = Label(text="[color=000000]Meio a meio[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1330,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título medio
        title_label1 = Label(text="[color=000000]Quebra-Cabeça[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=855,
                            markup=True)
        layout.add_widget(title_label1)
        
         # Layout superior para os botões "Voltar" 
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_QuebraCabecaImprimir)  # Associar a ação ao botão
        layout.add_widget(back_button)


       # Botões "Escolher"
        brn1 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/meio_a_meio/meio1.jpeg", 
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 470))#posicao
        brn1.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(brn1)
       
        brn2 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/qc/quebra1.jpeg", 
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 240))#posicao
        brn2.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(brn2)
       
        brn3 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/qc/quebra2.jpeg", 
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(240, 240))
        brn3.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(brn3)

        btn4 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/meio_a_meio/meio2.jpeg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(240, 470))#posicao
        btn4.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(btn4)
        
        self.add_widget(layout) 
    def trocar_para_tela_QuebraCabecaEscolher(self, instance):
        self.manager.current = 'QuebraCabecaEscolher' 
    def trocar_para_tela_QuebraCabecaImprimir(self, instance):
        self.manager.current = 'QuebraCabecaImprimir' 
    def trocar_para_tela_LicaoEscolhidaMat(self, instance):
        self.manager.current = 'licaoEscolhidaMat'    
class LicaoEscolhidaMatScreen(Screen):
    def __init__(self, **kwargs):
        super(LicaoEscolhidaMatScreen, self).__init__(**kwargs) 
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)
 
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_conteudo)  # Associar a ação ao botão
        layout.add_widget(back_button)

        # Layout para imagem central
        #img_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        #image = Image(source="py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Pc.png",
        #        size_hint=(None, None),
        #        size=(260, 260))
        #anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=290)
        #nchor_layout.add_widget(image)
        #img_layout.add_widget(anchor_layout)
        #layout.add_widget(img_layout)
        
        # Botões "trocar para get com imagem selecionada"
        brn1 = Button(text="", 
              background_normal="",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(300, 500), #tamanho
              markup=True,
              pos=(50, 145))#posicao
        layout.add_widget(brn1)
        
        # Botão "download"
        btn5 = Button(text="[color=000000]Download[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 80))
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        layout.add_widget(btn5)
        
       # Botão "Proximo"
        btn5 = Button(text="[color=000000]Proximo[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 20))
        btn5.bind(on_release=self.trocar_para_tela_licaoPostada)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        layout.add_widget(btn5)
        
        self.add_widget(layout) 
    def trocar_para_tela_LicaoEscolhidaMat(self, instance):
        self.manager.current = 'licaoEscolhidaMat'
    def trocar_para_tela_QuebraCabecaEscolher(self, instance):
        self.manager.current = 'QuebraCabecaEscolher' 
    def trocar_para_tela_conteudo(self, instance):
        self.manager.current = 'conteudo'
    def trocar_para_tela_licaoPostada(self, instance):
        self.manager.current = 'licaoPostada'         
class AtividadeAScreen(Screen):
    def __init__(self, **kwargs):
        super(AtividadeAScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\Atividade-A\Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Atividade\nAvaliativa[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1300,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_conteudo)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Imagem no canto superior direito
        image = Image(source="py.kivy/py/img_wireframe\ICONS\Atividade-A\Icone.png",
                size_hint=(None, None),
                size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=690)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        

       # Botão "Upload"
        brn3 = Button(text="[color=000000]Fazer upload de\nimagem[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#77C4FF"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 110))
        brn3.bind(on_release=self.trocar_para_tela_AtividadeAcriar)  # Associar a ação ao botão
        brn3.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(brn3)
        
        self.add_widget(layout) 
    def trocar_para_tela_AtividadeA(self, instance):
        self.manager.current = 'AtividadeA' 
    def trocar_para_tela_conteudo(self, instance):
        self.manager.current = 'conteudo'
    def trocar_para_tela_AtividadeAcriar(self, instance):
        self.manager.current = 'AtividadeAcriar'     
class AtividadeAcriarScreen(Screen):
    def __init__(self, **kwargs):
        super(AtividadeAcriarScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\Atividade-A\Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Atividade\nAvaliativa[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1330,
                            markup=True)
        layout.add_widget(title_label)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_AtividadeA)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Layout para imagem central
        img_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        image = Image(source="py.kivy/py/img_wireframe\ICONS\Atividade-A\Imagem1.png",
                size_hint=(None, None),
                size=(260, 260))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=290)
        anchor_layout.add_widget(image)
        img_layout.add_widget(anchor_layout)

        layout.add_widget(img_layout)
        
        
        # Botão "Upload"
        btn5 = Button(text="[color=000000]Upload[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#77C4FF"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 150))
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
        
        self.add_widget(layout) 
    def trocar_para_tela_AtividadeAcriar(self, instance):
        self.manager.current = 'AtividadeAcriar'  
    def trocar_para_tela_AtividadeA(self, instance):
        self.manager.current = 'AtividadeA'    
        
class MatematicaScreen(Screen):
    def __init__(self, **kwargs):
        super(MatematicaScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\Matematica\Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Matemática[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1300,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_conteudo)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Imagem no canto superior direito
        image = Image(source="py.kivy/py/img_wireframe\ICONS\Matematica\Matematica.png",
                size_hint=(None, None),
                size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=690)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        

       # Botão "Upload"
        brn3 = Button(text="[color=000000]Fazer upload de\nimagem[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 220))
        brn3.bind(on_release=self.trocar_para_tela_MatematicaCriar)  # Associar a ação ao botão
        brn3.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(brn3)
        
        # Botão "Imprimir"
        brn3 = Button(text="[color=000000]Pronto para imprimir[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 110))
        brn3.bind(on_release=self.trocar_para_tela_MatematicaImprimir)  # Associar a ação ao botão
        brn3.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(brn3)
        
        self.add_widget(layout) 
    def trocar_para_tela_Matematica(self, instance):
        self.manager.current = 'Matematica'
    def trocar_para_tela_conteudo(self, instance):
        self.manager.current = 'conteudo'
    def trocar_para_tela_MatematicaCriar(self, instance):
        self.manager.current = 'MatematicaCriar'  
    def trocar_para_tela_MatematicaImprimir(self, instance):
        self.manager.current = 'MatematicaImprimir'      
class MatematicaCriarScreen(Screen):
    def __init__(self, **kwargs):
        super(MatematicaCriarScreen, self).__init__(**kwargs)        
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\Matematica\Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Matemática[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1330,
                            markup=True)
        layout.add_widget(title_label)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_Matematica)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Layout para imagem central
        img_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        image = Image(source="py.kivy/py/img_wireframe\ICONS\Matematica\MatiCriar.png",
                size_hint=(None, None),
                size=(260, 260))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=290)
        anchor_layout.add_widget(image)
        img_layout.add_widget(anchor_layout)

        layout.add_widget(img_layout)
        
        
        # Botão "Upload"
        btn5 = Button(text="[color=000000]Upload[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 150))
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
        
        self.add_widget(layout) 
    def trocar_para_tela_MatematicaCriar(self, instance):
        self.manager.current = 'MatematicaCriar'
    def trocar_para_tela_Matematica(self, instance):
        self.manager.current = 'Matematica'   
        
class MatematicaImprimirScreen(Screen):
    def __init__(self, **kwargs):
        super(MatematicaImprimirScreen, self).__init__(**kwargs)   
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\Matematica\Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Matemática[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1300,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "logo"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_Matematica)  # Associar a ação ao botão
        layout.add_widget(back_button)
        

        # Imagem no canto superior direito
        image = Image(source="py.kivy/py/img_wireframe\ICONS\Matematica\Matematica.png",
                size_hint=(None, None),
                size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=690)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

        # Layout para Texto introdutorio
        text_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        font_name_cg = Label(text="[color=000000]Estão disponiveis\nquatro sessões sobre\nmatemática para a\nimpressão: 1 sessão -\nadição e subtração, 2ª\nsessão - multiplicação\ne divisão.[/color]",
                            font_size=20,
                            markup=True)
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=400)
        anchor_layout.add_widget(font_name_cg)
        text_layout.add_widget(anchor_layout)
        
        
        layout.add_widget(text_layout)
        


       # Botão "Acessar"
        btn5 = Button(text="[color=000000]ACESSAR[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 170))
        btn5.bind(on_release=self.trocar_para_tela_MatematicaEscolher)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
        
        self.add_widget(layout) 
    def trocar_para_tela_MatematicaImprimir(self, instance):
        self.manager.current = 'MatematicaImprimir'
    def trocar_para_tela_Matematica(self, instance):
        self.manager.current = 'Matematica'
    def trocar_para_tela_MatematicaEscolher(self, instance):
        self.manager.current = 'MatematicaEscolher'    
class MatematicaEscolherScreen(Screen):
    def __init__(self, **kwargs):
        super(MatematicaEscolherScreen, self).__init__(**kwargs)     
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\Matematica\Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título facil
        title_label1 = Label(text="[color=000000]+ e -[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1330,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título medio
        title_label1 = Label(text="[color=000000]* e /[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=855,
                            markup=True)
        layout.add_widget(title_label1)
        
         # Layout superior para os botões "Voltar" 
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_MatematicaImprimir)  # Associar a ação ao botão
        layout.add_widget(back_button)


       # Botões "Escolher"
        brn1 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/+-/adicao.jpeg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 470))#posicao
        brn1.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(brn1)
       
        brn2 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/×÷/multiplicacao.jpeg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 240))#posicao
        brn2.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(brn2)
       
        brn3 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/×÷/divisao.jpeg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(240, 240))
        brn3.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(brn3)

        btn4 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/+-/subtracao.jpeg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(240, 470))#posicao
        btn4.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(btn4)
        
        self.add_widget(layout) 
    def trocar_para_tela_MatematicaEscolher(self, instance):
        self.manager.current = 'MatematicaEscolher'  
    def trocar_para_tela_LicaoEscolhidaMat(self, instance):
        self.manager.current = 'licaoEscolhidaMat'    
    def trocar_para_tela_MatematicaImprimir(self, instance):
        self.manager.current = 'MatematicaImprimir'    
class licaoPostadaScreen(Screen):
    def __init__(self, **kwargs):
        super(licaoPostadaScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)
 
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_licaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(back_button)

        # Layout para imagem central
        #img_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        #image = Image(source="py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Pc.png",
        #        size_hint=(None, None),
        #        size=(260, 260))
        #anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=290)
        #nchor_layout.add_widget(image)
        #img_layout.add_widget(anchor_layout)
        #layout.add_widget(img_layout)
        
        # Botões "trocar para get com imagem selecionada"
        brn1 = Button(text="", 
              background_normal="",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(300, 500), #tamanho
              markup=True,
              pos=(50, 145))#posicao
        layout.add_widget(brn1)
        
        # Botão "posta"
        btn5 = Button(text="[color=000000]Postar[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 50))
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        layout.add_widget(btn5)
        
        self.add_widget(layout) 
    def trocar_para_tela_licaoPostada(self, instance):
        self.manager.current = 'licaoPostada'
    def trocar_para_tela_licaoEscolhidaMat(self, instance):
        self.manager.current = 'licaoEscolhidaMat' 
        
class PalavraCruzadaScreen(Screen):
    def __init__(self, **kwargs):
        super(PalavraCruzadaScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Palavras\nCruzadas[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1330,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_conteudo)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Imagem no canto superior direito
        image = Image(source="py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Pc-imagem.png",
                size_hint=(None, None),
                size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=690)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        

       # Botão "Upload"
        brn3 = Button(text="[color=000000]Fazer upload de\nimagem[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 220))
        brn3.bind(on_release=self.trocar_para_tela_PalavraCruzadaCriar)  # Associar a ação ao botão
        brn3.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(brn3)
        
        # Botão "Imprimir"
        brn3 = Button(text="[color=000000]Pronto para imprimir[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 110))
        brn3.bind(on_release=self.trocar_para_tela_PalavraCruzadaImprimir)  # Associar a ação ao botão
        brn3.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        layout.add_widget(brn3)
        
        self.add_widget(layout) 
    def trocar_para_tela_PalavraCruzada(self, instance):
        self.manager.current = 'PalavraCruzada'
    def trocar_para_tela_conteudo(self, instance):
        self.manager.current = 'conteudo'  
    def trocar_para_tela_PalavraCruzadaCriar(self, instance):
        self.manager.current = 'PalavraCruzadaCriar' 
    def trocar_para_tela_PalavraCruzadaImprimir(self, instance):
        self.manager.current = 'PalavraCruzadaImprimir'    
class PalavraCruzadaCriarScreen(Screen):
    def __init__(self, **kwargs):
        super(PalavraCruzadaCriarScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        
        # Imagem de fundo 
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Palavras\nCruzadas[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1330,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_PalavraCruzada)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Layout para imagem central
        img_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        image = Image(source="py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Pc.png",
                size_hint=(None, None),
                size=(260, 260))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=290)
        anchor_layout.add_widget(image)
        img_layout.add_widget(anchor_layout)

        layout.add_widget(img_layout)
        
        
        # Botão "Upload"
        btn5 = Button(text="[color=000000]Upload[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 150))
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
        
        self.add_widget(layout) 
    def trocar_para_tela_PalavraCruzadaCriar(self, instance):
        self.manager.current = 'PalavraCruzadaCriar'
    def trocar_para_tela_PalavraCruzada(self, instance):
        self.manager.current = 'PalavraCruzada'
        
class PalavraCruzadaImprimirScreen(Screen):
    def __init__(self, **kwargs):
        super(PalavraCruzadaImprimirScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Palavras\nCruzadas[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1330,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_PalavraCruzada)  # Associar a ação ao botão
        layout.add_widget(back_button)
        

        # Imagem no canto superior direito
        image = Image(source="py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Pc-imagem.png",
                size_hint=(None, None),
                size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=690)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

        # Layout para Texto introdutorio
        text_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        name_label = Label(text="[color=000000]Estão disponiveis três\nníveis de palavras\ncruzadas para a\nimpressão: nível fácil\n(1 a 5 palavras), nível\nmédio (de 5 a 10\npalavras), e o nível\ndifícil (contendo mais\nde 10 palavras).[/color]",
                            font_size=20,
                            markup=True)
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=490)
        anchor_layout.add_widget(name_label)
        text_layout.add_widget(anchor_layout)
        
        
        layout.add_widget(text_layout)
        


       # Botão "Acessar"
        btn5 = Button(text="[color=000000]ACESSAR[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 170))
        btn5.bind(on_release=self.trocar_para_tela_PalavraCruzadaEscolher)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
        
        self.add_widget(layout) 
    def trocar_para_tela_PalavraCruzadaImprimir(self, instance):
        self.manager.current = 'PalavraCruzadaImprimir' 
    def trocar_para_tela_PalavraCruzada(self, instance):
        self.manager.current = 'PalavraCruzada'
    def trocar_para_tela_PalavraCruzadaEscolher(self, instance):
        self.manager.current = 'PalavraCruzadaEscolher' 
        
class PalavraCruzadaEscolherScreen(Screen):
    def __init__(self, **kwargs):
        super(PalavraCruzadaEscolherScreen, self).__init__(**kwargs) 
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\Pc-Imprimir\Fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título facil
        title_label1 = Label(text="[color=000000]Fácil[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1330,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título medio
        title_label1 = Label(text="[color=000000]Médio[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=855,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título dificil
        title_label1 = Label(text="[color=000000]Dificil[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=400,
                            markup=True)
        layout.add_widget(title_label1)
        
         # Layout superior para os botões "Voltar" 
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_PalavraCruzadaImprimir)  # Associar a ação ao botão
        layout.add_widget(back_button)


       # Botões "Escolher"
        brn1 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/pc/facil1.jpg", 
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 470))#posicao
        brn1.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(brn1)
       
        brn2 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/pc/medio1.jpg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 240))#posicao
        brn2.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(brn2)
       
        brn3 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/pc/dificil1.jpg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(70, 9))
        brn3.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(brn3)

        btn4 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/pc/facil2.jpg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(240, 470))#posicao
        btn4.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(btn4)
       
        btn5 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/pc/medio2.jpg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(240, 240))#posicao
        btn5.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(btn5)
       
        btn6 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/pc/dificil2.jpg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(240, 9))
        btn6.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(btn6)
        
        self.add_widget(layout) 
    def trocar_para_tela_PalavraCruzadaEscolher(self, instance):
        self.manager.current = 'PalavraCruzadaEscolher' 
    def trocar_para_tela_PalavraCruzadaImprimir(self, instance):
        self.manager.current = 'PalavraCruzadaImprimir'
    def trocar_para_tela_LicaoEscolhidaMat(self, instance):
        self.manager.current = 'licaoEscolhidaMat'  
        
class PinturaScreen(Screen):
    def __init__(self, **kwargs):
        super(PinturaScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\pintura/fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Pintura[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1300,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_conteudo)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Imagem no canto superior direito
        image = Image(source="py.kivy/py/img_wireframe\ICONS\pintura\pinturap.png",
                size_hint=(None, None),
                size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=690)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        

       # Botão "Upload"
        brn3 = Button(text="[color=000000]Fazer upload de\nimagem[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("77C4FF"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 220))
        brn3.bind(on_release=self.trocar_para_tela_PinturaCriar)  # Associar a ação ao botão
        brn3.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(brn3)
        
        # Botão "Imprimir"
        brn3 = Button(text="[color=000000]Pronto para imprimir[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("77C4FF"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 110))
        brn3.bind(on_release=self.trocar_para_tela_PinturaImprimir)  # Associar a ação ao botão
        brn3.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(brn3)
        
        self.add_widget(layout) 
    def trocar_para_tela_Pintura(self, instance):
        self.manager.current = 'Pintura' 
    def trocar_para_tela_conteudo(self, instance):
        self.manager.current = 'conteudo'
    def trocar_para_tela_PinturaCriar(self, instance):
        self.manager.current = 'PinturaCriar'  
    def trocar_para_tela_PinturaImprimir(self, instance):
        self.manager.current = 'PinturaImprimir'     
class PinturaCriarScreen(Screen):
    def __init__(self, **kwargs):
        super(PinturaCriarScreen, self).__init__(**kwargs)   
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\pintura/fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Pintura[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1330,
                            markup=True)
        layout.add_widget(title_label)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_Pintura)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Layout para imagem central
        img_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        image = Image(source="py.kivy/py/img_wireframe\ICONS\pintura/pintura.png",
                size_hint=(None, None),
                size=(260, 260))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=290)
        anchor_layout.add_widget(image)
        img_layout.add_widget(anchor_layout)

        layout.add_widget(img_layout)
        
        
        # Botão "Upload"
        btn5 = Button(text="[color=000000]Upload[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("77C4FF"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 150))
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
        
        self.add_widget(layout) 
    def trocar_para_tela_PinturaCriar(self, instance):
        self.manager.current = 'PinturaCriar' 
    def trocar_para_tela_Pintura(self, instance):
        self.manager.current = 'Pintura' 
        
class PinturaImprimirScreen(Screen):
    def __init__(self, **kwargs):
        super(PinturaImprimirScreen, self).__init__(**kwargs)    
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe\ICONS\pintura/fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Pintura[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1300,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "logo"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_Pintura)  # Associar a ação ao botão
        layout.add_widget(back_button)
        

        # Imagem no canto superior direito
        image = Image(source="py.kivy/py/img_wireframe\ICONS\pintura\pinturap.png",
                size_hint=(None, None),
                size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=690)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

        # Layout para Texto introdutorio
        text_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        font_name_cg = Label(text="[color=000000]Estão disponiveis três\ntipos de modelos de\npintura para a\nimpressão: Animais,\nAlimentos e sobre as\ncores.[/color]",
                            font_size=20,
                            markup=True)
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=400)
        anchor_layout.add_widget(font_name_cg)
        text_layout.add_widget(anchor_layout)
        
        
        layout.add_widget(text_layout)
        


       # Botão "Acessar"
        btn5 = Button(text="[color=000000]ACESSAR[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("77C4FF"), 
              size_hint=(None, None), 
              size=(200, 45), 
              markup=True,
              pos=(150, 170))
        btn5.bind(on_release=self.trocar_para_tela_PinturaEscolher)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
        
        self.add_widget(layout) 
    def trocar_para_tela_PinturaImprimir(self, instance):
        self.manager.current = 'PinturaImprimir'
    def trocar_para_tela_Pintura(self, instance):
        self.manager.current = 'Pintura'
    def trocar_para_tela_PinturaEscolher(self, instance):
        self.manager.current = 'PinturaEscolher'
        
class PinturaEscolherScreen(Screen):
    def __init__(self, **kwargs):
        super(PinturaEscolherScreen, self).__init__(**kwargs)    
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="py.kivy/py/img_wireframe/ICONS/pintura/fundo.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título Animais
        title_label1 = Label(text="[color=000000]Animais[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1330,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título Alimentos
        title_label1 = Label(text="[color=000000]Alimentos[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=855,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título Cores
        title_label1 = Label(text="[color=000000]Cores[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=400,
                            markup=True)
        layout.add_widget(title_label1)
        
         # Layout superior para os botões "Voltar" 
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="py.kivy/py/img_wireframe/voltar.png",
                             background_down="py.kivy/py/img_wireframe/transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        back_button.bind(on_release=self.trocar_para_tela_PinturaImprimir)  # Associar a ação ao botão
        layout.add_widget(back_button)


# Botões "Escolher"
        brn1 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/P_animais/animal1.jpeg", 
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 470))#posicao
        brn1.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(brn1)
       
        brn2 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/P_alimentos/alimento1.jpeg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 240))#posicao
        brn2.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(brn2)
       
        brn3 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/Cores/cores1.jpeg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(70, 9))
        brn3.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(brn3)

        btn4 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/P_animais/animal2.jpeg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(240, 470))#posicao
        btn4.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(btn4)
       
        btn5 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/P_alimentos/alimento2.jpeg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(240, 240))#posicao
        btn5.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(btn5)
       
        btn6 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/Cores/cores2.jpeg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(240, 9))
        btn6.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(btn6)
        
        self.add_widget(layout) 
    def trocar_para_tela_PinturaEscolher(self, instance):
        self.manager.current = 'PinturaEscolher' 
    def trocar_para_tela_PinturaImprimir(self, instance):
        self.manager.current = 'PinturaImprimir' 
    def trocar_para_tela_LicaoEscolhidaMat(self, instance):
        self.manager.current = 'licaoEscolhidaMat'                                                                                                                                         
class LearPlusApp(App):
    def build(self):
        self.sm = ScreenManager()
        
        # Adicione as telas ao gerenciador de telas
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(LoginADMScreen(name='login'))
        self.sm.add_widget(SecretariaScreen(name='secretaria'))
        self.sm.add_widget(CadastroScreen(name='cadastro'))
        self.sm.add_widget(ListagemScreen(name='listagem'))
        self.sm.add_widget(ContaADMScreen(name='contaADM'))
        self.sm.add_widget(AlunoScreen(name='aluno'))
        self.sm.add_widget(EscolherScreen(name='escolher'))
        self.sm.add_widget(LoginALUNOScreen(name='loginAluno'))
        self.sm.add_widget(ContaALUNOScreen(name='contaALUNO'))
        self.sm.add_widget(licaoEscolhidaScreen(name='licaoEscolhida'))
        self.sm.add_widget(ProfessorScreen(name='professor'))
        self.sm.add_widget(LoginPROFScreen(name='loginProf'))
        self.sm.add_widget(ContaPROFScreen(name='contaProf'))
        self.sm.add_widget(AddContaScreen(name='addConta'))
        self.sm.add_widget(ConteudoScreen(name='conteudo'))
        self.sm.add_widget(QuebraCabecaScreen(name='QuebraCabeca'))
        self.sm.add_widget(QuebraCabecaCriarScreen(name='QuebraCabecaCriar'))
        self.sm.add_widget(QuebraCabecaImprimirScreen(name='QuebraCabecaImprimir'))
        self.sm.add_widget(QuebraCabecaEscolherScreen(name='QuebraCabecaEscolher'))
        self.sm.add_widget(LicaoEscolhidaMatScreen(name='licaoEscolhidaMat'))
        self.sm.add_widget(AtividadeAScreen(name='AtividadeA'))
        self.sm.add_widget(AtividadeAcriarScreen(name='AtividadeAcriar'))
        self.sm.add_widget(MatematicaScreen(name='Matematica'))
        self.sm.add_widget(MatematicaCriarScreen(name='MatematicaCriar'))
        self.sm.add_widget(MatematicaImprimirScreen(name='MatematicaImprimir'))
        self.sm.add_widget(MatematicaEscolherScreen(name='MatematicaEscolher'))
        self.sm.add_widget(licaoPostadaScreen(name='licaoPostada'))
        self.sm.add_widget(PalavraCruzadaScreen(name='PalavraCruzada'))
        self.sm.add_widget(PalavraCruzadaCriarScreen(name='PalavraCruzadaCriar'))
        self.sm.add_widget(PalavraCruzadaImprimirScreen(name='PalavraCruzadaImprimir'))
        self.sm.add_widget(PalavraCruzadaEscolherScreen(name='PalavraCruzadaEscolher'))
        self.sm.add_widget(PinturaScreen(name='Pintura'))
        self.sm.add_widget(PinturaCriarScreen(name='PinturaCriar'))
        self.sm.add_widget(PinturaImprimirScreen(name='PinturaImprimir'))
        self.sm.add_widget(PinturaEscolherScreen(name='PinturaEscolher'))
        return self.sm

if __name__ == '__main__':
    LearPlusApp().run()