def format_overview(overview_data:dict):
    """ Generate overview string data """
    return "\n---\n".join([f"{key}: {value}" for key, value in overview_data.items()])
