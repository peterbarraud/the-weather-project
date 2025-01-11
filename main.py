import win32clipboard
from bs4 import BeautifulSoup

def getClipboardData():
    # get clipboard data
    win32clipboard.OpenClipboard()
    if win32clipboard.IsClipboardFormatAvailable(1):
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data
    else:
        win32clipboard.CloseClipboard()
        return None
    

def main():
    while True:
        i = input("Copy the URL to the clipboard and press Enter to Continue or x to Exit:\n")
        if i in ['x','X']:
            break
        else:
            url : str = getClipboardData()
            if url.startswith('https://www.wunderground.com/history/monthly'):
                month = url.split("/")[-1]
                print(f"Month: {month}")
                i : str = input("Copy the Daily Observations table and press Enter to Continue or x to Exit:\n")
                if i in ['x','X']:
                    break
                else:
                    soup = BeautifulSoup(getClipboardData(), 'html.parser')
                    tables = soup.find_all('table',{"class":"days"})
                    if len(tables) == 1:
                        body = tables[0].tbody
                        for tr in body.find_all('tr'):
                            print(tr)
                            break
                        print(f"Done for: {month}")
                    else:
                        print("Are you sure you have copied the Daily Observations table??")
                        continue
            else:
                print(f"Invalid URL: {url}")
                continue

if __name__ == '__main__':
    x = getClipboardData()
    print(x)
    # soup = BeautifulSoup(getClipboardData(), 'html.parser')
    # tables = soup.find_all('table',{"class":"days"})
    # if len(tables) == 1:
    #     data_tables = tables[0].tbody.tr
    #     print(len(data_tables))

    # main()
    