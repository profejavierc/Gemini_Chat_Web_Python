
import gradio as gr
import google.generativeai as genai

# Configura tu API key
genai.configure(api_key='your_APIKEY')

# Inicializa el modelo
model = genai.GenerativeModel('gemini-pro')

def generate_text(prompt):
    response = model.generate_content(prompt)
    return response.text

# Crea la interfaz de Gradio
demo = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=2, placeholder="Ingresa tu prompt aqui"),
    outputs="text",
    title="Gemini AI Chat profejavierc",
    description="Chatea con el modelo Gemini de Google"
)

demo.launch()