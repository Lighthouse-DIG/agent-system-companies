
class KeyValueRecursiveFlatten:

    def __init__(self):
        self._output = None

    def __call__(self, data:dict):
        self._output = {}
        self._key_value_recursive_dict_flatten(data)
        return self._format_output()
        
    def _key_value_recursive_dict_flatten(self, data_dict, pattern_key=""):
        for key, data_inside in data_dict.items():
            self._process(key, data_inside, pattern_key)
            

    def _key_value_recursive_list_flatten(self, data_list, pattern_key=""):
        for key, data_inside in enumerate(data_list):
            self._process(key, data_inside, pattern_key)

    def _process(self, key, data_inside, pattern_key):
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
        return "\n---\n".join([f"{key}: {value}" for key, value in self._output.items()])
    
#if __name__ == "__main__":   
#    print(KeyValueRecursiveFlatten()({"a": {"b": [{"c":7}], "j":{"d":8}}}))