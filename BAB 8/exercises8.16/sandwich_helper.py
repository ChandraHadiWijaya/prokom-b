#import


def make_sandwich(*items):
    """Menampilkan isi sandwich."""
    print("\n🥪 Sandwich kamu isinya:")
    for item in items:
        print(f"  - {item}")
