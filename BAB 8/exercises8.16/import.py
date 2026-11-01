# cara 1 : import module_name
import sandwich_helper
sandwich_helper.make_sandwich('tuna', 'keju')

#cara 2 : from module_name import function_name
from sandwich_helper import make_sandwich
make_sandwich('telur', 'selada')

#cara 3 :from module_name import function_name as fn (Pakai alias fungsi)
from sandwich_helper import make_sandwich as ms
ms('daging asap', 'saus mayo')

#cara 4 :import module_name as mn (Pakai alias modul)
import sandwich_helper as sh
sh.make_sandwich('tomat', 'bawang')

#cara 5: from module_name import * (Ambil semua isi modul) 
import sandwich_helper as sh
sh.make_sandwich('tomat', 'bawang')
