"""
Exercise No. 59

Create a function that returns the count of all bridges in a two-dimensional grid.

Bridge B should be counted if:
    - It connects from one end of the grid to the one opposite do it.
    - It is unobstructed.

Examples:
    "#########/#    #/# #   #/#  #   #/###      ####/#      #       #/#     #   #/#     #/#########"

In this case the number 4 is returned because, when unraveled, the string reveals four bridges that meet the
requirements listed above as show:
    ########/
    #      #/
    #   #  #/
    ###  ###/
    #   #  #/
    #   #  #/
    #      #/
    ########

Notes:
    - Slashes / act as separators.
    - Intersecting bridges can still count, as shown.
    - Vertical bridges count as long as the requirements are met.
"""


def bridges(s):
    arr = s.split('/')
    hori = sum(set(i) == {'#'} for i in arr)
    vert = sum(set(i) == {'#'} for i in zip(*arr))
    return hori + vert


print(bridges("#########/#    #/# #   #/#  #   #/###     ####/#     #      #/#    #   #/#     #/#########"))
