import hgvs.parser
import hgvs.dataproviders.uta 
import hgvs.variantmapper
import hgvs.assemblymapper
import json

hdp = hgvs.dataproviders.uta.connect()
hp = hgvs.parser.Parser()
vm = hgvs.assemblymapper.AssemblyMapper(
    hdp, assembly_name='GRCh38')

file = open('hgvs_c_to_g_variant_list.txt', 'r')

var_dict = {}

for line in file:
    line_dict = {}
    proc_line = line.strip()
    if proc_line.startswith('N'):
        
        try:
            var = hp.parse_hgvs_variant(proc_line)
            vm.c_to_g(var)
        except Exception as e: 
            var_dict[proc_line] = f'invalid format error {e}'
        else:
            var = hp.parse_hgvs_variant(proc_line)
            var_g = vm.c_to_g(var)
            line_dict['start'] = str(var_g.posedit.pos.start)
            line_dict['end'] = str(var_g.posedit.pos.end)
            line_dict['ref'] = str(var_g.posedit.edit.ref)
            if str(var_g).find('dup') == -1 and str(var_g).find('inv') == -1:
                line_dict['alt'] = var_g.posedit.edit.alt

            var_dict[proc_line] = line_dict

with open('results.json', 'w') as outfile:
    json.dump(var_dict, outfile, indent = 2)


