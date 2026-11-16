# rentsmart-rm-imoveis
Sistema em Python com Programação Orientada a Objetos para cálculo de orçamentos de locação e projeção anual em CSV da R.M Imóveis.

# RentSmart — Orçamentos de Locação (R.M Imóveis)

O **RentSmart** é uma ferramenta de linha de comando feita em Python para ajudar os atendentes da **R.M Imóveis** a calcular orçamentos de aluguel de forma rápida e sem erros. Em vez de fazer as contas na mão durante o atendimento, o sistema recebe as escolhas do cliente, aplica os adicionais e descontos automaticamente e já gera uma planilha com a previsão de gastos do primeiro ano.

## O que o programa faz na prática

Ao rodar o script, você escolhe o tipo de imóvel e responde a algumas perguntas simples:

* **Apartamento:** começa em **R$ 700,00** (1 quarto). Se tiver 2 quartos, soma **R$ 200,00**; se tiver vaga de garagem, soma **R$ 300,00**. Para clientes sem crianças, o sistema aplica **5% de desconto** sobre o valor final do aluguel.
* **Casa:** começa em **R$ 900,00** (1 quarto). Com 2 quartos, acrescenta **R$ 250,00**, e com vaga de garagem, mais **R$ 300,00**.
* **Estúdio:** começa em **R$ 1.200,00**. Caso o cliente precise de estacionamento, há um pacote inicial de 2 vagas por **R$ 250,00**, e cada vaga extra além dessas duas custa **R$ 60,00**.
* **Taxa de contrato:** custa **R$ 2.000,00** e pode ser parcelada em até **5 vezes** — o resumo mostra esse valor separado do aluguel mensal para não confundir o cliente.

No final, o programa imprime o orçamento detalhado no terminal e salva o arquivo **`projecao_12_meses.csv`** na mesma pasta.

## Como a estrutura foi organizada

O código foi pensado com **Programação Orientada a Objetos** para manter cada regra no seu devido lugar:

* `rentsmart.py`: reúne a classe base `Imovel`, as subclasses específicas (`Apartamento`, `Casa` e `Estudio`), a classe `OrcamentoLocacao` (que monta o resumo e exporta o CSV) e as validações de entrada no terminal.
* `projecao_12_meses.csv`: planilha gerada após a execução, mostrando mês a mês o valor do aluguel, a parcela da taxa contratual (enquanto durar o parcelamento) e o total previsto no mês.

## Como testar no seu computador

1. Tenha o **Python 3** instalado na máquina.
2. Abra o terminal na pasta onde está o projeto e rode:
   ```bash
   python rentsmart.py
