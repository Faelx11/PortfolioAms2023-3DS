from os import path
import shutil
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image, AsyncImage
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.uix.behaviors import ButtonBehavior
import pyrebase as pb
import firebase_admin as fba
from firebase_admin import auth as auth_admin, storage as storage_admin, firestore as firestore_admin
from kivy.properties import StringProperty, DictProperty
import requests

from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager

config = {
    "apiKey": "AIzaSyBIEG-_aVTlJxTczKJuuHC2ETf3ERr7Aqk",
    "authDomain": "learplus-6ade0.firebaseapp.com",
    "projectId": "learplus-6ade0",
    "databaseURL": "https://default.firebaseio.com",
    "storageBucket": "learplus-6ade0.appspot.com",
    "messagingSenderId": "998440098612",
    "appId": "1:998440098612:web:e4e7ab00eb1fcdd3d76361"
}

# class FileChooser(MDApp):
#     on_select_path = None

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         Window.bind(on_keyboard=self.events)
#         self.on_select_path = lambda x: None
#         self.file_manager = MDFileManager(select_path=self.select_path, exit_manager=self.exit_manager, preview=True) 

#     def file_manager_open(self):
#         self.manager_open = True
#         self.file_manager.show("/")

#     def select_path(self, path):
#         self.on_select_path(path)
#         self.exit_manager()

#     def exit_manager(self):
#         self.file_manager.close()
#         self.manager_open = False

#     def events(self, instance, keyboard, keycode, text, modifiers):
#         if keyboard in (1001, 27):
#             if self.manager_open:
#                 self.file_manager.back()
#         return True

app = pb.initialize_app(config)
auth = app.auth()

cert = fba.credentials.Certificate("./serviceAccount.json")
app_admin = fba.initialize_app(cert, {
    "storageBucket": "learplus-6ade0.appspot.com"
})
db = firestore_admin.client()

class AsyncImageButton(ButtonBehavior, AsyncImage):
    pass

class EntradaScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(EntradaScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        # Botão central
        central_button = Button(text="",
                                background_normal="Primeira.jpg",
                                background_down="transparent.png",
                                border=(0, 0, 0, 0),
                                size_hint=(None, None),
                                size=(400, 400),
                                pos_hint={'center_x': 0.5, 'center_y': 0.54},
                                font_size='30sp')
        central_button.bind(on_release=self.trocar_para_tela_menu)
        layout.add_widget(central_button)

        # Texto abaixo do botão
        click_text = Label(text="Clique Aqui!",
                           size_hint=(None, None),
                           size=(200, 100),
                           pos_hint={'center_x': 0.5, 'center_y': 0.4},
                           font_size='30sp',
                           color=(0, 0, 0, 1))  # Cor preta)
        layout.add_widget(click_text)

        self.add_widget(layout)

        # Adiciona animação de entrada
        Clock.schedule_once(self.add_animation, 0)

    def add_animation(self, dt):
        # Animação para o botão e o texto
        central_button = self.children[0].children[0]
        click_text = self.children[0].children[1]
        
        # Configuração da animação para o botão
        anim_button = Animation(size=(200, 100), duration=0.5)
        anim_button += Animation(size=(220, 110), duration=0.5)
        anim_button.start(central_button)
        
        # Configuração da animação para o texto
        anim_text = Animation(opacity=1, duration=2)
        click_text.opacity = 0
        anim_text.start(click_text)

    def on_button_click(self, instance):
        # Exemplo de ação ao clicar no botão
        print("Botão clicado!")
    def trocar_para_tela_menu(self, instance):
              self.manager.current = 'menu'
        
class MenuScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = RelativeLayout(size_hint=(1, None), height=50, pos_hint={'top': 1})

        # Botão Voltar
        back_button = Button(text="",
                            font_size=20,
                            background_normal="perfil.png",
                            background_down="transparent.png",
                            border=(0, 0, 0, 0),
                            size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'x': 0.02, 'top': 0.98})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_login)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)

        # Botão "Login" ancorado no canto superior direito
        login_button = Button(text="",
                            font_size=7,
                            background_normal="",
                            background_down="transparent.png",
                            border=(0, 0, 0, 0),
                            size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'right': 0.98, 'top': 0.98})  # Posiciona no canto superior direito
        top_button_layout.add_widget(login_button)

        layout.add_widget(top_button_layout)


        # Botão "conteudo" centro
        Adicionar_button = Button(text="",
                                font_size=0,
                                background_normal="alunos.png",
                                background_down="transparent.png",
                                border=(0, 0, 0, 0),
                                size_hint=(None, None),
                                size=(240, 240),
                                pos_hint={'center_x': 0.5, 'center_y': 0.65})  # Posiciona no centro
        Adicionar_button.bind(on_release=self.trocar_para_tela_aluno)  # Associar a ação ao botão
        layout.add_widget(Adicionar_button)

        # Título "CONTEUDO"
        title_label = Label(text="[color=000000]Alunos[/color]",
                            font_size=30,
                            size_hint_y=None,
                            height=730,
                            markup=True,
                            pos_hint={'center_x': 0.5, 'center_y': 0.55})  # Posiciona no centro
        layout.add_widget(title_label)

        # Botão "conteúdo" centro
        validar_button = Button(text="",
                                font_size=0,
                                background_normal="professor.png",
                                background_down="transparent.png",
                                border=(0, 0, 0, 0),
                                size_hint=(None, None),
                                size=(240, 240),
                                pos_hint={'center_x': 0.5, 'center_y': 0.40})  # Posiciona no centro
        validar_button.bind(on_release=self.trocar_para_tela_professor)  # Associar a ação ao botão
        layout.add_widget(validar_button)

        # Título "CONTEUDO"
        title_label = Label(text="[color=000000]Professor[/color]",
                            font_size=30,
                            size_hint_y=None,
                            height=730,
                            markup=True,
                            pos_hint={'center_x': 0.5, 'center_y': 0.30})  # Posiciona no centro
        layout.add_widget(title_label)        

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
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(LoginADMScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = RelativeLayout(size_hint=(1, None), height=50, pos_hint={'top': 1})

        # Botão Voltar
        back_button = Button(text="",
                            font_size=20,
                            background_normal="voltar.png",
                            background_down="transparent.png",
                            border=(0, 0, 0, 0),
                            size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'x': 0.02, 'top': 0.98})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_menu)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)

        # Botão "Login" ancorado no canto superior direito
        login_button = Button(text="",
                            font_size=7,
                            background_normal="",
                            background_down="transparent.png",
                            border=(0, 0, 0, 0),
                            size_hint=(None, None),
                            size=(55, 55),
                            pos_hint={'right': 0.98, 'top': 0.98})  # Posiciona no canto superior direito
        top_button_layout.add_widget(login_button)

        layout.add_widget(top_button_layout)
            

        # Título (no topo do layout)
        title_label = Label(text="[color=000000]Secretaria[/color]",
                            font_size=40,
                            size_hint=(None, None),
                            size=(200, 50),
                            markup=True,
                            pos_hint={'center_x': 0.5, 'top': 0.95})  # Posiciona no centro horizontal e no topo
        layout.add_widget(title_label)


        # Título "CONTEUDO"
        title_label = Label(text="[color=000000]Login[/color]",
                            font_size=40,
                            size_hint_y=None,
                            height=730,
                            markup=True,
                            pos_hint={'center_x': 0.5, 'center_y': 0.85})  # Posiciona no centro
        layout.add_widget(title_label)
        
        
        
        # Crie um RelativeLayout para centralizar o conteúdo verticalmente
        content_layout = RelativeLayout()

        # Crie um GridLayout para os campos de entrada
        input_layout = GridLayout(cols=1, spacing=150, size_hint_y=None)

        # Layout para Email
        email_layout = BoxLayout(orientation='vertical', spacing=25)

        email_label = Label(text="[color=000000]EMAIL:[/color]",
                            font_size=26,
                            markup=True)
        email_layout.add_widget(email_label)

        self.email_input = TextInput(hint_text="Email",
                                background_color=("#77C4FF"),
                                background_normal='',
                                size_hint_y=None,
                                height=45)
        email_layout.add_widget(self.email_input)

        input_layout.add_widget(email_layout)

        # Layout para Senha
        senha_layout = BoxLayout(orientation='vertical', spacing=25)

        senha_label = Label(text="[color=000000]SENHA:[/color]",
                            font_size=26,
                            markup=True)
        senha_layout.add_widget(senha_label)

        self.senha_input = TextInput(hint_text="Senha", 
                                background_color=("#77C4FF"), 
                                background_normal='', 
                                size_hint_y=None, 
                                height=45,
                                password=True,          # Habilita o modo senha
                                password_mask='*')      # Define o asterisco como máscara
        senha_layout.add_widget(self.senha_input)

        input_layout.add_widget(senha_layout)

        # Centralize o input_layout verticalmente no content_layout
        input_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.57}

        content_layout.add_widget(input_layout)

        layout.add_widget(content_layout)

        # Botão "REALIZAR LOGIN"
        btn5 = Button(text="[color=000000]REALIZAR LOGIN[/color]",
                    background_color=("#77C4FF"),
                    background_down="transparent.png",
                    size_hint=(None, None),
                    size=(250, 80),
                    markup=True)

        # Posicione o botão abaixo dos campos de entrada
        btn5.pos_hint = {'center_x': 0.5, 'y': 0.3}

        btn5.bind(on_release=self.login)  # Associar a ação ao botão
        btn5.background_normal = ''  # Removemos o fundo padrão do botão
        layout.add_widget(btn5)


        
        self.add_widget(layout)
    def trocar_para_tela_secretaria(self, instance):
        self.manager.current = 'secretaria' 
    def trocar_para_tela_menu(self, instance):
        self.manager.current = 'menu'
    def trocar_para_tela_login(self, instance):
        self.manager.current = 'login'
    def login(self, *params):
        try:
            user = auth.sign_in_with_email_and_password(self.email_input.text, self.senha_input.text)
            self.manager.current = 'secretaria'
            self.senha_input.text = ""
            self.email_input.text = ""
        except:
            print("ERROR: LOGIN SECRETARIA")
        
class SecretariaScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(SecretariaScreen, self).__init__(**kwargs)
        
        layout = FloatLayout()

        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = RelativeLayout(size_hint=(1, None), height=50, pos_hint={'top': 1})

        # Botão Voltar
        back_button = Button(text="",
                            font_size=20,
                            background_normal="voltar.png",
                            background_down="transparent.png",
                            border=(0, 0, 0, 0),
                            size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'x': 0.02, 'top': 0.98})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_login)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)

        # Botão "Login" ancorado no canto superior direito
        login_button = Button(text="",
                            font_size=7,
                            background_normal="login.png",
                            background_down="transparent.png",
                            border=(0, 0, 0, 0),
                            size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'right': 0.98, 'top': 0.98})  # Posiciona no canto superior direito
        login_button.bind(on_release=self.trocar_para_tela_contaADM)  # Associar a ação ao botão
        top_button_layout.add_widget(login_button)

        layout.add_widget(top_button_layout)

        # Título (no topo do layout)
        title_label = Label(text="[color=000000]Secretaria[/color]",
                            font_size=40,
                            size_hint=(None, None),
                            size=(200, 50),
                            markup=True,
                            pos_hint={'center_x': 0.5, 'top': 0.95})  # Posiciona no centro horizontal e no topo
        layout.add_widget(title_label)

        # Botão "conteudo" centro
        Adicionar_button = Button(text="",
                                font_size=0,
                                background_normal="segue.png",
                                background_down="transparent.png",
                                border=(0, 0, 0, 0),
                                size_hint=(None, None),
                                size=(240, 240),
                                pos_hint={'center_x': 0.5, 'center_y': 0.65})  # Posiciona no centro
        Adicionar_button.bind(on_release=self.trocar_para_tela_addConta)  # Associar a ação ao botão
        layout.add_widget(Adicionar_button)

        # Título "CONTEUDO"
        title_label = Label(text="[color=000000]Adicionar Conta[/color]",
                            font_size=30,
                            size_hint_y=None,
                            height=730,
                            markup=True,
                            pos_hint={'center_x': 0.5, 'center_y': 0.55})  # Posiciona no centro
        layout.add_widget(title_label)

        # Botão "conteúdo" centro
        validar_button = Button(text="",
                                font_size=0,
                                background_normal="conta-verificada.png",
                                background_down="transparent.png",
                                border=(0, 0, 0, 0),
                                size_hint=(None, None),
                                size=(240, 240),
                                pos_hint={'center_x': 0.5, 'center_y': 0.38})  # Posiciona no centro
        validar_button.bind(on_release=self.trocar_para_tela_listagem)  # Associar a ação ao botão
        layout.add_widget(validar_button)

        # Título "CONTEUDO"
        title_label = Label(text="[color=000000]Validar Conta[/color]",
                            font_size=30,
                            size_hint_y=None,
                            height=250,
                            markup=True,
                            pos_hint={'center_x': 0.5, 'center_y': 0.28})  # Posiciona no centro
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
    def trocar_para_tela_listagem(self, instance):
        self.manager.current = 'listagem'      
class CadastroScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(CadastroScreen, self).__init__(**kwargs)
        
        layout = FloatLayout()
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0, 0, 0, 0),
                             size_hint=(None, None),
                             size=(55, 55),
                             pos_hint={'x': 0, 'top': 8.0})
        back_button.bind(on_release=self.trocar_para_tela_menu)
        top_button_layout.add_widget(back_button)
        
        layout.add_widget(top_button_layout)
        
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
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0, 0, 0, 0),
                             size_hint=(None, None),
                             size=(55, 55),
                             pos_hint={'x': 0, 'top': 8.0})
        back_button.bind(on_release=self.trocar_para_tela_menu)
        top_button_layout.add_widget(back_button)
        
        layout.add_widget(top_button_layout)
        
        # Campos de entrada
        input_layout = BoxLayout(orientation='vertical', spacing=10, padding=(10, 100, 10, 10))
        
        # Nome Completo
        name_layout = BoxLayout(orientation='vertical', spacing=8)
        
        name_label = Label(text="[color=000000]NOME COMPLETO:[/color]",
                            font_size=12,
                            markup=True)
        name_layout.add_widget(name_label)
        
        name_input = TextInput(hint_text="Nome Completo",
                              background_color=(0.7, 0.87, 0.38, 1),
                              size_hint_y=None,
                              height=30)
        name_layout.add_widget(name_input)
        
        input_layout.add_widget(name_layout)
        
        # Layout para Email
        email_layout = BoxLayout(orientation='vertical', spacing=8)
        
        email_label = Label(text="[color=000000]EMAIL:[/color]",
                            font_size=12,
                            markup=True)
        email_layout.add_widget(email_label)
        
        email_input = TextInput(hint_text="Email",
                               background_color=(0.7, 0.87, 0.38, 1),
                               size_hint_y=None,
                               height=30)
        email_layout.add_widget(email_input)
        
        input_layout.add_widget(email_layout)
        
        # Layout para Senha
        senha_layout = BoxLayout(orientation='vertical', spacing=8)
        
        senha_label = Label(text="[color=000000]SENHA:[/color]",
                            font_size=12,
                            markup=True)
        senha_layout.add_widget(senha_label)
        
        senha_input = TextInput(hint_text="Senha",
                               background_color=(0.7, 0.87, 0.38, 1),
                               size_hint_y=None,
                               height=30,
                               password=True,          # Habilita o modo senha
                                password_mask='*')      # Define o asterisco como máscara
        senha_layout.add_widget(senha_input)
        
        input_layout.add_widget(senha_layout)
        
        layout.add_widget(input_layout)
        
        
        self.add_widget(layout)
        
    def trocar_para_tela_secretaria(self, instance):
        self.manager.current = 'secretaria'
    
    def trocar_para_tela_menu(self, instance):
        self.manager.current = 'menu'
# class ListagemScreen(Screen):
#     def on_enter(self):
#         print("DEBUG-SCREEN: ", self.__class__.__name__)
#     def __init__(self, **kwargs):
#         super(ListagemScreen, self).__init__(**kwargs)
#         layout = FloatLayout()

#         # Layout superior para os botões "Voltar" e "Login"
#         top_button_layout = RelativeLayout(size_hint=(1, None), height=50, pos_hint={'top': 1})

#         # Botão Voltar
#         back_button = Button(text="",
#                             font_size='20sp',
#                             background_normal="voltar.png",
#                             background_down="transparent.png",
#                             border=(0, 0, 0, 0),
#                             size_hint=(None, None),
#                             size=(80, 80),
#                             pos_hint={'x': 0.02, 'top': 1})
#         back_button.bind(on_release=self.trocar_para_tela_secretaria)
#         top_button_layout.add_widget(back_button)

#         # Botão "Login" ancorado no canto superior direito
#         login_button = Button(text="",
#                             font_size='14sp',
#                             background_normal="",
#                             background_down="transparent.png",
#                             border=(0, 0, 0, 0),
#                             size_hint=(None, None),
#                             size=(55, 55),
#                             pos_hint={'right': 0.98, 'top': 1})
#         top_button_layout.add_widget(login_button)

#         layout.add_widget(top_button_layout)
#         # TELA PARA TROCAR
#         # Título (no topo do layout)
#         title_label = Label(text="[color=000000]Secretaria[/color]",
#                             font_size='40sp',
#                             size_hint=(None, None),
#                             size=(200, 50),
#                             markup=True,
#                             pos_hint={'center_x': 0.5, 'top': 0.97})
#         layout.add_widget(title_label)
        

#         # Crie um ScrollView para permitir rolagem
#         self.scroll_view = ScrollView(size_hint=(1, 0.7), size=(self.width, self.height * 0.7), do_scroll_x=False, do_scroll_y=True)
        
#         # Layout para os campos de entrada dentro do ScrollView
#         self.scroll_layout = GridLayout(cols=1, spacing=20, size_hint_y=None)
#         self.scroll_layout.bind(minimum_height=self.scroll_layout.setter('height'))

#         # Adiciona as seções de email e os botões agrupados
#         self.adicionar_secoes_email()

#         # Adiciona o ScrollView ao layout principal
#         self.scroll_view.add_widget(self.scroll_layout)
#         layout.add_widget(self.scroll_view)

#         # Adiciona a barra de rolagem ao lado direito
#         with self.scroll_view.canvas.after:
#             Color(0.5, 0.5, 0.5, 0.7)  # Cor da barra de rolagem
#             self.scroll_bar = Rectangle(size=(10, self.scroll_view.height), pos=(self.scroll_view.width - 10, 0))

#         self.bind(size=self._update_scroll_bar, pos=self._update_scroll_bar)
#         self.scroll_view.bind(scroll_y=self._update_scroll_bar)
#         self.scroll_view.bind(on_touch_up=self.scroll_released)

#         self.add_widget(layout)

#     def _update_scroll_bar(self, *args):
#         scroll_height = self.scroll_view.height
#         content_height = self.scroll_layout.height
#         scroll_y = self.scroll_view.scroll_y

#         # Atualiza a posição e tamanho da barra de rolagem
#         self.scroll_bar.pos = (self.scroll_view.width - 10, scroll_height * scroll_y)
#         self.scroll_bar.size = (10, scroll_height * (scroll_height / content_height))

#     def scroll_released(self, widget, touch):
#         if not self.scroll_view.collide_point(*touch.pos):
#             return False
#         # Permite que o scroll continue a funcionar normalmente após soltar
#         return super(ScrollView, self.scroll_view).on_touch_up(touch)

#     def adicionar_secoes_email(self):
#         # Adiciona a seção "Professor"
#         self.adicionar_email_secao("SESSÃO PROFESSOR", "")

#         # Adiciona a seção "Aluno"
#         self.adicionar_email_secao("SESSÃO ALUNO", "")
        

#     def adicionar_email_secao(self, secao_titulo,email):
#         # Layout para Email
#         email_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
#         email_layout.height = 240  # Define a altura do BoxLayout

#         email_label = Label(text=f"[color=000000]{secao_titulo}:[/color]",
#                             font_size='26sp',
#                             markup=True)
#         email_layout.add_widget(email_label)

#         email_input = TextInput(hint_text="Email",
#                                 background_color=(0.75, 0.75, 0.75, 1),
#                                 background_normal='',
#                                 size_hint_y=None,
#                                 height=45)
#         email_input.text = email
#         email_layout.add_widget(email_input)

#         # Layout para os botões adicionais
#         extra_buttons_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=None, height=80)
        
#         # Botão adicional 1
#         extra_button1 = Button(text="",
#                             font_size='20sp',
#                             background_normal="atualizar.png",
#                             background_down="transparent.png",
#                             border=(0, 0, 0, 0),
#                             size_hint=(None, None),
#                             size=(80, 80))
#         extra_button1.bind(on_release=self.trocar_para_tela_atzConta)
#         extra_buttons_layout.add_widget(extra_button1)
        
#         # Espaçador para centralizar o botão "Conta Verificada"
#         extra_buttons_layout.add_widget(BoxLayout(size_hint_x=1))  # Ocupa o espaço restante antes do botão "Conta Verificada"
        
#         # Botão adicional 2
#         extra_button2 = Button(text="",
#                             font_size='20sp',
#                             background_normal="conta-verificada.png",
#                             background_down="transparent.png",
#                             border=(0, 0, 0, 0),
#                             size_hint=(None, None),
#                             size=(80, 80))
#         extra_buttons_layout.add_widget(extra_button2)
        
#         # Botão adicional 3
#         extra_button3 = Button(text="",
#                             font_size='20sp',
#                             background_normal="deixar-de-seguir.png",
#                             background_down="transparent.png",
#                             border=(0, 0, 0, 0),
#                             size_hint=(None, None),
#                             size=(80, 80))
#         extra_buttons_layout.add_widget(BoxLayout(size_hint_x=1))  # Espaçador para empurrar o botão para a direita
#         extra_buttons_layout.add_widget(extra_button3)
        
#         email_layout.add_widget(extra_buttons_layout)
#         self.scroll_layout.add_widget(email_layout)

#     def trocar_para_tela_listagem(self, instance):
#         self.manager.current = 'listagem'
    
#     def trocar_para_tela_secretaria(self, instance):
#         self.manager.current = 'secretaria'
    
#     def trocar_para_tela_atzConta(self, instance):
#         self.manager.current = 'atzConta'
        
#     def verify(self, *params):
#         try:
#             user = auth_admin.get_user_by_email(self.email_input.text)
#             custom_claims = user.custom_claims
#             custom_claims["verified"] = True
#             auth_admin.set_custom_user_claims(user.uid, custom_claims)

#             self.manager.current = 'secretaria'
#         except:
#             print("ERROR: VERIFY")
        
        #########################AQUI ACABA A LISTAGEM ######################################################################################### 

class ListagemScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(ListagemScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = RelativeLayout(size_hint=(1, None), height=50, pos_hint={'top': 1})

        # Botão Voltar
        back_button = Button(text="",
                            font_size=20,
                            background_normal="voltar.png",
                            background_down="transparent.png",
                            border=(0, 0, 0, 0),
                            size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'x': 0.02, 'top': 0.98})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_secretaria)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)

        # Botão "Login" ancorado no canto superior direito
        login_button = Button(text="",
                            font_size=7,
                            background_normal="",
                            background_down="transparent.png",
                            border=(0, 0, 0, 0),
                            size_hint=(None, None),
                            size=(55, 55),
                            pos_hint={'right': 0.98, 'top': 0.98})  # Posiciona no canto superior direito
        top_button_layout.add_widget(login_button)

        layout.add_widget(top_button_layout)
        # TELA PARA TROCAR
        # Botão Voltar
        back_button = Button(text="",
                            font_size=20,
                            background_normal="atualizar.png",
                            background_down="transparent.png",
                            border=(0, 0, 0, 0),
                            size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'center_x': 0.08, 'center_y': -15})  # Posiciona no centro
        back_button.bind(on_release=self.trocar_para_tela_atzConta)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)
        
        
        # Botão Voltar
        back_button = Button(text="",
                            font_size=20,
                            background_normal="conta-verificada.png",
                            background_down="transparent.png",
                            border=(0, 0, 0, 0),
                            size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'center_x': 0.51, 'center_y': -15})  # Posiciona no centro
        back_button.bind(on_release=self.verify)
        top_button_layout.add_widget(back_button)
        
        
        # Botão Voltar
        back_button = Button(text="",
                            font_size=20,
                            background_normal="deixar-de-seguir.png",
                            background_down="transparent.png",
                            border=(0, 0, 0, 0),
                            size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'center_x': 0.92, 'center_y': -15})  # Posiciona no centro
        top_button_layout.add_widget(back_button)

        # Título (no topo do layout)
        title_label = Label(text="[color=000000]Secretaria[/color]",
                            font_size=40,
                            size_hint=(None, None),
                            size=(200, 50),
                            markup=True,
                            pos_hint={'center_x': 0.5, 'top': 0.95})  # Posiciona no centro horizontal e no topo
        layout.add_widget(title_label)
        
        
        
        # Crie um RelativeLayout para centralizar o conteúdo verticalmente
        content_layout = RelativeLayout()

        # Crie um GridLayout para os campos de entrada
        input_layout = GridLayout(cols=1, spacing=150, size_hint_y=None)

        # Layout para Email
        email_layout = BoxLayout(orientation='vertical', spacing=25)

        email_label = Label(text="[color=000000]EMAIL:[/color]",
                            font_size=26,
                            markup=True)
        email_layout.add_widget(email_label)

        self.email_input = TextInput(hint_text="Email",
                                background_color=("#BEBEBE"),
                                background_normal='',
                                size_hint_y=None,
                                height=45)
        email_layout.add_widget(self.email_input)

        input_layout.add_widget(email_layout)

        # # Layout para Senha
        # senha_layout = BoxLayout(orientation='vertical', spacing=25)

        # senha_label = Label(text="[color=000000]SENHA:[/color]",
        #                     font_size=26,
        #                     markup=True)
        # senha_layout.add_widget(senha_label)

        # senha_input = TextInput(hint_text="Senha", 
        #                         background_color=("#BEBEBE"), 
        #                         background_normal='', 
        #                         size_hint_y=None, 
        #                         height=45
        # senha_layout.add_widget(senha_input)

        # input_layout.add_widget(senha_layout)

        # Centralize o input_layout verticalmente no content_layout
        input_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.57}

        content_layout.add_widget(input_layout)

        layout.add_widget(content_layout)

        
        self.add_widget(layout)
    def trocar_para_tela_listagem(self, instance):
        self.manager.current = 'listagem'
    def trocar_para_tela_secretaria(self, instance):
        self.manager.current = 'secretaria'
    def trocar_para_tela_atzConta(self, instance):
        self.manager.current = 'atzConta'
    def verify(self, *params):
        try:
            user = auth_admin.get_user_by_email(self.email_input.text)
            custom_claims = user.custom_claims
            custom_claims["verified"] = True
            auth_admin.set_custom_user_claims(user.uid, custom_claims)

            self.manager.current = 'secretaria'
        except:
            print("ERROR: VERIFY")

class ContaADMScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(ContaADMScreen, self).__init__(**kwargs)
      # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.5}  # Define o topo do layout na parte superior da tela
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        
        # Botão Voltar
        back_button = Button(text="",
                    font_size=7,
                    background_normal="voltar.png",
                    background_down="transparent.png",
                    border=(0,0,0,0),
                    size_hint=(None, None),
                    size=(85, 85),
                    pos_hint={'x': 0, 'top': 16.2})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_secretaria)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)
        
         # Rótulo para o primeiro botão
        label1 = Label(text="[color=000000]Secretaria[/color]", 
                            font_size=30,
                            halign='center',
                            markup= True)
        layout.add_widget(label1)
        
        # Imagem no canto superior direito
        image = Image(source="Avaliacao.png",
            size_hint=(None, None),
            size=(240, 240))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=500)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        
        
        # Widget em branco para aumentar o espaço
        layout.add_widget(Widget(size=(1, 40)))  # Ajuste a altura conforme necessário


        
        # Botão "LISTAGEM"
        btn5 = Button(text="[color=000000]LISTAGEM[/color]", 
                    font_size=30,
                    background_color=(0.7, 0.87, 0.38, 1), 
                    size_hint=(None, None), 
                    size=(250, 70), 
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
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(AlunoScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = RelativeLayout(size_hint=(1, None), height=50, pos_hint={'top': 1})

        # Botão Voltar
        back_button = Button(text="",
                            font_size=20,
                            background_normal="voltar.png",
                            background_down="transparent.png",
                            border=(0, 0, 0, 0),
                            size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'x': 0.02, 'top': 0.98})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_menu)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)

        # Botão "Login" ancorado no canto superior direito
        login_button = Button(text="",
                            font_size=7,
                            background_normal="login.png",
                            background_down="transparent.png",
                            border=(0, 0, 0, 0),
                            size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'right': 0.98, 'top': 0.98})  # Posiciona no canto superior direito
        login_button.bind(on_release=self.trocar_para_tela_loginAluno)  # Associar a ação ao botão
        top_button_layout.add_widget(login_button)

        layout.add_widget(top_button_layout)


        # Botão "conteudo" centro
        Adicionar_button = Button(text="",
                                font_size=0,
                                background_normal="escolher_atividade.png",
                                background_down="transparent.png",
                                border=(0, 0, 0, 0),
                                size_hint=(None, None),
                                size=(240, 240),
                                pos_hint={'center_x': 0.5, 'center_y': 0.57})  # Posiciona no centro
        Adicionar_button.bind(on_release=self.trocar_para_tela_escolher)  # Associar a ação ao botão
        layout.add_widget(Adicionar_button)

        # Título "CONTEUDO"
        title_label = Label(text="[color=000000]Escolher Atividade[/color]",
                            font_size=34,
                            size_hint_y=None,
                            height=730,
                            markup=True,
                            pos_hint={'center_x': 0.5, 'center_y': 0.47})  # Posiciona no centro
        layout.add_widget(title_label)
        

        self.add_widget(layout)
    def trocar_para_tela_loginAluno(self, instance):
        self.manager.current = 'loginAluno'
    def trocar_para_tela_menu(self, instance):
        self.manager.current = 'menu'    
    def trocar_para_tela_escolher(self, instance):
        if auth.current_user:
            if auth.current_user.get("custom_claims"):
                if auth.current_user["custom_claims"].get("role") == "student":
                    self.manager.current = 'escolher'
                    return
        self.manager.current = "loginAluno"   
        
class EscolherScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(EscolherScreen, self).__init__(**kwargs)

        docs = db.collection("tasks").stream()

        tasks = {
            "math": [],
            "crossword": [],
            "exam": [],
            "puzzle": [],
            "paint": []
        }

        for doc in docs:
            task = {
               "id": doc.id,
               **doc.to_dict()
            }
            tasks[task["type"]].append(task)

        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        

        # Botão Voltar
        back_button = Button(text="",
                        font_size=7,
                        background_normal="voltar.png",
                        background_down="transparent.png",
                        border=(0,0,0,0),
                        size_hint=(None, None),
                        size=(85, 85),
                        pos=(3.5, 1350))
        back_button.bind(on_release=self.trocar_para_tela_aluno)  # Associar a ação ao botão
        layout.add_widget(back_button)

        title = Label(text="Escolha sua Atividade", font_size=40, size_hint_y=None, color="black")
        layout.add_widget(title)

        math_title = Label(text="Matemática", font_size=32, size_hint_y=None, color="black")
        puzzle_title = Label(text="Quebra-Cabeça", font_size=32, size_hint_y=None, color="black")
        exam_title = Label(text="Avaliativas", font_size=32, size_hint_y=None, color="black")
        crossword_title = Label(text="Palavras Cruzadas", font_size=32, size_hint_y=None, color="black")
        paint_title = Label(text="Pinturas", font_size=32, size_hint_y=None, color="black")


        if len(tasks["math"]) > 0:
            layout.add_widget(math_title)

            task_layout = GridLayout(cols=3, spacing=(10, 10))

            for task in tasks["math"]:
                btn = AsyncImageButton(
                    source=task["image"],
                    size_hint=(None, None), 
                    size=(145, 210)
                )

                btn.bind(on_release=self.trocar_para_tela_licaoEscolhida(task))

                task_layout.add_widget(btn)

            layout.add_widget(task_layout)

        if len(tasks["puzzle"]) > 0:
            layout.add_widget(puzzle_title)

            task_layout = GridLayout(cols=3, spacing=(10, 10))

            for task in tasks["puzzle"]:
                btn = AsyncImageButton(
                    source=task["image"],
                    size_hint=(None, None), 
                    size=(145, 210)
                )
                btn.bind(on_release=self.trocar_para_tela_licaoEscolhida(task))

                task_layout.add_widget(btn)
                
            layout.add_widget(task_layout)

        if len(tasks["crossword"]) > 0:
            layout.add_widget(crossword_title)

            task_layout = GridLayout(cols=3, spacing=(10, 10))

            for task in tasks["crossword"]:
                btn = AsyncImageButton(
                    source=task["image"],
                    size_hint=(None, None), 
                    size=(145, 210)
                )
                btn.bind(on_release=self.trocar_para_tela_licaoEscolhida(task))

                task_layout.add_widget(btn)
                
            layout.add_widget(task_layout)

        if len(tasks["exam"]) > 0:
            layout.add_widget(exam_title)

            task_layout = GridLayout(cols=3, spacing=(10, 10))

            for task in tasks["exam"]:
                btn = AsyncImageButton(
                    source=task["image"],
                    size_hint=(None, None), 
                    size=(145, 210)
                )
                btn.bind(on_release=self.trocar_para_tela_licaoEscolhida(task))

                task_layout.add_widget(btn)
                
            layout.add_widget(task_layout)

        if len(tasks["paint"]) > 0:
            layout.add_widget(paint_title)

            task_layout = GridLayout(cols=3, spacing=(10, 10))

            for task in tasks["paint"]:
                btn = AsyncImageButton(
                    source=task["image"],
                    size_hint=(None, None), 
                    size=(145, 210)
                )
                btn.bind(on_release=self.trocar_para_tela_licaoEscolhida(task))

                task_layout.add_widget(btn)
                
            layout.add_widget(task_layout)

        
    #       # Título 
    #     title_label1 = Label(text="[color=000000]Escolha sua Atividade[/color]",
    #                         font_size=40,
    #                         size_hint_y=None,
    #                         height=2550,
    #                         markup=True)
    #     layout.add_widget(title_label1)
        
    #       # Título medio
    #     title_label1 = Label(text="[color=#000000]Matemática[/color]",
    #                         font_size=40,
    #                         size_hint_y=None,
    #                         height=1600,
    #                         markup=True)
    #     layout.add_widget(title_label1)
        
    #       # Título dificil
    #     title_label1 = Label(text="[color=#000000]Nome Atividades[/color]",
    #                         font_size=40,
    #                         size_hint_y=None,
    #                         height=600,
    #                         markup=True)
    #     layout.add_widget(title_label1)
        
    #      # Layout superior para os botões "Voltar" 
    #     top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
    #     # Botão Voltar
    #     back_button = Button(text="",
    #                          font_size=7,
    #                          background_normal="voltar.png",
    #                          background_down="transparent.png",
    #                          border=(0,0,0,0),
    #                          size_hint=(None, None),
    #                          size=(85, 85),
    #                          pos=(3.5, 1350))
    #     back_button.bind(on_release=self.trocar_para_tela_aluno)  # Associar a ação ao botão
    #     layout.add_widget(back_button)


    #    # Botões "Escolher"
    #     btn1 = Button(text="", 
    #           background_normal="facil1.jpg", 
    #           background_down="transparent.png",
    #           size_hint=(None, None), 
    #           size=(145, 210), #tamanho
    #           markup=True,
    #           pos=(700, 950))#posicao
    #     btn1.bind(on_release=self.trocar_para_tela_licaoEscolhida)  # Associar a ação ao botão
    #     btn1.pos_hint = {'center_x': 0.3}  # Centralize o botão horizontalmente
    #     layout.add_widget(btn1)
       
    #     btn2 = Button(text="", 
    #           background_normal="quebra2.jpeg",
    #           background_down="transparent.png", 
    #           size_hint=(None, None), 
    #           size=(145, 210), #tamanho
    #           markup=True,
    #           pos=(700, 450))#posicao
    #     btn2.bind(on_release=self.trocar_para_tela_licaoEscolhida)  # Associar a ação ao botão
    #     btn2.pos_hint = {'center_x': 0.3}  # Centralize o botão horizontalmente
    #     layout.add_widget(btn2)
       
    #     btn3 = Button(text="", 
    #           background_normal="alimento1.jpeg", 
    #           background_down="transparent.png",
    #           size_hint=(None, None), 
    #           size=(145, 210), #tamanho
    #           markup=True,
    #           pos=(700, 9))
    #     btn3.bind(on_release=self.trocar_para_tela_licaoEscolhida)  # Associar a ação ao botão
    #     btn3.pos_hint = {'center_x': 0.3}  # Centralize o botão horizontalmente
    #     layout.add_widget(btn3)

    #     btn4 = Button(text="", 
    #           background_normal="medio1.jpg",
    #           background_down="transparent.png", 
    #           size_hint=(None, None), 
    #           size=(145, 210), #tamanho
    #           markup=True,
    #           pos=(700, 950))#posicao
    #     btn4.bind(on_release=self.trocar_para_tela_licaoEscolhida)  # Associar a ação ao botão
    #     btn4.pos_hint = {'center_x': 0.7}  # Centralize o botão horizontalmente
    #     layout.add_widget(btn4)
       
    #     btn5 = Button(text="", 
    #           background_normal="quebra1.jpeg", 
    #           size_hint=(None, None), 
    #           size=(145, 210), #tamanho
    #           markup=True,
    #          pos=(700, 450))#posicao
    #     btn5.bind(on_release=self.trocar_para_tela_licaoEscolhida)  # Associar a ação ao botão
    #     btn5.pos_hint = {'center_x': 0.7}  # Centralize o botão horizontalmente
    #     layout.add_widget(btn5)
       
    #     btn6 = Button(text="", 
    #           background_normal="alimento2.jpeg",
    #           size_hint=(None, None), 
    #           size=(145, 210), #tamanho
    #           markup=True,
    #           pos=(240, 9))
    #     btn6.bind(on_release=self.trocar_para_tela_licaoEscolhida)  # Associar a ação ao botão
    #     btn6.pos_hint = {'center_x': 0.7}  # Centralize o botão horizontalmente
    #     layout.add_widget(btn6)
        
        self.add_widget(layout)
    def trocar_para_tela_aluno(self, instance):
        self.manager.current = 'aluno'
    def trocar_para_tela_escolher(self, instance):
        self.manager.current = 'escolher'
    def trocar_para_tela_licaoEscolhida(self, task):
        def callback(instance):
            licao_escolhida_screen = self.manager.get_screen("licaoEscolhida")
            licao_escolhida_screen.task = task
            licao_escolhida_screen.__init__()

            self.manager.current = licao_escolhida_screen.name 
        return callback 
        
class LoginALUNOScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(LoginALUNOScreen, self).__init__(**kwargs)
       
        
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.5}  # Define o topo do layout na parte superior da tela
        
        # Título (no topo do layout)
        title_label = Label(text="[color=000000]Login[/color]",
                            font_size=40,
                            size_hint_y=None,
                            height=1200,
                            markup=True)
        layout.add_widget(title_label)
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        
        # Botão Voltar
        back_button = Button(text="",
                    font_size=7,
                    background_normal="voltar.png",
                    background_down="transparent.png",
                    border=(0,0,0,0),
                    size_hint=(None, None),
                    size=(80, 80),
                    pos_hint={'x': 0, 'top': 14})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_Aluno)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)

        

    # Imagem no canto superior direito
        image = Image(source="",
            size_hint=(None, None),
            size=(80, 80))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=700)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)


        # Campos de entrada
        input_layout = GridLayout(cols=2, spacing=150, size_hint_y=None, height=15, pos_hint={'x': 0.5})

        # # Layout para Nome Completo
        # name_layout = BoxLayout(orientation='vertical', spacing=30, padding=(0, 0, 0, 205))  # Adicionamos margem inferior de 170
        
        # name_label = Label(text="[color=000000]NOME COMPLETO:[/color]",
        #                     font_size=26,
        #                     markup=True)
        # name_layout.add_widget(name_label)
        

        # name_input = TextInput(hint_text="Nome Completo", background_color=("#77C4FF"), size_hint_y=None, height=45)
        # name_layout.add_widget(name_input)
        
        # layout.add_widget(name_layout)

        # Layout para Email
        email_layout = BoxLayout(orientation='vertical', spacing=25, padding=(0, 0, 0, 132))  # Adicionamos margem inferior de 20)

        email_label = Label(text="[color=000000]EMAIL:[/color]",
                            font_size=26,
                            markup=True)
        email_layout.add_widget(email_label)

        self.email_input = TextInput(hint_text="Email", background_color=("#77C4FF"), size_hint_y=None, height=45)
        email_layout.add_widget(self.email_input)
        
        layout.add_widget(email_layout)
        
    # Layout para Senha  
        senha_layout = BoxLayout(orientation='vertical', spacing=25, padding=(0, 0, 0, 60))  # Adicionamos margem inferior de 20)

        senha_label = Label(text="[color=000000]SENHA:[/color]",
                            font_size=26,
                            markup=True)
        senha_layout.add_widget(senha_label)

        self.senha_input = TextInput(hint_text="Senha", background_color=("#77C4FF"), size_hint_y=None, height=45,
        password=True,          # Habilita o modo senha
                                password_mask='*')      # Define o asterisco como máscara
        senha_layout.add_widget(self.senha_input)
        
        layout.add_widget(senha_layout)
        
        # Botão "Atualizar Conta"
        btn5 = Button(text="[color=000000] [/color]", size_hint=(None, None),background_down="transparent.png", size=(450, 75), markup=True)
       
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.background_normal = ''  # Removemos o fundo padrão do botão
        with btn5.canvas.before:

            self.rect = Rectangle(pos=btn5.pos, size=btn5.size)
        layout.add_widget(btn5)
        
        # Botão "Upload da Foto do Usuário"
        btn6 = Button(text="[color=000000]REALIZAR LOGIN[/color]", background_color=("#77C4FF"), size_hint=(None, None), size=(450, 75), markup=True)
        btn6.bind(on_release=self.login)  # Associar a ação ao botão
        btn6.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn6.background_normal = ''  # Removemos o fundo padrão do botão
        with btn6.canvas.before:
            self.rect = Rectangle(pos=btn6.pos, size=btn6.size)
        layout.add_widget(btn6)
        

        self.add_widget(layout)
        
        
        
        
        
    def trocar_para_tela_loginAluno(self, instance):
        self.manager.current = 'loginAluno'
    def trocar_para_tela_contaALUNO(self, instance):
        self.manager.current = 'contaALUNO'
    def trocar_para_tela_Aluno(self, instance):
        self.manager.current = 'aluno'
    def login(self, *params):
        email = self.email_input.text
        password = self.senha_input.text
        
        try:
            user: auth_admin.UserRecord = auth_admin.get_user_by_email(email)

            print(user.__dict__)

            if user.custom_claims.get("role") == "student":
                if user.custom_claims.get("verified"):
                    auth.sign_in_with_email_and_password(email, password)
                    auth.current_user["custom_claims"] = user.custom_claims
                    self.manager.current = 'aluno'
                    self.email_input.text = ""
                    self.senha_input.text = ""
                else:
                    print("Aluno não verificado")
        except:
            print("ERROR: LOGIN ALUNO")
class ContaALUNOScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(ContaALUNOScreen, self).__init__(**kwargs)
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.5}  # Define o topo do layout na parte superior da tela
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        
        # Botão Voltar
        back_button = Button(text="",
                    font_size=7,
                    background_normal="voltar.png",
                    background_down="transparent.png",
                    border=(0,0,0,0),
                    size_hint=(None, None),
                    size=(85, 85),
                    pos_hint={'x': 0, 'top': 16.2})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_loginAluno)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)
        
         # Rótulo para o primeiro botão
        label1 = Label(text="[color=000000]André da Silva[/color]", 
                            font_size=30,
                            halign='center',
                            markup= True)
        layout.add_widget(label1)
        
        # Imagem no canto superior direito
        image = Image(source="Alunos.png",
            size_hint=(None, None),
            size=(240, 240))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=500)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        
        
        # Widget em branco para aumentar o espaço
        layout.add_widget(Widget(size=(1, 40)))  # Ajuste a altura conforme necessário


        
        # Botão "LISTAGEM"
        btn5 = Button(text="[color=000000]ATIVIDADES[/color]", 
                    font_size=30,
                    background_color=(0.7, 0.87, 0.38, 1), 
                    size_hint=(None, None), 
                    size=(250, 70), 
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
    task = DictProperty()
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(licaoEscolhidaScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)
        
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1318))
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
        licao_image = AsyncImage(
            source=self.task.get("image"), 
            size_hint=(None, None),
            size=(450, 700)
        )
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=1700)
        anchor_layout.add_widget(licao_image)
        layout.add_widget(anchor_layout)
        
        #Botão "download"
        btn5 = Button(text="[color=000000]Download[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#77C4FF"), 
              size_hint=(None, None), 
              size=(240, 75), 
              markup=True,
              pos=(150, 270))
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.bind(on_release=self.download)  # Associar a ação ao botão
        layout.add_widget(btn5)

        
        self.add_widget(layout)
    def trocar_para_tela_licaoEscolhida(self, instance):
        self.manager.current = 'licaoEscolhida'  
    def trocar_para_tela_escolher(self, instance):
        self.manager.current = 'escolher'
    def download(self, *params):
        try:
            url = self.task["image"]
            filename = url.split("/")[-1]
            with open(f"/storage/emulated/0/Download/{filename}", "wb") as file:
                response = requests.get(url)
                file.write(response.content)
                self.manager.current = "escolher"
        except:
            print("ERROR: DOWNLOAD")
       
class ProfessorScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(ProfessorScreen, self).__init__(**kwargs)        
        
        layout = FloatLayout()

        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = RelativeLayout(size_hint=(1, None), height=50, pos_hint={'top': 1})

        # Botão Voltar
        back_button = Button(text="",
                            font_size=20,
                            background_normal="voltar.png",
                            background_down="transparent.png",
                            border=(0, 0, 0, 0),
                            size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'x': 0.02, 'top': 0.98})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_menu)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)

        # Botão "Login" ancorado no canto superior direito
        login_button = Button(text="",
                            font_size=7,
                            background_normal="login.png",
                            background_down="transparent.png",
                            border=(0, 0, 0, 0),
                            size_hint=(None, None),
                            size=(80, 80),
                            pos_hint={'right': 0.98, 'top': 0.98})  # Posiciona no canto superior direito
        login_button.bind(on_release=self.trocar_para_tela_loginProf)  # Associar a ação ao botão
        top_button_layout.add_widget(login_button)

        layout.add_widget(top_button_layout)


        # Botão "conteudo" centro
        Adicionar_button = Button(text="",
                                font_size=0,
                                background_normal="conteudo.png",
                                background_down="transparent.png",
                                 
                                border=(0, 0, 0, 0),
                                size_hint=(None, None),
                                size=(260, 260),
                                pos_hint={'center_x': 0.5, 'center_y': 0.57})  # Posiciona no centro
        Adicionar_button.bind(on_release=self.trocar_para_tela_conteudo)  # Associar a ação ao botão
        layout.add_widget(Adicionar_button)

        # Título "CONTEUDO"
        title_label = Label(text="[color=000000]Conteudo[/color]",
                            font_size=34,
                            size_hint_y=None,
                            height=730,
                            markup=True,
                            pos_hint={'center_x': 0.5, 'center_y': 0.47})  # Posiciona no centro
        layout.add_widget(title_label)
        

        self.add_widget(layout)
    def trocar_para_tela_loginAluno(self, instance):
        self.manager.current = 'loginAluno'
    def trocar_para_tela_escolher(self, instance):
        self.manager.current = 'escolher'    
    def trocar_para_tela_menu(self, instance):
        self.manager.current = 'menu'
    def trocar_para_tela_professor(self, instance):
        self.manager.current = 'professor'      
    def trocar_para_tela_menu(self, instance):
        self.manager.current = 'menu'    
    def trocar_para_tela_loginProf(self, instance):
        self.manager.current = 'loginProf' 
    def trocar_para_tela_conteudo(self, instance):
        if auth.current_user:
            if auth.current_user.get("custom_claims"):
                if auth.current_user["custom_claims"].get("role") == "teacher":
                    self.manager.current = 'conteudo'
                    return
        self.manager.current = "loginProf" 
class LoginPROFScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(LoginPROFScreen, self).__init__(**kwargs)
         # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.5}  # Define o topo do layout na parte superior da tela
        
        # Título (no topo do layout)
        title_label = Label(text="[color=000000]Login[/color]",
                            font_size=40,
                            size_hint_y=None,
                            height=1200,
                            markup=True)
        layout.add_widget(title_label)
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        
        # Botão Voltar
        back_button = Button(text="",
                    font_size=7,
                    background_normal="voltar.png",
                    background_down="transparent.png",
                    border=(0,0,0,0),
                    size_hint=(None, None),
                    size=(80, 80),
                    pos_hint={'x': 0, 'top': 14})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_professor)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)

        

    # Imagem no canto superior direito
        image = Image(source="",
            size_hint=(None, None),
            size=(80, 80))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=700)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)


        # Campos de entrada
        input_layout = GridLayout(cols=2, spacing=150, size_hint_y=None, height=15, pos_hint={'x': 0.5})

        # Layout para Nome Completo
        # name_layout = BoxLayout(orientation='vertical', spacing=30, padding=(0, 0, 0, 205))  # Adicionamos margem inferior de 170
        
        # name_label = Label(text="[color=000000]NOME COMPLETO:[/color]",
        #                     font_size=26,
        #                     markup=True)
        # name_layout.add_widget(name_label)
        

        # name_input = TextInput(hint_text="Nome Completo", background_color=("#77C4FF"), size_hint_y=None, height=45)
        # name_layout.add_widget(name_input)
        
        # layout.add_widget(name_layout)

        # Layout para Email
        email_layout = BoxLayout(orientation='vertical', spacing=25, padding=(0, 0, 0, 132))  # Adicionamos margem inferior de 20)

        email_label = Label(text="[color=000000]EMAIL:[/color]",
                            font_size=26,
                            markup=True)
        email_layout.add_widget(email_label)

        self.email_input = TextInput(hint_text="Email", background_color=("#77C4FF"), size_hint_y=None, height=45)
        email_layout.add_widget(self.email_input)
        
        layout.add_widget(email_layout)
        
    # Layout para Senha  
        senha_layout = BoxLayout(orientation='vertical', spacing=25, padding=(0, 0, 0, 60))  # Adicionamos margem inferior de 20)

        senha_label = Label(text="[color=000000]SENHA:[/color]",
                            font_size=26,
                            markup=True)
        senha_layout.add_widget(senha_label)

        self.senha_input = TextInput(hint_text="Senha", background_color=("#77C4FF"), size_hint_y=None, height=45,
        password=True,          # Habilita o modo senha
                                password_mask='*')      # Define o asterisco como máscara
        senha_layout.add_widget(self.senha_input)
        
        layout.add_widget(senha_layout)
        
        # Botão "Atualizar Conta"
        btn5 = Button(text="[color=000000] [/color]", size_hint=(None, None),background_down="transparent.png", size=(450, 75), markup=True)
       
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.background_normal = ''  # Removemos o fundo padrão do botão
        with btn5.canvas.before:

            self.rect = Rectangle(pos=btn5.pos, size=btn5.size)
        layout.add_widget(btn5)
        
        # Botão "Upload da Foto do Usuário"
        btn6 = Button(text="[color=000000]REALIZAR LOGIN[/color]", background_color=("#77C4FF"), size_hint=(None, None), size=(450, 75), markup=True)
        btn6.bind(on_release=self.login)  # Associar a ação ao botão
        btn6.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn6.background_normal = ''  # Removemos o fundo padrão do botão
        with btn6.canvas.before:
            self.rect = Rectangle(pos=btn6.pos, size=btn6.size)
        layout.add_widget(btn6)
        

        self.add_widget(layout)
    def trocar_para_tela_secretaria(self, instance):
        self.manager.current = 'secretaria' 
    def trocar_para_tela_loginAluno(self, instance):
        self.manager.current = 'loginProf' 
    def trocar_para_tela_professor(self, instance):
        self.manager.current = 'professor'
    def trocar_para_tela_contaProf(self, instance):
        self.manager.current = 'contaProf'
    def login(self, *params):
        email = self.email_input.text
        password = self.senha_input.text
        
        try:
            user: auth_admin.UserRecord = auth_admin.get_user_by_email(email)

            print(user.__dict__)

            if user.custom_claims.get("role") == "teacher":
                if user.custom_claims.get("verified"):
                    auth.sign_in_with_email_and_password(email, password)
                    auth.current_user["custom_claims"] = user.custom_claims
                    self.manager.current = 'contaProf'
                    self.email_input.text = ""
                    self.senha_input.text = ""
                else:
                    print("Professor não verificado")
        except:
            print("ERROR: LOGIN PROFESSOR")
        
class ContaPROFScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(ContaPROFScreen, self).__init__(**kwargs)   
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.5}  # Define o topo do layout na parte superior da tela
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        
        # Botão Voltar
        back_button = Button(text="",
                    font_size=7,
                    background_normal="voltar.png",
                    background_down="transparent.png",
                    border=(0,0,0,0),
                    size_hint=(None, None),
                    size=(85, 85),
                    pos_hint={'x': 0, 'top': 16.2})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_loginProf)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)
        
         # Rótulo para o primeiro botão
        label1 = Label(text="[color=000000]Prof: Jaqueline Maciel[/color]", 
                            font_size=30,
                            halign='center',
                            markup= True)
        layout.add_widget(label1)
        
        # Imagem no canto superior direito
        image = Image(source="Jaqueline_Maciel.png",
            size_hint=(None, None),
            size=(300, 300))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=600)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        
        
        # Widget em branco para aumentar o espaço
        layout.add_widget(Widget(size=(1, 40)))  # Ajuste a altura conforme necessário


        
        # Botão "LISTAGEM"
        btn5 = Button(text="[color=000000]CONTEUDO[/color]", 
                    font_size=30,
                    background_color=(0.7, 0.87, 0.38, 1), 
                    size_hint=(None, None), 
                    size=(250, 70), 
                    markup=True)
        btn5.bind(on_release=self.trocar_para_tela_conteudo)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.background_normal = ''  # Removemos o fundo padrão do botão
        with btn5.canvas.before:

            self.rect = Rectangle(pos=btn5.pos, size=btn5.size)
        layout.add_widget(btn5)
          
        self.add_widget(layout)
    def trocar_para_tela_contaProf(self, instance):
        self.manager.current = 'contaProf'
    def trocar_para_tela_loginProf(self, instance):
        self.manager.current = 'loginProf'
    def trocar_para_tela_conteudo(self, instance):
        self.manager.current = 'conteudo'
        
class AddContaScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(AddContaScreen, self).__init__(**kwargs)
        Window.clearcolor = (1,1,1,1)
        
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.5}  # Define o topo do layout na parte superior da tela
        
        # Título (no topo do layout)
        title_label = Label(text="[color=000000]Secretaria[/color]",
                            font_size=40,
                            size_hint_y=None,
                            height=1200,
                            markup=True)
        layout.add_widget(title_label)
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        
        # Botão Voltar
        back_button = Button(text="",
                    font_size=7,
                    background_normal="voltar.png",
                    background_down="transparent.png",
                    border=(0,0,0,0),
                    size_hint=(None, None),
                    size=(80, 80),
                    pos_hint={'x': 0, 'top': 14})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_secretaria)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)

        

    # Imagem no canto superior direito
        image = Image(source="Imagem1.png",
            size_hint=(None, None),
            size=(80, 80))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=700)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)


        # Campos de entrada
        input_layout = GridLayout(cols=2, spacing=150, size_hint_y=None, height=15, pos_hint={'x': 0.5})

        # Layout para Nome Completo
        name_layout = BoxLayout(orientation='vertical', spacing=30, padding=(0, 0, 0, 205))  # Adicionamos margem inferior de 170
        
        name_label = Label(text="[color=000000]NOME COMPLETO:[/color]",
                            font_size=26,
                            markup=True)
        name_layout.add_widget(name_label)
        

        self.name_input = TextInput(hint_text="Nome Completo", background_color=(0.7, 0.87, 0.38, 1), size_hint_y=None, height=45)
        name_layout.add_widget(self.name_input)
        
        layout.add_widget(name_layout)

        # Layout para Email
        email_layout = BoxLayout(orientation='vertical', spacing=30, padding=(0, 0, 0, 132))  # Adicionamos margem inferior de 20)

        email_label = Label(text="[color=000000]EMAIL:[/color]",
                            font_size=26,
                            markup=True)
        email_layout.add_widget(email_label)

        self.email_input = TextInput(hint_text="Email", background_color=(0.7, 0.87, 0.38, 1), size_hint_y=None, height=45)
        email_layout.add_widget(self.email_input)
        
        layout.add_widget(email_layout)
        
    # Layout para Senha  
        senha_layout = BoxLayout(orientation='vertical', spacing=30, padding=(0, 0, 0, 60))  # Adicionamos margem inferior de 20)

        senha_label = Label(text="[color=000000]SENHA:[/color]",
                            font_size=26,
                            markup=True)
        senha_layout.add_widget(senha_label)

        self.senha_input = TextInput(hint_text="Senha", background_color=(0.7, 0.87, 0.38, 1), size_hint_y=None, height=45,
        password=True,          # Habilita o modo senha
                                password_mask='*')      # Define o asterisco como máscara
        senha_layout.add_widget(self.senha_input)
        
        layout.add_widget(senha_layout)

        # Botão "Atualizar Conta"
        btn5 = Button(text="[color=000000]FINALIZAR CADASTRO[/color]", background_color=(0.7, 0.87, 0.38, 1), size_hint=(None, None), size=(450, 75), markup=True)
        btn5.bind(on_release=self.register)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.background_normal = ''  # Removemos o fundo padrão do botão
        with btn5.canvas.before:

            self.rect = Rectangle(pos=btn5.pos, size=btn5.size)
        layout.add_widget(btn5)
        
        # Botão "Upload da Foto do Usuário"
        btn6 = Button(text="[color=000000]UPLOAD DA FOTO DO USUÁRIO[/color]", background_color=(0.7, 0.87, 0.38, 1), size_hint=(None, None), size=(450, 75), markup=True)
        btn6.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn6.background_normal = ''  # Removemos o fundo padrão do botão
        with btn6.canvas.before:
            self.rect = Rectangle(pos=btn6.pos, size=btn6.size)
        layout.add_widget(btn6)
        

        self.add_widget(layout)  
    def trocar_para_tela_secretaria(self, instance):
        self.manager.current = 'secretaria'
    def register(self, *params):
        try:
            email = str(self.email_input.text)
            password = self.senha_input.text
            name = self.name_input.text
            user = auth_admin.create_user(email=email, password=password, display_name=name)

            if email.split("@")[0].endswith(".prof"):
                auth_admin.set_custom_user_claims(user.uid, {"role": "teacher"})
            elif email.split("@")[0].endswith(".alu"):
                auth_admin.set_custom_user_claims(user.uid, {"role": "student"})

            self.manager.current = 'secretaria'
            print(user)
        except:
            print("ERROR: CRIAR USUÁRIO")
             
class ConteudoScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(ConteudoScreen, self).__init__(**kwargs)   
        
        layout = FloatLayout()
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        # Botão Voltar
        back_button = Button(text="",
                             font_size=20,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_contaProf)  # Associar a ação ao botão
        voltar_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint_y=None, height=1430)
        voltar_layout.add_widget(back_button)
        top_button_layout.add_widget(voltar_layout)

        layout.add_widget(top_button_layout)
        
        #titulo Conteudo
        title_label = Label(text="[color=000000]Conteúdo[/color]",
                            font_size=40,
                            size_hint_y=None,
                            height=2750,
                            markup=True)
        layout.add_widget(title_label)
        
        # Botao e label "atividade avaliativa" 
        btn1 = Button(text="", 
        background_normal="Icone.png",
        background_down="transparent.png",
        border=(0,0,0,0),
        size_hint=(None, None), 
        size=(150, 160), 
        markup=True,
        pos=(70, 900))
        btn1.pos_hint = {'center_x': 0.3}  # Centralize o botão horizontalmente
        btn1.bind(on_release=self.trocar_para_tela_AtividadeA)  # Associar a ação ao botão
        layout.add_widget(btn1)
       
       # Botao e label "palavras cruzadas"
        btn2 = Button(text="", 
              background_normal="Pc-imagem.png",
              background_down="transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(150, 160), #tamanho
              markup=True,
              pos=(70, 670))#posicao
        btn2.pos_hint = {'center_x': 0.3}  # Centralize o botão horizontalmente
        btn2.bind(on_release=self.trocar_para_tela_PalavraCruzada)  # Associar a ação ao botão
        layout.add_widget(btn2)
        
       
       # Botao e label "quebra cabeça"
        btn3 = Button(text="", 
              background_normal="quebra-cabeca.png",
              background_down="transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(150, 160), 
              markup=True,
              pos=(70, 670))#posicao
        btn3.pos_hint = {'center_x': 0.7}  # Centralize o botão horizontalmente
        btn3.bind(on_release=self.trocar_para_tela_QuebraCabeca)  # Associar a ação ao botão
        layout.add_widget(btn3)
        

        
        # Botao e label "matematica"
        btn4 = Button(text="", 
              background_normal="Matematica.png",
              background_down="transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(150, 160), #tamanho
              markup=True,
              pos=(240, 900))#posicao
        btn4.pos_hint = {'center_x': 0.7}  # Centralize o botão horizontalmente
        btn4.bind(on_release=self.trocar_para_tela_Matematica)  # Associar a ação ao botão
        layout.add_widget(btn4)
        
        
        # Botao e label "pintura"
        btn5 = Button(text="", 
              background_normal="Pinturap.png",  
              background_down="transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(150, 160), #tamanho
              markup=True,
              pos=(240, 470))#posicao
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.bind(on_release=self.trocar_para_tela_Pintura)  # Associar a ação ao botão
        layout.add_widget(btn5)

        
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
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(QuebraCabecaScreen, self).__init__(**kwargs)  
         
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="FundoQC.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Quebra cabeça[/color]",
                            font_size=40,
                            size_hint_y=None,
                            height=2750,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_Conteudo)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Imagem no canto superior direito
        image = Image(source="quebra-cabeca.png",
                size_hint=(None, None),
                size=(85, 85))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=1400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        

       # Botão "Upload"
        brn3 = Button(text="[color=000000]Fazer upload de\nimagem[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(350, 75), 
              markup=True,
              pos=(150, 220))
        brn3.bind(on_release=self.file_chooser_upload)  # Associar a ação ao botão
        brn3.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(brn3)
        
        # Botão "Imprimir"
        brn3 = Button(text="[color=000000]Pronto para imprimir[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(350, 75), 
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
    def file_chooser_upload(self, *params):
        def on_select_path(path):
            if path == None: return
            
            quebra_cabeca_criar_screen = self.manager.get_screen("QuebraCabecaCriar")
            quebra_cabeca_criar_screen.upload_image_path = path
            quebra_cabeca_criar_screen.__init__()

            self.manager.current = quebra_cabeca_criar_screen.name 
        
        app = MDApp.get_running_app()
        app.on_select_path = on_select_path
        app.file_manager_open() 

class QuebraCabecaCriarScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    upload_image_path = StringProperty()
    def __init__(self, **kwargs):
        super(QuebraCabecaCriarScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="FundoQC.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Quebra cabeça[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=2750,
                            markup=True)
        layout.add_widget(title_label)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_QuebraCabeca)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Layout para imagem central
        img_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        image = Image(source=self.upload_image_path,
                size_hint=(None, None),
                size=(400, 400))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=1200)
        anchor_layout.add_widget(image)
        img_layout.add_widget(anchor_layout)

        layout.add_widget(img_layout)
        
        
        # Botão "Upload"
        btn5 = Button(text="[color=000000]Upload[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(350, 75), 
              markup=True,
              pos=(150, 150))
        btn5.bind(on_release=self.upload)
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
         
        self.add_widget(layout) 
    def trocar_para_tela_QuebraCabecaCriar(self, instance):
        self.manager.current = 'QuebraCabecaCriar'
    def trocar_para_tela_QuebraCabeca(self, instance):
        self.manager.current = 'QuebraCabeca'
    def upload(self, *params):
        try:
            bucket = storage_admin.bucket()
            
            blob = bucket.blob(f"puzzle/upload/{int(time.time())}_{path.basename(self.upload_image_path)}")
            blob.upload_from_filename(self.upload_image_path)

            blob.make_public()

            print("URL:", blob.public_url)

            db.collection("tasks").add({
                "image": blob.public_url,
                "teacher": auth.current_user["localId"],
                "type": "puzzle"
            })

            screen = self.manager.get_screen("escolher")
            screen.__init__()

            self.manager.current = "conteudo"


        except:
            print("ERROR: UPLOAD IMAGEM")    
        
class QuebraCabecaImprimirScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(QuebraCabecaImprimirScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="FundoQC.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Quebra cabeça[/color]",
                            font_size=50,
                            size_hint_y=None,
                            height=2000,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "logo"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_QuebraCabeca)  # Associar a ação ao botão
        layout.add_widget(back_button)
        

        # Imagem no canto superior direito
        image = Image(source="quebra-cabeca.png",
                size_hint=(None, None),
                size=(85, 85))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=1400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

        # Layout para Texto introdutorio
        text_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        font_name_cg = Label(text="[color=000000]Estão disponiveis dois\ntipos de modelos de\nquebra-cabeça para a\nimpressão: Meio a meio\ne o quebra-cabeça.[/color]",
                            font_size=40,
                            markup=True)
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=1100)
        anchor_layout.add_widget(font_name_cg)
        text_layout.add_widget(anchor_layout)
        
        
        layout.add_widget(text_layout)
        


       # Botão "Acessar"
        btn5 = Button(text="[color=000000]ACESSAR[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(350, 75), 
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
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(QuebraCabecaEscolherScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="FundoQC.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título facil
        title_label1 = Label(text="[color=000000]Meio a meio[/color]",
                            font_size=40,
                            size_hint_y=None,
                            height=2100,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título medio
        title_label1 = Label(text="[color=000000]Quebra-Cabeça[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1300,
                            markup=True)
        layout.add_widget(title_label1)
        
         # Layout superior para os botões "Voltar" 
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_QuebraCabecaImprimir)  # Associar a ação ao botão
        layout.add_widget(back_button)


       # Botões "Escolher"
        brn1 = Button(text="", 
              background_normal="meio1.jpeg", 
              background_down="transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(440, 850))#posicao
        brn1.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(brn1)
       
        brn2 = Button(text="", 
              background_normal="quebra1.jpeg", 
              background_down="transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(440, 470))#posicao
        brn2.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(brn2)
       
        brn3 = Button(text="", 
              background_normal="quebra2.jpeg", 
              background_down="transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(200, 850))
        brn3.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(brn3)

        btn4 = Button(text="", 
              background_normal="meio2.jpeg",
              background_down="transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(200, 470))#posicao
        btn4.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(btn4)
        
        self.add_widget(layout) 
    def trocar_para_tela_QuebraCabecaEscolher(self, instance):
        self.manager.current = 'QuebraCabecaEscolher' 
    def trocar_para_tela_QuebraCabecaImprimir(self, instance):
        self.manager.current = 'QuebraCabecaImprimir' 
    def trocar_para_tela_LicaoEscolhidaMat(self, instance):
        licao_escolhida_screen = self.manager.get_screen("licaoEscolhidaMat")
        licao_escolhida_screen.image_path = instance.background_normal
        licao_escolhida_screen.type = "puzzle"

        licao_escolhida_screen.__init__()

        self.manager.current = licao_escolhida_screen.name   
class LicaoEscolhidaMatScreen(Screen):
    image_path = StringProperty()
    type = StringProperty()
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(LicaoEscolhidaMatScreen, self).__init__(**kwargs) 
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)
 
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
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
        licao_button = Button(text="", 
                              background_normal=self.image_path,
                              background_down="transparent.png",
                          
                              border=(0,0,0,0),
                              size_hint=(None, None),
                              size=(450, 700))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=1700)
        anchor_layout.add_widget(licao_button)
        layout.add_widget(anchor_layout)
        
        
        #Botão "download"
        btn5 = Button(text="[color=000000]Download[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(240, 75), 
              markup=True,
              pos=(150, 270))
        btn5.bind(on_release=self.download)
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        layout.add_widget(btn5)
        
       # Botão "Proximo"
        btn5 = Button(text="[color=000000]Proximo[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(240, 75), 
              markup=True,
              pos=(150, 160))
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
        licao_postada_screen = self.manager.get_screen("licaoPostada")
        licao_postada_screen.image_path = self.image_path
        licao_postada_screen.type = self.type
        licao_postada_screen.__init__()

        self.manager.current = licao_postada_screen.name
    def download(self, instance):
        try:
            shutil.copy(self.image_path, f"/storage/emulated/0/Download/{int(time.time())}_{self.image_path}")
        except:
            print("ERROR: DOWNLOAD")
class AtividadeAScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(AtividadeAScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="FundoA.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Atividade\nAvaliativa[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=2750,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_conteudo)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Imagem no canto superior direito
        image = Image(source="Icone.png",
                size_hint=(None, None),
                size=(55, 55))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None,  height=1400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        

       # Botão "Upload"
        brn3 = Button(text="[color=000000]Fazer upload de\nimagem[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#77C4FF"), 
              size_hint=(None, None), 
              size=(350, 75), 
              markup=True,
              pos=(150, 220))
        brn3.bind(on_release=self.file_chooser_upload)  # Associar a ação ao botão
        brn3.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(brn3)
        
        self.add_widget(layout) 
    def trocar_para_tela_AtividadeA(self, instance):
        self.manager.current = 'AtividadeA' 
    def trocar_para_tela_conteudo(self, instance):
        self.manager.current = 'conteudo'
    def trocar_para_tela_AtividadeAcriar(self, instance):
        self.manager.current = 'AtividadeAcriar'
    def file_chooser_upload(self, *params):
        def on_select_path(path):
            if path == None: return
            
            atividade_a_criar_screen = self.manager.get_screen("AtividadeAcriar")
            atividade_a_criar_screen.upload_image_path = path
            atividade_a_criar_screen.__init__()

            self.manager.current = atividade_a_criar_screen.name   
        
        app = MDApp.get_running_app()
        app.on_select_path = on_select_path
        app.file_manager_open()

class AtividadeAcriarScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    upload_image_path = StringProperty()
    def __init__(self, **kwargs):
        super(AtividadeAcriarScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="FundoA.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Atividade\nAvaliativa[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=2750,
                            markup=True)
        layout.add_widget(title_label)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_AtividadeA)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Layout para imagem central
        img_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        image = Image(source=self.upload_image_path,
                size_hint=(None, None),
                size=(400, 400))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=1200)
        anchor_layout.add_widget(image)
        img_layout.add_widget(anchor_layout)

        layout.add_widget(img_layout)
        
        
        # Botão "Upload"
        btn5 = Button(text="[color=000000]Upload[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#77C4FF"), 
              size_hint=(None, None), 
              size=(350, 75), 
              markup=True,
              pos=(150, 150))
        btn5.bind(on_release=self.upload)
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
        
        self.add_widget(layout) 
    def trocar_para_tela_AtividadeAcriar(self, instance):
        self.manager.current = 'AtividadeAcriar'  
    def trocar_para_tela_AtividadeA(self, instance):
        self.manager.current = 'AtividadeA'

    def upload(self, *params):
        try:
            bucket = storage_admin.bucket()
            
            blob = bucket.blob(f"exam/upload/{int(time.time())}_{path.basename(self.upload_image_path)}")
            blob.upload_from_filename(self.upload_image_path)

            blob.make_public()

            print("URL:", blob.public_url)

            db.collection("tasks").add({
                "image": blob.public_url,
                "teacher": auth.current_user["localId"],
                "type": "exam"
            })

            screen = self.manager.get_screen("escolher")
            screen.__init__()

            self.manager.current = "conteudo"


        except:
            print("ERROR: UPLOAD IMAGEM")
        
class MatematicaScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(MatematicaScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="FundoM.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Matemática[/color]",
                            font_size=40,
                            size_hint_y=None,
                            height=2750,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_conteudo)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Imagem no canto superior direito
        image = Image(source="Matematica.png",
                size_hint=(None, None),
                size=(85, 85))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=1400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        

       # Botão "Upload"
        brn3 = Button(text="[color=000000]Fazer upload de\nimagem[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(350, 75), 
              markup=True,
              pos=(150, 220))
        brn3.bind(on_release=self.file_chooser_upload)  # Associar a ação ao botão
        brn3.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(brn3)
        
        # Botão "Imprimir"
        brn3 = Button(text="[color=000000]Pronto para imprimir[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(350, 75), 
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
    def file_chooser_upload(self, *params):  
        def on_select_path(path):
            if path == None: return

            matematica_criar_screen = self.manager.get_screen("MatematicaCriar")
            matematica_criar_screen.upload_image_path = path
            matematica_criar_screen.__init__()

            self.manager.current = matematica_criar_screen.name
        
        app = MDApp.get_running_app()
        app.on_select_path = on_select_path
        app.file_manager_open()

     
class MatematicaCriarScreen(Screen):
    upload_image_path = StringProperty()
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(MatematicaCriarScreen, self).__init__(**kwargs)        
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="FundoM.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Matemática[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=2750,
                            markup=True)
        layout.add_widget(title_label)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_Matematica)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Layout para imagem central
        img_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        image = Image(source=self.upload_image_path,
                size_hint=(None, None),
                size=(400, 400))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=1200)
        anchor_layout.add_widget(image)
        img_layout.add_widget(anchor_layout)

        layout.add_widget(img_layout)
        
        
        # Botão "Upload"
        btn5 = Button(text="[color=000000]Upload[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(350, 75), 
              markup=True,
              pos=(150, 150))
        btn5.bind(on_release=self.upload)
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
        
        self.add_widget(layout) 
    def trocar_para_tela_MatematicaCriar(self, instance):
        self.manager.current = 'MatematicaCriar'
    def trocar_para_tela_Matematica(self, instance):
        self.manager.current = 'Matematica'
    def upload(self, *params):
        try:
            bucket = storage_admin.bucket()
            
            blob = bucket.blob(f"math/upload/{int(time.time())}_{path.basename(self.upload_image_path)}")
            blob.upload_from_filename(self.upload_image_path)

            blob.make_public()

            print("URL:", blob.public_url)

            db.collection("tasks").add({
                "image": blob.public_url,
                "teacher": auth.current_user["localId"],
                "type": "math"
            })

            screen = self.manager.get_screen("escolher")
            screen.__init__()

            self.manager.current = "conteudo"


        except:
            print("ERROR: UPLOAD IMAGEM")
        
class MatematicaImprimirScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(MatematicaImprimirScreen, self).__init__(**kwargs)   
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="FundoM.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Matemática[/color]",
                            font_size=50,
                            size_hint_y=None,
                            height=2000,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "logo"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_Matematica)  # Associar a ação ao botão
        layout.add_widget(back_button)
        

        # Imagem no canto superior direito
        image = Image(source="Matematica.png",
                size_hint=(None, None),
                size=(85, 85))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=1400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

        # Layout para Texto introdutorio
        text_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        font_name_cg = Label(text="[color=000000]Estão disponiveis\nquatro sessões sobre\nmatemática para a\nimpressão: 1 sessão -\nadição e subtração, 2ª\nsessão - multiplicação\ne divisão.[/color]",
                            font_size=40,
                            markup=True)
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=1100)
        anchor_layout.add_widget(font_name_cg)
        text_layout.add_widget(anchor_layout)
        
        
        layout.add_widget(text_layout)
        


       # Botão "Acessar"
        btn5 = Button(text="[color=000000]ACESSAR[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C985FF"), 
              size_hint=(None, None), 
              size=(350, 75), 
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
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(MatematicaEscolherScreen, self).__init__(**kwargs)     
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="FundoM.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título facil
        title_label1 = Label(text="[color=000000]Meio a meio[/color]",
                            font_size=40,
                            size_hint_y=None,
                            height=2100,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título medio
        title_label1 = Label(text="[color=000000]Quebra-Cabeça[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1300,
                            markup=True)
        layout.add_widget(title_label1)
        
         # Layout superior para os botões "Voltar" 
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1350))
        back_button.bind(on_release=self.trocar_para_tela_MatematicaImprimir)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
       # Botões "Escolher"
        btn1 = Button(text="", 
              background_normal="meio1.jpeg", 
              background_down="transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(440, 850))#posicao
        btn1.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        btn1.pos_hint = {'center_x': 0.3}  # Centralize o botão horizontalmente
        layout.add_widget(btn1)
       
        btn2 = Button(text="", 
              background_normal="quebra1.jpeg", 
              background_down="transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(440, 470))#posicao
        btn2.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        btn2.pos_hint = {'center_x': 0.3}  # Centralize o botão horizontalmente
        layout.add_widget(btn2)
       
        btn3 = Button(text="", 
              background_normal="quebra2.jpeg", 
              background_down="transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(200, 850))
        btn3.pos_hint = {'center_x': 0.7}  # Centralize o botão horizontalmente
        btn3.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        layout.add_widget(btn3)

        btn4 = Button(text="", 
              background_normal="meio2.jpeg",
              background_down="transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(200, 470))#posicao
        btn4.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        btn4.pos_hint = {'center_x': 0.7}  # Centralize o botão horizontalmente
        layout.add_widget(btn4)
        
        self.add_widget(layout) 
    def trocar_para_tela_MatematicaEscolher(self, instance):
        self.manager.current = 'MatematicaEscolher'  
    def trocar_para_tela_LicaoEscolhidaMat(self, instance):
        licao_escolhida_screen = self.manager.get_screen("licaoEscolhidaMat")
        licao_escolhida_screen.image_path = instance.background_normal
        licao_escolhida_screen.type = "math"
        licao_escolhida_screen.__init__()

        self.manager.current = licao_escolhida_screen.name  
    def trocar_para_tela_MatematicaImprimir(self, instance):
        self.manager.current = 'MatematicaImprimir'    
class licaoPostadaScreen(Screen):
    image_path = StringProperty()
    type = StringProperty()
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(licaoPostadaScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)
 
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
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
        licao_button = Button(text="", 
                              background_normal=self.image_path,
                              background_down="transparent.png",
                              
                              border=(0,0,0,0),
                              size_hint=(None, None),
                              size=(450, 700))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=1700)
        anchor_layout.add_widget(licao_button)
        layout.add_widget(anchor_layout)
        
        
        #Botão "download"
        btn5 = Button(text="[color=000000]Postar[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(240, 75), 
              markup=True,
              pos=(150, 270))
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.bind(on_release=self.post)
        layout.add_widget(btn5)
        
        self.add_widget(layout) 
    def trocar_para_tela_licaoPostada(self, instance):
        self.manager.current = 'licaoPostada'
    def trocar_para_tela_licaoEscolhidaMat(self, instance):
        self.manager.current = 'licaoEscolhidaMat' 
    def post(self, *params):
        try:
            bucket = storage_admin.bucket()
            
            blob = bucket.blob(f"{self.type}/ready/{int(time.time())}_{path.basename(self.image_path)}")
            blob.upload_from_filename(self.image_path)

            blob.make_public()

            print("URL:", blob.public_url)

            db.collection("tasks").add({
                "image": blob.public_url,
                "teacher": auth.current_user["localId"],
                "type": self.type
            })

            screen = self.manager.get_screen("escolher")
            screen.__init__()

            self.manager.current = "conteudo"
        except:
            print("ERROR: UPLOAD IMAGEM")
        
class PalavraCruzadaScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(PalavraCruzadaScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="FundoPC.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Palavras\nCruzadas[/color]",
                            font_size=40,
                            size_hint_y=None,
                            height=2750,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_conteudo)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Imagem no canto superior direito
        image = Image(source="Pc-imagem.png",
                size_hint=(None, None),
                size=(85, 85))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=1400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        

       # Botão "Upload"
        brn3 = Button(text="[color=000000]Fazer upload de\nimagem[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(350, 75), 
              markup=True,
              pos=(150, 220))
        brn3.bind(on_release=self.file_chooser_upload)  # Associar a ação ao botão
        brn3.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(brn3)
        
        # Botão "Imprimir"
        brn3 = Button(text="[color=000000]Pronto para imprimir[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(350, 75), 
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
    def file_chooser_upload(self, *params):     
        def on_select_path(path):
            if path == None: return
            
            palavra_cruzada_criar_screen = self.manager.get_screen("PalavraCruzadaCriar")
            palavra_cruzada_criar_screen.upload_image_path = path
            palavra_cruzada_criar_screen.__init__()

            self.manager.current = palavra_cruzada_criar_screen.name 
        
        app = MDApp.get_running_app()
        app.on_select_path = on_select_path
        app.file_manager_open()
   
class PalavraCruzadaCriarScreen(Screen):
    upload_image_path = StringProperty()
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(PalavraCruzadaCriarScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        
        # Imagem de fundo 
        background_image = Image(source="FundoPC.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Palavras\nCruzadas[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=2750,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_PalavraCruzada)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Layout para imagem central
        img_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        image = Image(source=self.upload_image_path,
                size_hint=(None, None),
                size=(400, 400))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=1200)
        anchor_layout.add_widget(image)
        img_layout.add_widget(anchor_layout)

        layout.add_widget(img_layout)
        
        
        # Botão "Upload"
        btn5 = Button(text="[color=000000]Upload[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(350, 75), 
              markup=True,
              pos=(150, 150))
        btn5.bind(on_release=self.upload)
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
        
        self.add_widget(layout) 
    def trocar_para_tela_PalavraCruzadaCriar(self, instance):
        self.manager.current = 'PalavraCruzadaCriar'
    def trocar_para_tela_PalavraCruzada(self, instance):
        self.manager.current = 'PalavraCruzada'
    def upload(self, *params):
        try:
            bucket = storage_admin.bucket()
            
            blob = bucket.blob(f"crossword/upload/{int(time.time())}_{path.basename(self.upload_image_path)}")
            blob.upload_from_filename(self.upload_image_path)

            blob.make_public()

            print("URL:", blob.public_url)

            db.collection("tasks").add({
                "image": blob.public_url,
                "teacher": auth.current_user["localId"],
                "type": "crossword"
            })

            screen = self.manager.get_screen("escolher")
            screen.__init__()

            self.manager.current = "conteudo"


        except:
            print("ERROR: UPLOAD IMAGEM")
    
        
class PalavraCruzadaImprimirScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(PalavraCruzadaImprimirScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="FundoPC.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Palavras\nCruzadas[/color]",
                            font_size=50,
                            size_hint_y=None,
                            height=2200,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_PalavraCruzada)  # Associar a ação ao botão
        layout.add_widget(back_button)
        

        # Imagem no canto superior direito
        image = Image(source="Pc-imagem.png",
                size_hint=(None, None),
                size=(85, 85))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=1400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

        # Layout para Texto introdutorio
        text_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        name_label = Label(text="[color=000000]Estão disponiveis três\nníveis de palavras\ncruzadas para a\nimpressão: nível fácil\n(1 a 5 palavras), nível\nmédio (de 5 a 10\npalavras), e o nível\ndifícil (contendo mais\nde 10 palavras).[/color]",
                            font_size=40,
                            markup=True)
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=1100)
        anchor_layout.add_widget(name_label)
        text_layout.add_widget(anchor_layout)
        
        
        layout.add_widget(text_layout)
        


       # Botão "Acessar"
        btn5 = Button(text="[color=000000]ACESSAR[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("#C3FF93"), 
              size_hint=(None, None), 
              size=(350, 75), 
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
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(PalavraCruzadaEscolherScreen, self).__init__(**kwargs) 
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="FundoPC.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título facil
        title_label1 = Label(text="[color=000000]Fácil[/color]",
                            font_size=40,
                            size_hint_y=None,
                            height=2400,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título medio
        title_label1 = Label(text="[color=000000]Médio[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1600,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título dificil
        title_label1 = Label(text="[color=000000]Dificil[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=700,
                            markup=True)
        layout.add_widget(title_label1)
        
         # Layout superior para os botões "Voltar" 
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_PalavraCruzadaImprimir)  # Associar a ação ao botão
        layout.add_widget(back_button)


       # Botões "Escolher"
        btn1 = Button(text="", 
              background_normal="facil1.jpg", 
              background_down="transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(440, 950))#posicao
        btn1.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        btn1.pos_hint = {'center_x': 0.3}  # Centralize o botão horizontalmente
        layout.add_widget(btn1)
       
        btn2 = Button(text="", 
              background_normal="medio1.jpg",
              background_down="transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(440, 550))#posicao
        btn2.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        btn2.pos_hint = {'center_x': 0.3}  # Centralize o botão horizontalmente
        layout.add_widget(btn2)
       
        btn3 = Button(text="", 
              background_normal="dificil1.jpg",
              background_down="transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(70, 90))
        btn3.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        btn3.pos_hint = {'center_x': 0.3}  # Centralize o botão horizontalmente
        layout.add_widget(btn3)

        btn4 = Button(text="", 
              background_normal="facil2.jpg",
              background_down="transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(200, 950))#posicao
        btn4.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        btn4.pos_hint = {'center_x': 0.7}  # Centralize o botão horizontalmente
        layout.add_widget(btn4)
       
        btn5 = Button(text="", 
              background_normal="medio2.jpg",
              background_down="transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(200, 550))#posicao
        btn5.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.7}  # Centralize o botão horizontalmente
        layout.add_widget(btn5)
       
        btn6 = Button(text="", 
              background_normal="dificil2.jpg",
              background_down="transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(240, 90))
        btn6.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        btn6.pos_hint = {'center_x': 0.7}  # Centralize o botão horizontalmente
        layout.add_widget(btn6)
        
        self.add_widget(layout) 
    def trocar_para_tela_PalavraCruzadaEscolher(self, instance):
        self.manager.current = 'PalavraCruzadaEscolher' 
    def trocar_para_tela_PalavraCruzadaImprimir(self, instance):
        self.manager.current = 'PalavraCruzadaImprimir'
    def trocar_para_tela_LicaoEscolhidaMat(self, instance):
        licao_escolhida_screen = self.manager.get_screen("licaoEscolhidaMat")
        licao_escolhida_screen.image_path = instance.background_normal
        licao_escolhida_screen.type = "crossword"
        licao_escolhida_screen.__init__()

        self.manager.current = licao_escolhida_screen.name 
        
class PinturaScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(PinturaScreen, self).__init__(**kwargs)  
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="fundoP.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Pintura[/color]",
                            font_size=40,
                            size_hint_y=None,
                            height=2750,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_conteudo)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Imagem no canto superior direito
        image = Image(source="pinturap.png",
                size_hint=(None, None),
                size=(85, 85))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=1400)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)
        

       # Botão "Upload"
        brn3 = Button(text="[color=000000]Fazer upload de\nimagem[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("77C4FF"), 
              size_hint=(None, None), 
              size=(350, 75), 
              markup=True,
              pos=(150, 220))
        brn3.bind(on_release=self.file_chooser_upload)  # Associar a ação ao botão
        brn3.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(brn3)
        
        # Botão "Imprimir"
        brn3 = Button(text="[color=000000]Pronto para imprimir[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("77C4FF"), 
              size_hint=(None, None), 
              size=(350, 75), 
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
    def file_chooser_upload(self, *params):
        def on_select_path(path):
            if path == None: return
            
            pintura_criar_screen = self.manager.get_screen("PinturaCriar")
            pintura_criar_screen.upload_image_path = path
            pintura_criar_screen.__init__()

            self.manager.current = pintura_criar_screen.name
        
        app = MDApp.get_running_app()
        app.on_select_path = on_select_path
        app.file_manager_open()
class PinturaCriarScreen(Screen):
    upload_image_path = StringProperty()
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(PinturaCriarScreen, self).__init__(**kwargs)   
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="fundoP.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Pintura[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=2750,
                            markup=True)
        layout.add_widget(title_label)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_Pintura)  # Associar a ação ao botão
        layout.add_widget(back_button)
        
        # Layout para imagem central
        img_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        image = Image(source=self.upload_image_path,
                size_hint=(None, None),
                size=(400, 400))
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=1200)
        anchor_layout.add_widget(image)
        img_layout.add_widget(anchor_layout)

        layout.add_widget(img_layout)
        
        
        # Botão "Upload"
        btn5 = Button(text="[color=000000]Upload[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("77C4FF"), 
              size_hint=(None, None), 
              size=(350, 75), 
              markup=True,
              pos=(150, 150))
        btn5.bind(on_release=self.upload)
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(btn5)
        
        self.add_widget(layout) 
    def trocar_para_tela_PinturaCriar(self, instance):
        self.manager.current = 'PinturaCriar' 
    def trocar_para_tela_Pintura(self, instance):
        self.manager.current = 'Pintura'
    def upload(self, *params):
        try:
            bucket = storage_admin.bucket()
            
            blob = bucket.blob(f"paint/upload/{int(time.time())}_{path.basename(self.upload_image_path)}")
            blob.upload_from_filename(self.upload_image_path)

            blob.make_public()

            print("URL:", blob.public_url)

            db.collection("tasks").add({
                "image": blob.public_url,
                "teacher": auth.current_user["localId"],
                "type": "paint"
            })

            screen = self.manager.get_screen("escolher")
            screen.__init__()

            self.manager.current = "conteudo"


        except:
            print("ERROR: UPLOAD IMAGEM")
        
class PinturaImprimirScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(PinturaImprimirScreen, self).__init__(**kwargs)    
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="fundoP.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]Pintura[/color]",
                            font_size=50,
                            size_hint_y=None,
                            height=2000,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "logo"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_Pintura)  # Associar a ação ao botão
        layout.add_widget(back_button)
        

        # Imagem no canto superior direito
        image = Image(source="pinturap.png",
                size_hint=(None, None),
                size=(85, 85))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=1410)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)

        # Layout para Texto introdutorio
        text_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 220))  # Adicionamos margem inferior de 170
        
        font_name_cg = Label(text="[color=000000]Estão disponiveis três\ntipos de modelos de\npintura para a\nimpressão: Animais,\nAlimentos e sobre as\ncores.[/color]",
                            font_size=40,
                            markup=True)
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=1100)
        anchor_layout.add_widget(font_name_cg)
        text_layout.add_widget(anchor_layout)
        
        
        layout.add_widget(text_layout)
        


       # Botão "Acessar"
        btn5 = Button(text="[color=000000]ACESSAR[/color]", 
              background_normal="",  # Remova o fundo padrão
              background_color=("77C4FF"), 
              size_hint=(None, None), 
              size=(350, 75), 
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
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(PinturaEscolherScreen, self).__init__(**kwargs)    
        layout = FloatLayout()
        
        # Imagem de fundo
        background_image = Image(source="fundoP.png", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background_image)

        
          # Título Animais
        title_label1 = Label(text="[color=000000]Animais[/color]",
                            font_size=40,
                            size_hint_y=None,
                            height=2400,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título Alimentos
        title_label1 = Label(text="[color=000000]Alimentos[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=1600,
                            markup=True)
        layout.add_widget(title_label1)
        
          # Título Cores
        title_label1 = Label(text="[color=000000]Cores[/color]",
                            font_size=32,
                            size_hint_y=None,
                            height=700,
                            markup=True)
        layout.add_widget(title_label1)
        
         # Layout superior para os botões "Voltar" 
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                             font_size=7,
                             background_normal="voltar.png",
                             background_down="transparent.png",
                             border=(0,0,0,0),
                             size_hint=(None, None),
                             size=(85, 85),
                             pos=(3.5, 1310))
        back_button.bind(on_release=self.trocar_para_tela_PinturaImprimir)  # Associar a ação ao botão
        layout.add_widget(back_button)


# Botões "Escolher"
        brn1 = Button(text="", 
              background_normal="animal1.jpeg", 
              background_down="transparent.png",
              border=(0,0,0,0),
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(440, 950))#posicao
        brn1.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        brn1.pos_hint = {'center_x': 0.3}  # Centralize o botão horizontalmente
        layout.add_widget(brn1)
       
        brn2 = Button(text="", 
              background_normal="alimento1.jpeg",
              background_down="transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(440, 550))#posicao
        brn2.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        brn2.pos_hint = {'center_x': 0.3}  # Centralize o botão horizontalmente
        layout.add_widget(brn2)
       
        brn3 = Button(text="", 
              background_normal="cores1.jpeg",
              background_down="transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(70, 90))
        brn3.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        brn3.pos_hint = {'center_x': 0.3}  # Centralize o botão horizontalmente
        layout.add_widget(brn3)

        btn4 = Button(text="", 
              background_normal="animal2.jpeg",
              background_down="transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(200, 950))#posicao
        btn4.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        btn4.pos_hint = {'center_x': 0.7}  # Centralize o botão horizontalmente
        layout.add_widget(btn4)
       
        btn5 = Button(text="", 
              background_normal="alimento2.jpeg",
              background_down="transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(200, 550))#posicao
        btn5.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.7}  # Centralize o botão horizontalmente
        layout.add_widget(btn5)
       
        btn6 = Button(text="", 
              background_normal="cores2.jpeg",
              background_down="transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(240, 90))
        btn6.bind(on_release=self.trocar_para_tela_LicaoEscolhidaMat)  # Associar a ação ao botão
        btn6.pos_hint = {'center_x': 0.7}  # Centralize o botão horizontalmente
        layout.add_widget(btn6)
        
        self.add_widget(layout) 
    def trocar_para_tela_PinturaEscolher(self, instance):
        self.manager.current = 'PinturaEscolher' 
    def trocar_para_tela_PinturaImprimir(self, instance):
        self.manager.current = 'PinturaImprimir' 
    def trocar_para_tela_LicaoEscolhidaMat(self, instance):
        licao_escolhida_screen = self.manager.get_screen("licaoEscolhidaMat")
        licao_escolhida_screen.image_path = instance.background_normal
        licao_escolhida_screen.type = "paint"

        licao_escolhida_screen.__init__()

        self.manager.current = licao_escolhida_screen.name   
        
class atzContaScreen(Screen):
    def on_enter(self):
        print("DEBUG-SCREEN: ", self.__class__.__name__)
    def __init__(self, **kwargs):
        super(atzContaScreen, self).__init__(**kwargs)   
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.5}  # Define o topo do layout na parte superior da tela
        
        # Título (no topo do layout)
        title_label = Label(text="[color=000000]Secretaria[/color]",
                            font_size=40,
                            size_hint_y=None,
                            height=1200,
                            markup=True)
        layout.add_widget(title_label)
        
        # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        
        # Botão Voltar
        back_button = Button(text="",
                    font_size=7,
                    background_normal="voltar.png",
                    background_down="transparent.png",
                    border=(0,0,0,0),
                    size_hint=(None, None),
                    size=(80, 80),
                    pos_hint={'x': 0, 'top': 14})  # Posiciona no canto superior esquerdo
        back_button.bind(on_release=self.trocar_para_tela_listagem)  # Associar a ação ao botão
        top_button_layout.add_widget(back_button)

        

    # Imagem no canto superior direito
        image = Image(source="Imagem2.png",
            size_hint=(None, None),
            size=(80, 80))
        anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=700)
        anchor_layout.add_widget(image)
        top_button_layout.add_widget(anchor_layout)

        layout.add_widget(top_button_layout)


        # Campos de entrada
        input_layout = GridLayout(cols=2, spacing=150, size_hint_y=None, height=15, pos_hint={'x': 0.5})

        # Layout para Nome Completo
        name_layout = BoxLayout(orientation='vertical', spacing=30, padding=(0, 0, 0, 205))  # Adicionamos margem inferior de 170
        
        name_label = Label(text="[color=000000]NOME COMPLETO:[/color]",
                            font_size=26,
                            markup=True)
        name_layout.add_widget(name_label)
        

        name_input = TextInput(hint_text="Nome Completo", background_color=(0.7, 0.87, 0.38, 1), size_hint_y=None, height=45)
        name_layout.add_widget(name_input)
        
        layout.add_widget(name_layout)

        # Layout para Email
        email_layout = BoxLayout(orientation='vertical', spacing=25, padding=(0, 0, 0, 132))  # Adicionamos margem inferior de 20)

        email_label = Label(text="[color=000000]EMAIL:[/color]",
                            font_size=26,
                            markup=True)
        email_layout.add_widget(email_label)

        email_input = TextInput(hint_text="Email", background_color=(0.7, 0.87, 0.38, 1), size_hint_y=None, height=40)
        email_layout.add_widget(email_input)
        
        layout.add_widget(email_layout)
        
    # Layout para Senha  
        senha_layout = BoxLayout(orientation='vertical', spacing=25, padding=(0, 0, 0, 60))  # Adicionamos margem inferior de 20)

        senha_label = Label(text="[color=000000]SENHA:[/color]",
                            font_size=26,
                            markup=True)
        senha_layout.add_widget(senha_label)

        senha_input = TextInput(hint_text="Senha", background_color=(0.7, 0.87, 0.38, 1), size_hint_y=None, height=40,
        password=True,          # Habilita o modo senha
                                password_mask='*')      # Define o asterisco como máscara
        senha_layout.add_widget(senha_input)
        
        layout.add_widget(senha_layout)

        # Botão "Atualizar Conta"
        btn5 = Button(text="[color=000000]ATUALIZAR CONTA[/color]", background_color=(0.7, 0.87, 0.38, 1), size_hint=(None, None), size=(450, 75), markup=True)
        btn5.bind(on_release=self.trocar_para_tela_secretaria)  # Associar a ação ao botão
        btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn5.background_normal = ''  # Removemos o fundo padrão do botão
        with btn5.canvas.before:

            self.rect = Rectangle(pos=btn5.pos, size=btn5.size)
        layout.add_widget(btn5)
        
        # Botão "Upload da Foto do Usuário"
        btn6 = Button(text="[color=000000]UPLOAD DA FOTO DO USUÁRIO[/color]", background_color=(0.7, 0.87, 0.38, 1), size_hint=(None, None), size=(450, 75), markup=True)
        btn6.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
        btn6.background_normal = ''  # Removemos o fundo padrão do botão
        with btn6.canvas.before:
            self.rect = Rectangle(pos=btn6.pos, size=btn6.size)
        layout.add_widget(btn6)
        
        self.add_widget(layout) 
    def trocar_para_tela_secretaria(self, instance):
        self.manager.current = 'secretaria'   
    def trocar_para_tela_atzConta(self, instance):
        self.manager.current = 'atzConta' 
    def trocar_para_tela_listagem(self, instance):
        self.manager.current = 'listagem'                                                                                                                                      
class LearPlusApp(MDApp):
    def build(self):
        self.sm = ScreenManager()
        
        # Adicione as telas ao gerenciador de telas
        self.sm.add_widget(EntradaScreen(name='entrada'))
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
        self.sm.add_widget(atzContaScreen(name='atzConta'))
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

        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True
        )

        self.on_select_path = lambda: None

        return self.sm
    
    def file_manager_open(self):
        self.file_manager.show('/storage/emulated/0')

    def select_path(self, path):
        self.on_select_path(path)
        self.exit_manager()

    def exit_manager(self, *args):
        self.file_manager.close()

if __name__ == '__main__':
    LearPlusApp().run()
