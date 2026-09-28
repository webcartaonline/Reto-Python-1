SYSTEM_NAME = "CollectiVault"
TOTAL_PIECES = 10


def show_welcome_message():
    print("=" * 50)
    print(f"Welcome to {SYSTEM_NAME}")
    print("You are entering the collectible pieces catalog.")
    print("=" * 50)


def ask_piece_data(piece_number):
    print(f"\n--- Piece {piece_number} of {TOTAL_PIECES} ---")
    return {
        "id": input("Identifier: ").strip(),
        "name": input("Name: ").strip(),
        "category": input("Category: ").strip(),
        "price": float(input("Price: ")),
        "status": input("Status (disponible/reservada/vendida): ").strip().lower(),
        "description": input("Description: ").strip(),
    }


def register_pieces():
    catalog = []
    for piece_number in range(1, TOTAL_PIECES + 1):
        catalog.append(ask_piece_data(piece_number))
    return catalog


def main():
    show_welcome_message()
    catalog = register_pieces()
    print(f"\n{len(catalog)} pieces registered successfully.")


if __name__ == "__main__":
    main()
