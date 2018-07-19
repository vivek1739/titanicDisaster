import os
from dotenv import find_dotenv, load_dotenv
from requests import session
import logging

# payload for login to kaggle
payload = {
    'action':'login',
    'username': os.environ.get("KAGGLE_USERNAME"),
    'password': os.environ.get("KAGGLE_PASSWORD")
}

def extract_data(url, file_path):
    with session() as c:
        c.post('https://www.kaggle.com/account/login',data=payload)
        # open file to write
        with open(file_path, 'w') as handle:
        # using a with statement we get, better syntax and it will 
        # automatically close the resources like file
            response = c.get(url,stream=True)
            # stream is True so that we get response as a stream
            for block in response.iter_content(1024):
                handle.write(str(block))
                
def main(project_dir):
    
    # get logger
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')
    
    # urls
    train_url = "https://www.kaggle.com/c/3136/download/train.csv"
    test_url = "https://www.kaggle.com/c/3136/download/test.csv"

    # file paths
    raw_data_path = os.path.join(os.path.pardir,"data","raw")
    train_data_path = os.path.join(raw_data_path,'train.csv')
    test_data_path = os.path.join(raw_data_path,'test.csv')

    # extract data
    extract_data(train_url,train_data_path)
    extract_data(test_url,test_data_path)
    logger.info('downloaded raw training and test data')

if __name__ == '__main__':
    # getting the root directory
    project_dir = os.path.join(os.path.dirname(__file__),os.pardir,os.pardir)
    print("project directory is:",project_dir)
    
    # setup logger and log format
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    # find .env
    dotenv_path = find_dotenv()
    # load up entries as environmental variables
    load_dotenv(dotenv_path)
    
    # call the main
    main(project_dir)