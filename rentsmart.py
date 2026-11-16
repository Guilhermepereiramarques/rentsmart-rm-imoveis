import csv


class Imovel:
    def __init__(self, tipo, valor_base):
        self.tipo = tipo
        self.valor_base = valor_base

    def calcular_aluguel(self):
        return self.valor_base


class Apartamento(Imovel):
    def __init__(self, quartos, tem_garagem, tem_criancas):
        super().__init__("Apartamento", 700.00)
        self.quartos = quartos
        self.tem_garagem = tem_garagem
        self.tem_criancas = tem_criancas

    def calcular_aluguel(self):
        valor = self.valor_base
        if self.quartos == 2:
            valor += 200.00
        if self.tem_garagem:
            valor += 300.00
        if not self.tem_criancas:
            valor = valor * 0.95
        return valor


class Casa(Imovel):
    def __init__(self, quartos, tem_garagem):
        super().__init__("Casa", 900.00)
        self.quartos = quartos
        self.tem_garagem = tem_garagem

    def calcular_aluguel(self):
        valor = self.valor_base
        if self.quartos == 2:
            valor += 250.00
        if self.tem_garagem:
            valor += 300.00
        return valor


class Estudio(Imovel):
    def __init__(self, vagas_estacionamento):
        super().__init__("Estúdio", 1200.00)
        self.vagas_estacionamento = vagas_estacionamento

    def calcular_aluguel(self):
        valor = self.valor_base
        if self.vagas_estacionamento > 0:
            valor += 250.00
            if self.vagas_estacionamento > 2:
                vagas_extras = self.vagas_estacionamento - 2
                valor += vagas_extras * 60.00
        return valor


class OrcamentoLocacao:
    TAXA_CONTRATUAL = 2000.00

    def __init__(self, imovel, parcelas_taxa):
        self.imovel = imovel
        self.parcelas_taxa = parcelas_taxa
        self.aluguel_mensal = self.imovel.calcular_aluguel()
        self.valor_parcela_taxa = self.TAXA_CONTRATUAL / self.parcelas_taxa

    def exibir_resumo(self):
        print("\n" + "=" * 50)
        print("       ORÇAMENTO DE LOCAÇÃO - R.M IMÓVEIS")
        print("=" * 50)
        print(f"Categoria do Imóvel : {self.imovel.tipo}")
        print(f"Aluguel-Base        : R$ {self.imovel.valor_base:.2f}")

        if isinstance(self.imovel, Apartamento):
            print(f"Quartos             : {self.imovel.quartos}")
            print(f"Vaga de Garagem     : {'Sim (+R$ 300,00)' if self.imovel.tem_garagem else 'Não'}")
            print(f"Possui Crianças     : {'Sim' if self.imovel.tem_criancas else 'Não (Desconto de 5% aplicado)'}")
        elif isinstance(self.imovel, Casa):
            print(f"Quartos             : {self.imovel.quartos}")
            print(f"Vaga de Garagem     : {'Sim (+R$ 300,00)' if self.imovel.tem_garagem else 'Não'}")
        elif isinstance(self.imovel, Estudio):
            print(f"Vagas Estacionamento: {self.imovel.vagas_estacionamento}")

        print("-" * 50)
        print(f"ALUGUEL MENSAL FINAL: R$ {self.aluguel_mensal:.2f}")
        print("-" * 50)
        print(f"Taxa Contratual     : R$ {self.TAXA_CONTRATUAL:.2f} (custo separado)")
        print(f"Parcelamento Taxa   : {self.parcelas_taxa}x de R$ {self.valor_parcela_taxa:.2f}")
        print("=" * 50)

    def gerar_csv_12_meses(self, nome_arquivo="projecao_12_meses.csv"):
        with open(nome_arquivo, mode="w", newline="", encoding="utf-8-sig") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow([
                "Mês",
                "Categoria",
                "Aluguel Mensal (R$)",
                "Parcela Taxa Contratual (R$)",
                "Total Previsto no Mês (R$)"
            ])

            for mes in range(1, 13):
                parcela_atual = self.valor_parcela_taxa if mes <= self.parcelas_taxa else 0.0
                total_mes = self.aluguel_mensal + parcela_atual
                escritor.writerow([
                    f"Mês {mes}",
                    self.imovel.tipo,
                    f"{self.aluguel_mensal:.2f}".replace(".", ","),
                    f"{parcela_atual:.2f}".replace(".", ","),
                    f"{total_mes:.2f}".replace(".", ",")
                ])

        print(f"\nArquivo '{nome_arquivo}' gerado com sucesso!")


def ler_opcao(mensagem, opcoes_validas):
    while True:
        escolha = input(mensagem).strip().lower()
        if escolha in opcoes_validas:
            return escolha
        print(f"Opção inválida! Digite uma das opções: {', '.join(opcoes_validas)}")


def ler_inteiro(mensagem, minimo, maximo=None):
    while True:
        try:
            valor = int(input(mensagem).strip())
            if valor < minimo:
                print(f"O valor deve ser no mínimo {minimo}.")
            elif maximo is not None and valor > maximo:
                print(f"O valor deve ser no máximo {maximo}.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")


def main():
    print("=== SISTEMA RENTSMART - R.M IMÓVEIS ===")
    print("1 - Apartamento (Base: R$ 700,00)")
    print("2 - Casa        (Base: R$ 900,00)")
    print("3 - Estúdio     (Base: R$ 1.200,00)")

    categoria = ler_opcao("Escolha a categoria do imóvel (1/2/3): ", ["1", "2", "3"])

    if categoria == "1":
        quartos = ler_inteiro("Quantidade de quartos (1 ou 2): ", 1, 2)
        garagem = ler_opcao("Deseja vaga de garagem? (s/n): ", ["s", "n"]) == "s"
        criancas = ler_opcao("Possui crianças morando no imóvel? (s/n): ", ["s", "n"]) == "s"
        imovel = Apartamento(quartos, garagem, criancas)

    elif categoria == "2":
        quartos = ler_inteiro("Quantidade de quartos (1 ou 2): ", 1, 2)
        garagem = ler_opcao("Deseja vaga de garagem? (s/n): ", ["s", "n"]) == "s"
        imovel = Casa(quartos, garagem)

    else:
        quer_vagas = ler_opcao("Deseja pacote de estacionamento? (s/n): ", ["s", "n"])
        if quer_vagas == "s":
            vagas = ler_inteiro("Quantas vagas deseja? (mínimo 2 no pacote inicial): ", 2)
        else:
            vagas = 0
        imovel = Estudio(vagas)

    parcelas = ler_inteiro("Em quantas parcelas deseja pagar a taxa contratual de R$ 2.000,00? (1 a 5): ", 1, 5)

    orcamento = OrcamentoLocacao(imovel, parcelas)
    orcamento.exibir_resumo()
    orcamento.gerar_csv_12_meses()


if __name__ == "__main__":
    main()