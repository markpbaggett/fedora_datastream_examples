import requests
import argparse

parser = argparse.ArgumentParser(description='Use to specify a collection')
parser.add_argument("-p", "--pid", dest="pid", help="pid of object", required=True)
parser.add_argument("-d", "--dsid", dest="dsid", help="dsid of object", required=True)
parser.add_argument("-r", "--request", dest="request", help="specify request", required=True)
args = parser.parse_args()

def purgedatastream(user, password, url):
    x = requests.delete(url, auth=(user, password))
    if x.status_code == 200:
        print("\n\nYour datastream was deleted.")
    else:
        print("\n\nUh oh!  Something went wrong.")


def adddatastream(user, password, url):
    x = requests.post(url, auth=(user, password))
    if x.status_code == 201:
        print("\n\nYour datastream was added.")
    else:
        print("\n\nUh oh! Something went wrong!")

if __name__ == "__main__":

    # Defaults
    fedoraurl = 'http://localhost:8080/fedora/'
    fedorauser = 'fedoraAdmin'
    fedorapassword = 'fedoraAdmin'
    fedorapid = args.pid
    fedoradsid = args.dsid
    request = args.request

    if request == "purge":
        fedoraurl = fedoraurl + 'objects/' + fedorapid + '/datastreams/' + fedoradsid
        purgedatastream(fedorauser,fedorapassword,fedoraurl)
    if request == "add":
        fedoraurl = fedoraurl + 'objects/' + fedorapid + '/datastreams/' + fedoradsid + '?controlGroup=M&dsLocation='
        dsidLocation = input("URL to dsid content: ")
        fedoraurl = fedoraurl + dsidLocation
        adddatastream(fedorauser, fedorapassword, fedoraurl)

