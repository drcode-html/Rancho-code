import gradio as gr
hunger = 5
happiness = 5
pet_name = ""
def hhprint():
    return f"Hunger: {hunger}\nHappiness: {happiness}"
def limits():
  global hunger,happiness 
  if hunger >10:
   hunger = 10
  if hunger <0:
   hunger = 0
  if happiness<0:
   happiness = 0
  if happiness>10:
   happiness = 10

def feedpet():
 global hunger,happiness
 hunger -= 2
 limits()
 return f"{pet_name} is eating! \n{hhprint()}" 
    
def playwithpet():
  global hunger,happiness
  happiness += 2
  hunger += 3
  limits()
  return f"You played with, {pet_name}\n{hhprint()}"

def rest():
  global hunger,happiness
  happiness += 3
  hunger -= 3
  limits() 
  return f"{pet_name}, is resting, rest is important.\n{hhprint()}"

def winnlose():
  if hunger == 10:
   return f"your pet is very hungry \n ---Game Over---"
  if happiness == 0:
   return f"your pet is very sad\n ---Game Over---"
  return None 

def start_game(name):
  global pet_name
  pet_name = name
  return (
   gr.update(visible=False),
   gr.update(visible=True),
   f"{hhprint()}"

 )
 
with gr.Blocks() as app:
   with gr.Column(visible=True) as setup_screen:
     name_box = gr.Textbox(label="Pet Name")
     start_btn = gr.Button("Start")
   with gr.Column(visible=False) as game_screen:
    status = gr.Textbox(label=f"---{pet_name}---")
    feed_btn = gr.Button(f"Feed {pet_name}")
    play_btn = gr.Button(f"Play with{pet_name}")
    rest_btn = gr.Button(f"give {pet_name} rest and food")

    start_btn.click(
      start_game,
      inputs=name_box,
      outputs=[setup_screen,game_screen,status])
    feed_btn.click(
    feedpet,
    outputs=status
    )
   play_btn.click(  
  playwithpet,
  outputs=status
  )
   rest_btn.click( 
   rest,
   outputs=status
   )
app.launch()
 


 
 