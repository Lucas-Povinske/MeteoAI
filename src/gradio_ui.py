import gradio as gr
from src.agent.ollama_agent import OllamaAgent


def run_gradio(agent: OllamaAgent) -> None:
    # Função para processar a entrada do usuário e obter a resposta do agente
    def process_input(user_inp):
        response = agent.chat(user_inp)
        return response

    # Configura a interface Gradio
    with gr.Blocks() as demo:
        gr.Markdown("## MeteoAI - Agente de Clima")
        user_input = gr.Textbox(label="Digite sua pergunta sobre o clima:")
        output = gr.Textbox(label="Resposta do Agente:", interactive=False)
        submit_btn = gr.Button("Enviar")

        # Define a ação do botão para processar a entrada do usuário
        submit_btn.click(fn=process_input, inputs=user_input, outputs=output)

    # Inicia a interface Gradio
    demo.launch(server_name="0.0.0.0", server_port=7860)
