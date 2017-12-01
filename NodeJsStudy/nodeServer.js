console.log("Hello World!")
var domainName = "www.json.com"
var remove = function(domainName){
	console.log(domainName);
	return domainName;
}

var dn = remove(domainName);
console.log(dn);
function output1(domainName,name,email,age,click){
	console.log('output callback'+domainName+'|'+name+'|'+email+'|'+age+'|'+click);
}
function read1(callback,domainName,name,email,age,click){
	console.log("read function");
	callback(domainName,name,email,age,click);
}

read1(output1,'www.json.com','json','bill@sina.com',23,3000);


function WebSite(domainName,name,email,age,click){
	this.domainName = domainName;
	this.name = name;
	this.email = email;
	this.age = age;
	this.click = click;
	// this.setDomainName = function(domainName){
	// 	this.domainName = domainName;
	// }
	// this.getDomianName = function(){
	// 	return this.domainName;
	// }
}
WebSite.prototype.setDomainName = function(domainName){
	this.domainName = domainName;
}
WebSite.prototype.getDomianName = function(){
	return this.domainName;
}

// function webSite(d,n,e,a,c){
// 	var myDomainName ,myName,myEmail,myAge,myClick;
// 	function set(domainName, name ,email,age,click){
// 		myDomainName = domainName;
// 		myName = name;
// 		myEmail = email;
// 		myAge = age;
// 		myClick = click;
// 	}
// 	set(d,n,e,a,c);
// 	return [myDomainName, myName ,myEmail,myAge,myClick];
// }

// console.log(webSite('www.json.com','json','bill@sina.com',23,3000))


// var webSite1 = {};
// webSite1.domainName = "www.json.com";
// webSite1.name = "json";
// webSite1.email = "bill@sina.com";
// webSite1.age = 22;
// webSite1.click = 3000;

// console.log(webSite1)

// webSite1.setDomainName = function(domainName){
// 	this.domainName = domainName;
// }

// webSite1.getDomianName = function(){
// 	return this.domainName;
// }

// webSite1.setDomainName("www.bill.com");
// console.log(webSite1);

var webSite2 = new WebSite("www.baidu.com","baidu","email@baidu.com",10,200);
webSite2.setDomainName("baidu.com")
console.log("webSite2:",webSite2)

var http = require('http');
function requestListener(req,res){

}
var server = http.createServer(requestListener);

server.listen(7798);