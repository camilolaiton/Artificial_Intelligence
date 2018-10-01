function nuevoCaracter(){
	var c = floor(random(32, 123));

	return String.fromCharCode(c);
}

function ADN(cantidad){
	this.genes = [];
	this.fitness = 0;

	for (var i = 0; i < cantidad; i++) {
		this.genes[i] = nuevoCaracter();
	}

	this.calcularFitness = function(target){

		var puntaje = 0;

		for (var i = 0; i < this.genes.length; i++) {

			if(this.genes[i] == target.charAt(i)){

				puntaje++;
			}
		}

		this.fitness = puntaje / target.length;
		this.fitness = pow(this.fitness, 2) + 0.01;
	}

	this.obtenerFitness = function(){
		return this.fitness;
	}

	this.crossover = function(padre){

		var hijo = new ADN(this.genes.length);
		var puntoMedio = floor(random(this.genes.length));

		for (var i = 0; i < this.genes.length; i++) {
			if(i > puntoMedio) hijo.genes[i] = this.genes[i];
			else hijo.genes[i] = padre.genes[i];
		}

		return hijo;
	}

	this.mutacion = function(porcentajeMutacion){

		for (var i = 0; i < this.genes.length; i++) {
			
			if(random(1) < porcentajeMutacion){
				this.genes[i] = nuevoCaracter();
			}
		}
	}

	this.comparar = function(objetivo){

		for (var i = 0; i < this.genes.length; i++) {
			
			if(this.genes[i] != target.charAt(i)){
				return false;
			}
		}

		return true;
	}

	this.obtenerFrase = function(){
		return this.genes.join("");
	}
}