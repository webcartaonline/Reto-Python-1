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

## Technologies

- Python 3
- Git and GitHub

## How to run

```bash
python main.py
```
