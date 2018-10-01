var target;
var N;
var rangoMutacion;
var poblacion;

var mejorFrase;
var frases;
var estadisticas;

function setup() {
	mejorFrase = createP("Mejor frase: ");
	mejorFrase.class("mejorFrase");

	frases = createP("Todas las frases: ");
	frases.position(600, 10);
	frases.class("frases");

	estadisticas = createP("Estadisticas: ");
	estadisticas.class("estadisticas");

	target = "Camilo adnres Laiton BonadieQQ@z"; //Objetivo
	N = 800; //Poblacion maxima
	rangoMutacion = 0.01; //Porcentaje de mutacion

	poblacion = new Population(target, N, rangoMutacion); //Se crea el objeto poblacion con el objetivo
}

function draw(){

	poblacion.calcularFitness(); //Calculo el fitness de todos los elementos de la poblacion

	//poblacion.apareamiento(); //Genero la piscina de apareamiento para elegir los padres segun su fitness - seleccion

	poblacion.generar(); //Genero una nueva poblacion apartir de la piscina de apareamiento

	poblacion.evaluar();

	if(poblacion.isFinished() == true){
		noLoop();
	}

	mostrarInfo();	
}

function mostrarInfo(){

	var respuesta = poblacion.respuesta;

	mejorFrase.html("Mejor frase:<br>" + respuesta);

	var textoEstadisticas = "Total generaciones: " + poblacion.generaciones + "<br>";
	textoEstadisticas += "Total poblacion: " + N + "<br>";
	textoEstadisticas += "Porcentaje de mutacion: " + rangoMutacion;

	estadisticas.html(textoEstadisticas);
	frases.html("Todas las frases:<br>" + poblacion.todasLasFrases());		
}