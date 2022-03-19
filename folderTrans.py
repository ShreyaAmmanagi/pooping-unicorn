import dropbox
class TransferFold :
    def __init__(self,access_token):
        self.access_token = access_token
    def uploadFile(self, fromFold, toFold):
        db = dropbox.Dropbox(self.access_token)
        f= open(fromFold,'rb')
        db.files_upload(f.read(),toFold)
def main():
    access_token = input('access token__ ')
    transfer = TransferFold(access_token)
    fromFold = input("path of your folder to be moved__ ")
    toFold = input("destination, please__ ")
    transfer.uploadFile(fromFold,toFold)
    print("job perfectly done!")
main()