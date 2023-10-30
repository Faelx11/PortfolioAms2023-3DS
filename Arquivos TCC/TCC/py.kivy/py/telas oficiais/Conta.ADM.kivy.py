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
from kivy.graphics import Color, Rectangle

class LearPlusApp(App):
      def build(self):
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
          btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
          btn5.background_normal = ''  # Removemos o fundo padrão do botão
          with btn5.canvas.before:

              self.rect = Rectangle(pos=btn5.pos, size=btn5.size)
          layout.add_widget(btn5)
        
          return layout
          
if __name__ == '__main__':
      LearPlusApp().run()
