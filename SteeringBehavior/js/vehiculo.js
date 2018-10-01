function Vehiculo(x, y) {
	this.pos = createVector(x, y);
	this.vel = createVector();
	this.acel = createVector();
	this.maxSpeed = 5;
	this.maxForce = 0.5;
	this.r = 5;
	this.salud = 1;

	this.adn = [];

	// Peso de la comida
	this.adn[0] = random(-2, 2);

	//Peso de el veneno
	this.adn[1] = random(-2, 2);

	//Percepcion de la comida
	this.adn[2] = random(0, 100);

	//Percepcion del veneno
	this.adn[3] = random(0, 100);
}

Vehiculo.prototype.applyForce = function(fuerza) {
	this.acel.add(fuerza);
}

Vehiculo.prototype.show = function() {
	/*
	stroke(255);
	strokeWeight(30);
	//triangle(300, 100, 320, 100, 310, 80);
	point(this.pos.x, this.pos.y);
	*/
	console.log("INFORMACION: " + this.vel);
	noFill();
	stroke(0,255,0);
	ellipse(this.pos.x , this.pos.y, this.adn[2] * 2);

	stroke(255, 0, 0);
	ellipse(this.pos.x, this.pos.y, this.adn[3] * 2);
	
	var angulo = this.vel.heading() + PI/2;
	fill(127);
	stroke(200);
	strokeWeight(1);
	push();
	translate(this.pos.x, this.pos.y);
	rotate(angulo);
	beginShape();
	vertex(0, -this.r*2);
	vertex(-this.r, this.r * 2);
	vertex(this.r, this.r*2);
	endShape(CLOSE);
	pop();
}

Vehiculo.prototype.update = function () {
	this.salud -= 0.01;

	console.log(this.salud);
	this.pos.add(this.vel);
	this.vel.add(this.acel);
	this.acel.mult(0);
}

Vehiculo.prototype.seek = function (target) {
	var desired = p5.Vector.sub(target, this.pos);
	var d = desired.mag();
	var speed = this.maxSpeed;
	/*
	if(d < 100) {
		speed = map(d, 0, 100, 0, this.maxSpeed);
	}
	*/
	desired.setMag(speed);
	var steer = p5.Vector.sub(desired, this.vel);
	steer.limit(this.maxForce);
	return steer;
}

Vehiculo.prototype.behaviors = function (target) {
	var seek = this.seek(target);
	this.applyForce(seek);
}

Vehiculo.prototype.eat = function (listaComida, vida, percepcion) {
	var record = Infinity;
	var cercanoIndex = -1;

	for (var i = 0; i < listaComida.length; i++) {
		var d = this.pos.dist(listaComida[i]);

		if(d < record && d < percepcion) {
			record = d;
			cercanoIndex = i;
		}
	}


	if (record < 5) {
		listaComida.splice(cercanoIndex, 1);
		this.salud = this.salud + vida;
	}
	else if(cercanoIndex > -1){
		return this.seek(listaComida[cercanoIndex]);
	}

	return createVector(0, 0);
	
}

Vehiculo.prototype.comportamiento = function (bueno, malo) {
	var comidaBuena = this.eat(bueno, 0.5, this.adn[2]);
	var comidaMala = this.eat(malo, -0.5, this.adn[3]);

	comidaBuena.mult(this.adn[0]);
	comidaMala.mult(this.adn[1]);

	this.applyForce(comidaBuena);
	this.applyForce(comidaMala);
}

Vehiculo.prototype.isDead = function () {
	
	if (this.salud <= 0) {
		return true;
	}

	return false;
}

Vehiculo.prototype.inTheWalls = function () {
	
	var d = 25;
	var desired = null;

	if (this.pos.x < d) {
		desired = createVector(this.maxSpeed, this.vel.y);
	}
	else if (this.pos.x > width - d) {
		desired = createVector(-this.maxSpeed, this.vel.y);
	}

	if (this.pos.y < d) {
		desired = createVector(this.vel.x, this.maxSpeed);
	}
	else if (this.pos.y > height - d) {
		desired = createVector(this.vel.x, -this.maxSpeed);
	}

	if (desired != null) {
		desired.normalize();
		desired.mult(this.maxSpeed);
		var steer = p5.Vector.sub(desired, this.vel);
		steer.limit(this.maxForce);
		this.applyForce(steer);
	}
}