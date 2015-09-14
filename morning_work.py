#!/usr/local/bin/python3
"""Open browser tabs for morning schedule at work"""
import subprocess

CHROME_APP = r'/Applications/Google Chrome.app'

def main():
    """Entry function"""
    try:
        subprocess.run(['open', '-a', CHROME_APP, 'https://autodiscover.nymag.biz/'], stderr=subprocess.STDOUT)
        subprocess.run(['open', '-a', CHROME_APP, 'https://nymedia.slack.com/'], stderr=subprocess.STDOUT)
        subprocess.run(['open', '-a', CHROME_APP, 'https://amateurpreneur.slack.com/'], stderr=subprocess.STDOUT)
        subprocess.run(['open', '-a', CHROME_APP, 'https://inbox.google.com/'], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as ex:
        print(ex)

if __name__ == '__main__':
    main()
