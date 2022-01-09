import requests
import random


# r = requests.get("https://poetrydb.org/title/Ozymandias/lines.json")
# r = requests.get("https://poetrydb.org/linecount/18/lines.json")


def randompoem():
    randomnumber=random.randint(0, 2972)
    r = requests.get("https://poetrydb.org/title")
    if r.status_code == 200:
        title = r.json()["titles"][randomnumber].strip()
        tempreq = requests.get("https://poetrydb.org/title/{}/author,title,lines,linecount".format(title))
        if tempreq.status_code == 200:
            res = tempreq.json()
            r.close()
            tempreq.close()
            return res
        else:
            r.close()
            tempreq.close()
            return "Poem Access Failure"
    else:
        r.close()
        return "Poem Access Failure"


def stringifypoem(poem):
    try:
        body = "\n".join(poem[0]["lines"])
        poet = poem[0]["author"]
        title = poem[0]["title"].strip()
        linecount = poem[0]["linecount"]
        return title + "\n\n" + poet + "\n\n" + body
    except:
        print("could not format poem")


if __name__ == '__main__':
    print(stringifypoem(randompoem(random.randint(0, 2972))))
    # print(randompoem(89)[0])
    # print(r.json()["titles"])
