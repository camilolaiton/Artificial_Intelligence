var vehiculos = [];
var comida = [];
var veneno = [];

function setup() {
	createCanvas(600,600);
	
	for (var i = 0; i < 10; i++) {
		var x = random(width);
		var y = random(height);
		vehiculos[i] = new Vehiculo(x, y);
	}
	 
	comida = crearElementos(40);
	veneno = crearElementos(20);
}

function draw() {
	background(51);

	mostrarElementos(comida, 'rgb(0,255,0)');
	mostrarElementos(veneno, 'rgb(255,0,0)');

	if (random(1) < 0.01) {
		var x = random(width);
		var y = random(height);
		comida.push(createVector(x, y));
	}

	if (random(1) < 0.005) {
		var x = random(width);
		var y = random(height);
		veneno.push(createVector(x, y));
	}

	for (var i = 0; i < vehiculos.length; i++) {
		vehiculos[i].inTheWalls();
		vehiculos[i].comportamiento(comida, veneno);
		vehiculos[i].update();
		vehiculos[i].show();

		if (vehiculos[i].isDead()) {
			vehiculos.splice(i, 1);
		}
	}

	if (vehiculos.length == 0) {
		noLoop();
	}
}


function crearElementos(cantidadElementos) {
	
	var lista = [];

	for (var i = 0; i < cantidadElementos; i++) {
		var x = random(width);
		var y = random(height);
		lista.push(createVector(x, y));
	}

	return lista;
}

function mostrarElementos(lista, color) {
	
	for (var i = 0; i < lista.length; i++) {
		fill(color);
		noStroke();
		ellipse(lista[i].x, lista[i].y, 8, 8);
	}
}