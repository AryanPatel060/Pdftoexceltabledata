from flask import Flask, render_template, request, send_file
import os
import tabula
app = Flask(__name__)
deletepath  = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename

        PdfToCSV(file,filename)
        # downloadFile(filename)
        return render_template("download.html",filename = filename )
          
def PdfToCSV(pdfLoc,filename):
    global deletepath
    if deletepath is not None:
        os.remove(deletepath)
    tabula.convert_into(pdfLoc, "Uploads/"+filename+".csv", output_format="csv", pages='all')



@app.route('/download/<string:filename>',methods = ['GET','POST'])
def downloadFile(filename):
    path = 'Uploads/'+filename+'.csv'
    downloade_path= filename+'.csv'
    global deletepath 
    deletepath = path
    return send_file(path, mimetype='text/csv', as_attachment=True, download_name= downloade_path)


 
if __name__ == "__main__":
    app.run(debug=True)