# Set the player name (7 chars) for Minecraft PI Edition
# Written by Richard Garsthagen - richard@coderdojo-zoetermeer.nl
#
# Use at own risk. Please make a backup of minecraft-pi first!
#
# Close Minecraft PI before using!
#

namestart= 1026250

fh = open("/opt/minecraft-pi/minecraft-pi", "r+b")
fh.seek(namestart)

print ("Current name: {} ".format(fh.read(7)))

piname = raw_input("New player name: ")

if len(piname) > 1:
    if len(piname) > 7: piname = piname[:7]
    if len(piname) < 7:
        extraspaces = 7 - len(piname)
        for x in xrange(0,extraspaces):
            piname = piname + " "
    print ("Changed name to:" + piname + " - " + str(len(piname)))
    fh.seek(namestart)
    fh.write(piname)
else:
    print ("No new name given")

fh.close()
