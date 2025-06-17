# FORMULARIO UPPER E LOWER
🎈CONVERTA SEU TEXTO PARA UPPER, LOWER OU MISTO.

<img src="FOTO.png" align="center" width="500"> <br>

## DESCRIÇÃO:
O **FORMULARIO - UPPER | LOWER | MISTO** é um aplicativo simples e prático desenvolvido em Python com a biblioteca Tkinter. Ele permite ao usuário formatar textos rapidamente em letras maiúsculas, minúsculas ou com a primeira letra de cada palavra em maiúsculo (estilo título). Além disso, oferece funcionalidades úteis como copiar o texto formatado com um clique (com notificação visual) e limpar os campos com validação.

## FUNCIONALIDADES:
1. **Entrada de Texto:**

   * Campo expansível para digitar ou colar qualquer texto.
   * Aceita parágrafos, frases ou palavras.

2. **Opções de Conversão (via ComboBox):**

   * **UPPER**: Converte todo o texto para **letras maiúsculas**.
   * **LOWER**: Converte todo o texto para **letras minúsculas**.
   * **MISTO**: Converte para **estilo título**, onde **cada palavra começa com letra maiúscula**.

3. **Campo de Texto Formatado (Somente Leitura):**

   * O resultado da conversão é exibido em uma área protegida contra digitação.
   * O usuário pode visualizar facilmente o texto convertido.

4. **Botão "CONVERTER":**

   * Aplica a conversão selecionada ao texto inserido.
   * Valida se o campo de entrada está preenchido antes de processar.

5. **Botão "COPIAR":**

   * Copia o conteúdo do campo formatado para a área de transferência.
   * Mostra um **pop-up temporário estilizado** com fundo preto e texto branco dizendo: **"TEXTO COPIADO"**.

6. **Botão "LIMPAR":**

   * Limpa os dois campos de texto.
   * Garante que só será executado se algum campo contiver conteúdo.

7. **Rodapé de Créditos:**

   * Apresenta os créditos do criador no final da janela.

## COMO EXECUTAR O PROJETO?
1. **Inicie o Aplicativo**:
   * Para executar o script Python, navegue até o diretório `./CODIGO` e use o comando:

   ```bash
   python CODIGO.py
   ```

2. **Usar a interface conforme abaixo:**

   * **Digite ou cole** seu texto na primeira caixa de texto.
   * **Escolha a opção de conversão** na ComboBox.
   * Clique em **"CONVERTER"** para aplicar a formatação.
   * Visualize o resultado na segunda caixa (somente leitura).
   * Clique em **"COPIAR"** para copiar o texto convertido (confirmação visual será exibida).
   * Clique em **"LIMPAR"** para apagar os campos.
   * Para **fechar o aplicativo**, use o botão padrão de fechamento da janela.

## SOBRE O EXECUTAVEL:
### 1. EXECUTANDO:
   * O executável gerado está disponível apenas para sistemas **Windows x64** e pode ser encontrado no diretório `./APP`.
   * Para executá-lo, basta dar dois cliques. Ele é especialmente útil em máquinas onde o **Python não está instalado**.
   * Trata-se da **mesma aplicação contida no arquivo `./CODIGO/CODIGO.py`**, porém empacotada de forma independente.
   * Se necessário, você pode recompilar o executável a qualquer momento.

### 2. GERANDO:
> **IMPORTANTE:** Antes de gerar o novo `executável`, certifique-se de excluir o arquivo `./APP/FORMULARIO UPPER E LOWER.exe`.

   **1. Instalação do [PyInstaller:](https://pyinstaller.org/en/stable/)**
   - Certifique-se de ter o PyInstaller instalado. Se não tiver, instale usando o comando abaixo:
   ```bash
   pip install pyinstaller
   ```

   **2. Gerando o Executável:**
   - No diretório `./CODIGO`, execute o comando abaixo para gerar o executável a partir do arquivo `.spec`:

   ```bash
   pyinstaller EXECUTAVEL.spec
   ```

   - O arquivo `FORMULARIO UPPER E LOWER.exe` será criado dentro da pasta `./CODIGO/dist`.

   - Após a geração, você pode mover o executável para `./APP` e remover as pastas temporárias `./CODIGO/build` e `./CODIGO/dist`.

   - Para executar o aplicativo, basta dar dois cliques no arquivo `.exe`.

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE TKINTER](https://github.com/VILHALVA/CURSO-DE-TKINTER)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)





