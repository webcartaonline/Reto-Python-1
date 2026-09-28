SYSTEM_NAME = "CollectiVault"
TOTAL_PIECES = 10
ALLOWED_STATUSES = ("disponible", "reservada", "vendida")


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


def filter_by_status(catalog, status):
    return [piece for piece in catalog if piece["status"] == status]


def filter_by_min_price(catalog, min_price):
    return [piece for piece in catalog if piece["price"] > min_price]


def show_piece_short(piece):
    print(f"[{piece['id']}] {piece['name']} - {piece['price']:.2f} ({piece['status']})")


def show_filtered_pieces(title, pieces):
    print(f"\n--- {title} ---")
    if not pieces:
        print("No pieces found.")
        return
    for piece in pieces:
        show_piece_short(piece)


def show_pieces_by_status(catalog):
    for status in ALLOWED_STATUSES:
        show_filtered_pieces(f"Pieces with status '{status}'", filter_by_status(catalog, status))


def ask_min_price():
    while True:
        try:
            return float(input("\nEnter a minimum price: "))
        except ValueError:
            print("Invalid price. Please enter a numeric value.")


def show_pieces_above_price(catalog):
    min_price = ask_min_price()
    pieces = filter_by_min_price(catalog, min_price)
    show_filtered_pieces(f"Pieces with price above {min_price:.2f}", pieces)


def main():
    show_welcome_message()
    catalog = register_pieces()
    categories = get_unique_categories(catalog)
    show_catalog(catalog)
    show_catalog_summary(catalog, categories)
    show_pieces_by_status(catalog)
    show_pieces_above_price(catalog)


if __name__ == "__main__":
    main()
