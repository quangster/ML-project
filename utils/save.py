import pickle


def save_data(data, file_name: str):
    """
    This function takes data and a file name,
    and writes the data to a file in the 'pickle' format.

    Parameters:
    data: The data to be saved.
    file_name (str): The name of the file to save the data to.

    Returns:
    None
    """
    try:
        path = f"data/{file_name}.pkl"
        with open(path, "wb") as f:
            pickle.dump(data, f)
            print(f"Successfully save data: {path}")
    except Exception as e:
        print(f"An error occurred when save pickle file: {e}")


def load_data(file_name: str):
    """
    This function takes a file name,
    and loads data from the file in the 'pickle' format.

    Parameters:
    file_name (str): The name of the file to load the data from.

    Returns:
    The data loaded from the file.
    """
    try:
        path = f"data/{file_name}.pkl"
        with open(path, "rb") as f:
            data = pickle.load(f)
            return data
    except Exception as e:
        print(f"An error occurred when load pickle file: {e}")
        return None
