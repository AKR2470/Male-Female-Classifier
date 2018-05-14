#CAUTION : Apply for the correct directory ... Be in the correct directory

import os
i = 0
for dirname in os.listdir("."):
    os.rename(dirname, "Male" + str(i) + ".jpg" )
    i = i+1
