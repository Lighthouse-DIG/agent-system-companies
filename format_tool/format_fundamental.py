class KeyValueRecursiveFlatten:
    """
    A class to recursively flatten nested dictionaries and lists into a key-value pair format.
    """

    def __init__(self):
        """
        Initializes the KeyValueRecursiveFlatten object and sets the initial output to None.
        """
        self._output = None

    def __call__(self, data: dict):
        """
        Flattens a nested dictionary or list and formats the output into a key-value pair format.
        
        Args:
            data (dict): The input dictionary to be flattened.
        
        Returns:
            str: The flattened dictionary in key-value pair format.
        """
        self._output = {}
        self._key_value_recursive_dict_flatten(data)
        return self._format_output()

    def _key_value_recursive_dict_flatten(self, data_dict, pattern_key=""):
        """
        Recursively flattens a dictionary into a key-value pair format.
        
        Args:
            data_dict (dict): The dictionary to be flattened.
            pattern_key (str, optional): The key path used to build the final key. Defaults to an empty string.
        """
        for key, data_inside in data_dict.items():
            self._process(key, data_inside, pattern_key)

    def _key_value_recursive_list_flatten(self, data_list, pattern_key=""):
        """
        Recursively flattens a list into a key-value pair format.

        Args:
            data_list (list): The list to be flattened.
            pattern_key (str, optional): The key path used to build the final key. Defaults to an empty string.
        """
        for key, data_inside in enumerate(data_list):
            self._process(key, data_inside, pattern_key)

    def _process(self, key, data_inside, pattern_key):
        """
        Processes each item in the dictionary or list, adding it to the output with the appropriate key.
        
        Args:
            key (str): The current key in the dictionary or index in the list.
            data_inside (various): The value associated with the current key or index.
            pattern_key (str): The current key path to form the final key.
        """
        new_pattern_key = f"{pattern_key}.{key}" if pattern_key else key
        if isinstance(data_inside, dict):
            self._key_value_recursive_dict_flatten(data_dict=data_inside, pattern_key=new_pattern_key)
        elif isinstance(data_inside, list):
            self._key_value_recursive_list_flatten(data_list=data_inside, pattern_key=new_pattern_key)
        elif isinstance(data_inside, str):
            self._output[new_pattern_key] = data_inside
        else:
            self._output[new_pattern_key] = str(data_inside)

    def _format_output(self):
        """
        Formats the flattened output into a string representation with each key-value pair separated by a newline.
        
        Returns:
            str: The formatted string of flattened key-value pairs.
        """
        return "\n---\n".join([f"{key}: {value}" for key, value in self._output.items()])

#if __name__ == "__main__":   
#    print(KeyValueRecursiveFlatten()({"a": {"b": [{"c":7}], "j":{"d":8}}}))