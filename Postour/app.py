from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage, Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle

# Configurações de janela para tamanho de celular
Window.size = (360, 640)
Window.clearcolor = (0.95, 0.95, 0.95, 1)

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.name = 'login'
        
        with self.canvas.before:
            Color(0.2, 0.6, 1, 1)
            self.rect = Rectangle(size=Window.size, pos=self.pos)
        
        self.bind(pos=self.update_rect, size=self.update_rect)
        
        layout = GridLayout(cols=1, spacing=dp(15), padding=dp(30))
        layout.size_hint = (0.9, 0.9)
        layout.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        
        # Logo do app (substitua por sua própria imagem)
        
        
        layout.add_widget(Label(text="Postour", font_size=dp(24), color=(1, 1, 1, 1)))
        
        self.username = TextInput(
            size_hint=(1, None),
            height=dp(45),
            hint_text="Usuário",
            multiline=False,
            background_color=(1, 1, 1, 0.8)
        )
        layout.add_widget(self.username)
        
        self.password = TextInput(
            size_hint=(1, None),
            height=dp(45),
            hint_text="Senha",
            password=True,
            multiline=False,
            background_color=(1, 1, 1, 0.8)
        )
        layout.add_widget(self.password)
        
        btn_entrar = Button(
            text="Entrar",
            size_hint=(1, None),
            height=dp(50),
            background_color=(0.9, 0.9, 0.1, 1),
            color=(0, 0, 0, 1)
        )
        btn_entrar.bind(on_press=self.login)
        layout.add_widget(btn_entrar)
        
        btn_cadastrar = Button(
            text="Criar nova conta",
            size_hint=(1, None),
            height=dp(40),
            background_color=(0.1, 0.1, 0.1, 0.5),
            color=(1, 1, 1, 1)
        )
        btn_cadastrar.bind(on_press=self.ir_para_cadastro)
        layout.add_widget(btn_cadastrar)
        
        self.add_widget(layout)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
    
    def login(self, instance):
        print(f"Login tentado: {self.username.text}")
        self.manager.current = 'main'
    
    def ir_para_cadastro(self, instance):
        self.manager.current = 'cadastro'

class CadastroScreen(Screen):
    def __init__(self, **kwargs):
        super(CadastroScreen, self).__init__(**kwargs)
        self.name = 'cadastro'
        
        layout = GridLayout(cols=1, spacing=dp(15), padding=dp(25))
        layout.size_hint = (0.9, 0.9)
        layout.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        
        layout.add_widget(Label(text="Cadastro", font_size=dp(24), color=(0, 0, 0, 1)))
        
        self.nome_completo = TextInput(
            size_hint=(1, None),
            height=dp(45),
            hint_text="Nome completo",
            multiline=False
        )
        layout.add_widget(self.nome_completo)
        
        self.email = TextInput(
            size_hint=(1, None),
            height=dp(45),
            hint_text="E-mail",
            multiline=False
        )
        layout.add_widget(self.email)
        
        self.senha = TextInput(
            size_hint=(1, None),
            height=dp(45),
            hint_text="Senha",
            password=True,
            multiline=False
        )
        layout.add_widget(self.senha)
        
        self.confirmar_senha = TextInput(
            size_hint=(1, None),
            height=dp(45),
            hint_text="Confirmar senha",
            password=True,
            multiline=False
        )
        layout.add_widget(self.confirmar_senha)
        
        btn_cadastrar = Button(
            text="Cadastrar",
            size_hint=(1, None),
            height=dp(50),
            background_color=(0.3, 0.7, 0.3, 1),
            color=(1, 1, 1, 1)
        )
        btn_cadastrar.bind(on_press=self.cadastrar)
        layout.add_widget(btn_cadastrar)
        
        btn_voltar = Button(
            text="Voltar para login",
            size_hint=(1, None),
            height=dp(40),
            background_color=(0.8, 0.8, 0.8, 1),
            color=(0, 0, 0, 1)
        )
        btn_voltar.bind(on_press=self.voltar_login)
        layout.add_widget(btn_voltar)
        
        self.add_widget(layout)
    
    def cadastrar(self, instance):
        if self.senha.text != self.confirmar_senha.text:
            print("Erro: As senhas não coincidem!")
            return
            
        print(f"Novo cadastro:\nNome: {self.nome_completo.text}\nEmail: {self.email.text}")
        self.manager.current = 'main'
    
    def voltar_login(self, instance):
        self.manager.current = 'login'

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.name = 'main'
        
        main_layout = BoxLayout(orientation='vertical', spacing=dp(5))
        
        # Cabeçalho
        header = BoxLayout(size_hint=(1, None), height=dp(50), padding=(dp(10), 0))
        header.add_widget(Label(text="Minha Coleção", font_size=dp(20)))
        
        btn_config = Button(
            text="⚙️",
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            background_color=(0, 0, 0, 0)
        )
        btn_config.bind(on_press=self.ir_para_config)
        header.add_widget(btn_config)
        
        main_layout.add_widget(header)
        
        # Área de coleção (ScrollView)
        scroll = ScrollView()
        content = GridLayout(cols=2, spacing=dp(10), padding=dp(10), size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))
        
        # Exemplo de itens da coleção (substitua por seus dados reais)
        colecao = [
            {"nome": "Foto 1", "imagem": "https://via.placeholder.com/150"},
            {"nome": "Foto 2", "imagem": "https://via.placeholder.com/150"},
            {"nome": "Foto 3", "imagem": "https://via.placeholder.com/150"},
            {"nome": "Foto 4", "imagem": "https://via.placeholder.com/150"},
            {"nome": "Foto 5", "imagem": "https://via.placeholder.com/150"},
            {"nome": "Foto 6", "imagem": "https://via.placeholder.com/150"},
        ]
        
        for item in colecao:
            item_box = BoxLayout(orientation='vertical', size_hint=(1, None), height=dp(180))
            
            img = AsyncImage(
                source=item["imagem"],
                size_hint=(1, None),
                height=dp(150),
                keep_ratio=True,
                allow_stretch=True
            )
            
            lbl = Label(
                text=item["nome"],
                size_hint=(1, None),
                height=dp(30),
                halign='center'
            )
            
            item_box.add_widget(img)
            item_box.add_widget(lbl)
            content.add_widget(item_box)
        
        scroll.add_widget(content)
        main_layout.add_widget(scroll)
        
        # Menu inferior
        menu = BoxLayout(size_hint=(1, None), height=dp(50), spacing=dp(5), padding=(dp(5), 0))
        
        btn_colecao = Button(text="Coleção", background_color=(0.2, 0.6, 1, 1))
        btn_camera = Button(text="Câmera", background_color=(0.9, 0.1, 0.1, 1))
        btn_config = Button(text="Config", background_color=(0.3, 0.3, 0.3, 1))
        
        btn_config.bind(on_press=self.ir_para_config)
        
        menu.add_widget(btn_colecao)
        menu.add_widget(btn_camera)
        menu.add_widget(btn_config)
        
        main_layout.add_widget(menu)
        
        self.add_widget(main_layout)
    
    def ir_para_config(self, instance):
        self.manager.current = 'config'

class ConfigScreen(Screen):
    def __init__(self, **kwargs):
        super(ConfigScreen, self).__init__(**kwargs)
        self.name = 'config'
        
        layout = GridLayout(cols=1, spacing=dp(15), padding=dp(30))
        layout.size_hint = (0.9, 0.9)
        layout.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        
        layout.add_widget(Label(text="Configurações", font_size=dp(24), color=(0, 0, 0, 1)))
        
        # Opções de configuração
        btn_conta = Button(
            text="Minha Conta",
            size_hint=(1, None),
            height=dp(50)
        )
        layout.add_widget(btn_conta)
        
        btn_notificacoes = Button(
            text="Notificações",
            size_hint=(1, None),
            height=dp(50)
        )
        layout.add_widget(btn_notificacoes)
        
        btn_privacidade = Button(
            text="Privacidade",
            size_hint=(1, None),
            height=dp(50)
        )
        layout.add_widget(btn_privacidade)
        
        btn_ajuda = Button(
            text="Ajuda",
            size_hint=(1, None),
            height=dp(50)
        )
        layout.add_widget(btn_ajuda)
        
        btn_sair = Button(
            text="Sair",
            size_hint=(1, None),
            height=dp(50),
            background_color=(0.8, 0.1, 0.1, 1),
            color=(1, 1, 1, 1)
        )
        btn_sair.bind(on_press=self.logout)
        layout.add_widget(btn_sair)
        
        btn_voltar = Button(
            text="Voltar",
            size_hint=(1, None),
            height=dp(40),
            background_color=(0.8, 0.8, 0.8, 1)
        )
        btn_voltar.bind(on_press=self.voltar)
        layout.add_widget(btn_voltar)
        
        self.add_widget(layout)
    
    def logout(self, instance):
        print("Usuário deslogado")
        self.manager.current = 'login'
    
    def voltar(self, instance):
        self.manager.current = 'main'

class PostourApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen())
        sm.add_widget(CadastroScreen())
        sm.add_widget(MainScreen())
        sm.add_widget(ConfigScreen())
        return sm

if __name__ == "__main__":
    PostourApp().run()