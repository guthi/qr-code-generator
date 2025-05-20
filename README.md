
# 📦 Gerador de QR Code com Flask

Este é um aplicativo web simples feito com **Flask** que permite gerar QR Codes personalizados a partir de qualquer texto ou link. O QR gerado pode ser visualizado e baixado diretamente da interface.

---

## ⚙️ Funcionalidades

- Inserção de texto ou link
- Geração instantânea de QR Code
- Visualização do QR na tela
- Download do QR Code em PNG

---

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [qrcode](https://pypi.org/project/qrcode/)
- [Pillow (PIL)](https://python-pillow.org/)
- [Bootstrap](https://getbootstrap.com/) (via CDN)

---

## 📂 Estrutura do Projeto

```
qr-code-generator/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── qr_codes/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ Como Rodar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/qr-code-generator.git
cd qr-code-generator
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Inicie o servidor:

```bash
python app.py
```

4. Acesse o navegador:

```
http://127.0.0.1:5000
```

---

## 📋 Requisitos

- Python 3.7 ou superior
- Pip

---

## ✍️ Autor

**Guthierre**  
🔗 [LinkedIn](https://www.linkedin.com/in/guthierre/)  
💻 [GitHub](https://github.com/guthi/)
