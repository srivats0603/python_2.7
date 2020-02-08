import sys
sys.path.append(r'C:\Users\IBM_ADMIN\Documents\PythonScripts\generalexamples\createPackages\package0')
print sys.path
from Module1 import println

println("")
println("hi how are you")
println(1234)
println(str(12)+"34$")

sys.path.append(r'C:\Users\IBM_ADMIN\Documents\PythonScripts\generalexamples\createPackages\package2')
#package2 does not have an __init__ file
from Module4 import printline
printline("hi how are you")
