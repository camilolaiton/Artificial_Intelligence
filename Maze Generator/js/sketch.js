var cols, rows;
var w = 20; // w diffent from 0
var grid = [];

var current;

var stack = [];

function setup() {
	createCanvas(400,400);
	//frameRate(10);

	cols = floor(width/w);
	rows = floor(height/w);

	for (var j = 0; j < rows; j++) {
		for (var i = 0; i < cols; i++) {
			var cell = new Cell(i, j);
			grid.push(cell);
		}
	}

	current = grid[0];
}

function draw() {
  	background(100);

  	for (var i = 0; i < grid.length; i++) {
  		grid[i].show();
  	}

  	current.visited = true;
  	current.highlight();

  	//Paso 1
  	var next = current.checkNeighbors();
  	
  	if(next){
  		next.visited = true;

  		//Paso 2
  		stack.push(current);

  		//Paso 3
  		removeWalls(current, next);

  		current = next;
  	}
  	else if(stack.length > 0){
  		//Backtracking
  		current = stack.pop();
  	}
}

function index(i, j) {
	
	if(j < 0 || i < 0 || i > cols-1 || j > rows-1){
		return -1;
	}

	return i + j * cols;
}

function Cell(i, j){

	this.i = i;
	this.j = j;
	this.walls = [true, true, true, true]; // top, right, bottom, left
	this.visited = false;

	this.checkNeighbors = function () {
		
		var neighbors = [];

		var top = grid[index(i, j-1)];
		var right = grid[index(i+1, j)];
		var bottom = grid[index(i, j+1)];
		var left = grid[index(i-1, j)];

		if(top && !top.visited){
			neighbors.push(top);
		}

		if(right && !right.visited){
			neighbors.push(right);
		}

		if(bottom && !bottom.visited){
			neighbors.push(bottom);
		}

		if(left && !left.visited){
			neighbors.push(left);
		}

		if(neighbors.length > 0){
			var r = floor(random(0, neighbors.length));
			return neighbors[r];
		}else{
			return undefined;
		}
	}

	this.show = function(){
		var x = this.i * w;
		var y = this.j * w;
		stroke(255);

		if(this.walls[0]){
			line(x,y,x+w,y);
		}
		
		if(this.walls[1]){
			line(x+w,y,x+w,y);
		}
		
		if(this.walls[2]){
			line(x+w,y+w,x,y+w);
		}
			
		if(this.walls[3]){
			line(x,y+w,x,y);
		}
		
		if(this.visited){
			noStroke();

			if(this == grid[grid.length-1]){
				fill('rgb(255, 0 , 0)');
			}
			else{
				fill(255, 180, 255, 150);
			}
			
			rect(x,y,w,w);
		}
	}

	this.highlight = function(){
		var x = this.i * w;
		var y = this.j * w;
		noStroke();
		fill('rgb(0,255,0)');
		rect(x, y, w, w);
	}
}

function removeWalls(a, b){

	var x = a.i - b.i;

	if(x == 1){
		a.walls[3] = false;
		b.walls[1] = false;
	}
	else if(x == -1){
		a.walls[1] = false;
		b.walls[3] = false;
	}

	var y = a.j - b.j;

	if(y == 1){
		a.walls[0] = false;
		b.walls[2] = false;
	}
	else if(y == -1){
		a.walls[2] = false;
		b.walls[0] = false;
	}
}