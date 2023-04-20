import os

def get_data(database:str, data_type:str):

    """
    database: name of data file
    data_type: file format, csv or json
    """
    file_name = f'{database}.{data_type}'
    url = (
        f"https://ai-jobs.net/salaries/download/{file_name}"
    )

    # for pandas to be able to open the file
    if url.endswith('.json'):
        data_type = data_type
    else:
        data_type = data_type
            
    os.system(f"mkdir data; cd ./data; wget {url} -O {file_name}")  
          
    return None   

# Test function
get_data(database="salaries", data_type="json")         