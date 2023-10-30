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
          image = Image(source="py.kivy/py/img_wireframe/Imagem2.png",
                size_hint=(None, None),
                size=(47, 47))
          anchor_layout = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height=400)
          anchor_layout.add_widget(image)
          top_button_layout.add_widget(anchor_layout)

          layout.add_widget(top_button_layout)


          # Campos de entrada
          input_layout = GridLayout(cols=2, spacing=10, size_hint_y=None, height=80, pos_hint={'x': 0})

          # Layout para Nome Completo
          name_layout = BoxLayout(orientation='vertical', spacing=8, padding=(0, 0, 0, 205))  # Adicionamos margem inferior de 170
          
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

          # Botão "Atualizar Conta"
          btn5 = Button(text="[color=000000]ATUALIZAR CONTA[/color]", background_color=(0.7, 0.87, 0.38, 1), size_hint=(None, None), size=(270, 75), markup=True)
          btn5.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
          btn5.background_normal = ''  # Removemos o fundo padrão do botão
          with btn5.canvas.before:

              self.rect = Rectangle(pos=btn5.pos, size=btn5.size)
          layout.add_widget(btn5)
          
            # Botão "Upload da Foto do Usuário"
          btn6 = Button(text="[color=000000]UPLOAD DA FOTO DO USUÁRIO[/color]", background_color=(0.7, 0.87, 0.38, 1), size_hint=(None, None), size=(270, 75), markup=True)
          btn6.pos_hint = {'center_x': 0.5}  # Centralize o botão horizontalmente
          btn6.background_normal = ''  # Removemos o fundo padrão do botão
          with btn6.canvas.before:
              self.rect = Rectangle(pos=btn6.pos, size=btn6.size)
          layout.add_widget(btn6)


          return layout
          
if __name__ == '__main__':
      LearPlusApp().run()