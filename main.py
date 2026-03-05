from random import choice, shuffle, sample
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

# ============================
# BANDEIRAS — nomes limpos!
# ============================

COUNTRIES_FLAGS = {
    "Brasil": {"image": "./bandeiras/brasil.png", "capital": "Brasilia", "continent": "America do Sul", "language": "Portugues", "population": "215 milhoes"},
    "Inglaterra": {"image": "./bandeiras/inglaterra.png", "capital": "Londres", "continent": "Europa", "language": "Ingles", "population": "56 milhoes"},
    "Franca": {"image": "./bandeiras/franca.png", "capital": "Paris", "continent": "Europa", "language": "Frances", "population": "67 milhoes"},
    "Alemanha": {"image": "./bandeiras/alemanha.png", "capital": "Berlim", "continent": "Europa", "language": "Alemao", "population": "83 milhoes"},
    "Estados Unidos": {"image": "./bandeiras/estados_unidos.png", "capital": "Washington", "continent": "America do Norte", "language": "Ingles", "population": "331 milhoes"},
    "Mexico": {"image": "./bandeiras/mexico.png", "capital": "Cidade do Mexico", "continent": "America do Norte", "language": "Espanhol", "population": "126 milhoes"},
    "Argentina": {"image": "./bandeiras/argentina.png", "capital": "Buenos Aires", "continent": "America do Sul", "language": "Espanhol", "population": "45 milhoes"},
    "Italia": {"image": "./bandeiras/italia.png", "capital": "Roma", "continent": "Europa", "language": "Italiano", "population": "60 milhoes"},
    "Africa do Sul": {"image": "./bandeiras/africa_do_sul.png", "capital": "Pretoria", "continent": "Africa", "language": "11 idiomas oficiais", "population": "59 milhoes"},
    "Portugal": {"image": "./bandeiras/portugal.png", "capital": "Lisboa", "continent": "Europa", "language": "Portugues", "population": "10 milhoes"},
    "Marrocos": {"image": "./bandeiras/marrocos.png", "capital": "Rabat", "continent": "Africa", "language": "Arabe", "population": "37 milhoes"},
    "Emirados Arabes": {"image": "./bandeiras/emirados_arabes.png", "capital": "Abu Dhabi", "continent": "Asia", "language": "Arabe", "population": "10 milhoes"},
    "Tunisia": {"image": "./bandeiras/tunisia.png", "capital": "Tunise", "continent": "Africa", "language": "Arabe", "population": "12 milhoes"},
    "China": {"image": "./bandeiras/china.png", "capital": "Pequim", "continent": "Asia", "language": "Mandarim", "population": "1.4 bilhao"},
    "Japao": {"image": "./bandeiras/japao.png", "capital": "Toquio", "continent": "Asia", "language": "Japones", "population": "125 milhoes"},
    "Chipre": {"image": "./bandeiras/chipre.png", "capital": "Nicosia", "continent": "Europa", "language": "Grego/Turco", "population": "1.2 milhao"},
    "Libano": {"image": "./bandeiras/libano.png", "capital": "Beirute", "continent": "Asia", "language": "Arabe", "population": "6 milhoes"},
    "Oman": {"image": "./bandeiras/oman.png", "capital": "Mascate", "continent": "Asia", "language": "Arabe", "population": "5 milhoes"},
    "Iemen": {"image": "./bandeiras/iemen.png", "capital": "Sana", "continent": "Asia", "language": "Arabe", "population": "30 milhoes"},
    "Iraque": {"image": "./bandeiras/iraque.png", "capital": "Bagda", "continent": "Asia", "language": "Arabe", "population": "40 milhoes"},
    "Irlanda": {"image": "./bandeiras/irlanda.png", "capital": "Dublin", "continent": "Europa", "language": "Ingles/Irlandes", "population": "5 milhoes"},
    "Albania": {"image": "./bandeiras/albania.png", "capital": "Tirana", "continent": "Europa", "language": "Albanes", "population": "2.8 milhoes"},

    # NOVOS PAÍSES ADICIONADOS
    "Espanha": {"image": "./bandeiras/espanha.png", "capital": "Madrid", "continent": "Europa", "language": "Espanhol", "population": "47 milhoes"},
    "Canada": {"image": "./bandeiras/canada.png", "capital": "Ottawa", "continent": "America do Norte", "language": "Ingles/Frances", "population": "38 milhoes"},
    "Australia": {"image": "./bandeiras/australia.png", "capital": "Camberra", "continent": "Oceania", "language": "Ingles", "population": "26 milhoes"},
    "Nova Zelandia": {"image": "./bandeiras/nova_zelandia.png", "capital": "Wellington", "continent": "Oceania", "language": "Ingles", "population": "5 milhoes"},
    "Coreia do Sul": {"image": "./bandeiras/coreia_do_sul.png", "capital": "Seul", "continent": "Asia", "language": "Coreano", "population": "51 milhoes"},
    "Coreia do Norte": {"image": "./bandeiras/coreia_do_norte.png", "capital": "Pyongyang", "continent": "Asia", "language": "Coreano", "population": "25 milhoes"},
    "Nigeria": {"image": "./bandeiras/nigeria.png", "capital": "Abuja", "continent": "Africa", "language": "Ingles", "population": "213 milhoes"},
    "Egito": {"image": "./bandeiras/egito.png", "capital": "Cairo", "continent": "Africa", "language": "Arabe", "population": "103 milhoes"},
    "Arabia Saudita": {"image": "./bandeiras/arabia_saudita.png", "capital": "Riad", "continent": "Asia", "language": "Arabe", "population": "35 milhoes"},
    "Turquia": {"image": "./bandeiras/turquia.png", "capital": "Ancara", "continent": "Europa/Asia", "language": "Turco", "population": "85 milhoes"},
    "Grecia": {"image": "./bandeiras/grecia.png", "capital": "Atenas", "continent": "Europa", "language": "Grego", "population": "10 milhoes"},
    "Holanda": {"image": "./bandeiras/holanda.png", "capital": "Amsterdam", "continent": "Europa", "language": "Holandes", "population": "17 milhoes"},
    "Noruega": {"image": "./bandeiras/noruega.png", "capital": "Oslo", "continent": "Europa", "language": "Noruegues", "population": "5 milhoes"},
    "Suecia": {"image": "./bandeiras/suecia.png", "capital": "Estocolmo", "continent": "Europa", "language": "Sueco", "population": "10 milhoes"},
    "Finlandia": {"image": "./bandeiras/finlandia.png", "capital": "Helsinque", "continent": "Europa", "language": "Finlandes", "population": "5.5 milhoes"},
    "Polonia": {"image": "./bandeiras/polonia.png", "capital": "Varsovia", "continent": "Europa", "language": "Polones", "population": "37 milhoes"},
    "Peru": {"image": "./bandeiras/peru.png", "capital": "Lima", "continent": "America do Sul", "language": "Espanhol", "population": "33 milhoes"},
    "Chile": {"image": "./bandeiras/chile.png", "capital": "Santiago", "continent": "America do Sul", "language": "Espanhol", "population": "19 milhoes"},
    "Colombia": {"image": "./bandeiras/colombia.png", "capital": "Bogota", "continent": "America do Sul", "language": "Espanhol", "population": "51 milhoes"},
}

# =============================
# DIFICULDADES (reorganizadas)
# =============================

DIFFICULTY_LEVELS = {
    "facil": [
        "Brasil", "Franca", "Alemanha", "Estados Unidos",
        "Italia", "Inglaterra", "Espanha", "Canada"
    ],

    "medio": [
        "Mexico", "Argentina", "Portugal", "Japao", "China",
        "Africa do Sul", "Australia", "Nova Zelandia",
        "Peru", "Chile", "Colombia"
    ],

    "dificil": [
        country for country in COUNTRIES_FLAGS
        if country not in [
            "Brasil", "Franca", "Alemanha", "Estados Unidos", "Italia",
            "Inglaterra", "Espanha", "Canada",
            "Mexico", "Argentina", "Portugal", "Japao",
            "China", "Africa do Sul", "Australia",
            "Nova Zelandia", "Peru", "Chile", "Colombia"
        ]
    ]
}

# Ícone da dica e número de perguntas
DICA_ICON_PATH = "./imagens/dica.png"
MAX_QUESTIONS = 10

# ===========================================


class BaseScreen(Screen):
    def create_button(self, text, size=(1, 0.2), callback=None):
        button = Button(text=text, size_hint=size,
                        background_color=BTN_BG_COLOR, color=BTN_TEXT_COLOR)
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

        self.layout = FloatLayout()

        self.clue_button = Button(background_normal=DICA_ICON_PATH, background_down=DICA_ICON_PATH,
                                  size_hint=(0.18, 0.18), pos_hint={"x": 0.02, "top": 0.98}, border=(0, 0, 0, 0))
        self.clue_button.bind(on_release=self.show_clue)
        self.layout.add_widget(self.clue_button)

        self.flag_image = Image(size_hint=(0.7, 0.5), pos_hint={"center_x": 0.5, "y": 0.35})
        self.layout.add_widget(self.flag_image)

        self.option_box = BoxLayout(orientation="vertical", size_hint=(0.7, 0.3),
                                    spacing=10, pos_hint={"center_x": 0.5, "y": 0.05})
        self.layout.add_widget(self.option_box)

        self.add_widget(self.layout)

    def start_game(self, level):
        self.score = self.total = 0
        self.level = level

        # NOVO: Seleção aleatória sem repetição
        self.available_countries = sample(DIFFICULTY_LEVELS[level], min(MAX_QUESTIONS, len(DIFFICULTY_LEVELS[level])))

        self.clue_used = False
        self.clue_button.disabled = False

        self.new_round()

    def new_round(self, *_):
        if not self.available_countries:
            self.manager.current = "final"
            self.manager.get_screen("final").show_result(self.score, MAX_QUESTIONS)
            return

        self.option_box.clear_widgets()
        self.option_buttons = []

        self.current_answer = self.available_countries.pop(0)
        self.flag_image.source = COUNTRIES_FLAGS[self.current_answer]["image"]

        options = [self.current_answer]
        all_countries = list(COUNTRIES_FLAGS.keys())

        while len(options) < 4:
            country = choice(all_countries)
            if country not in options:
                options.append(country)

        shuffle(options)

        for country in options:
            button = Button(text=country, size_hint=(1, 0.3),
                            background_color=BTN_BG_COLOR, color=BTN_TEXT_COLOR)
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

        back_button = Button(text="Voltar ao início", size_hint=(1, 0.2),
                             background_color=BTN_BG_COLOR, color=BTN_TEXT_COLOR)
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
