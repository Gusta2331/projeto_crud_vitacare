def menu_relatorios(consulta_service):

    while True:

        print("\n" + "=" * 55)
        print("              VITACARE - RELATÓRIOS")
        print("=" * 55)

        print("1 - Atendimentos e faturamento por médico")
        print("2 - Média do valor das consultas por especialidade")
        print("0 - Voltar ao menu principal")

        print("=" * 55)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":

            print("\n")
            print("=" * 70)
            print("       RELATÓRIO DE ATENDIMENTOS E FATURAMENTO")
            print("=" * 70)

            resultados = consulta_service.get_atendimentos_faturamento_por_medico()

            if not resultados:

                print("\nNenhum médico cadastrado.")

            else:

                print(
                    f"\n{'MÉDICO':<30}"
                    f"{'CONSULTAS':>12}"
                    f"{'FATURAMENTO':>20}"
                )

                print("-" * 70)

                faturamento_geral = 0
                total_consultas = 0

                for item in resultados:

                    nome = item["nome"]
                    quantidade = item["quantidade"]
                    faturamento = item["faturamento_total"]

                    print(
                        f"{nome:<30}"
                        f"{quantidade:>12}"
                        f"R$ {faturamento:>16.2f}"
                    )

                    total_consultas += quantidade
                    faturamento_geral += faturamento

                print("-" * 70)

                print(
                    f"{'TOTAL GERAL':<30}"
                    f"{total_consultas:>12}"
                    f"R$ {faturamento_geral:>16.2f}"
                )

            print("=" * 70)

        elif opcao == "2":

            print("\n")
            print("=" * 65)
            print("       MÉDIA DO VALOR POR ESPECIALIDADE")
            print("=" * 65)

            resultados = consulta_service.get_media_valor_por_especialidade()

            if not resultados:

                print("\nNenhuma consulta encontrada.")

            else:

                print(
                    f"\n{'ESPECIALIDADE':<35}"
                    f"{'MÉDIA DAS CONSULTAS':>25}"
                )

                print("-" * 65)

                for item in resultados:

                    especialidade = item["especialidade"]
                    media = item["media_valor"]

                    print(
                        f"{especialidade:<35}"
                        f"R$ {media:>21.2f}"
                    )

            print("=" * 65)

        elif opcao == "0":

            print("\nVoltando ao menu principal...")

            break

        else:

            print("\nOpção inválida! Tente novamente.")

        input("\nPressione ENTER para continuar...")