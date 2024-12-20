import gameStore
import time
import os
import addGames
# Trabalho feito por Samuel e Marcelo

def main():
    store = gameStore.GameStore()
    addGames.addGames(store)

    while True:
        print("\n--- SteamMS ---")
        print("\033[32m1. Adicionar Jogo\033[0m")
        print("2. Buscar Jogos por Preço")
        print("3. Buscar Jogos por Faixa de Preço")
        print("4. Buscar Jogos por Gênero")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            game_id = int(input("ID do Jogo: "))
            title = input("Título do Jogo: ")
            price = int(input("Preço do Jogo (inteiro): "))
            genres = input("Gêneros do Jogo (separados por vírgula): ").split(",")
            time.sleep(2)
            os.system("cls")
            genres = [genre.strip() for genre in genres]
            store.add_game(game_id, title, price, genres)
            print(f"Jogo '{title}' adicionado com sucesso!")

        elif choice == "2":
            price = int(input("Digite o preço para busca: "))
            time.sleep(2)
            os.system("cls")
            games = store.search_by_price(price)
            if games:
                time.sleep(2)
                os.system("cls")
                print("Jogos encontrados:")
                for game in games:
                    print(
                        f"\033[34mID:\033[0m {game['id']}, \033[32mTítulo:\033[0m {game['title']}, \033[36mPreço:\033[0m {game['price']}, \033[35mGêneros:\033[0m {', '.join(game['genres'])}"
                    )
            else:
                print("Nenhum jogo encontrado com esse preço.")

        elif choice == "3":
            min_price = int(input("Preço mínimo: "))
            max_price = int(input("Preço máximo: "))
            time.sleep(2)
            os.system("cls")
            games = store.search_by_price_range(min_price, max_price)
            if games:
                print("Jogos encontrados:")
                for game in games:
                    print(
                        f"\033[34mID:\033[0m {game['id']}, \033[32mTítulo:\033[0m {game['title']}, \033[36mPreço:\033[0m {game['price']}, \033[35mGêneros:\033[0m {', '.join(game['genres'])}"
                    )
            else:
                print("Nenhum jogo encontrado na faixa de preço.")

        elif choice == "4":
            genre = input("Digite o gênero para busca: ").strip()
            time.sleep(2)
            os.system("cls")
            games = store.search_by_genre(genre)
            if games:
                print("Jogos encontrados:")
                for game in games:
                    print(
                        f"\033[34mID:\033[0m {game['id']}, \033[32mTítulo:\033[0m {game['title']}, \033[36mPreço:\033[0m {game['price']}, \033[35mGêneros:\033[0m {', '.join(game['genres'])}"
                    )
            else:
                print("Nenhum jogo encontrado para esse gênero.")

        elif choice == "5":
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()
