# ATIVIDADE_AVALIATIVA — Cenário B: Cinema

Projeto Flask MVC — Aula 11

## Como rodar

```bash
pip install -r requirements.txt
python app.py
```

Acesse: http://127.0.0.1:5000

## Estrutura

```
ATIVIDADE_AVALIATIVA/
├── app.py
├── dados_iniciais.py
├── requirements.txt
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── filme.py
│   ├── sala.py
│   ├── sessao.py
│   └── ingresso.py
├── controllers/
│   ├── __init__.py
│   ├── dashboard_controller.py
│   └── cinema_controller.py
└── views/
    ├── static/css/style.css
    └── templates/
        ├── layout.html
        ├── index.html
        └── cinema/
            ├── lista_sessoes.html
            └── formulario_sessao.html
```
