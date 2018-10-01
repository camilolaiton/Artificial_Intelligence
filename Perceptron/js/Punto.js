function punto() {

	if (arguments.length != 0) {
		this.x = arguments[0];
		this.y = arguments[1];
	} else {
		this.x = random(width);
		this.y = random(height);
		this.etiqueta;
	}

	if (this.x > this.y) {
		this.etiqueta = 1;
	}
	else {
		this.etiqueta = -1;
	}

}

punto.prototype.show = function() {
	
	stroke(0);

	if (this.etiqueta == -1 ) {
		fill(255);
	}
	else {
		fill(0);
	}

	ellipse(this.x, this.y, 10, 10);
}