function Population(target, N, mutation){

	this.target = target; //Objetivo
	this.cantidad = N; //Cantidad de elementos en la poblacion
	this.mutacion = mutation; //Rango de mutacion
	this.generaciones = 0; //Cantidad de generaciones en la poblacion
	this.finished = false; //Si ya termino el proceso
	this.poblacion = []; //Array donde se guardan los elementos de la poblacion
	this.respuesta = "";

	for (var i = 0; i < this.cantidad; i++) { //Creacion de la poblacion
		this.poblacion[i] = new ADN(this.target.length); //ADN - palabras misma len de target
	}

	this.calcularFitness = function(){ //Se calcula el fitness de cada elemento de la poblacion
		for (var i = 0; i < this.poblacion.length; i++) {
			this.poblacion[i].calcularFitness(this.target);
		}
	}

	this.apareamiento = function(){ //Momento de apareamiento entre elementos de la poblacion
		
		this.piscinaApareamiento = [];

		var maxFitness = 0;
		//Se encuentra el maximo fitness dentro de la poblacion para mapear y elegir uno random
		for (var i = 0; i < this.poblacion.length; i++) {
			
			if(this.poblacion[i].fitness > maxFitness){
				maxFitness = this.poblacion[i].fitness;
			}
		}

		for (var i = 0; i < this.poblacion.length; i++) {
			
			var fitness = map(this.poblacion[i].fitness, 0, maxFitness, 0, 1); //Se mapea el maximo fitness para poder elegir de ellos en un array
			var n = floor(fitness*100);

			for (var j = 0; j < n; j++) {
				this.piscinaApareamiento.push(this.poblacion[i]); //Se meten dentro de la piscina de apareamiento para luego elegir dos
			}
		}
	}

	this.generar = function(){//Funcion para elegir los padres y generar nuevos hijos

		var maxFitness = 0;
		//Se encuentra el maximo fitness dentro de la poblacion para mapear y elegir uno random
		for (var i = 0; i < this.poblacion.length; i++) {
			
			if(this.poblacion[i].fitness > maxFitness){
				maxFitness = this.poblacion[i].fitness;
			}
		}

		var nuevaPoblacion = [];

		for (var i = 0; i < this.poblacion.length; i++) {//Recorro toda la poblacion


			var padreA = this.aceptarRechazar(maxFitness);
			var padreB = this.aceptarRechazar(maxFitness);

			var hijo = padreA.crossover(padreB);//Hago el crossover de forma random entre los padres y genero otro elemento ADN hijo
			hijo.mutacion(this.mutacion);//Realizo la mutacion de el hijo que es nuevo elemento
			hijo.calcularFitness(this.target);

			nuevaPoblacion[i] = hijo;//Introduzco hijo en poblacion y asi genero una nueva poblacion
		}

		this.poblacion = nuevaPoblacion;
		this.generaciones++; //Aumento la cantidad de generaciones
	}

	this.isFinished = function(){

		return this.finished;
	}

	this.mejorFrase = function(){

		return this.respuesta;
	}

	this.evaluar = function(){
		var mejorPuntaje = 0.0;
		var index = 0;

		for (var i = 0; i < this.poblacion.length; i++) {
			
			if(this.poblacion[i].fitness > mejorPuntaje){
				index = i;
				mejorPuntaje = this.poblacion[i].obtenerFitness();
				
			}
		}

		this.respuesta = this.poblacion[index].obtenerFrase();

		if(mejorPuntaje >= 1){
			
			this.finished = true;
		}
	}

	this.todasLasFrases = function(){
		var todo = "";

		var limite = min(this.poblacion.length, 30);

		for (var i = 0; i < limite; i++) {
			todo += this.poblacion[i].obtenerFrase() + "<br>";
		}

		return todo;
	}


	this.aceptarRechazar = function(maxFitness){

		while(true){

			var padre = this.poblacion[floor(random(this.poblacion.length))];
			var valor = random(maxFitness);

			if(valor < padre.fitness){
				return padre;
			}
		}
	}
}