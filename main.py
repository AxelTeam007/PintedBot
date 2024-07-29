import tkinter as tk
from tkinter import ttk, messagebox
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pyttsx3
import threading
from textblob import TextBlob

# Télécharger les ressources nécessaires pour NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Initialisation de pyttsx3 pour text-to-speech
engine = pyttsx3.init()

class ChatbotApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Chatbot Application")
        self.geometry("800x600")

        # Initialisation des préférences par défaut
        self.speak_enabled = False  # Par défaut, la fonction Text to Speech est désactivée
        self.save_interactions_enabled = True  # Par défaut, la sauvegarde des interactions est activée
        self.learning_enabled = False  # Par défaut, le mode d'apprentissage est désactivé

        self.create_widgets()
        self.load_knowledge()
        self.load_interactions()
        self.load_learned_responses()
        self.load_preferences()  # Charger les préférences au démarrage de l'application

        # Informations sur le chatbot
        self.bot_info = {
            "name": "PintedBot",
            "function": "Répondre aux questions et apprendre des interactions.",
            "options": "Text to Speech, Sauvegarde des interactions"
        }

        # Longueur maximale des réponses
        self.MAX_RESPONSE_LENGTH = 50


    def create_widgets(self):
        self.control_panel = tk.Frame(self, width=200, bg='gray')
        self.control_panel.pack(side='left', fill='y')

        self.chat_button = tk.Button(self.control_panel, text="Chat", command=self.show_chat)
        self.chat_button.pack(fill='x')

        self.settings_button = tk.Button(self.control_panel, text="Settings", command=self.show_settings)
        self.settings_button.pack(fill='x')

        self.chat_frame = tk.Frame(self, bg='white')
        self.settings_frame = tk.Frame(self, bg='white')

        self.create_chat_page()
        self.create_settings_page()

        self.show_chat()

    def create_chat_page(self):
        self.chat_canvas = tk.Canvas(self.chat_frame, bg='white')
        self.chat_canvas.pack(expand=True, fill='both', side='left')

        self.chat_scrollbar = tk.Scrollbar(self.chat_frame, orient='vertical', command=self.chat_canvas.yview)
        self.chat_scrollbar.pack(side='right', fill='y')

        self.chat_canvas.configure(yscrollcommand=self.chat_scrollbar.set)
        self.chat_canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)

        self.chat_display = tk.Frame(self.chat_canvas, bg='white')
        self.chat_canvas.create_window((0, 0), window=self.chat_display, anchor='nw')

        self.chat_display.bind('<Configure>', lambda e: self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox('all')))

        self.chat_entry = tk.Entry(self.chat_frame)
        self.chat_entry.pack(fill='x')
        self.chat_entry.bind('<Return>', self.handle_user_input)

    def create_settings_page(self):
        self.save_interactions_var = tk.BooleanVar(value=True)
        self.speak_var = tk.BooleanVar(value=False)

        self.save_interactions_check = tk.Checkbutton(
            self.settings_frame, text="Save interactions", variable=self.save_interactions_var, command=self.toggle_save_interactions
        )
        self.save_interactions_check.pack(anchor='w', padx=10, pady=10)

        self.speak_check = tk.Checkbutton(
            self.settings_frame, text="Text to Speech", variable=self.speak_var, command=self.toggle_speak
        )
        self.speak_check.pack(anchor='w', padx=10, pady=10)

    def show_chat(self):
        self.settings_frame.pack_forget()
        self.chat_frame.pack(expand=True, fill='both')

    def show_settings(self):
        self.chat_frame.pack_forget()
        self.settings_frame.pack(expand=True, fill='both')

    def toggle_save_interactions(self):
        self.save_interactions_enabled = self.save_interactions_var.get()
        self.save_preferences()

    def toggle_speak(self):
        self.speak_enabled = self.speak_var.get()
        self.save_preferences()

    def handle_user_input(self, event):
        user_input = self.chat_entry.get()
        self.chat_entry.delete(0, tk.END)
        self.add_message(user_input, "user")

        # Analyser le sentiment de l'utilisateur
        sentiment_score = self.analyze_sentiment(user_input)

        # Animation de réflexion du chatbot
        self.add_typing_animation()

        # Utiliser un thread séparé pour obtenir la réponse du chatbot afin de ne pas bloquer l'interface
        threading.Thread(target=self.get_and_display_response, args=(user_input, sentiment_score)).start()

    def add_message(self, message, sender):
        bubble_color = "#DCF8C6" if sender == "user" else "#E5E5EA"
        anchor = 'e' if sender == "user" else 'w'
        frame = tk.Frame(self.chat_display, bg='white')
        frame.pack(anchor=anchor, pady=5, padx=5, fill='x')

        bubble = tk.Label(frame, text=message, bg=bubble_color, wraplength=400, justify='left', bd=5, relief="solid")
        bubble.pack(anchor=anchor, padx=10, pady=2)

        self.chat_canvas.update_idletasks()
        self.chat_canvas.yview_moveto(1)

    def add_typing_animation(self):
        self.typing_label = tk.Label(self.chat_display, text="Chatbot is typing...", bg='white', fg='gray', font=('Arial', 10, 'italic'))
        self.typing_label.pack(anchor='w', pady=5, padx=10)
        self.chat_canvas.update_idletasks()
        self.chat_canvas.yview_moveto(1)

    def remove_typing_animation(self):
        if hasattr(self, 'typing_label') and self.typing_label.winfo_exists():
            self.typing_label.pack_forget()

    def get_and_display_response(self, user_input, sentiment_score):
        response = self.get_bot_response(user_input, sentiment_score)
        
        # Supprimer l'animation de réflexion
        self.remove_typing_animation()
        
        self.add_message(response, "bot")

        if self.speak_enabled:
            engine.say(response)
            engine.runAndWait()

        if self.save_interactions_enabled:
            self.save_interaction(user_input, response)

        if response == "Je suis désolé, je ne sais pas répondre à cette question.":
            self.add_message("Que devrais-je répondre à cette question ?", "bot")
            self.learning_enabled = True
            self.last_user_input = user_input

    def load_knowledge(self):
        self.knowledge = {}
        knowledge_dir = 'knowledge'
        for file_name in os.listdir(knowledge_dir):
            if file_name.endswith('.txt'):
                with open(os.path.join(knowledge_dir, file_name), 'r', encoding='utf-8') as file:
                    self.knowledge[file_name] = file.read()

    def load_interactions(self):
        self.interactions = []
        interactions_file = 'userdb/interactions.txt'
        if os.path.exists(interactions_file):
            with open(interactions_file, 'r', encoding='utf-8') as file:
                for line in file:
                    self.interactions.append(line.strip())

    def load_learned_responses(self):
        self.learned_responses = {}
        learned_file = 'userdb/learned.txt'
        if os.path.exists(learned_file):
            with open(learned_file, 'r', encoding='utf-8') as file:
                for line in file:
                    if line.startswith("Q: "):
                        question = line[3:].strip()
                    elif line.startswith("R: "):
                        response = line[3:].strip()
                        self.learned_responses[question] = response

    def save_preferences(self):
        with open('userdb/preferences.txt', 'w', encoding='utf-8') as file:
            file.write(f"SaveInteractions: {self.save_interactions_var.get()}\n")
            file.write(f"TextToSpeech: {self.speak_var.get()}\n")

    def load_preferences(self):
        preferences_file = 'userdb/preferences.txt'
        if os.path.exists(preferences_file):
            with open(preferences_file, 'r', encoding='utf-8') as file:
                for line in file:
                    if line.startswith("SaveInteractions: "):
                        self.save_interactions_var.set(line.split(": ")[1].strip() == 'True')
                        self.save_interactions_enabled = self.save_interactions_var.get()
                    elif line.startswith("TextToSpeech: "):
                        self.speak_var.set(line.split(": ")[1].strip() == 'True')
                        self.speak_enabled = self.speak_var.get()

    def save_interaction(self, user_input, response):
        if not self.save_interactions_enabled:
            return
        with open('userdb/interactions.txt', 'a', encoding='utf-8') as file:
            file.write(f"Q: {user_input}\nR: {response}\n")

    def save_learned_response(self, user_input, response):
        if not self.save_interactions_enabled:
            return
        with open('userdb/learned.txt', 'a', encoding='utf-8') as file:
            file.write(f"Q: {user_input}\nR: {response}\n")
        self.learned_responses[user_input] = response

    def get_bot_response(self, question, sentiment_score):
        if self.learning_enabled:
            if question.lower() != "i don't know":
                self.save_learned_response(self.last_user_input, question)
                self.learning_enabled = False
                return f"Merci ! J'ai appris que je devrais répondre : {question}"
            else:
                self.learning_enabled = False
                return "Pas de souci. Peut-être que je pourrai répondre la prochaine fois."

        if question in self.learned_responses:
            return self.learned_responses[question]

        response = self.get_bot_info(question)
        if response != "Je suis PintedBot un assistant virtuel.":
            return response

        responses = {}
        for file_name, content in self.knowledge.items():
            if question.lower() in content.lower():
                responses[file_name] = content.lower().count(question.lower())

        if not responses:
            return "Je suis désolé, je ne sais pas répondre à cette question."

        best_match_file = max(responses, key=responses.get)
        response = self.extract_relevant_section(best_match_file, question)

        # Limiter la longueur de la réponse
        response_words = response.split()[:self.MAX_RESPONSE_LENGTH]
        return ' '.join(response_words) + '...' if len(response_words) == self.MAX_RESPONSE_LENGTH else ' '.join(response_words)

    def extract_relevant_section(self, file_name, query):
        content = self.knowledge[file_name]
        lines = content.split('\n')
        relevant_section = []
        recording = False

        for line in lines:
            if query.lower() in line.lower():
                recording = True
            if recording:
                relevant_section.append(line)
            if recording and line.strip() == "":
                break

        return "\n".join(relevant_section) if relevant_section else content

    def get_bot_info(self, question):
        if question == "qui es-tu ?":
            return f"Je suis {self.bot_info['name']}."
        elif question == "quel est ton nom ?":
            return f"Mon nom est {self.bot_info['name']}."
        elif question == "quelles sont tes fonctions ?":
            return self.bot_info['function']
        elif question == "quelles sont tes options ?":
            return self.bot_info['options']
        return "Je suis PintedBot un assistant virtuel."

    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        return sentiment_score

    def _on_mouse_wheel(self, event):
        self.chat_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

if __name__ == "__main__":
    app = ChatbotApp()
    app.mainloop()