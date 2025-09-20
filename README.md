# GenAI SDK

Um projeto Python para integração com a API do Google Gemini usando o SDK oficial do Google GenAI.

## 🚀 Funcionalidades

- Integração com Google Gemini 2.5 Flash Lite
- Geração de conteúdo em streaming
- Gerenciamento seguro de chaves de API
- Configuração via variáveis de ambiente

## 📋 Pré-requisitos

- Python 3.11 ou superior
- Chave de API do Google AI Studio
- [uv](https://docs.astral.sh/uv/) (gerenciador de pacotes Python)

## 🛠️ Instalação

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd genai-sdk
   ```

2. **Instale as dependências**:
   ```bash
   uv sync
   ```

3. **Configure a chave da API**:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione sua chave de API:
     ```env
     GOOGLE_GENAI_API_KEY=sua_chave_aqui
     ```

## 🔑 Como obter a chave da API

1. Acesse [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Faça login com sua conta Google
3. Clique em "Create API Key"
4. Copie a chave gerada
5. Cole no arquivo `.env`

## 🎯 Como usar

### Execução básica

```bash
uv run main.py
```

### Exemplo de código

```python
import os
from dotenv import load_dotenv
from google import genai

# Carrega as variáveis de ambiente
load_dotenv()
api_key = os.getenv("GOOGLE_GENAI_API_KEY")

# Cria o cliente
client = genai.Client(api_key=api_key)

# Gera conteúdo em streaming
res = client.models.generate_content_stream(
    model="gemini-2.5-flash-lite",
    contents="Escreva um poema sobre a vida"
)

# Exibe o resultado em tempo real
for chunk in res:
    print(chunk.text, end="", flush=True)
```

## 📁 Estrutura do projeto

```
genai-sdk/
├── main.py              # Código principal
├── pyproject.toml       # Configurações do projeto
├── .env                 # Variáveis de ambiente (não commitado)
├── .env.example         # Exemplo de configuração
├── .gitignore          # Arquivos ignorados pelo Git
└── README.md           # Este arquivo
```

## 🔒 Segurança

- ✅ Chaves de API armazenadas em variáveis de ambiente
- ✅ Arquivo `.env` protegido pelo `.gitignore`
- ✅ Validação de chave obrigatória
- ✅ Sem chaves hardcoded no código

## 🧪 Desenvolvimento

### Instalar dependências de desenvolvimento

```bash
uv sync --dev
```

### Executar o projeto

```bash
uv run main.py
```

## 📚 Documentação

- [Google GenAI SDK](https://ai.google.dev/docs)
- [Google AI Studio](https://aistudio.google.com/)
- [Documentação do Gemini](https://ai.google.dev/gemini-api/docs)

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🆘 Suporte

Se você encontrar algum problema ou tiver dúvidas:

1. Verifique se a chave da API está configurada corretamente
2. Confirme se todas as dependências estão instaladas
3. Abra uma issue no repositório

---

**Nota**: Este projeto é um exemplo de integração com a API do Google Gemini. Para uso em produção, considere implementar tratamento de erros mais robusto e logging adequado.
