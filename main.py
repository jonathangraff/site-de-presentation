from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__)

algos_Python = "algos_Python"
dico_dicos_portfolio = {
    algos_Python:
        {"titre": "Algorithmes en Python",
         "intro": " Voici différents algorithmes implémentés lors de la résolution de problèmes, en général sur le site Codingame. Ces algorithmes m'ont permis de découvrir "
                  "de nouvelles notions, de les mettre en pratique, ainsi que d'utiliser des tests unitaires grâce au package unittest. ",
         "outils": "Python, Pycharm, unittest",
         "cover_image": "python_algos.png",
         },
    "bibliotheque-C":
        {"titre": "Interface d'une bibliothèque en C",
         "intro": "J’ai réalisé cette application console dans le cadre d'un projet. L'objectif était de créer une application qui simule une bibliothèque universitaire. "
                  "L'utilisateur doit se créer un compte, puis se connecter à l'aide de son mot de passe écrit dans un fichier crypté. Les utilisateurs peuvent faire une recherche "
                  "parmi les livres pouvant être empruntés (par titre et auteur) et les étudiants peuvent emprunter trois livres pour un maximum de 2 minutes chacun.<br>"
                  "Les professeurs peuvent eux emprunter cinq livres pour un maximum de 3 minutes chacun, mais aussi ajouter un livre à la collection.<br> Tant qu'un livre est en retard, "
                  "on ne peut plus en emprunter d'autres.",
         "outils": "C, devC++",
         "image": "appli_bibli.jpg",
         "lien": "https://github.com/jonathangraff/bibliotheque_C",
         },
    "PizzaMama":
        {"titre": "Site Web et application pour un restaurant",
         "titre_court": "Site web d'un restaurant",
         "intro": "J’ai réalisé un site Web, une API et une application pour me former plus particulièrement au côté back-end de la programmation Web. "
                  "<br><br> Une interface administrateur sur mesure permet de modifier sa carte très facilement et les changements sont répercutés directement "
                  "sur le site et l'application : <br><a href='https://jgpizzamama.herokuapp.com/admin'> "
                  "Interface Admin</a> (Login : admin et mot de passe : adminadmin)",
         "outils": "HTML5, CSS3, Django, Python, Heroku",
         "image": "project1.jpg",
         "lien": "https://github.com/jonathangraff/Pizza_Mama",
         "autre": "<div style='text-align:center'><a class='contact-button' style='display: inline-block; margin-top: 8px;  href='https://jgpizzamama.herokuapp.com' target='_blank'>"
                  "Voir le site web du projet</a><br></div>",
         },
    "Galaxy":
        {"titre": "Jeu vidéo mobile Galaxy",
         "intro": "J’ai réalisé ce jeu simple pour me familiariser avec le framework de Python, Kivy. "
                  "Le jeu consiste simplement à déplacer un vaisseau, représenté"
                  "par un triangle le long d'une route tracée aléatoirement sans tomber. ",
         "outils": "Python, Kivy",
         "image": "galaxy.jpg",
         "lien": "https://github.com/jonathangraff/Jeu_Galaxy",
         },
    "MrBeat":
        {"titre": "Boîte à rythmes \"Mr Beat\"",
         "intro": "J’ai réalisé une application mobile qui permet de charger différents"
                  " sons et de les jouer selon un rythme défini. Possibilité de moduler la vitesse.",
         "outils": "Python, Kivy",
         "image": "mrbeat.jpg",
         "lien": "https://github.com/jonathangraff/Boite_a_rythmes",
         },
    "stageM2-Coq":
        {
            "titre": "Stage M2 - Programmation en Coq d'algorithmes de pilotage de bras de robot",
            "titre_court": "Programmation de bras de robot en Coq",
            "intro": "Lors de mon stage de Master 2, j'ai du implémenter des mouvements de différents bras de robots grâce aux algèbres géométriques, "
                     "puis à l'aide du logiciel d'assistant de preuve Coq, prouver que l'algorithme était correct, c'est-à-dire qu'il faisait bien ce qu'on"
                     " lui demandait, qu'il n'y avait pas de \"bugs\".",
            "outils": "Coq, programmation fonctionnelle, algèbres géométriques",
            "image": "coq.png",
            "lien": "https://github.com/jonathangraff/Memoire_M2",
        },
    "projetM2-data":
        {
            "titre": "Projet M2 - Apprentissage par renforcement profond pour des problèmes combinatoires",
            "titre_court": "Apprentissage par renforcement profond",
            "intro": "Le but de ce projet de Master 2 était de comprendre comment marchait l'apprentissage par renforcement profond pour pouvoir "
                     "appliquer plus tard ce principe aux problèmes des réseaux d'échangeur de chaleur. "
                     "<br><br> J'ai implémenté en Python un agent qui a appris où se déplacer dans une grille grâce à un système de récompense pour pouvoir"
                     "trouver un \"trésor\" en évitant des obstacles et des \"bombes\". ",
            "outils": "Python, Tensorflow",
            "image": "renforcement.jpg",
            "lien": "https://github.com/jonathangraff/Projet_M2_Data",
        },
    "stageM1-Typescript":
        {
            "titre": "Stage M1 - Algorithme de déformations de surfaces vers des surfaces minimales en Typescript",
            "titre_court": "Surfaces minimales en Typescript",
            "intro": "J'ai effectué ce stage lors de ma première année de master CSMI. Il s'agissait d'implémenter un algorithme qui, à partir d'une surface et d'un maillage"
                     "déformait la surface vers une surface minimale par itérations.<br><br>"
                     " Cet algorithme a ensuite pu être mis dans la bibliothèque Mathis de TypeScript.  ",
            "outils": "TypeScript, surfaces minimales",
            "image": "catenoide.gif",
            "lien": "https://github.com/jonathangraff/Stage_M1_TypeScript",
        }
}
nb_projets = len(dico_dicos_portfolio)
liste_dicos_algos_Python = [
    {
        "titre": "Algorithme de backtracking",
        "corps": """On donne une grille représentant un parcours de golf.
                Sur chaque grille se trouve une certaine quantité de balles et une quantité égale de trous. 
                L'objectif est de tracer le trajet de chaque balle vers un trou différent sans que les trajets ne se croisent.
                Le programme doit afficher la solution unique du parcours.

                Pour chaque parcours, chaque case est représentée par un caractère :
                <ul>
                    <li>Un point . pour une cellule vide, représentant du gazon.</li>
                    <li>Un entier allant de 1 à 9, représentant une balle. La valeur indique son nombre de coups.</li>
                    <li>La lettre X, représentant un obstacle d'eau.</li>
                    <li>La lettre H, représentant un trou.</li>
                </ul> 
                Une balle peut être tapée plusieurs fois, autant que son nombre de coups.
                
                Le programme doit afficher sur la sortie standard une grille de taille égale à celle donnée en entrée, contenant des flèches indiquant comment les balles doivent être tapées.
                
                Le nombre de coups d'une balle indique aussi le nombre de cases qu'elle traverse la première fois qu'elle bouge. Le prochain coup ira une case moins loin, chaque coup décrémente le nombre de cases que 
                la balle traverse de 1. À chaque nouveau coup la balle pourra être tapée dans une nouvelle direction. Quand le prochain coup devient 0 ou que la balle s'arrête sur une case trou, la balle ne peut plus bouger.
                
                Chaque balle doit atteindre un trou. Un trou peut recevoir au plus 1 balle.
                
                Une balle ne peut pas quitter la grille, ni atterrir dans un obstacle d'eau. Elle peut cependant passer par dessus.""",
        "prog": "golf.py",
    },
    {
        "titre": "Algorithme glouton - ordonnancement",
        "corps": "A partir d'une liste de taches comprenant pour chacune la date de début, et la durée (en jours), et sachant que deux tâches ne peuvent pas être exécutées en même temps,"
                 " déterminer combien de tâches pourront être exécutées au total.",
        "prog": "ordonnancement.py",
    }
]


@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html",
                           liste_dicos_portfolio=dico_dicos_portfolio, )


@app.route("/CV/")
def cv():
    return render_template("CV.html",
                           liste_dicos_portfolio=dico_dicos_portfolio, )


@app.route("/contact/")
def contact():
    return render_template("contact.html",
                           liste_dicos_portfolio=dico_dicos_portfolio,
                           section_grise=True)


@app.route("/portfolio/")
def portfolio():
    return render_template("portfolio.html",
                           liste_dicos_portfolio=dico_dicos_portfolio,
                           nb_projets=nb_projets,
                           section_grise=True,
                           enumerate=enumerate)


@app.route("/portfolio/<nom_page>")
def portfolio_item(nom_page):
    return render_template("portfolio_item.html",
                           liste_dicos_portfolio=dico_dicos_portfolio,
                           dico=dico_dicos_portfolio[nom_page],
                           section_grise=True,
                           nom_page=nom_page)


@app.route("/portfolio/algos_Python")
def portfolio_algos_Python():
    return render_template("portfolio_algos_Python.html",
                           liste_dicos_portfolio=dico_dicos_portfolio,
                           liste_dicos_algos_Python=liste_dicos_algos_Python,
                           nom_page=algos_Python,
                           dico=dico_dicos_portfolio[algos_Python],
                           section_grise=True,)