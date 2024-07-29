# PintedBot
<a href="https://github.com/AxelTeam007/PintedBot">
	<div>
		<img src="https://raw.githubusercontent.com/AxelTeam007/PintedBot/master/PintedBot.png" alt="Logo PintedBot">
	</div>
  
<br>
 
 <a href="https://github.com/AxelTeam007/SimpleChat">  **An improved version of the old project :** 
 
 <br>
 
  <a href="https://github.com/AxelTeam007/SimpleChat">
   <div>
     <img src="https://logosmarcas.net/wp-content/uploads/2020/12/GitHub-Simbolo-650x366.png" height="100" width="150" alt="Logo GitHub">
   </div>

## Importations
- `import tkinter as tk` : Importe le module `tkinter` pour créer l'interface graphique.
- `from tkinter import ttk, messagebox` : Importe les composants avancés et les boîtes de dialogue de `tkinter`.
- `import os` : Importe le module `os` pour interagir avec le système de fichiers.
- `import nltk` : Importe le module `nltk` pour le traitement du langage naturel.
- `from nltk.tokenize import word_tokenize` : Importe la fonction `word_tokenize` pour diviser le texte en mots.
- `from nltk.corpus import stopwords` : Importe la liste des stopwords (mots vides) de `nltk`.
- `import pyttsx3` : Importe le module `pyttsx3` pour la synthèse vocale.
- `import threading` : Importe le module `threading` pour gérer les threads.
- `from textblob import TextBlob` : Importe `TextBlob` pour l'analyse de sentiment.
- `nltk.download('punkt")` : Télécharge le tokenizer `punkt` de `nltk`.
- `nltk.download('stopwords')` : Télécharge la liste des stopwords de `nltk`.
- `engine = pyttsx3.init()` : Initialise le moteur de synthèse vocale `pyttsx3`.

## Classe ChatbotApp - Initialisation
- ﻿﻿`class ChatbotApp(tk.Tk):`: Définit une classe `ChatbotApp` héritant de `tk.Tk`.
- `def __init__(self):`: Constructeur de la classe.
- `super().__init__()` : Appelle le constructeur de la classe parente `tk.Tk`.
- `self.title("Chatbot Application")`: Définit le titre de la fenêtre.
- `self.geometry("800x600")` : Définit la taille de la fenêtre.
- `self.speak_enabled = False` : Désactive la fonction Text to Speech par défaut.
- `self.save_interactions_enabled = True` : Active la sauvegarde des interactions par défaut.
- `self.learning_enabled = False` : Désactive le mode d'apprentissage par défaut.
- `self.create_widgets()` : Appelle la méthode pour créer les widgets.
- `self.load_knowledge()` : Appelle la méthode pour charger les connaissances.
- `self.load_interactions()` : Appelle la méthode pour charger les interactions.
- `self.load_learned_responses()` : Appelle la méthode pour charger les réponses apprises.
- `self.load_preferences()` : Appelle la méthode pour charger les préférences.
- `self.bot_info = { ... }` : Définit les informations sur le chatbot.
- `self.MAX_RESPONSE_LENGTH = 50` : Définit la longueur maximale des réponses.

## Méthodes de Création de Widgets
- `def create_widgets(self):`: Déclare la méthode `create_widgets`.
- `self.control_panel = tk.Frame(self, width=200, bg='gray')` : Crée un panneau de contrôle avec une largeur de 200 et un fond gris.
- `self.control_panel.pack(side='left', fill='y')` : Place le panneau de contrôle à gauche et le remplit verticalement.
- `self.chat_button = tk.Button(self.control panel, text="Chat", command=self.show_chat)`: Crée un bouton pour le chat.
- `self.chat_button.pack(fill='x')` : Remplit horizontalement le bouton de chat.
- `self.settings_button = tk.Button(self.control_panel, text="Settings", command=self.show_settings)` : Crée un bouton pour les paramètres.
- `self.settings_button.pack(fill='x')` : Remplit horizontalement le bouton de paramètres.
- `self.chat_frame = tk.Frame(self, bg='white')` : Crée un cadre pour le chat avec un fond
blanc.
- `self.settings_frame = tk.Frame(self, bg='white')`: Crée un cadre pour les paramètres avec un fond blanc.
- `self.create_chat_page()` : Appelle la méthode pour créer la page de chat.
- `self.create_settings_page()` : Appelle la méthode pour créer la page des paramètres.
- `self.show_chat()`: Affiche la page de chat par défaut.

## Méthodes de Création des Pages de Chat et Paramètres
- `def create_chat_page(self):` : Déclare la méthode `create_chat_page`.
- `self.chat_canvas = tk.Canvas(self.chat_frame, bg='white')`: Crée un canvas pour le chat avec un fond blanc.
- `self.chat_canvas.pack(expand-True, fill='both', side='left')` : Remplit le canvas dans toutes les directions et l'attache à gauche.
- `self.chat_scrollbar = tk.Scrollbar(self.chat_frame, orient='vertical',`
 `command=self.chat_canvas.yview)` : Crée une barre de défilement verticale pour le canvas.
- `self.chat_scrollbar.pack(side='right', fill='y')` : Place la barre de défilement à droite et la remplit verticalement.
- `self.chat_canvas.configure(yscrollcommand=self.chat_scrollbar.set)` : Configure le canvas
pour utiliser la barre de défilement.
- `self.chat_canvas.bind_all("<Mousewheel>", self._on_mouse_wheel)` : Lie l'événement de la molette de la souris à une méthode.
- `self.chat_display = tk.Frame(self.chat_canvas, bg='white')` : Crée un cadre pour afficher le chat avec un fond blanc.
- `self.chat_canvas.create_window((0, 0), window-self.chat_display, anchor='nw')` : Crée une fenêtre dans le canvas pour le cadre du chat.
- `self.chat_display.bind('<Configure>', lambda e:`
 `self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox('all')))` : Met à jour la région de défilement du canvas lorsque la taille du cadre change.
- `self.chat_entry = tk.Entry(self.chat_frame)` : Crée une entrée pour le texte de l'utilisateur.
- `self.chat_entry.pack(fill='x')'` : Remplit horizontalement l'entrée de texte.
- `self.chat_entry.bind('<Return>', self.handle_user_input)` : Lie l'événement de la touche `Return` à la méthode de gestion de l'entrée utilisateur.
## Méthodes de Création des Pages de Paramètres
- ﻿`def create_settings_page(self):` : Déclare la méthode `create_settings_page`.
- `ttk.Label(self.settings_frame, text="Settings", font=("Helvetica",
16)).pack(anchor='w', padx-10, pady=10)` : Crée une étiquette "Settings" et la place dans le cadre des paramètres.
- `self.speak_var = tk.BooleanVar(value=self.speak_enabled)` : Crée une variable booléenne pour le Text to Speech.
- `self.save_interactions_var = tk.Booleanvar (value=self.save_interactions_enabled)` : Crée une variable booléenne pour la sauvegarde des interactions.
- `self.learning_var = tk.BooleanVar(value=self.learning_enabled)` : Crée une variable booléenne pour l'apprentissage.
- `ttk.checkbutton(self.settings_frame, text="Enable Text to Speech",
variable=self.speak_var, command-self.toggle_speak).pack(anchor='w', padx=20, pady-5)` : Crée une case à cocher pour activer le Text to Speech.
- `ttk.checkbutton(self.settings_frame, text="Save Interactions", variable=self.save_interactions_var,
command=self.toggle_save_interactions).pack(anchor='w', padx=20, pady-5)` : Crée une case
à cocher pour sauvegarder les interactions.
- `ttk.Checkbutton(self.settings_frame, text="Enable Learning",
variable=self.learning_var, command=self.toggle_learning).pack(anchor='w', padx=20, pady-5)` : Crée une case à cocher pour activer l'apprentissage.
- `ttk.Button(self.settings_frame, text="Save Settings",
command=self.save_preferences)-pack (anchor='w', padx=10, pady-20)` : Crée un bouton pour
sauvegarder les préférences.

## Méthodes pour Afficher les Pages de Chat et Paramètres
- `def show_chat(self):` : Déclare la méthode `show_chat`.
- `self.settings_frame.pack_forget ()` : Cache le cadre des paramètres.
- `self.chat_frame.pack(expand-True, fill='both')` : Affiche le cadre du chat.
- `def show_settings (self):` : Déclare la méthode`show_settings`.
- `self.chat_frame.pack_forget()` : Cache le cadre du chat.
- `self.settings_frame.pack(expand=True, fill='both')` : Affiche le cadre des paramètres.

## Méthodes pour Charger les Connaissances et Interactions
- ﻿`def load_knowledge(self):` : Déclare la méthode `load_knowledge`.
- `self.knowledge = {}`: Initialise le dictionnaire des connaissances.
- `knowledge_folder = 'knowledge'` : Définit le dossier des connaissances.
- `if not os.path.exists(knowledge_folder): os.makedirs(knowledge_folder)` : Crée le dossier des connaissances s'il n'existe pas.
- `for file_name in os.listdir(knowledge_folder):` : Parcourt les fichiers dans le dossier des connaissances.
- `if file_name.endswith('.txt'):`: Vérifie que le fichier a une extension.txt.
- `with open(os.path.join(knowledge_folder, file_name), 'r', encoding='utf-8') as file:`: Ouvre le fichier en lecture avec encodage UTF-8.
- `self.knowledge[file_name] = file.read()` : Lit le contenu du fichier et le stocke dans le dictionnaire des connaissances.
- `def load_interactions (self): : Déclare la méthode `load_interactions`.
- `self.interactions = []` : Initialise la liste des interactions.
- `if os.path.exists('interactions.txt'):`: Vérifie si le fichier interactions.txt existe.
- `with open('interactions.txt', 'r', encoding='utf-8') as file:` : Ouvre le fichier en lecture avec encodage UTF-8.
- `self.interactions = file.readlines()` : Lit les lignes du fichier et les stocke dans la liste des interactions.
- `def load_learned_responses (self): : Déclare la méthode "load_learned_responses`.
- `self.learned_responses = {}` : Initialise le dictionnaire des réponses apprises.
- `if os.path.exists('learned_responses.txt'):`: Vérifie si le fichier learned_responses.txt existe.
- `with open('learned_responses.txt', 'r', encoding='utf-8') as file:` : Ouvre le fichier en lecture avec encodage UTF-8.
- `for line in file:` : Parcourt chaque ligne du fichier.
- `question, response = line.strip().split('\t')` : Sépare la question et la réponse par un tabulateur.
- `self.learned_responses[question] = response` : Stocke la question et la réponse dans le dictionnaire des réponses apprises.
- `def_load_preferences(self):`: Déclare la méthode `load_preferences`.
- `if os.path.exists('preferences.txt'):`: Vérifie si le fichier preferences.txt existe.
- `with open('preferences.txt', 'r', encoding='utf-8') as file:` : Ouvre le fichier en lecture avec encodage UTF-8.
- `preferences = file.readlines()` : Lit les lignes du fichier et les stocke dans la liste des préférences.
- `self.speak_enabled = preferences[0].strip() == 'True'` : Détermine si la synthèse vocale est activée.
- `self.save_interactions_enabled = preferences[1].strip() == 'True"` : Détermine si la sauvegarde des interactions est activée.
- `self.learning_enabled = preferences[2].strip() == 'True'` : Détermine si l'apprentissage
est activé.
- `self.update_settings()` : Met à jour les paramètres.

## Méthodes pour Sauvegarder les Préférences
﻿- `def save_preferences (self):`: Déclare la méthode `save_preferences`.
- `with open('preferences.txt', 'w', encoding='utf-8') as file:`: Ouvre le fichier preferences.txt en écriture avec encodage UTF-8.
- `file.write(f"{self.speak_var.get()}\n")` : Écrit la préférence de synthèse vocale dans le
fichier.
- `file.write(f"{self.save_interactions_var.get()}\n")` : Écrit la préférence de sauvegarde des interactions dans le fichier.
- `file.write(f"{self.learning_var.get()}\n")` : Écrit la préférence d'apprentissage dans le
fichier.
- `self.speak_enabled = self.speak_var.get()` : Met à jour l'état de la synthèse vocale.
- `self.save_interactions_enabled = self.save_interactions_var.get()` : Met à jour l'état de la sauvegarde des interactions.
- `self.learning_enabled = self.learning_var.get()` : Met à jour l'état de l'apprentissage.
- `self.update_settings()` : Met à jour les paramètres.
- `def toggle_speak(self):` : Déclare la méthode `toggle_speak`.
- `self.speak_enabled = self.speak_var.get()` : Met à jour l'état de la synthèse vocale
- `def toggle_save_interactions(self):`: Déclare la méthode `toggle_save_interactions`.
- `self.save_interactions_enabled = self.save_interactions_var.get()` : Met à jour l'état de la sauvegarde des interactions.
- `def toggle_learning(self):` : Déclare la méthode `toggle_learning`.
- `self.learning_enabled = self.learning_var.get()` : Met à jour l'état de l'apprentissage.
- `def update_settings(self): pass` : Déclare une méthode vide `update_settings`.

## Méthodes pour Sauvegarder les Interactions et les Réponses Apprises
﻿- `def save_interaction(self, interaction):`: Déclare la méthode `save_interaction`.
- `with open('interactions.txt', 'a', encoding='utf-8') as file:` : Ouvre le fichier interactions.txt en mode append (ajout) avec encodage UTF-8.
- `file.write(f"{interaction}\n")` : Écrit l'interaction dans le fichier.
- `def save_learned_response(self, question, response):` : Déclare la méthode `save_learned_response`.
- `with open('learned_responses.txt', 'a', encoding='utf-8') as file:` : Ouvre le fichier learned_responses.txt en mode append (ajout) avec encodage UTF-8.
- `file.write(f"{question}\t{response}\n")` : Écrit la question et la réponse séparées par un
tabulateur dans le fichier.
- `self.learned_responses[question] = response` : Ajoute la question et la réponse au dictionnaire des réponses apprises.

## Méthodes pour Obtenir une Réponse et Gérer l'Apprentissage
﻿- `def get_response(self, question):`: Déclare la méthode "get_response".
- `processed question = self.preprocess(question)` : Pré-traite la question.
- `best_match = None` : Initialise la meilleure correspondance à None.
- `best_score = 0` : Initialise le meilleur score à 0.
- `for file_name, content in self.knowledge.items():`: Parcourt chaque fichier et son contenu dans les connaissances.
- `processed_content = self.preprocess (content)` : Pré-traite le contenu du fichier.
- `score = self.similarity(processed_question, processed_content)` : Calcule la similarité entre la question et le contenu.
- `if score > best_score:` : Si le score est meilleur que le meilleur score actuel...
- `best_score = score` : Met à jour le meilleur score.
- `best_match = file_name` : Met à jour la meilleure correspondance.
- `if best_match:`: Si une meilleure correspondance a été trouvée...
- `response = self.knowledge[best_match]` : Récupère la réponse correspondante.
- `if self.learning_enabled:` : Si l'apprentissage est activé...
- `self.save_learned_response(question, response)` : Sauvegarde la réponse apprise.
- `return response : Retourne la réponse.
- `else:` : Si aucune correspondance n'a été trouvée...
- `return "I'm sorry, I don't know the answer to that."` : Retourne un message d'excuse.
- `def preprocess(self, text):`: Déclare la méthode `preprocess`.
- `tokens = word_tokenize(text.lower())`: Divise le texte en mots (tokens) et les met en minuscule.
- `stop_words = set(stopwords.words('english'))` : Crée un ensemble de mots vides en anglais.
- `filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]` : Filtre les tokens pour garder seulement les mots alphanumériques qui ne sont pas des mots vides.
- `return filtered_tokens` : Retourne les tokens filtrés.
- `def similarity(self, tokens1, tokens2):` : Déclare la méthode `similarity`.
- `return len(set(tokens1) & set(tokens2)) / float(len(set(tokens1) | set(tokens2)))`: Calcule la similarité entre deux ensembles + tokens.

## Boucle Principale pour l'Interaction avec l'Utilisateur
- `def run(self):` : Déclare la méthode `run`.
- `self.root.mainloop()` : Démarre la boucle principale de l'interface graphique.

## Méthode Principale pour Lancer l'Application
- `if __name__ == "__main__":` : Vérifie si le script est exécuté directement.
- `app = ChatbotApp()` : Crée une instance de la classe ChatbotApp.
- `app.run()` : Appelle la méthode `run` pour démarrer l'application.
