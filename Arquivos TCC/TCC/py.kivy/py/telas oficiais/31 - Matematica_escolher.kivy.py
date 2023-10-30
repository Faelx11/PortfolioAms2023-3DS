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
        layout.add_widget(brn1)
       
        brn2 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/×÷/multiplicacao.jpeg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(70, 240))#posicao
        layout.add_widget(brn2)
       
        brn3 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/×÷/divisao.jpeg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), 
              markup=True,
              pos=(240, 240))
        layout.add_widget(brn3)

        btn4 = Button(text="", 
              background_normal="py.kivy/py/img_wireframe/conteudo_img/+-/subtracao.jpeg",
              background_down="py.kivy/py/img_wireframe/transparent.png",
              border=(0,0,0,0), 
              size_hint=(None, None), 
              size=(115, 160), #tamanho
              markup=True,
              pos=(240, 470))#posicao
        layout.add_widget(btn4)

        return layout
        
if __name__ == '__main__':
    LearPlusApp().run()