from openai import OpenAI
client = OpenAI()


thread = client.beta.threads.create()


run = client.beta.threads.messages.create(
  thread_id=thread.id,
  model="gpt-4",
  role="role",
  instructions="Please address the user as Jane Doe. The user has a premium account."
)

if run.status == 'completed': 
  print(run.choices[0].messages.content)
else:
  print(run.status)