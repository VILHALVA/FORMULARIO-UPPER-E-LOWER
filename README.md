# FORMULÁRIO UPPER E LOWER
🎈CONVERTA SEU TEXTO PARA UPPER, LOWER OU MISTO.

<img src="FOTO.png" align="center" width="500"> <br>

## DESCRIÇÃO:
O "Aplicativo de Formulário UPPER, LOWER e MISTO" é uma ferramenta simples, porém útil, desenvolvida em Python com o uso da biblioteca Tkinter para criar uma interface gráfica de usuário. O aplicativo oferece uma maneira conveniente de formatar e manipular texto, permitindo que os usuários convertam o texto para letras maiúsculas, minúsculas ou ambas, copiem o texto formatado para a área de transferência e limpem os campos de texto quando necessário.

## RECURSOS:
1. **Entrada de Texto Flexível:** O aplicativo fornece uma área de entrada de texto onde os usuários podem inserir ou colar texto de sua escolha. A entrada de texto é flexível e acomoda parágrafos ou texto simples.

2. **Conversão para Maiúsculas, Minúsculas ou Misturado:** O aplicativo oferece três botões distintos, "UPPER", "lOWER" e "MISTO", que permitem aos usuários converter o texto inserido para letras maiúsculas, minúsculas ou misturado (Apenas a primeira letra inicial de cada palavra fica maiúscula), respectivamente. Isso é útil para padronizar o texto ou realizar formatação de acordo com as necessidades do usuário.

3. **Visualização do Texto Formatado:** O texto formatado após a conversão é exibido em uma área designada, onde os usuários podem revisar o resultado. Isso torna fácil verificar se o texto foi convertido de acordo com as preferências do usuário.

4. **Cópia Simples para a Área de Transferência:** O aplicativo oferece a capacidade de copiar o texto formatado diretamente para a área de transferência do sistema com um simples clique no botão "COPIAR". Isso é conveniente quando os usuários desejam colar o texto em outros aplicativos ou documentos.

5. **Limpeza Fácil dos Campos:** O botão "LIMPAR" permite que os usuários limpem tanto o campo de entrada de texto quanto o campo de texto formatado, facilitando a preparação para a entrada de novo texto ou a realização de novas conversões.

## EXECUTANDO O PROJETO:
1. **Executando o Código:** Navegue até o diretório `./CODIGO`, e execute o arquivo Python com o comando:
```bash
python CODIGO.py
```

2. **Inserir Texto**: Na primeira caixa de texto, insira o texto que deseja converter. Você pode digitar manualmente ou colar texto de outra fonte.

3. **Selecionar Opção de Conversão**: Na ComboBox, selecione o tipo de conversão desejado:
   - **UPPER**: Converte todo o texto para letras maiúsculas.
   - **LOWER**: Converte todo o texto para letras minúsculas.
   - **MISTO**: Converte o texto para o formato "misto", onde a primeira letra de cada palavra é maiúscula e o restante é minúscula.

4. **Converter**: Depois de inserir o texto e selecionar a opção de conversão, clique no botão "CONVERTER". O texto convertido será exibido na segunda caixa de texto.

5. **Copiar Texto Convertido**: Se desejar, você pode clicar no botão "COPIAR" para copiar o texto convertido para a área de transferência do sistema.

6. **Limpar Campos**: Para limpar os campos de entrada e saída, clique no botão "LIMPAR". Isso apagará o texto inserido e o texto convertido.

7. **Fechar o Aplicativo**: Para fechar o aplicativo, você pode clicar no botão de fechar na janela ou usar o método de fechamento padrão do seu sistema operacional.

## SOBRE O EXECUTAVEL:
### 1. EXECUTANDO:
- Este arquivo executável está disponível apenas para `Windows X64`. Para executá-lo, basta dar dois cliques. O executável é bastante útil caso o Python não esteja instalado. Trata-se da mesma aplicação do arquivo `CODIGO.py`. Se desejar, você pode recompilá-lo novamente; é para isso que forneci o arquivo `imagem.ico`.

### 2. GERANDO:
   **1. Instalação do [PyInstaller:](https://pyinstaller.org/en/stable/)**
   - Certifique-se de ter o PyInstaller instalado. Se não tiver, instale usando o comando abaixo:
   ```bash
   pip install pyinstaller
   ```

   **2. Gerando o Executável:**
   - Para gerar o executável, utilize o comando `pyinstaller` seguido de opções:
      - `--icon="imagem.ico"`: Especifica o ícone do executável.
      - `-w`: Especifica que o executável será do tipo "windowed", ou seja, sem exibir uma janela de console.
      - `-F`: Gera um único arquivo executável em vez de vários.
      - `CODIGO.py`: Substitua "CODIGO.py" pelo nome do seu arquivo Python principal.
   ```bash
   pyinstaller --icon="imagem.ico" -w -F CODIGO.py
   ```

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CURSO DE TKINTER](https://github.com/VILHALVA/CURSO-DE-TKINTER)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)





