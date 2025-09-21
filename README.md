# Ozymandias_KEYLOGGER
Ozymandias – Keylogger modular para fins educacionais e de pesquisa, com captura de teclas em tempo real, buffer inteligente, parser avançado, criptografia de logs, auto-aprendizado e análise offline.

---

## Advertência Legal

**Aviso:** Este software é fornecido **exclusivamente para fins educacionais, de pesquisa e teste em ambiente controlado**.  
Não me responsabilizo por qualquer uso indevido ou ilegal deste código.  
O uso em computadores de terceiros sem autorização é **ilegal e punível por lei**.  
Ao clonar ou executar este repositório, você assume total responsabilidade pelos seus atos.

---

## Introdução

O nome **Ozymandias** foi inspirado no personagem de histórias em quadrinhos, simbolizando vigilância e análise detalhada. "Contemplem minhas obras, ó Poderosos, e desesperem!"
O keylogger é projetado para capturar entradas de teclado de forma discreta e precisa, mantendo registros seguros e segmentados, sem interferir no funcionamento da máquina alvo.

---

## Estrutura do Projeto

Ozymandias/
├─ README.md                   # Documentação geral
├─ src/                        # Código-fonte do Keylogger
│  ├─ main.py                  # Entry point
│  ├─ keylogger_core.py         # Captura de teclas e buffer inteligente
│  ├─ parser.py                 # Parser e pré-processamento de dados
│  ├─ crypto_storage.py         # Criptografia e armazenamento seguro
│  ├─ analysis_offline.py       # Análise offline e geração de relatórios
│  ├─ ai_module.py              # Auto-aprendizado e triggers dinâmicas
│  └─ utils.py                  # Funções auxiliares (clipboard, screenshots, Telegram)
├─ tests/                       # Scripts de teste unitário
├─ docs/                        # Documentação detalhada e fluxos de dados
│  └─ blueprint_ascii.txt       # Blueprint ASCII detalhando fluxo de dados
└─ scripts/                     # Scripts auxiliares (gerar PDF híbrido, setup de persistência)

---

## Funcionalidades

- Captura de teclas em tempo real  
- Buffer Circular Inteligente (FIFO, thread-safe, overflow controlado)  
- Parser avançado com compressão adaptativa  
- Criptografia AES com hash SHA256  
- Logging paralelo e segmentado  
- Auto-aprendizado com triggers dinâmicas  
- Captura de clipboard e screenshots conforme necessário  
- Persistência invisível  
- Geração de PDF híbrido para testes em ambiente seguro  
- Transferência segura de logs e análise offline  

---

## Uso Seguro

- Executar apenas em ambientes controlados ou laboratórios virtuais  
- Testar preferencialmente em máquinas sandbox ou VM isoladas  
- Nunca utilizar em computadores de terceiros sem autorização  

--
