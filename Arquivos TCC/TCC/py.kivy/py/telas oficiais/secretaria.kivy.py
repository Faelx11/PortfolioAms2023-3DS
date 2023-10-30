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


class LearPlusApp(App):
    def build(self):
        # Defina a cor de fundo
        Window.clearcolor = (240/255, 240/255, 240/255, 1)  # Cor cinza claro (R, G, B, alpha)
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


        return layout
          
if __name__ == '__main__':
      LearPlusApp().run() 