from city_functions import format_city_country

def test_city_country():
    """Memverifikasi pemanggilan fungsi dengan 2 parameter (Solo tanpa jumlah penduduk)."""
    hasil_format = format_city_country('solo', 'indonesia')
    assert hasil_format == 'Solo, Indonesia'

def test_city_country_population():
    """Memverifikasi pemanggilan fungsi dengan 3 parameter (Solo dengan jumlah penduduk)."""
    hasil_format = format_city_country('solo', 'indonesia', population=500000)
    assert hasil_format == 'Solo, Indonesia - population 500000'
