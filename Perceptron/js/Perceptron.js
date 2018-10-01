function perceptron() {
	this.pesos = [];
	this.lr = 0.1;

	for (var i = 0; i < 2; i++) {
		this.pesos[i] = random(-1, 1);
	}
}

perceptron.prototype.salida = function(entradas) {

	var suma = 0;

	for (var i = 0; i < this.pesos.length; i++) {
		suma += this.pesos[i] * entradas[i]
	}

	return signo(suma);
}

//Ajustar todos los pesos
perceptron.prototype.entrenar = function(entradas, objetivo) {

	var guess = this.salida(entradas);
	var error = objetivo - guess;

	for (var i = 0; i < this.pesos.length; i++) {
		this.pesos[i] += error * entradas[i] * this.lr;
	}
}

function signo(numero) {

	if (numero >= 0) {
		return 1;
	}
	else {
		return -1;
	}
}