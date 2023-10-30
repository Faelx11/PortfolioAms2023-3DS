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
        back_button = Button(text="Voltar",
                            font_size=7,
                            background_normal="py.kivy/py/img_wireframe/voltar.png",
                            size_hint=(None, None),
                            size=(55, 55),
                            pos_hint={'x': 0, 'top': 8.0})  # Posiciona no canto superior esquerdo
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
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.bind(on_release=self.trocar_para_tela_login)  # Associar a ação ao botão
        btn5.background_normal = ''  # Removemos o fundo padrão do botão
        layout.add_widget(btn5)

        # Botão "Upload da Foto do Usuário"
        btn6 = Button(text="[color=000000]UPLOAD DA FOTO DO USUÁRIO[/color]", background_color=(0.7, 0.87, 0.38, 1), size_hint=(None, None), size=(270, 75), markup=True)
        btn6.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn6.background_normal = ''  # Removemos o fundo padrão do botão
        layout.add_widget(btn6)

        self.add_widget(layout)

    def trocar_para_tela_login(self, instance):
        self.manager.current = 'login'

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
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
        back_button = Button(text="Voltar",
                            font_size=7,
                            background_normal="py.kivy/py/img_wireframe/voltar.png",
                            size_hint=(None, None),
                            size=(55, 55),
                            pos_hint={'x': 0, 'top': 5.3})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_cadastro)  # Associar a ação ao botão
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
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.bind(on_release=self.trocar_para_tela_aluno)  # Associar a ação ao botão
        layout.add_widget(btn5)

        self.add_widget(layout)
        
    def trocar_para_tela_cadastro(self, instance):
        self.manager.current = 'cadastro'
    def trocar_para_tela_aluno(self, instance):
        self.manager.current = 'aluno'
        
class AlunoScreen(Screen):
    def __init__(self, **kwargs):
        super(AlunoScreen, self).__init__(**kwargs)
    # Defina a cor de fundo
        Window.clearcolor = (1, 1, 1, 1)  # Cor Branca (R, G, B, alpha)
          
           # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.5}  # Define o topo do layout na parte superior da tela
          
          # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

          
          # Botão Voltar
        back_button = Button(text="Voltar",
                      font_size=7,
                      background_normal="py.kivy/py/img_wireframe/voltar.png",
                      size_hint=(None, None),
                      size=(55, 55),
                      pos_hint={'x': 0, 'top': 9.0})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_login)  # Associar a ação ao botão
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
                        size_hint=(None, None), 
                        size=(200, 35), 
                        markup=True)
        btn5.bind(on_release=self.trocar_para_tela_escolher)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.background_normal = ''  # Removemos o fundo padrão do botão
        with btn5.canvas.before:

          self.add_widget(layout)
              
        layout.add_widget(btn5)
        
    def trocar_para_tela_escolher(self, instance):
          self.manager.current = 'escolher'    
    def trocar_para_tela_login(self, instance):
          self.manager.current = 'login'
          
class EscolherScreen(Screen):
    def __init__(self, **kwargs):
        super(EscolherScreen, self).__init__(**kwargs)
        # Defina a cor de fundo
        Window.clearcolor = (240/255, 240/255, 240/255, 1)  # Cor cinza claro (R, G, B, alpha)

        layout = FloatLayout()

        
          # Título 
        title_label1 = Label(text="[color=000000]Escolha sua Atividade[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1330,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título medio
        title_label1 = Label(text="[color=#000000]Nome Atividades[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=855,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título dificil
        title_label1 = Label(text="[color=#000000]Nome Atividades[/color]",
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
                             size_hint=(None, None),
                             size=(60, 60),
                             pos=(3.5, 640))
        layout.add_widget(back_button)


       # Botões "Escolher"
        brn1 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 470))#posicao
        layout.add_widget(brn1)
       
        brn2 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 240))#posicao
        layout.add_widget(brn2)
       
        brn3 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(70, 9))
        layout.add_widget(brn3)

        btn4 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(240, 470))#posicao
        layout.add_widget(btn4)
       
        btn5 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(240, 240))#posicao
        layout.add_widget(btn5)
       
        btn6 = Button(text="", 
              background_normal="", 
              background_color=("#808080"), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(240, 9))
        layout.add_widget(btn6)
        
        self.add_widget(layout)
        
    def trocar_para_tela_escolher(self, instance):
        self.manager.current = 'escolher'

class LearPlusApp(App):
    def build(self):
        self.sm = ScreenManager()
        
        # Adicione as telas ao gerenciador de telas
        self.sm.add_widget(CadastroScreen(name='cadastro'))
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(AlunoScreen(name='aluno'))
        self.sm.add_widget(EscolherScreen(name='escolher'))
        return self.sm

if __name__ == '__main__':
    LearPlusApp().run()
