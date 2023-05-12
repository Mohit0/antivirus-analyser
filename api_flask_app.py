from flask import Flask, make_response, request, render_template, url_for
import os
from main import one_by_one
from compile_rules import compile_rules

app = Flask(__name__)

app.config['SECRET_KEY'] = '6Ed2)2Ou,0T?DB+'


# landing page for application
@app.route('/')
def welcome():
    return render_template("ui.html")


@app.route('/scan', methods=['POST'])
def scan_file():
    # get file from UI and save it in local storage
    f = request.files['file']
    f.save(os.path.join("payloads", f.filename))
    path = str(os.path.join("payloads", f.filename))
    # print(path)

    # print file size
    size = os.path.getsize(path)
    if size > 20000000:
        print("File is greater than 20MB")
        os.remove(path)
        return make_response(
            'File Size Exceeds than 20MB.',
            200
        )

    # scan the file and get the results
    result = one_by_one(path)
    print(result)

    # file is removed from system as its already scanned
    os.remove(path)

    # return results back to UI
    if result == "Malicious":
        return make_response(
            'Malicious',
            200
        )

    elif result == "Clean":
        return make_response(
            'Clean',
            200
        )

    else:
        return make_response(
            'Undetermined',
            200
        )


if __name__ == "__main__":
    compile_rules()
    app.run(host ='0.0.0.0', port=5000, debug=False)
