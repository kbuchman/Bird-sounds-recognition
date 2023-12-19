
"""
fucntion that analyszes and picks files to use as test subset

"""

def choose_filesI(std_devs: dict, n: int):
    """function accepts a dictionary of file paths, and their standard deviations. Analyzes standard deviations, and saves paths to test files

    Args:
        std_devs (dict): file_path: std_dev
    
    Returns:
        test_file_paths (list): list of test files 
    """
    
    #TODO:
        # Plot histogram ????
        # Take X highest value stds
        # Save their paths
    
    sorted_paths = list(dict(sorted(std_devs.items(), key = lambda x:x[1])).keys())
    return sorted_paths[-n:]