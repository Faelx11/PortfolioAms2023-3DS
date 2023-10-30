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
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 440))#posicao
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
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 230))#posicao
        layout.add_widget(brn2)
        
        voltar_label = Label(text="[color=000000]Palavras acruzadas[/color]",
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
              size=(115, 160), 
              markup=True,
              pos=(150, 40))
        layout.add_widget(brn3)

        voltar_label = Label(text="[color=000000]Quebra cabeça[/color]",
                            font_size=20,
                            size_hint=(None, None),
                            height=60,
                            width=420,
                            markup=True)
        layout.add_widget(voltar_label)
        
        # Botao e label "matematica"
        btn4 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/ICONS/Matematica/Matematica.png",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(240, 440))#posicao
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
              size=(115, 160), #tamanho
              markup=True,
              pos=(240, 230))#posicao
        layout.add_widget(btn5)
       
        voltar_label = Label(text="[color=000000]Pintura[/color]",
                            font_size=20,
                            size_hint=(None, None),
                            height=430,
                            width=600,
                            markup=True)
        layout.add_widget(voltar_label)
        
        return layout
if __name__ == '__main__':
    LearPlusApp().run()