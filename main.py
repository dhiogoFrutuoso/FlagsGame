from random import choice, shuffle
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.utils import get_color_from_hex

# Definindo a cor do fundo da tela
Window.clearcolor = (0.7, 0.85, 1, 1)

# Cores usadas na interface
BTN_BG_COLOR = get_color_from_hex("#003366")
SUCCESS_COLOR = get_color_from_hex("#00ff00")
ERROR_COLOR = get_color_from_hex("#ff0000")
BTN_TEXT_COLOR = (1, 1, 1, 1)

# Informações sobre as bandeiras
COUNTRIES_FLAGS = {
    "Brasil": {"image": "./bandeiras/brasil.png", "capital": "Brasília", "continent": "América do Sul", "language": "Português", "population": "215 milhões"},
    "Inglaterra": {"image": "./bandeiras/inglaterra.png", "capital": "Londres", "continent": "Europa", "language": "Inglês", "population": "56 milhões"},
    "França": {"image": "./bandeiras/franca.png", "capital": "Paris", "continent": "Europa", "language": "Francês", "population": "67 milhões"},
    "Alemanha": {"image": "./bandeiras/alemanha.png", "capital": "Berlim", "continent": "Europa", "language": "Alemão", "population": "83 milhões"},
    "Estados Unidos": {"image": "./bandeiras/estados_unidos.png", "capital": "Washington, D.C.", "continent": "América do Norte", "language": "Inglês", "population": "331 milhões"},
    "México": {"image": "./bandeiras/mexico.png", "capital": "Cidade do México", "continent": "América do Norte", "language": "Espanhol", "population": "126 milhões"},
    "Argentina": {"image": "./bandeiras/argentina.png", "capital": "Buenos Aires", "continent": "América do Sul", "language": "Espanhol", "population": "45 milhões"},
    "Itália": {"image": "./bandeiras/italia.png", "capital": "Roma", "continent": "Europa", "language": "Italiano", "population": "60 milhões"},
    "África do Sul": {"image": "./bandeiras/africa_do_sul.png", "capital": "Pretória", "continent": "África", "language": "11 idiomas oficiais", "population": "59 milhões"},
    "Portugal": {"image": "./bandeiras/portugal.png", "capital": "Lisboa", "continent": "Europa", "language": "Português", "population": "10 milhões"},
    "Marrocos": {"image": "./bandeiras/marrocos.png", "capital": "Rabat", "continent": "África", "language": "Árabe", "population": "37 milhões"},
    "Emirados Árabes": {"image": "./bandeiras/emirados_arabes.png", "capital": "Abu Dhabi", "continent": "Ásia", "language": "Árabe", "population": "10 milhões"},
    "Tunísia": {"image": "./bandeiras/tunisia.png", "capital": "Túnis", "continent": "África", "language": "Árabe", "population": "12 milhões"},
    "China": {"image": "./bandeiras/china.png", "capital": "Pequim", "continent": "Ásia", "language": "Mandarim", "population": "1,4 bilhão"},
    "Japão": {"image": "./bandeiras/japao.png", "capital": "Tóquio", "continent": "Ásia", "language": "Japonês", "population": "125 milhões"},
    "Chipre": {"image": "./bandeiras/chipre.png", "capital": "Nicósia", "continent": "Europa", "language": "Grego e Turco", "population": "1,2 milhão"},
    "Líbano": {"image": "./bandeiras/libano.png", "capital": "Beirute", "continent": "Ásia", "language": "Árabe", "population": "6 milhões"},
    "Oman": {"image": "./bandeiras/oman.png", "capital": "Mascate", "continent": "Ásia", "language": "Árabe", "population": "5 milhões"},
    "Yemen": {"image": "./bandeiras/yemen.png", "capital": "Sana", "continent": "Ásia", "language": "Árabe", "population": "30 milhões"},
    "Iraque": {"image": "./bandeiras/iraque.png", "capital": "Bagdá", "continent": "Ásia", "language": "Árabe", "population": "40 milhões"},
    "Irlanda": {"image": "./bandeiras/irlanda.png", "capital": "Dublin", "continent": "Europa", "language": "Inglês e Irlandês", "population": "5 milhões"},
    "Albânia": {"image": "./bandeiras/albania.png", "capital": "Tirana", "continent": "Europa", "language": "Albanês", "population": "2,8 milhões"},
}

# Definição das categorias de dificuldade e seus respectivos países
DIFFICULTY_LEVELS = {
    "facil": ["Brasil", "França", "Alemanha", "Estados Unidos", "Itália", "Inglaterra"],
    "medio": ["México", "Argentina", "Portugal", "Japão", "China", "África do Sul"],
    "dificil": [country for country in COUNTRIES_FLAGS if country not in ["Brasil", "França", "Alemanha", "Estados Unidos", "Itália", "Inglaterra", "México", "Argentina", "Portugal", "Japão", "China", "África do Sul"]]
}

# Ícone da dica e número máximo de perguntas
DICA_ICON_PATH = "./imagens/dica.png"
MAX_QUESTIONS = 10


class BaseScreen(Screen):
    def create_button(self, text, size=(1, 0.2), callback=None):
        """Cria um botão com o texto e a função passada."""
        button = Button(text=text, size_hint=size, background_color=BTN_BG_COLOR, color=BTN_TEXT_COLOR)
        if callback:
            button.bind(on_release=callback)
        return button


class StartScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=40, spacing=30)
        layout.add_widget(Label(text="Jogo das Bandeiras", font_size=40, bold=True, color=(0, 0, 0, 1)))
        layout.add_widget(self.create_button("Jogar", callback=lambda *_: setattr(self.manager, "current", "difficulty")))
        self.add_widget(layout)


class DifficultyScreen(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", spacing=20, padding=40)
        layout.add_widget(Label(text="Selecione a Dificuldade", font_size=30, color=(0, 0, 0, 1)))
        for name, level in [("Fácil", "facil"), ("Médio", "medio"), ("Difícil", "dificil")]:
            layout.add_widget(self.create_button(name, callback=lambda _, l=level: self.start_game(l)))
        self.add_widget(layout)

    def start_game(self, level):
        game_screen = self.manager.get_screen("game")
        game_screen.start_game(level)
        self.manager.current = "game"


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.score = self.total = 0
        self.option_buttons = []
        self.current_answer = ""
        self.available_countries = []
        self.clue_used = False
        self.max_questions = MAX_QUESTIONS

        self.layout = FloatLayout()
        self.clue_button = Button(background_normal=DICA_ICON_PATH, background_down=DICA_ICON_PATH,
                                  size_hint=(0.18, 0.18), pos_hint={"x": 0.02, "top": 0.98}, border=(0, 0, 0, 0))
        self.clue_button.bind(on_release=self.show_clue)
        self.layout.add_widget(self.clue_button)

        self.flag_image = Image(size_hint=(0.7, 0.5), pos_hint={"center_x": 0.5, "y": 0.35})
        self.layout.add_widget(self.flag_image)

        self.option_box = BoxLayout(orientation="vertical", size_hint=(0.7, 0.3), spacing=10, pos_hint={"center_x": 0.5, "y": 0.05})
        self.layout.add_widget(self.option_box)
        self.add_widget(self.layout)

    def start_game(self, level):
        self.score = self.total = 0
        self.level = level
        self.available_countries = DIFFICULTY_LEVELS[level][:MAX_QUESTIONS]
        self.max_questions = len(self.available_countries)

        self.clue_used = False
        self.clue_button.disabled = False
        self.new_round()

    def new_round(self, *_):
        if not self.available_countries or self.total >= self.max_questions:
            self.manager.current = "final"
            self.manager.get_screen("final").show_result(self.score, self.max_questions)
            return

        self.total += 1
        self.option_box.clear_widgets()
        self.option_buttons = []

        self.current_answer = choice(self.available_countries)
        self.available_countries.remove(self.current_answer)
        self.flag_image.source = COUNTRIES_FLAGS[self.current_answer]["image"]

        options = [self.current_answer]
        all_countries = list(COUNTRIES_FLAGS.keys())
        while len(options) < 4:
            country = choice(all_countries)
            if country not in options:
                options.append(country)
        shuffle(options)

        for country in options:
            button = Button(text=country, size_hint=(1, 0.3), background_color=BTN_BG_COLOR, color=BTN_TEXT_COLOR)
            button.bind(on_release=self.select_answer)
            self.option_buttons.append(button)
            self.option_box.add_widget(button)

    def select_answer(self, instance):
        for button in self.option_buttons:
            button.disabled = True
        color = SUCCESS_COLOR if instance.text == self.current_answer else ERROR_COLOR
        anim = Animation(background_color=color, duration=0.2) + Animation(background_color=BTN_BG_COLOR, duration=0.2)
        anim.start(instance)
        if instance.text == self.current_answer:
            self.score += 1
        Clock.schedule_once(self.new_round, 0.7)

    def show_clue(self, *_):
        if self.clue_used:
            return
        data = COUNTRIES_FLAGS[self.current_answer]
        clues = [f"{k.capitalize()}: {v}" for k, v in data.items() if k != "image"]
        popup = Popup(title="Dica", content=Label(text=choice(clues), font_size=20), size_hint=(0.7, 0.4))
        popup.open()
        self.clue_used = True
        self.clue_button.disabled = True


class FinalScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", spacing=20, padding=40)
        self.result_label = Label(text="", font_size=32, color=(0, 0, 0, 1))
        layout.add_widget(self.result_label)
        back_button = Button(text="Voltar ao início", size_hint=(1, 0.2), background_color=BTN_BG_COLOR, color=BTN_TEXT_COLOR)
        back_button.bind(on_release=lambda *_: setattr(self.manager, "current", "inicio"))
        layout.add_widget(back_button)
        self.add_widget(layout)

    def show_result(self, score, total):
        self.result_label.text = f"Você acertou {score} de {total}!"


class FlagsApp(App):
    def build(self):
        screen_manager = ScreenManager(transition=NoTransition())
        screen_manager.add_widget(StartScreen(name="inicio"))
        screen_manager.add_widget(DifficultyScreen(name="difficulty"))
        screen_manager.add_widget(GameScreen(name="game"))
        screen_manager.add_widget(FinalScreen(name="final"))
        return screen_manager


if __name__ == "__main__":
    FlagsApp().run()
