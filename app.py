from flask import Flask, request, redirect, render_template_string
import re

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Cotizador eBay</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
      background: #f8f9fa;
    }
    h2 {
      color: #333;
    }
    input[type="text"] {
      width: 100%;
      padding: 12px;
      font-size: 16px;
      margin-bottom: 15px;
      border-radius: 5px;
      border: 1px solid #ccc;
    }
    button {
      background-color: #007bff;
      color: white;
      padding: 12px 20px;
      border: none;
      border-radius: 5px;
      font-size: 16px;
      width: 100%;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <h2>Cotizador Hollander → eBay</h2>
  <form method="POST">
    <input type="text" name="url" placeholder="Pega aquí el URL de Hollander" required>
    <button type="submit">🔍 Buscar en eBay</button>
  </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        match = re.search(r'\d{3}-\d+', url)
        if match:
            codigo = match.group()
            return redirect(f'https://www.ebay.com/sch/i.html?_nkw={codigo}')
        return "Código Hollander no encontrado en el URL."
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run()
