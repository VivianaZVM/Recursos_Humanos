from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# Crud del Area
@app.route('/area')
def area():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
    cursor = conn.cursor()
    cursor.execute('select idArea, nombre from area order by idArea')
    datos = cursor.fetchall()
    return render_template("area.html", area = datos)

@app.route('/area_editar/<string:id>')
def area_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('select idArea, nombre from area where idArea = %s', (id))
    dato  = cursor.fetchall()
    return render_template("area_edi.html", area=dato[0])

@app.route('/area_fedita/<string:id>',methods=['POST'])
def area_fedita(id):
    if request.method == 'POST':
        desc=request.form['nombre']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
        cursor = conn.cursor()
        cursor.execute('update area set nombre=%s where idArea=%s', (desc,id))
        conn.commit()
    return redirect(url_for('area'))

@app.route('/area_borrar/<string:id>')
def area_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('delete from area where idArea = {0}'.format(id))
    conn.commit()
    return redirect(url_for('area'))

@app.route('/area_agregar')
def area_agregar():
    return render_template("area_agr.html")

@app.route('/area_fagrega', methods=['POST'])
def area_fagrega():
    if request.method == 'POST':
        desc = request.form['nombre']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into area (nombre) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('area'))

# Crud carrera
@app.route('/carrera')
def carrera():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
    cursor = conn.cursor()
    cursor.execute('select idCarrera, nombre from carrera order by idCarrera')
    datos = cursor.fetchall()
    return render_template("carrera.html", carrera = datos)

@app.route('/carrera_editar/<string:id>')
def carrera_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('select idCarrera, nombre from carrera where idCarrera = %s', (id))
    dato  = cursor.fetchall()
    return render_template("carrera_edi.html", carrera=dato[0])

@app.route('/carrera_fedita/<string:id>',methods=['POST'])
def carrera_fedita(id):
    if request.method == 'POST':
        desc=request.form['nombre']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
        cursor = conn.cursor()
        cursor.execute('update carrera set nombre=%s where idCarrera=%s', (desc,id))
        conn.commit()
    return redirect(url_for('carrera'))

@app.route('/carrera_borrar/<string:id>')
def carrera_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('delete from carrera where idCarrera = {0}'.format(id))
    conn.commit()
    return redirect(url_for('carrera'))

@app.route('/carrera_agregar')
def carrera_agregar():
    return render_template("carrera_agr.html")

@app.route('/carrera_fagrega', methods=['POST'])
def carrera_fagrega():
    if request.method == 'POST':
        desc = request.form['nombre']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into carrera (nombre) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('carrera'))

# Crud escolaridad
@app.route('/escolaridad')
def escolaridad():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
    cursor = conn.cursor()
    cursor.execute('select idEscolaridad, nombre from escolaridad order by idEscolaridad')
    datos = cursor.fetchall()
    return render_template("escolaridad.html", escolaridad = datos)

@app.route('/escolaridad_editar/<string:id>')
def escolaridad_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('select idEscolaridad, nombre from escolaridad where idEscolaridad = %s', (id))
    dato  = cursor.fetchall()
    return render_template("escolaridad_edi.html", escolaridad=dato[0])

@app.route('/escolaridad_fedita/<string:id>',methods=['POST'])
def escolaridad_fedita(id):
    if request.method == 'POST':
        desc=request.form['nombre']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
        cursor = conn.cursor()
        cursor.execute('update escolaridad set nombre=%s where idEscolaridad=%s', (desc,id))
        conn.commit()
    return redirect(url_for('escolaridad'))


@app.route('/escolaridad_borrar/<string:id>')
def escolaridad_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('delete from escolaridad where idEscolaridad = {0}'.format(id))
    conn.commit()
    return redirect(url_for('escolaridad'))

@app.route('/escolaridad_agregar')
def escolaridad_agregar():
    return render_template("escolaridad_agr.html")

@app.route('/escolaridad_fagrega', methods=['POST'])
def escolaridad_fagrega():
    if request.method == 'POST':
        desc = request.form['nombre']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into escolaridad (nombre) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('escolaridad'))

# Crud del estadocivil 
@app.route('/estadocivil')
def estadocivil():
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
 cursor = conn.cursor()
 cursor.execute('select idEstadocivil, nombre from estadocivil order by idEstadocivil')
 datos = cursor.fetchall()
 return render_template("estadocivil.html", estadocivil = datos)

@app.route('/estadocivil_editar/<string:id>')
def estadocivil_editar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
 cursor = conn.cursor()
 cursor.execute('select idEstadocivil, nombre from estadocivil where idEstadocivil = %s', (id))
 dato = cursor.fetchall()
 return render_template("estadocivil_edi.html", estadocivil=dato[0])

@app.route('/estadocivil_fedita/<string:id>',methods=['POST'])
def estadocivil_fedita(id):
 if request.method == 'POST':
    Nombre_estadocivil = request.form['nombre']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('update estadocivil set nombre=%s where idEstadocivil=%s', ( Nombre_estadocivil, id))
    conn.commit()
    return redirect(url_for('estadocivil'))

@app.route('/estadocivil_borrar/<string:id>')
def estadocivil_borrar(id):
 conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
 cursor = conn.cursor()
 cursor.execute('delete from estadocivil where idEstadocivil = {0}'.format(id))
 conn.commit()
 return redirect(url_for('estadocivil'))

@app.route('/estadocivil_agregar')
def estadocivil_agregar():
 return render_template("estadocivil_agr.html")

@app.route('/estadocivil_fagrega', methods=['POST'])
def estadocivil_fagrega():
 if request.method == 'POST':
    Nombre_estadocivil = request.form['nombre']
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
    cursor = conn.cursor()
    cursor.execute('insert into estadocivil (nombre) values (%s)', (Nombre_estadocivil))
    conn.commit()
    return redirect(url_for('estadocivil'))


# Crud del Grado de Avance
@app.route('/gradoAvance')
def gradoAvance():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('SELECT idGradoAvance, nombre FROM grado_avance ORDER BY idGradoAvance')
    datos = cursor.fetchall()
    return render_template("gradoAvance.html", grado_avance = datos)

@app.route('/gradoAvance_editar/<string:id>')
def gradoAvance_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('select idGradoAvance, nombre from grado_avance where idGradoAvance = %s', (id))
    datos = cursor.fetchall()
    return render_template("gradoAvance_edit.html", grado_avance=datos[0])

@app.route('/gradoAvance_feditar/<string:id>',methods=['POST'])
def gradoAvance_feditar(id):
    if request.method == 'POST':
        desc=request.form['nombre']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
        cursor = conn.cursor()
        cursor.execute('update grado_avance set nombre=%s where idGradoAvance=%s', (desc,id))
        conn.commit()
    return redirect(url_for('gradoAvance'))

@app.route('/gradoAvance_borrar/<string:id>')
def gradoAvance_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('delete from grado_avance where idGradoAvance = {0}'.format(id))
    conn.commit()
    return redirect(url_for('gradoAvance'))

@app.route('/gradoAvance_agregar')
def gradoAvance_agregar():
    return render_template("gradoAvance_agr.html")

@app.route('/gradoAvance_fagregar', methods=['POST'])
def gradoAvance_fagregar():
    if request.method == 'POST':
        desc = request.form['nombre']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into grado_avance (nombre) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('gradoAvance'))

# Crud habilidades
@app.route('/habilidad')
def habilidades():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
    cursor = conn.cursor()
    cursor.execute('select idHabilidad, nombre from habilidad order by idHabilidad')
    datos = cursor.fetchall()
    return render_template("habilidad.html", habilidad = datos)

@app.route('/habilidad_editar/<string:id>')
def habilidad_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('select idHabilidad, nombre from habilidad where idHabilidad = %s', (id))
    dato  = cursor.fetchall()
    return render_template("habilidad_edi.html", habilidad=dato[0])

@app.route('/habilidad_fedita/<string:id>',methods=['POST'])
def habilidad_fedita(id):
    if request.method == 'POST':
        desc=request.form['nombre']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
        cursor = conn.cursor()
        cursor.execute('update habilidad set nombre=%s where idHabilidad=%s', (desc,id))
        conn.commit()
    return redirect(url_for('habilidades'))

@app.route('/habilidad_borrar/<string:id>')
def habilidad_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('delete from habilidad where idHabilidad = {0}'.format(id))
    conn.commit()
    return redirect(url_for('habilidades'))

@app.route('/habilidad_agregar')
def habilidad_agregar():
    return render_template("habilidad_agr.html")

@app.route('/habilidad_fagrega', methods=['POST'])
def habilidad_fagrega():
    if request.method == 'POST':
        desc = request.form['nombre']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into habilidad (nombre) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('habilidades'))

# Crud Idioma
@app.route('/idioma')
def idioma():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
    cursor = conn.cursor()
    cursor.execute('select idIdioma, nombre from idioma order by idIdioma')
    datos = cursor.fetchall()
    return render_template("idioma.html", idioma = datos)

@app.route('/idioma_editar/<string:id>')
def idioma_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('select idIdioma, nombre from idioma where idIdioma = %s', (id))
    dato  = cursor.fetchall()
    return render_template("idioma_edi.html", idioma=dato[0])

@app.route('/idioma_fedita/<string:id>',methods=['POST'])
def idioma_fedita(id):
    if request.method == 'POST':
        desc=request.form['nombre']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
        cursor = conn.cursor()
        cursor.execute('update idioma set nombre=%s where idIdioma=%s', (desc,id))
        conn.commit()
    return redirect(url_for('idioma'))

@app.route('/idioma_borrar/<string:id>')
def idioma_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('delete from idioma where idIdioma = {0}'.format(id))
    conn.commit()
    return redirect(url_for('idioma'))

@app.route('/idioma_agregar')
def idioma_agregar():
    return render_template("idioma_agr.html")

@app.route('/idioma_fagrega', methods=['POST'])
def idioma_fagrega():
    if request.method == 'POST':
        desc = request.form['nombre']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into idioma (nombre) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('idioma'))

# Crud de Medio  de Publicidad
@app.route('/medioPublic')
def medioPublic():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('SELECT idMedioPublic, nombre FROM mediopublic ORDER BY idMedioPublic')
    datos = cursor.fetchall()
    return render_template("medioPublic.html", mediopublic = datos)

@app.route('/medioPublic_editar/<string:id>')
def medioPublic_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('select idMedioPublic, nombre from mediopublic where idMedioPublic = %s', (id))
    datos = cursor.fetchall()
    return render_template("medioPublic_edi.html", mediopublic=datos[0])

@app.route('/medioPublic_feditar/<string:id>',methods=['POST'])
def medioPublic_feditar(id):
    if request.method == 'POST':
        desc=request.form['nombre']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
        cursor = conn.cursor()
        cursor.execute('update mediopublic set nombre=%s where idMedioPublic=%s', (desc,id))
        conn.commit()
    return redirect(url_for('medioPublic'))

@app.route('/medioPublic_borrar/<string:id>')
def medioPublic_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('delete from mediopublic where idMedioPublic = {0}'.format(id))
    conn.commit()
    return redirect(url_for('medioPublic'))

@app.route('/medioPublic_agregar')
def medioPublic_agregar():
    return render_template("medioPublic_agr.html")

@app.route('/medioPublic_fagregar', methods=['POST'])
def medioPublic_fagregar():
    if request.method == 'POST':
        desc = request.form['nombre']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into mediopublic (nombre) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('medioPublic'))




@app.route('/puesto')
def puesto():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
    cursor = conn.cursor()
    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()
    return render_template("puesto.html", pue=datos, dat='   ', catArea='   ', catEdoCivil='   ', catEscolaridad='   ',
                           catGradoAvance='    ', catCarrera='    ', catIdioma=' ', catHabilidad=' ')

@app.route('/puesto_fdetalle/<string:idP>', methods=['GET'])
def puesto_fdetalle(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()

    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
            'funciones,edad,sexo,idEstadocivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
            'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select a.idArea, a.nombre from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))
    datos1 = cursor.fetchall()

    cursor.execute('select a.idEstadocivil, a.nombre from estadocivil a, puesto b where a.idEstadocivil = b.idEstadocivil and b.idPuesto = %s', (idP))
    datos2 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.nombre from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s', (idP))
    datos3 = cursor.fetchall()

    cursor.execute('select a.idGradoAvance, a.nombre from grado_avance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s', (idP))
    datos4 = cursor.fetchall()

    cursor.execute('select a.idCarrera, a.nombre from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s', (idP))
    datos5 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.nombre from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
    datos6 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidad, b.nombre from puesto a, habilidad b, puesto_has_habilidad c '
                   'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
    datos7 = cursor.fetchall()
    return render_template("puesto.html", pue = datos, dat=dato[0], catArea=datos1[0], catEdoCivil=datos2[0], catEscolaridad=datos3[0],
                           catGradoAvance=datos4[0], catCarrera=datos5[0], catIdioma=datos6, catHabilidad=datos7)

@app.route('/puesto_borrar/<string:idP>')
def puesto_borrar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('delete from puesto_has_habilidad where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('delete from puesto where idPuesto = %s',(idP))
    conn.commit()
    return redirect(url_for('puesto'))

@app.route('/puesto_agregar')
def puesto_agregar():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('select idArea, nombre from area ')
    datos1  = cursor.fetchall()

    cursor.execute('select idEstadocivil, nombre from estadocivil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, nombre from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, nombre from grado_avance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, nombre from carrera ')
    datos5 = cursor.fetchall()

    cursor.execute('select idIdioma, nombre from idioma ')
    datos6 = cursor.fetchall()

    cursor.execute('select idHabilidad, nombre from habilidad ')
    datos7 = cursor.fetchall()

    return render_template("puesto_agr.html", catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3, catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7)

@app.route('/puesto_fagrega', methods=['POST'])
def puesto_fagrega():
    if request.method == 'POST':
        if  'idArea' in request.form:
            idAr = request.form['idArea']
        else:
            idAr = '1'
        if 'idEstadoCivil' in request.form:
            idEC = request.form['idEstadocivil']
        else:
            idEC = '1'
        if 'idEscolaridad' in request.form:
            idEs = request.form['idEscolaridad']
        else:
            idEs = '1'
        if 'idGradoAvance' in request.form:
            idGA = request.form['idGradoAvance']
        else:
            idGA = '1'
        if 'idCarrera' in request.form:
            idCa = request.form['idCarrera']
        else:
            idCa = '1'
        if 'sexo' in request.form:
            sex = request.form['sexo']
        else:
            sex = '1'
        codP = request.form['codPuesto']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']


    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute(
        'insert into puesto (codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
        'funciones,edad,sexo,idEstadocivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
        'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
        (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda, sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF, reqP, resp, conT))
    conn.commit()

    cursor.execute('select idPuesto, nomPuesto from puesto where idPuesto=(select max(idPuesto) from puesto) ')
    dato=cursor.fetchall()
    idpue = dato[0]
    idP = idpue[0]

    cursor.execute('select count(*) from idioma ')
    dato = cursor.fetchall()
    nidio = dato[0]
    ni = nidio[0] + 1

    for i in range(1, ni):
        idio = 'i' + str(i)
        if idio in request.form:
            cursor.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,%s)', (idP, i))
            conn.commit()

    cursor.execute('select count(*) from habilidad ')
    dato = cursor.fetchall()
    nhab = dato[0]
    nh = nhab[0] + 1

    for i in range(1, nh):
        habi = 'h' + str(i)
        if habi in request.form:
            cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)', (idP, i))
            conn.commit()

    return redirect(url_for('puesto'))


@app.route('/puesto_editar/<string:idP>')
def puesto_editar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
        'funciones,edad,sexo,idEstadocivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
        'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select idArea, nombre from area ')
    datos1 = cursor.fetchall()

    cursor.execute('select idEstadocivil, nombre from estadocivil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, nombre from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, nombre from grado_avance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, nombre from carrera ')
    datos5 = cursor.fetchall()

    cursor.execute('select idIdioma, nombre from idioma ')
    datos6 = cursor.fetchall()

    cursor.execute('select idHabilidad, nombre from habilidad ')
    datos7 = cursor.fetchall()

    cursor.execute('select a.idArea, a.nombre from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s',
                   (idP))
    datos11 = cursor.fetchall()

    cursor.execute(
        'select a.idEstadocivil, a.nombre from estadocivil a, puesto b where a.idEstadocivil = b.idEstadocivil and b.idPuesto = %s',
        (idP))
    datos12 = cursor.fetchall()

    cursor.execute(
        'select a.idEscolaridad, a.nombre from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s',
        (idP))
    datos13 = cursor.fetchall()

    cursor.execute(
        'select a.idGradoAvance, a.nombre from grado_avance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s',
        (idP))
    datos14 = cursor.fetchall()

    cursor.execute(
        'select a.idCarrera, a.nombre from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s',
        (idP))
    datos15 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.nombre from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
    datos16 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidad, b.nombre from puesto a, habilidad b, puesto_has_habilidad c '
                   'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
    datos17 = cursor.fetchall()

    return render_template("puesto_edi.html", dat=dato[0], catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,
                           catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7,
                           Area=datos11[0], EdoCivil=datos12[0], Escolaridad=datos13[0], GradoAvance=datos14[0],
                           Carrera=datos15[0], Idioma=datos16, Habilidad=datos17)


@app.route('/puesto_fedita/<string:idP>', methods=['POST'])
def puesto_fedita(idP):
    if request.method == 'POST':
        if 'idGradoAvance' in request.form:
            idGA = request.form['idGradoAvance']
        else:
            idGA = '1'
        if 'idCarrera' in request.form:
            idCa = request.form['idCarrera']
        else:
            idCa = '1'
        codP = request.form['codPuesto']
        idAr = request.form['idArea']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        sex = request.form['sexo']
        idEC = request.form['idEstadocivil']
        idEs = request.form['idEscolaridad']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('update puesto set codPuesto = %s, idArea = %s, nomPuesto = %s, puestoJefeSup = %s, jornada = %s, '
                   'remunMensual = %s, prestaciones = %s, descripcionGeneral = %s, funciones = %s, edad = %s, sexo = %s, '
                   'idEstadocivil = %s, idEscolaridad = %s, idGradoAvance = %s, idCarrera = %s, experiencia = %s, '
                   'conocimientos = %s, manejoEquipo = %s, reqFisicos = %s, reqPsicologicos = %s, responsabilidades = %s, '
                   'condicionesTrabajo = %s where idPuesto = %s', (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda,
                   sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF, reqP, resp, conT, idP))
    conn.commit()
    return redirect(url_for('puesto'))

# Crud de Requisicion

@app.route('/requisicion')
def requisicion():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
    cursor = conn.cursor()
    cursor.execute('select folio, nomSolicita  from requisicion order by idRequisicion')
    datos = cursor.fetchall()
    return render_template("requisicion_agr.html", req=datos, dat='   ', catArea='   ', catEdoCivil='   ', catEscolaridad='   ', catPuesto='   ', catEdad='   ', catSexo='   ', catFunciones='   ', catDescrG='   ', catRemu='   ', catPuestoJS='   ', catJornada='   ', catmotReq='   ', catEsp='   ', folio='   ', puestovac='   ')

@app.route('/requisicion_agregar')
def requisicion_agregar():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('select idArea, nombre from area')
    datos1  = cursor.fetchall()
    cursor.execute('select idPuesto, nomPuesto from puesto')
    datos2 = cursor.fetchall()

    return render_template("requisicion_agr.html", catArea=datos1, catPuesto=datos2)



@app.route('/req_fagrega', methods=['POST'])
def req_fagrega():
    if request.method == 'POST':
        if  'idArea' in request.form:
            idA = request.form['idArea']
        else:
            idA = '1'

        if  'idPuesto' in request.form:
            idPu = request.form['idPuesto']
        else:
            idPu = '1'

        if 'motivoRequisicion' in request.form:
            moti = request.form['motivoRequisicion']
        else:
            moti = '1'

        fol = request.form['folio']
        feelab = request.form['fechaElab']
        ferecl = request.form['fechaRecluta']
        feini = request.form['fechaInicVac']
        moti = request.form['motReq']
        motiE = request.form['motivoEspecifique']
        tipo = request.form['tipo']
        nomS = request.form['nomSolicita']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute(
        'insert into requisicion (folio,idArea,idPuesto,fechaElab,fechaRecluta,fechaInicVac,motivoRequisicion,motivoEspecifique,tipoVacante,nomSolicita) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(fol, idA, idPu, feelab, ferecl, feini, moti, motiE, tipo, nomS))
    conn.commit()
    return redirect(url_for('requisicion'))

@app.route('/requisicion_pen')
def requisicion_pen():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
    cursor = conn.cursor()
    cursor.execute('select idRequisicion, nomSolicita from requisicion where autorizada=0 order by idRequisicion')
    datos = cursor.fetchall()
    return render_template("requisicion_pen.html", req=datos, dat='   ', catArea='   ', catEdoCivil='   ', catEscolaridad='   ', catPuesto='   ', catEdad='   ', catSexo='   ', catFunciones='   ', catDescrG='   ', catRemu='   ', catPuestoJS='   ', catJornada='   ', catmotReq='   ', catEsp='   ')


@app.route('/requisicion_fdetalle/<string:idReq>', methods=['GET'])
def requisicion_fdetalle(idReq):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    
    cursor.execute('select idRequisicion, nomSolicita from requisicion where autorizada=0 order by idRequisicion')
    datos = cursor.fetchall()

    cursor.execute('select  idRequisicion,folio ,fechaElab, fechaRecluta , fechaInicVac, nomSolicita, motivoRequisicion , motivoEspecifique, tipoVacante, idPuesto, idArea from requisicion where idRequisicion = %s', (idReq))
    dato = cursor.fetchall()

    cursor.execute('select a.idArea, a.nombre from area a, requisicion b where a.idArea = b.idArea and b.idRequisicion = %s', (idReq))
    datos1 = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.nomPuesto from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idReq))
    datos2 = cursor.fetchall()

    cursor.execute('select a.idEstadocivil, a.nombre from estadocivil a, puesto b, requisicion c where a.idEstadocivil = b.idEstadocivil and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
    datos3 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.nombre from escolaridad a, puesto b, requisicion c where a.idEscolaridad = b.idEscolaridad and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
    datos4 = cursor.fetchall()

    cursor.execute('select a.edad from puesto a, puesto b, requisicion c where a.edad = b.edad and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
    datos5 = cursor.fetchall()

    cursor.execute('select a.sexo from puesto a, puesto b, requisicion c where a.sexo = b.sexo and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
    datos6 = cursor.fetchall()

    cursor.execute('select a.funciones from puesto a, puesto b, requisicion c where a.funciones = b.funciones and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
    datos7 = cursor.fetchall()

    cursor.execute('select a.descripciongeneral from puesto a, puesto b, requisicion c where a.descripciongeneral = b.descripciongeneral and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
    datos8 = cursor.fetchall()

    cursor.execute('select a.remunMensual from puesto a, puesto b, requisicion c where a.remunMensual = b.remunMensual and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
    datos9 = cursor.fetchall()

    cursor.execute('select a.puestoJefeSup from puesto a, puesto b, requisicion c where a.puestoJefeSup = b.puestoJefeSup and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
    datos10 = cursor.fetchall()

    cursor.execute('select a.jornada from puesto a, puesto b, requisicion c where a.jornada = b.jornada and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
    datos11 = cursor.fetchall()

    cursor.execute('select a.motivoRequisicion from requisicion a, requisicion b where a.motivoRequisicion = b.motivoRequisicion and b.idRequisicion = %s', (idReq))
    datos12 = cursor.fetchall()

    cursor.execute('select a.motivoEspecifique from requisicion a, requisicion b where a.motivoEspecifique = b.motivoEspecifique and b.idRequisicion = %s', (idReq))
    datos13 = cursor.fetchall()

    return render_template("requisicion_pen.html", req = datos, dat=dato[0], catArea=datos1[0], catPuesto=datos2[0], catEdoCivil=datos3[0], catEscolaridad=datos4[0], catEdad=datos5[0], catSexo=datos6[0], catFunciones=datos7[0], catDescrG=datos8[0], catRemu=datos9[0], catPuestoJS=datos10[0], catJornada=datos11[0], catmotReq=datos12[0], catEsp=datos13[0])


@app.route('/req_borrar/<string:idReq>')
def req_borrar(idReq):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('delete from requisicion where idRequisicion = %s',(idReq))
    conn.commit()
    return redirect(url_for('requisicion_pen'))



@app.route('/requisicion_aut')
def requisicion_aut():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
    cursor = conn.cursor()
    cursor.execute('select idRequisicion, nomSolicita  from requisicion where autorizada=1 order by idRequisicion')
    datos = cursor.fetchall()
    return render_template("requisicion_aut.html", req=datos, dat='   ', catArea='   ', catEdoCivil='   ', catEscolaridad='   ', catPuesto='   ', catEdad='   ', catSexo='   ', catFunciones='   ', catDescrG='   ', catRemu='   ', catPuestoJS='   ', catJornada='   ', catmotReq='   ', catEsp='   ', folio='   ', puestovac='   ')

@app.route('/requisicion_aut_fadetalle/<string:idReq>', methods=['GET'])
def requisicion_aut_fdetalle(idReq):
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
        cursor = conn.cursor()

        cursor.execute('select idRequisicion, nomSolicita  from requisicion where autorizada=1 order by idRequisicion')
        datos = cursor.fetchall()

        cursor.execute('select  idRequisicion,folio ,fechaElab, fechaRecluta , fechaInicVac, nomSolicita, motivoRequisicion , motivoEspecifique, tipoVacante, idPuesto, idArea from requisicion where idRequisicion = %s', (idReq))
        dato = cursor.fetchall()

        cursor.execute('select a.idArea, a.nombre from area a, requisicion b where a.idArea = b.idArea and b.idRequisicion = %s', (idReq))
        datos1 = cursor.fetchall()

        cursor.execute('select a.idPuesto, a.nomPuesto from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idReq))
        datos2 = cursor.fetchall()

        cursor.execute('select a.idEstadocivil, a.nombre from estadocivil a, puesto b, requisicion c where a.idEstadocivil = b.idEstadocivil and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
        datos3 = cursor.fetchall()

        cursor.execute('select a.idEscolaridad, a.nombre from escolaridad a, puesto b, requisicion c where a.idEscolaridad = b.idEscolaridad and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
        datos4 = cursor.fetchall()

        cursor.execute('select a.edad from puesto a, puesto b, requisicion c where a.edad = b.edad and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
        datos5 = cursor.fetchall()

        cursor.execute('select a.sexo from puesto a, puesto b, requisicion c where a.sexo = b.sexo and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
        datos6 = cursor.fetchall()

        cursor.execute('select a.funciones from puesto a, puesto b, requisicion c where a.funciones = b.funciones and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
        datos7 = cursor.fetchall()

        cursor.execute('select a.descripciongeneral from puesto a, puesto b, requisicion c where a.descripciongeneral = b.descripciongeneral and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
        datos8 = cursor.fetchall()

        cursor.execute('select a.remunMensual from puesto a, puesto b, requisicion c where a.remunMensual = b.remunMensual and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
        datos9 = cursor.fetchall()

        cursor.execute('select a.puestoJefeSup from puesto a, puesto b, requisicion c where a.puestoJefeSup = b.puestoJefeSup and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
        datos10 = cursor.fetchall()

        cursor.execute('select a.jornada from puesto a, puesto b, requisicion c where a.jornada = b.jornada and b.idPuesto = c.idPuesto and idRequisicion = %s', (idReq))
        datos11 = cursor.fetchall()

        cursor.execute('select a.motivoRequisicion from requisicion a, requisicion b where a.motivoRequisicion = b.motivoRequisicion and b.idRequisicion = %s', (idReq))
        datos12 = cursor.fetchall()

        cursor.execute('select a.motivoEspecifique from requisicion a, requisicion b where a.motivoEspecifique = b.motivoEspecifique and b.idRequisicion = %s', (idReq))
        datos13 = cursor.fetchall()

        return render_template("requisicion_aut.html", req = datos, dat=dato[0], catArea=datos1[0], catPuesto=datos2[0], catEdoCivil=datos3[0], catEscolaridad=datos4[0], catEdad=datos5[0], catSexo=datos6[0], catFunciones=datos7[0], catDescrG=datos8[0], catRemu=datos9[0], catPuestoJS=datos10[0], catJornada=datos11[0], catmotReq=datos12[0], catEsp=datos13[0])


@app.route('/autoriza')
def autoriza():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
    cursor = conn.cursor()
    cursor.execute('select idRequisicion, nomSolicita  from requisicion where autorizada=1 order by idRequisicion')
    datos = cursor.fetchall()
    return render_template("autoriza.html", req=datos, dat='   ', catArea='   ', catEdoCivil='   ', catEscolaridad='   ', catPuesto='   ', catEdad='   ', catSexo='   ', catFunciones='   ', catDescrG='   ', catRemu='   ', catPuestoJS='   ', catJornada='   ', catmotReq='   ', catEsp='   ', folio='   ', puestovac='   ')

@app.route('/autoriza_fagrega', methods=['POST'])
def autoriza_fagrega():
    if request.method == 'POST':

        nomR = request.form['nomRevisa']
        nomA = request.form['nomAutoriza']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()
    cursor.execute('update requisicion set nomRevisa = %s, nomAutoriza = %s, autorizada = 1',(nomR, nomA))
    conn.commit()
    return redirect(url_for('requisicion_aut'))


@app.route('/autoriza_fdetalle/<string:idReq>', methods=['GET'])
def autoriza_fdetalle(idReq):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda')
    cursor = conn.cursor()

    cursor.execute('select a.folio from requisicion a where a.idRequisicion = %s', (idReq))
    datos1 = cursor.fetchall()

    cursor.execute('select a.idPuesto, a.nomPuesto from puesto a, requisicion b where a.idPuesto = b.idPuesto and b.idRequisicion = %s', (idReq))
    datos2 = cursor.fetchall()

    print(datos1)
    print(datos2)
    print(idReq)

    return render_template("autoriza.html", folio=datos1[0], puestovac=datos2[0])


if __name__ == "__main__":
    app.run(debug=True)