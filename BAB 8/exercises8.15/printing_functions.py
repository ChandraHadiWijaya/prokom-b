# printing models

def print_models(unprinted_designs, completed_models):
    """Simulasi mencetak setiap desain 3D sampai habis."""
    while unprinted_designs:
        current_design = unprinted_designs.pop(0)
        print(f"Sedang mencetak model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Menampilkan semua model yang selesai dicetak."""
    print("\nBerikut model yang sudah jadi:")
    for model in completed_models:
        print(f"- {model}")
