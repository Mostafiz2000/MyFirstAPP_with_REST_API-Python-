from flask import Flask,jsonify


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/armstrong/<int:n>")
def armstrong(n):
    sum=0;
    order = len(str(n))
    copy_n=n
    while(n>0):
        digit=n%10
        sum+=digit**order
        n=n//10
    if sum == copy_n:
        print("is a armstrong number")
        result={
            "Number":copy_n,
            "Armstrong":True,
            "Server IP":"122.233.233.122" }
    else :
        print("Is not an armstrong number")
        result={
            "Number":copy_n,
            "Armstrong":False,
            "Server IP":"122.233.233.122" }
    return jsonify(result)
@app.route("/user/<string:n>")
def details(n):
    profile={
        "name":"Mostafizur Rahman",
        "Age":22,
        "Department":"CSE",
        "Portfolio":"https://mostafiz2000.github.io/myportfolio/"

    }
    return jsonify(profile)
if __name__ =="__main__":
    app.run(debug=True)