import matplotlib.pyplot as plt
import numpy as np
import os


def create_grids(initial_n, final_n, L):
    def create_all_grids(L, initial_n, final_n):
        """
        Generates a series of LxL grids, starting with initial_n occupied sites,
        and incrementally adds sites up to final_n, storing each grid state.
        
        Args:
        - L (int): The dimension of the grid (LxL).
        - initial_n (int): The initial number of occupied sites.
        - final_n (int): The final number of occupied sites.
        
        Returns:
        - list: A list of numpy.ndarray, each representing a grid state.
        """
        if final_n > L*L:
            raise ValueError("Final number of occupied sites cannot exceed total grid sites.")
        if initial_n > final_n:
            raise ValueError("Initial number of occupied sites cannot be greater than final number.")

        # Initialize the initial grid
        grid = np.zeros((L, L), dtype=int)
        occupied_positions = np.random.choice(L*L, size=initial_n, replace=False)
        for pos in occupied_positions:
            row = pos // L
            col = pos % L
            grid[row, col] = 1

        grids = [grid.copy()]  # Store the initial grid state

        # Incrementally add occupied sites and store each grid state
        current_n = initial_n
        while current_n < final_n:
            unoccupied_positions = np.where(grid.flatten() == 0)[0]
            new_pos = np.random.choice(unoccupied_positions, size=1)
            row, col = divmod(new_pos[0], L)
            grid[row, col] = 1
            current_n += 1
            grids.append(grid.copy())

        return grids
    return create_all_grids(L, initial_n, final_n)










""" def create_grids_plots(initial_n, final_n, L):

    def plot_grid(grid, filepath):
       
        plt.figure(figsize=(L, L))
        plt.imshow(grid, cmap='Greys', interpolation='nearest')
        plt.colorbar(label='Occupied Sites')
        plt.title('Grid Visualization')
        plt.savefig(filepath)
        plt.close() """


"""   def create_all_grids(L, initial_n, final_n):
    
    if final_n > L*L:
        raise ValueError("Final number of occupied sites cannot exceed total grid sites.")
    if initial_n > final_n:
        raise ValueError("Initial number of occupied sites cannot be greater than final number.")

    # Initialize the initial grid
    grid = np.zeros((L, L), dtype=int)
    occupied_positions = np.random.choice(L*L, size=initial_n, replace=False)
    for pos in occupied_positions:
        row = pos // L
        col = pos % L
        grid[row, col] = 1

    grids = [grid.copy()]  # Store the initial grid state

    # Incrementally add occupied sites and store each grid state
    current_n = initial_n
    while current_n < final_n:
        unoccupied_positions = np.where(grid.flatten() == 0)[0]
        new_pos = np.random.choice(unoccupied_positions, size=1)
        row, col = divmod(new_pos[0], L)
        grid[row, col] = 1
        current_n += 1
        grids.append(grid.copy())

    return grids


def save_grid_plots(grids, directory):
    
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create the directory if it does not exist
    
    for i, grid in enumerate(grids):
        filepath = os.path.join(directory, f'grid_{i}.png')
        plot_grid(grid, filepath)
        print(f'Saved: {filepath}')

save_grid_plots(create_all_grids(L, initial_n, final_n), 'c:\\Users\\Florian\\Desktop\\Studium\\5.Semester\\simo23\\Projekt\\plots') """

