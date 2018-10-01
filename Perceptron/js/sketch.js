
var p;
var puntos = [];

function setup() {
	createCanvas(500, 500);
	p = new perceptron();
	console.log(p.salida([-1, 0.5]));

	for (var i = 0; i < 50; i++) {
		puntos[i] = new punto();
	}
}

function draw() {
  	background(150);
  	stroke(0);
  	line(0, 0, width, height);

  	for (var i = 0; i < puntos.length; i++) {
  		puntos[i].show();
  	}

  	for (var i = 0; i < puntos.length; i++) {
  		//p.entrenar([puntos[i].x, puntos[i].y], puntos[i].etiqueta);

  		var guess = p.salida([puntos[i].x, puntos[i].y]);

  		if (guess == puntos[i].etiqueta) {
  			fill(0, 255, 0);
  		} else {
  			fill(255, 0, 0);	
  		}

  		noStroke();
  		ellipse(puntos[i].x, puntos[i].y, 7, 7);
  	}
}

function mousePressed() {
	for (var i = 0; i < puntos.length; i++) {
  		p.entrenar([puntos[i].x, puntos[i].y], puntos[i].etiqueta);
  	}

  	console.log("Pesos: ", p.pesos);
  	console.log("MouseX: ", mouseX, " y MouseY: ", mouseY);
  	puntos.push(new punto(mouseX, mouseY));
}