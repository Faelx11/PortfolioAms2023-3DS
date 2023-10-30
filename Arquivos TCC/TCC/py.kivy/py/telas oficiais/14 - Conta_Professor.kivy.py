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
        brn.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente

        layout.add_widget(brn)

        return layout
if __name__ == '__main__':
    LearPlusApp().run()