from flask import Flask, render_template, request
from morse_code import morse_code
app=Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def show_website():
    if request.method=="POST":
        list_of_char=[]
        input_string=request.form['inputtextarea']
        input_string_uppercase=input_string.upper()
        for i in input_string_uppercase:
            try:
                list_of_char.append(morse_code[i])
            except KeyError:
                output_string='#'
            else:
                output_string=" ".join(list_of_char)
        return render_template('index.html', output=output_string, input_string=input_string)
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)
