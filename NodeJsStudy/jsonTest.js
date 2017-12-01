// li =  [1,2,3,4];
// var s = JSON.stringify(li)//序列化
// var newli = JSON.parse(s)//反序列化
// console.log(newli)

// var formular = '8*8';
// console.log(eval(formular))                                                                                                                                                                                                                                                                                                                                                                                                                           
xo = "alex";                                                                                                                                                                                                                    
function func(){

	var xo = 'eric';
	function inner(){
		console.log(xo)
	}
	var xo = 'tony';
	return inner;
}                

var ret = func();
ret()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 	