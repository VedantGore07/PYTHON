import argparse

def hello(name,lang):
    greetings={
        "English":"Hello",
        "Spanish":"Hola",
        "German":"Hallo",
        "Hindi":"Namaste" }
    return f"{greetings[lang]}, {name}"

# print(hello(args.name, args.lang)) 

parser = argparse.ArgumentParser(
    description="provides a personal greeting"
)

parser.add_argument("-n","--name",metavar="name",required=True,
                    help="the name of the person to greet")

parser.add_argument("-l","--lang",metavar="language",required=True,choices=["English","Spanish","German"],
                    help="The language of the greeting")

args = parser.parse_args()
# msg = f"{greetings[lang]} {name}!"

# print(msg)












