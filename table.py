import gradio as gr

def mult_table(n):
    table = ""
    for i in range(1,100):
     f"{n} * {i} = {n*i}\n"
    return table  

app = gr.Interface(
   fn = mult_table,
   inputs = gr.Number(label = "Enter a number"),
   outputs = gr.Textbox(label = "Multiplication table")
)  
app.launch(server_port = 8080)