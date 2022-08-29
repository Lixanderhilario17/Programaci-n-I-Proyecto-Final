from flask import Flask, render_template, request 
import sqlite3

servidor = Flask(__name__)
servidor.config['SECRET_KEY']= '12345'

@servidor.route('/')
def Inicio():
    return render_template('index.html')

@servidor.route('/catalogo')
def catalogo():
    return render_template('catálogo.html')

@servidor.route('/devolucion')
def devolucion():
    return render_template('devolucion.html')

@servidor.route('/doriangrey')
def doriangrey():
    return render_template('doriangrey.html')

@servidor.route('/gacias')
def gacias():
    return render_template('gacias.html')

@servidor.route('/gracias2')
def gracias2():
    return render_template('gracias2.html')

@servidor.route('/hamlet')
def hamlet():
    return render_template('hamlet.html')

@servidor.route('/harrypotter')
def harrypotter():
    return render_template('harrypotter.html')

@servidor.route('/magodeoz')
def magodeoz():
    return render_template('magodeoz.html')

@servidor.route('/principito')
def principito():
    return render_template('principito.html')

@servidor.route('/quijote')
def quijote():
    return render_template('quijote.html')

@servidor.route('/soledad')
def soledad():
    return render_template('soledad.html')

@servidor.route('/solicitud')
def solicitud():
    return render_template('solicitud.html')

@servidor.route('/agregar/solicitud', methods=['POST'])
def coronel():
    
    base_Datos = sqlite3.connect('registros.db', check_same_thread=False)
    manejo_db = base_Datos.cursor()
    
    estudiante = request.form['Estudiante']
    curso = request.form['Curso']
    numero = request.form['Numero']
    codigo = request.form['Codigo']
    titulo = request.form['Titulo']
    autor = request.form['Autor']
    estante = request.form['Estante']
    despacho = request.form['Despacho']
    entrega = request.form['Entrega']
    
    registroAgenda = estudiante, curso, numero, codigo, titulo, autor, estante, despacho, entrega
    
    manejo_db.execute('INSERT into citas(estudiante, curso, numero, codigo, titulo, autor, estante, despacho, entrega) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', registroAgenda)
    base_Datos.commit()
    
    return render_template('gracias.html')


if __name__=='__main__':
    servidor.run(debug=True)