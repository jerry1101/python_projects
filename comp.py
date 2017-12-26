import filecmp


dc = filecmp.cmp('./local.properties', './local_a.properties')
print ('Common:', dc.common)
print ('Left  :', dc.left_only)
print ('Right :', dc.right_only)
#print ('common_file:') 
#print (filecmp.cmp('./local.properties', 
#                  './local_a.properties'))

