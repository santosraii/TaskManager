from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    custo = db.Column(db.Float, nullable=False)
    data_limite = db.Column(db.Date, nullable=False)
    ordem_apresentacao = db.Column(db.Integer, nullable=False, unique=True)

    def __repr__(self):
        return f"Tarefa('{self.nome}', '{self.custo}', '{self.data_limite}')"

@app.route('/')
def index():
    tarefas = Tarefa.query.order_by(Tarefa.ordem_apresentacao).all()  # Ordena as tarefas pela ordem de apresentação
    
    for tarefa in tarefas:
        tarefa.data_limite_formatada = tarefa.data_limite.strftime('%d/%m/%Y')
    
    return render_template('index.html', tarefas=tarefas)

@app.route('/criar', methods=['POST'])
def criar_tarefa():
    nome = request.form['nome']
    custo = float(request.form['custo'])
    data_limite = datetime.strptime(request.form['data_limite'], '%Y-%m-%d').date()
    
    ultima_tarefa = Tarefa.query.order_by(Tarefa.ordem_apresentacao.desc()).first()
    ordem_apresentacao = ultima_tarefa.ordem_apresentacao + 1 if ultima_tarefa else 1
    
    if Tarefa.query.filter_by(nome=nome).first():
        flash('Tarefa com esse nome já existe.')
        return redirect(url_for('index'))
    
    tarefa = Tarefa(nome=nome, custo=custo, data_limite=data_limite, ordem_apresentacao=ordem_apresentacao)
    db.session.add(tarefa)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['POST'])
def editar_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    tarefa.nome = request.form['nome']
    tarefa.custo = float(request.form['custo'])
    tarefa.data_limite = datetime.strptime(request.form['data_limite'], '%Y-%m-%d').date()
    
    if Tarefa.query.filter(Tarefa.id != tarefa.id, Tarefa.nome == tarefa.nome).first():
        flash('Tarefa com esse nome já existe.')
        return redirect(url_for('index'))
    
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/excluir/<int:id>', methods=['POST'])
def excluir_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/subir/<int:id>', methods=['POST'])
def subir_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    tarefa_anterior = Tarefa.query.filter(Tarefa.ordem_apresentacao == (tarefa.ordem_apresentacao - 1)).first()
    
    if tarefa_anterior:
        tarefa_anterior.ordem_apresentacao += 1
        tarefa.ordem_apresentacao -= 1
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/descer/<int:id>', methods=['POST'])
def descer_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    tarefa_posterior = Tarefa.query.filter(Tarefa.ordem_apresentacao == (tarefa.ordem_apresentacao + 1)).first()
    
    if tarefa_posterior:
        tarefa_posterior.ordem_apresentacao -= 1
        tarefa.ordem_apresentacao += 1
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/reordenar', methods=['POST'])
def reordenar_tarefas():
    order = request.json['order']
    for i, id in enumerate(order):
        tarefa = Tarefa.query.get(id)
        tarefa.ordem_apresentacao = i + 1
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
