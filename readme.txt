CALCULATEUR DE GRECQUES + PRICER D'OPTIONS PAR BLACK-SCHOLES
========================================

Cette application Streamlit calcule le prix d'une option européenne ainsi que
les grecques suivantes selon le modèle de Black-Scholes, avec un dividende continu :

- Delta (Δ)
- Gamma (Γ)
- Theta (Θ), exprimé par jour
- Vega, pour une variation de 1 point de volatilité
- Rho, pour une variation de 1 point du taux sans risque


PRÉREQUIS
---------

Il faut disposer de Python 3.9 ou d'une version plus récente.

Les bibliothèques utilisées sont :

    streamlit
    numpy
    scipy


INSTALLATION
------------

Depuis un terminal, placez-vous dans le dossier du projet.


Il est recommandé de créer un environnement virtuel :

    python3 -m venv .venv
    source .venv/bin/activate

Installez ensuite les dépendances :

    pip install streamlit numpy scipy


LANCER L'APPLICATION
--------------------

Dans le même terminal, exécutez :

    streamlit run app.py

Streamlit ouvre normalement l'application dans votre navigateur. Si ce n'est
pas le cas, ouvrez l'adresse affichée dans le terminal, en général.


Pour arrêter l'application, revenez au terminal et utilisez Ctrl+C.


UTILISATION
-----------

Les paramètres se règlent dans la barre latérale gauche. 

Les résultats sont mis à jour automatiquement après chaque modification. L'intérêt de cette application est d'observer les variations des grecques lorsque l'on modifie les paramètres de l'option.


REMARQUES
---------

- Le modèle s'applique à des options européennes.
- À l'échéance (T = 0), l'application retourne la valeur intrinsèque de
  l'option ; les grecques autres que le delta sont affichées à zéro.
