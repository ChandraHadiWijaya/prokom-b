#informasi mobil

def make_car(manufacturer, model, **car_info):
    """Menyimpan informasi tentang mobil ke dalam dictionary."""
    car_info['manufacturer_name'] = manufacturer
    car_info['model_name'] = model
    return car_info


car = make_car('ford', 'ranger', color='black', transmission='manual', drive_type='4x4')

print("\n🚗 Data mobil berhasil disimpan:")
print(car)
