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


        return layout
        
if __name__ == '__main__':
    pcc().run()