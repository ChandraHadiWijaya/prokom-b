#sandwich

def make_sandwich(*items):
    """Menampilkan ringkasan isian sandwich yang dipesan."""
    print("\n🥪 Membuat sandwich pesanan kamu dengan isian:")
    for item in items:
        print(f"  - {item}")

make_sandwich('tuna', 'keju slice', 'selada')
make_sandwich('telur mata sapi', 'saus mayo')
make_sandwich('daging asap', 'tomat', 'bawang bombay', 'keju lumer')

