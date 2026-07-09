"""
=====================================================
Workstation Tasks
Arquivo Principal da Aplicação
Versão: 0.1.0
=====================================================
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)