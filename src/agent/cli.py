from src.agent.ollama_agent import OllamaAgent


# Função para rodar o agente no terminal, permitindo interação direta com o usuário
def run_cli(agent: OllamaAgent) -> None:
    print("\n--- MeteoAI - Agente de Clima ---")
    while True:
        txt = input("\nDigite sua pergunta sobre o clima:")
        if txt.lower() in ['sair', 'exit']:
            break
        print(f"\nResposta do Agente: {agent.chat(txt)}")
