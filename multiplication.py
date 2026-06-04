import gradio as gr 

def multiplication_table(n): 
    table = ""
    for i in range(1,100):
     table += f"{n} * {i} = {n*i}\n"
    return table 

app = gr.Interface(
   fn = multiplication_table,
   inputs = gr.Number(label = "Enter a Number"),
   outputs = gr.Textbox(label = "Multiplication table")

)

app.launch(server_port=8000,server_name="0.0.0.0",share=True)
