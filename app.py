from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Page de présentation
@app.route('/')
def index():
    return render_template('index.html')

# Page du questionnaire
@app.route('/questionnaire')
def questionnaire():
    return render_template('questionnaire.html')

# Route pour afficher les résultats
@app.route('/resultats')
def resultats():
    # Récupération des paramètres envoyés
    nom = request.args.get('nom')
    age = request.args.get('age')

    # Message personnalisé
    message = f"Merci {nom}, vous avez {age} ans."
    
    return render_template('resultats.html', message=message)

# Gestion de la soumission du formulaire
@app.route('/submit', methods=['POST'])
def submit():
    # Récupérer les données du formulaire
    nom = request.form['nom']
    age = request.form['age']

    # Rediriger vers la page des résultats avec les données
    return redirect(url_for('resultats', nom=nom, age=age))

if __name__ == "__main__":
    app.run(debug=True)
