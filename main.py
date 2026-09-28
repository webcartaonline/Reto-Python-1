SYSTEM_NAME = "CollectiVault"
TOTAL_PIECES = 10
ALLOWED_STATUSES = ("disponible", "reservada", "vendida")
REQUIRED_DESCRIPTION_WORDS = ("usada", "certificada")


def show_welcome_message():
    print("=" * 50)
    print(f"Welcome to {SYSTEM_NAME}")
    print("You are entering the collectible pieces catalog.")
    print("=" * 50)


def ask_non_empty_text(prompt, field_name):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(f"{field_name} cannot be empty. Please try again.")


def ask_positive_price():
    while True:
        raw_price = input("Price: ").strip()
        try:
            price = float(raw_price)
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
            continue
        if price > 0:
            return price
        print("Invalid price. It must be greater than zero.")


def ask_status():
    allowed = "/".join(ALLOWED_STATUSES)
    while True:
        status = input(f"Status ({allowed}): ").strip().lower()
        if status in ALLOWED_STATUSES:
            return status
        print(f"Invalid status. Allowed values: {', '.join(ALLOWED_STATUSES)}.")


def has_required_word(description):
    lower_description = description.lower()
    return any(word in lower_description for word in REQUIRED_DESCRIPTION_WORDS)


def ask_description():
    while True:
        description = ask_non_empty_text("Description: ", "Description")
        if has_required_word(description):
            return description
        print("Invalid description. It must include 'usada' or 'certificada'.")


def ask_piece_data(piece_number):
    print(f"\n--- Piece {piece_number} of {TOTAL_PIECES} ---")
    return {
        "id": ask_non_empty_text("Identifier: ", "Identifier"),
        "name": ask_non_empty_text("Name: ", "Name"),
        "category": ask_non_empty_text("Category: ", "Category"),
        "price": ask_positive_price(),
        "status": ask_status(),
        "description": ask_description(),
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


def can_be_published(piece):
    return piece["price"] > 0 and piece["status"] == "disponible"


def requires_review(piece):
    return piece["status"] == "reservada" or piece["status"] == "vendida"


def filter_unsold(catalog):
    return [piece for piece in catalog if not piece["status"] == "vendida"]


def format_yes_no(condition):
    return "Yes" if condition else "No"


def show_business_rules(catalog):
    print("\n--- Publication and review rules ---")
    for piece in catalog:
        print(
            f"[{piece['id']}] {piece['name']} -> "
            f"Can be published: {format_yes_no(can_be_published(piece))} | "
            f"Requires review: {format_yes_no(requires_review(piece))}"
        )
    show_filtered_pieces("Unsold pieces", filter_unsold(catalog))


def show_piece_concatenated(piece):
    print("Piece " + piece["id"] + ": " + piece["name"] + " (" + piece["category"] + ") - " + str(piece["price"]))


def show_piece_interpolated(piece):
    print(f"Piece {piece['id']}: {piece['name']} ({piece['category']}) - {piece['price']:.2f}")


def parse_tags(raw_tags):
    return [tag.strip() for tag in raw_tags.split(",") if tag.strip()]


def replace_used_with_certified(description):
    return description.replace("usada", "certificada")


def normalize_piece_name(name):
    return " ".join(name.split()).title()


def show_user_name_formats(user_name):
    clean_name = user_name.strip()
    print(f"Trimmed: '{clean_name}'")
    print(f"Lowercase: {clean_name.lower()}")
    print(f"Uppercase: {clean_name.upper()}")
    print(f"Title: {clean_name.title()}")


def show_string_operations(catalog):
    print("\n--- String operations ---")
    piece = catalog[0]
    show_piece_concatenated(piece)
    show_piece_interpolated(piece)

    tags = parse_tags(input("\nEnter tags separated by commas: "))
    print(f"Tags: {tags}")

    print(f"Original description: {piece['description']}")
    print(f"Updated description: {replace_used_with_certified(piece['description'])}")

    show_user_name_formats(input("\nEnter your user name: "))
    print(f"Normalized piece name: {normalize_piece_name(piece['name'])}")


def count_by_status(catalog, status):
    return len(filter_by_status(catalog, status))


def calculate_total_price(catalog):
    return sum(piece["price"] for piece in catalog)


def calculate_average_price(catalog):
    if not catalog:
        return 0.0
    return calculate_total_price(catalog) / len(catalog)


def show_enumerated_pieces(catalog):
    for position, piece in enumerate(catalog, start=1):
        print(f"{position}. {piece['name']}")


def show_catalog_metrics(catalog):
    print("\n--- Catalog metrics ---")
    for status in ALLOWED_STATUSES:
        print(f"Pieces '{status}': {count_by_status(catalog, status)}")
    print(f"Total pieces: {len(catalog)}")
    print(f"Total price: {calculate_total_price(catalog):.2f}")
    print(f"Average price: {calculate_average_price(catalog):.2f}")
    print("\nNumbered pieces:")
    show_enumerated_pieces(catalog)


def show_average_price(catalog):
    print(f"\nAverage price: {calculate_average_price(catalog):.2f}")


def show_menu():
    print("\n" + "=" * 50)
    print(f"{SYSTEM_NAME} - Main menu")
    print("=" * 50)
    print("1. Show all pieces")
    print("2. Show available pieces")
    print("3. Show average price")
    print("4. Show catalog metrics")
    print("5. Exit")


def run_menu(catalog):
    menu_actions = {
        "1": lambda: show_catalog(catalog),
        "2": lambda: show_filtered_pieces(
            "Available pieces", filter_by_status(catalog, "disponible")
        ),
        "3": lambda: show_average_price(catalog),
        "4": lambda: show_catalog_metrics(catalog),
    }
    while True:
        show_menu()
        option = input("Choose an option: ").strip()
        if option == "5":
            print(f"\nThank you for using {SYSTEM_NAME}. Goodbye!")
            break
        action = menu_actions.get(option)
        if action is None:
            print("Invalid option. Please choose a number from 1 to 5.")
            continue
        action()


def main():
    show_welcome_message()
    catalog = register_pieces()
    categories = get_unique_categories(catalog)
    show_catalog(catalog)
    show_catalog_summary(catalog, categories)
    show_pieces_by_status(catalog)
    show_pieces_above_price(catalog)
    show_business_rules(catalog)
    show_string_operations(catalog)
    run_menu(catalog)


if __name__ == "__main__":
    main()
