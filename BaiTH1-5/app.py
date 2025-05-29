from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher
app = Flask(__name__)

# router routes for home page
@app.route("/")
def home():
    return render_template('index.html')

# router routes for caesar cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')
# router routes for caesar encryption
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

# router routes for caesar decryption
@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"
#----------------------------------------------------------------------------
@app.route("/vigenere_encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    cipher = VigenereCipher()
    encrypted_text = cipher.vigenere_encrypt(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"
@app.route("/vigenere_decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    cipher = VigenereCipher()
    decrypted_text = cipher.vigenere_decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"
#----------------------------------------------------------------------------
@app.route("/railfence_encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    cipher = RailFenceCipher()
    encrypted_text = cipher.rail_fence_encrypt(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/railfence_decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    cipher = RailFenceCipher()
    decrypted_text = cipher.rail_fence_decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"

@app.route("/playfair_encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    encrypted_text = cipher.playfair_encrypt(text, matrix)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/playfair_decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    cipher = PlayFairCipher()
    matrix = cipher.create_playfair_matrix(key)
    decrypted_text = cipher.playfair_decrypt(text, matrix)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"
@app.route("/transposition_encrypt", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    cipher = TranspositionCipher()
    encrypted_text = cipher.encrypt(text, key)
    return f"text: {text}<br>key: {key}<br>encrypted text: {encrypted_text}"

@app.route("/transposition_decrypt", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    cipher = TranspositionCipher()
    decrypted_text = cipher.decrypt(text, key)
    return f"text: {text}<br>key: {key}<br>decrypted text: {decrypted_text}"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5054, debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5054, debug=True)