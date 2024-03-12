from account_manager import AccountManager
from crypto import Crypto


def get_key():
    seed = "123456789asdF!" + "eisy"
    return Crypto.generate_fenet_key(seed)


path_data = "save_file_data.mpw"
auth_key = get_key()

manager = AccountManager(path_data, auth_key)
# manager.create_test_data()

