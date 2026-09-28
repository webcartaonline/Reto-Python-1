# CollectiVault

Console program written in Python to manage a basic catalog of collectible pieces.

## Objective

Register collectible pieces from the terminal, query the catalog information,
apply filters, calculate metrics and validate the data entered by the user.

## Catalog context

Each piece in the catalog stores the following data:

| Field         | Type    | Description                          |
|---------------|---------|--------------------------------------|
| `id`          | `str`   | Unique identifier of the piece       |
| `name`        | `str`   | Name of the piece                    |
| `category`    | `str`   | Category the piece belongs to        |
| `price`       | `float` | Sale price or reference value        |
| `status`      | `str`   | `disponible`, `reservada` or `vendida` |
| `description` | `str`   | Must include `usada` or `certificada` |

## Features

- Welcome message when the program starts.
- Registration of 10 collectible pieces from the terminal.
- Full catalog listing with a summary of unique categories.
- Filters by status (`disponible`, `reservada`, `vendida`) and by minimum price.
- Business rules: publication, review and unsold pieces.
- String utilities: concatenation, interpolation, tags parsing,
  description replacement and name formatting.
- Interactive menu that repeats until the user chooses to exit.
- Catalog metrics: pieces per status, total pieces, total and average price,
  and a numbered list of pieces.

## Input validations

When a value is not valid, the program shows a clear message and asks for it again:

- Identifier, name and category cannot be empty.
- The price must be numeric and greater than zero.
- The status must be one of the allowed statuses.
- The description must include `usada` or `certificada`.
- The menu only accepts the listed options.

## Menu options

| Option | Action                    |
|--------|---------------------------|
| 1      | Show all pieces           |
| 2      | Show available pieces     |
| 3      | Show average price        |
| 4      | Show catalog metrics      |
| 5      | Exit                      |

## Technologies

- Python 3
- Git and GitHub

## How to run

```bash
python main.py
```

## Project structure

```text
.
├── main.py     # Program source code
└── README.md   # Project documentation
```
