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


def get_unique_categories(catalog):
    return {piece["category"] for piece in catalog}


def show_piece(piece):
    print(f"ID: {piece['id']}")
    print(f"Name: {piece['name']}")
    print(f"Category: {piece['category']}")
    print(f"Price: {piece['price']:.2f}")
    print(f"Status: {piece['status']}")
    print(f"Description: {piece['description']}")


def show_catalog(catalog):
    print("\n" + "=" * 50)
    print(f"{SYSTEM_NAME} - Full catalog")
    print("=" * 50)
    for piece in catalog:
        print("-" * 50)
        show_piece(piece)


def show_catalog_summary(catalog, categories):
    print("\n" + "=" * 50)
    print("Catalog summary")
    print("=" * 50)
    print(f"Total pieces: {len(catalog)}")
    print(f"Unique categories: {', '.join(sorted(categories))}")
    print(f"Different categories: {len(categories)}")


def main():
    show_welcome_message()
    catalog = register_pieces()
    categories = get_unique_categories(catalog)
    show_catalog(catalog)
    show_catalog_summary(catalog, categories)


if __name__ == "__main__":
    main()
