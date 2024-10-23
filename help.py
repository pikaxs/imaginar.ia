from openai import OpenAI
client = OpenAI()
patata=input("ingresa una tematica: ")
patata2=input("ingresa un tema a elegir: ")
text="quiero que sigas mis instruccion para empezar no digas claro te voy ayudar con esto simplmente genera el cuento, tambien quiero que a mitad del cuento hagas alguna pregunta dicha pregunta debe de ser sobre alguna ensenianza que des o en algun momento donde tu creas que se puede dar una ensenianza a los ninios y quiero que especificamente pares de generar el cuento hasta que te responda la pregunta esta pregunta se tiene que sentir parte de la historia como si fueras un personaje mas de la historia por ejemplo es como el programa de dora que le rpegunta al espectador, ahora para empezar quiero que crees un cuento de la tematica {0} y con el tema principal que seria: {1} ".format(patata, patata2)


uwu=[
    {"role": "system", "content": "eres un exeperto en crear cuentos infantines para los niños donde sobre todo los creas dando una enseñanza ya sea moral, etica o relacionada al tema que se te sugiera, cabe a destacar que solo vas a permitir el uso de temas y tematocas aptas para los infantes en cualquier otro caso mostraras el rechazo a ese tema y indicaras que use terminos adecuados"},
    {"role": "user", "content": text}
  ]
completion = client.chat.completions.create(
  model="gpt-4o",
  messages=uwu
)
print(completion.choices[0].message.content)
aux=completion.choices[0].message.content




num=2
user_in=""







uwu.append({"role": "assistant", "content": aux})
while True:
  if num==0:
    break
  user_in=input()
  uwu.append({"role": "user","content": user_in})
  completion = client.chat.completions.create(
    model="gpt-4o",
    messages=uwu
  )
  print(completion.choices[0].message.content)
  num=num-1