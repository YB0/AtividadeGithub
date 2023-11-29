## Documentação Básica 

__Para rodar o programa, execute "python calculadora.py" no terminal;__

A aplicação é uma calculadora simples desenvolvida em Python usando a biblioteca Tkinter para criar uma interface gráfica. Abaixo, detalharemos as classes e métodos utilizados para a sua construção.

### CalculatorApp (Classe)

**Atributos:**
calculation (str): Armazena a expressão matemática inserida pelo usuário; text_result (Tkinter.Text): Widget Tkinter usado para exibir a expressão e o resultado.

### Métodos

**__init__(self):** Construtor da classe CalculatorApp. Inicializa a janela principal, configura os atributos iniciais e chama o método create_buttons para a criação dos botões da interface. Não utiliza parâmetros; 

**add_to_calculation(self, symbol):** Utilizada para que, quando o usuário apertar um botão, o caractere seja adicionado à variável calculation. Além disso, atualiza a interface gráfica para refletir a mudança na expressão. Seu único parâmetro é symbol, do tipo str, que representa o símbolo a ser adicionado na expressão;

**evaluate_calculation(self):** Avalia a expressão matemática atual e exibe o resultado na calculadora. Se houver um erro na avaliação, exibe "Error" na interface. Não utiliza parâmetros;

**clear_field(self):** Limpa a expressão matemática e o campo de resultado, atualizando a interface gráfica para refletir a limpeza. Não utiliza parâmetros;

**create_buttons(self):** Cria os botões da calculadora e os associa aos métodos correspondentes (add_to_calculation, evaluate_calculation, clear_field). Os botões são organizados com base em um layout predefinido. Não utiliza parâmetros;

    button_layout: lista de tuplas utilizada no método create_buttons onde cada tupla contém informações sobre como um botão deve ser organizado na interface gráfica da calculadora. Cada tupla possui quatro elementos: texto do botão, linha, coluna e número de colunas que o botão ocupa;

### Comportamento dos Botões

- **Botões Numéricos e Operadores:** Adicionam seus respectivos símbolos à expressão matemática (chamando o método add_to_calculation e passando para ele seu valor);

- **Botão "C":** Limpa a expressão matemática (chamando o método clear_field);

- **Botão "=":** Avalia a expressão matemática e exibe o resultado (chamando o método evaluate_calculation);