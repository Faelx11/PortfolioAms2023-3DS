from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout


class pcc(App):
    def build(self):
        # Defina a cor de fundo
        Window.clearcolor = (240/255, 240/255, 240/255, 1)  # Cor cinza claro (R, G, B, alpha)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None, height=200)
        layout.pos_hint = {'top': 0.67}  # Define o topo do layout na parte superior da tela
        
          # Título (no topo do layout)
        title_label = Label(text="[color=000000]LOGIN[/color]",
                            font_size=40,
                            size_hint_y=None,
                            height=450,
                            markup=True)
        layout.add_widget(title_label)
        
         # Layout superior para os botões "Voltar" e "Login"
        top_button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
        
        # Botão Voltar
        back_button = Button(text="",
                            font_size=7,
                            background_normal="py.kivy/py/img_wireframe/voltar.png",
                            background_down="py.kivy/py/img_wireframe/transparent.png",
                            size_hint=(None, None),
                            border=(0,0,0,0),
                            size=(55, 55),
                            pos_hint={'x': 0, 'top': 5.3})  # Posiciona no canto superior esquerdo
        voltar_layout = AnchorLayout(anchor_x='left', anchor_y='top', size_hint_y=None, height=320)
        voltar_layout.add_widget(back_button)
        top_button_layout.add_widget(voltar_layout)
        
        layout.add_widget(top_button_layout)
        
 # Campos de entrada
        input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=80, pos_hint={'x': 0})

        # Nome Completo
        name_layout = BoxLayout (orientation='vertical', spacing=8, padding=(0, 0, 0, 160))

        # Nome Completo
        name_label = Label(text="[color=000000]NOME COMPLETO:[/color]",
                            font_size=12,
                            markup=True)
        name_layout.add_widget(name_label)

        name_input = TextInput(hint_text="Nome Completo", background_color=("#77C4FF"),background_normal = '', size_hint_y=None, height=30)
        name_layout.add_widget(name_input)

        layout.add_widget(name_layout)
        
        # Layout para Email
        email_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 100))  # Adicionamos margem inferior de 20)

        email_label = Label(text="[color=000000]EMAIL:[/color]",
                              font_size=12,
                              markup=True)
        email_layout.add_widget(email_label)

        email_input = TextInput(hint_text="Email", background_color=("#77C4FF"),background_normal = '', size_hint_y=None, height=30)
        email_layout.add_widget(email_input)
          
        layout.add_widget(email_layout)
          
        # Layout para Senha  
        senha_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 40))  # Adicionamos margem inferior de 20)

        senha_label = Label(text="[color=000000]SENHA:[/color]",
                              font_size=12,
                              markup=True)
        senha_layout.add_widget(senha_label)

        senha_input = TextInput(hint_text="Senha", background_color=("#77C4FF"),background_normal = '', size_hint_y=None, height=30)
        senha_layout.add_widget(senha_input)
          
        layout.add_widget(senha_layout)

        # Botão "Finalizar Cadastro"
        btn5 = Button(text="[color=000000]REALIZAR LOGIN[/color]", 
                      background_color=("#77C4FF"), 
                      background_down="py.kivy/py/img_wireframe/transparent.png",
                      size_hint=(None, None), 
                      size=(175, 50), 
                      markup=True)
        btn5.pos_hint = {'center_x': 0.5}# Centralize o botão horizontalmente
        btn5.background_normal = ''  # Removemos o fundo padrão do botão
        layout.add_widget(btn5)

        return layout
        
if __name__ == '__main__':
    pcc().run()