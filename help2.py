from flask import Flask, render_template, request, redirect, url_for
from openai import OpenAI

app = Flask(__name__)
client = OpenAI()
A=0
# Definimos una variable para almacenar las conversaciones
conversacion = []

def generar_cuento_interactivo(patata, patata2, user_in=None):
    if A>0:
        text = f"quiero que sigas mis instruccion para empezar no digas claro te voy ayudar con esto simplemente genera el cuento. También quiero que a mitad del cuento hagas alguna pregunta sobre alguna enseñanza para los niños y pares de generar el cuento hasta que respondan la pregunta. La temática es {patata} y el tema principal es {patata2}."
        messages = [
            {"role": "system", "content": "eres un experto en crear cuentos infantiles para los niños donde sobre todo los creas dando una enseñanza moral o ética."},
            {"role": "user", "content": text}
        ]
    else:
        messages = conversacion

    # Si el usuario responde, añadimos esa respuesta a la conversación
    if user_in:
        messages.append({"role": "user", "content": user_in})

    # Generamos el siguiente bloque del cuento
    completion = client.chat.completions.create(
        model="gpt-4",  # Asegúrate de que estás usando el modelo correcto
        messages=messages
    )

    # Guardamos el contenido generado
    response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": response})
    conversacion = messages  # Actualizamos la conversación

    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    global conversacion
    cuento = ""
    
    if request.method == 'POST':
        if 'theme' in request.form and 'topic' in request.form:
            # Primera interacción: el usuario ingresa la temática y el tema
            patata = request.form['theme']
            patata2 = request.form['topic']
            cuento = generar_cuento_interactivo(patata, patata2)
        elif 'user_input' in request.form:
            # Segunda interacción: el usuario responde a la pregunta del cuento
            user_input = request.form['user_input']
            cuento = generar_cuento_interactivo(None, None, user_input)
    A=A+1
    return render_template('inicio.html', cuento=cuento)

@app.route('/reset')
def reset():
    global conversacion
    conversacion = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
