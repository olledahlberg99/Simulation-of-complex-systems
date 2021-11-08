import numpy as np 
from tkinter import *
from PIL import Image
from PIL import ImageTk as itk
import time
import matplotlib.pyplot as plt

res = 500   # Animation resolution
tk = Tk()  
tk.geometry( str(int(res*1.1)) + 'x'  +  str(int(res*1.3)) )
tk.configure(background='white')

canvas = Canvas(tk, bd=2)            # Generate animation window 
tk.attributes('-topmost', 0)
canvas.place(x=res/20, y=res/20, height= res, width= res)
ccolor = ['#0008FF', '#DB0000', '#12F200']



# Parameters of the simulation
l = 16     # Lattice size

# Physical parameters of the system 
S = np.zeros((l,l))                     # Status array, 0: No trees, 1: Trees 2: Burned  3: Expanding fire  
forest_image = np.zeros((l,l,3))        # Image array for the forest
fire_count = 0                          # Number of fire events
count = 0
fire_store = []
while count < 10000:
    
    count += 1
    R = 0.01               # get growth rate from GUI
    LP = 0.2         # get lightning probability from GUI

    S[( np.random.rand(l,l)<R ) & (S==0) ] = 1                # Apply tree growth with the corresponding probability
    lightning_location = (np.random.rand(2)*l).astype(int)    # Randomly select a lightning location   
    if (S[lightning_location[0],lightning_location[1]] == 1) and (np.random.rand()<LP):    # If lightning falls on a tree
        numberOfTreesBurned = 1
        fire_count += 1                                                       # Fire event
        S[lightning_location[0],lightning_location[1]] = 3                    # Start expanding fire
        while sum(sum(S==3))>0:                                               # fire expansion loop
            for i,j in zip(np.where(S==3)[0],np.where(S==3)[1]):              # loop over expanding nodes
                if S[min(i+1,l-1),j] == 1:                                    # check expansion to the right
                    S[min(i+1,l-1),j] = 3
                    numberOfTreesBurned += 1
                if S[max(i-1,0),j] == 1:                                      # check expansion to the left
                    S[max(i-1,0),j] = 3
                    numberOfTreesBurned += 1
                if S[i,min(j+1,l-1)] == 1:                                    # check expansion upwards   
                    S[i,min(j+1,l-1)] = 3
                    numberOfTreesBurned += 1
                if S[i,max(j-1,0)] == 1:                                      # check expansion downwards
                    S[i,max(j-1,0)] = 3
                    numberOfTreesBurned += 1
                
                S[i,j] = 2                                                    # previous expansion node burned   
        
        fire_store.append(numberOfTreesBurned)

    forest_image[:,:,:] = 0                               # Create image object for the forest, background black
    forest_image[:,:,0] =   (S == 2)*255                  # Burned trees are red
    forest_image[:,:,1] =   (S == 1)*255                  # Grown trees are green
    img = itk.PhotoImage(Image.fromarray(np.uint8(forest_image),'RGB').resize((res,res)))
    canvas.create_image(0,0, anchor=NW, image=img) 
    tk.title('Fires:' + str(fire_count))
    tk.update()
    if sum(sum(S==2))>0:
        time.sleep(0.05)
    
    S[S==2] = 0                                           # Burned trees will go back to status 0 (no trees)
    print(count)

Tk.mainloop(canvas)                                     # Release animation handle (close window to finish)

print(fire_store)
plt.hist(fire_store, bins = 20) 
plt.title("Forest fire histogram")
plt.show()