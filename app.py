from flask import Flask, request, redirect, render_template_string
import re

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head><title>Cotizador eBay</title></head>
<body>
  <h2>Cotizador Hollander → eBay</h2>
  <form method="POST">
    <input type="text" name="url" placeholder="Pega el URL de Hollander" required style="width:300px">
    <button type="submit">Buscar en eBay</button>
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
