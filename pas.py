import  subprocess


def extract_wifi_passwords():
    try:
        profiles_data = subprocess.check_output('netsh wlan show profiles').decode('utf-8').split('\n')
    except:
        profiles_data = subprocess.check_output('netsh wlan show profiles').decode('CP866').split('\n')
   # print(profiles_data)
    profiles = [i.split(':')[1].strip() for i in profiles_data if 'Все профили пользователей' in i or 'All User Profile' in i]
    #print(profiles)
    for profile in profiles:
        try:
            profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode('utf-8').split('\n')
        except:
            profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode('CP866').split('\n')
        #print(profile_info)
        try:
            password = [i.split(':')[1].strip() for i in profile_info if 'Содержимое ключа' in i or 'Key Content' in i][0]
        except IndexError:
            password = None

        with open(file='wifi_passwords.txt', mode='a', encoding='utf-8') as file:
            file.write(f'Profile: {profile}\nPassword: {password}\n{"#" * 20}\n')


def main():
    extract_wifi_passwords()


if __name__ == '__main__':
    main()
