import hgvs.parser
import hgvs.dataproviders.uta 
import hgvs.variantmapper
import hgvs.assemblymapper


hdp = hgvs.dataproviders.uta.connect()
hp = hgvs.parser.Parser()

file = open('hgvs_c_to_g_variant_list.txt', 'r')


proc_line = 'NM_004006.2:c.92_93ins90_93'
var = hp.parse_hgvs_variant(proc_line)
print(f"no error parsing {var}")
vm = hgvs.assemblymapper.AssemblyMapper(
    hdp, assembly_name='GRCh38')
var_g = vm.c_to_g(var)
print(var_g)
print(var_g.posedit)