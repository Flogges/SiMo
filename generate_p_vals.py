import numpy as np
import generate_grid
import union_find
import matplotlib.pyplot as plt

def generate_grid_dict(dict_size, n_max, L):
    grid_dict = {}
    for i in range(0, dict_size):
        grid_dict[f'gridlist{i}'] = generate_grid.create_grids(0, n_max, L)
    return grid_dict

def grid_to_p_vals(dict_size, n_max, L):
    grid_dict = generate_grid_dict(dict_size, n_max, L)
    p_vals = []
    for key in grid_dict:
        processed_grids = union_find.process_grids(grid_dict[key]) #returns a list of ones and zeros
        first_percolation = find_first_one(processed_grids)
        p_current = first_percolation/(L*L)
        p_vals.append(p_current)
    return p_vals
    # return processed_grids



def find_first_one(lst):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == 1 and (mid == 0 or lst[mid - 1] == 0):
            return mid
        elif lst[mid] == 1:
            high = mid - 1
        else:
            low = mid + 1
    return -1  # Return -1 if there are no ones in the list


#we have an L*L sized grid
#we have a bucket of tickets, each one correspondimg to a unique square on the grid
#we perform an experiment(e_y), each step (s) of which picks aticket of the bucket randomly and turns the corresponding square black
#when we see that percolation at step s_p, we define p_c = s_p/L*L
#we perform the experiment a total number of times e_ymax and therefore get a list (s_p_e) of s_p's and p_c's (p_c_e)

#create_y_vals receives the list p_vals, that contains the probabilities, at which percolation occured the first time. 


#dict_size represents the amount of grid-evolutions
#n-max is the amount of black squares we occupiy at the most
#L is the length of one side of the grid 

#dict_size = e_ymax, nmax = is the step, when the grid stops to have squares turn black,
# todo : get rid of n_max
def create_y_vals(dict_size, n_max, L):  
    p_vals = grid_to_p_vals(dict_size, n_max, L)
    Qp = [0]*100
    for p in p_vals:
        Qp[(int(p*100))] += 1
    return Qp

print(create_y_vals(100, 100, 10))
x_vals = np.arange(0, 1, 0.01)
print(grid_to_p_vals(500, 100, 10))
plt.plot(x_vals, create_y_vals(500, 100, 10), marker='o')  # 'o' adds circle markers to each data point
plt.xlabel('p')  # Optional: Add label for the x-axis
plt.ylabel('N (occurence of first perculation)')  # Optional: Add label for the y-axis
plt.title('Simple Plot')   # Optional: Add title to the plot
plt.grid(True)              # Optional: Show grid
plt.show()