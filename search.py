from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view-data')
def view_data():
    # Read the Excel file
    df = pd.read_excel('Web_Scrapping.xlsx')
    
    # Convert DataFrame to HTML
    data_html = df.to_html()
    
    return render_template('view_data.html', data_html=data_html)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if query:
        df = pd.read_excel('Web_Scrapping.xlsx')
        results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
        data_html = results.to_html()
    else:
        data_html = "No results found."
    
    return render_template('search_results.html', data_html=data_html)

if __name__ == '__main__':
    app.run(debug=True)
