 $(document).ready(function () {
        

             $('body').on("click", "#compute", function(e) {
                e.stopPropagation();
                e.preventDefault();
            jQuery.support.cors = true;
            console.log("in ajax req")
            console.log("compute: ",this.form.display.value);
            var exp = this.form.display.value;
            exp = exp.replace('^','**')
            if(exp.includes("sqrt ")){
            exp = exp.replace('sqrt ',"math.sqrt(");
            exp = exp+')';
        }
            else if(exp.includes("ln ")){
            exp = exp.replace('ln ',"log(");
            exp = exp+')';
            }
            else if(exp.includes("sin ")){
            exp = exp.replace('sin ',"sin(");
            exp = exp+')';
            }
            console.log("exp after replace: ",exp)
            // if(checkExpression(exp)){

                $.ajax(
                {
                    
                    url: 'http://localhost:8085/compute',
                    type: "GET",
                    data: {"exp":exp,"operationType":"math"},
                    //dataType:"jsonp",
                    //jsonp:"callback",
                    crossDomain: true,
                    //contentType: "application/json; charset=utf-8",

                    dataType: "json",
          //            headers: {
          //           //     "User-Agent":"Chrome",
          //     "accept": "application/json",
          //     "Access-Control-Allow-Origin":"*"
          //     // "Access-Control-Request-Method": "POST",
          //     // "Access-Control-Request-Headers": "X-PINGOTHER, Content-Type"
          // },
                    //dataType: "json",
                    success: function (data) {
                        console.log("in success response: ",data)
                        console.log("result here: ",data["result"])

                        //console.log("randNum here: ",data["randNum"])
                        
                        // this.form.display.value = data["result"];

                       $("#display").val(data["result"]);


                        
                    },
                    error: function () {
                        console.log("in error response: ")
                       

                        // alert('error trapped in error: function(msg, url, line)');
                        // alert('msg = ' + msg + ', url = ' + url + ', line = ' + line);

                    }
                });

            // }
            

        });

             $('body').on("click", ".btnStr", function(e) {
                e.stopPropagation();
                e.stopImmediatePropagation();
                e.preventDefault();
                console.log("in str: ",$(this).attr('id'))
                operation  = $(this).attr('id');
            jQuery.support.cors = true;
            console.log("in ajax req")
            console.log("compute string: ",this.form.display1.value);
            console.log("compute string: ",this.form.display2.value);
            var exp1 = this.form.display1.value;
            var exp2 = this.form.display2.value;
           

                $.ajax(
                {
                    
                    url: 'http://localhost:8085/compute',
                    type: "GET",
                    data: {"exp1":exp1,"exp2":exp2,"operationType":"string","operation":operation},
                    //dataType:"jsonp",
                    //jsonp:"callback",
                    crossDomain: true,
                    //contentType: "application/json; charset=utf-8",

                    dataType: "json",
          //            headers: {
          //           //     "User-Agent":"Chrome",
          //     "accept": "application/json",
          //     "Access-Control-Allow-Origin":"*"
          //     // "Access-Control-Request-Method": "POST",
          //     // "Access-Control-Request-Headers": "X-PINGOTHER, Content-Type"
          // },
                    //dataType: "json",
                    success: function (data) {
                        console.log("in success response: ",data)
                        console.log("result here: ",data["result"])

                        //console.log("randNum here: ",data["randNum"])
                        
                        // this.form.display.value = data["result"];

                       $("#str-display1").val(data["result"]);


                        
                    },
                    error: function () {
                        console.log("in error response: ")
                       

                        // alert('error trapped in error: function(msg, url, line)');
                        // alert('msg = ' + msg + ', url = ' + url + ', line = ' + line);

                    }
                });

            
            

        });
    });
 function checkExpression(str){
    console.log("checking validity of exp");
    for (var i = 0; i < str.length; i++) {
        var ch = str.charAt(i);
        if (ch < "0" || ch > "9") {
            if (ch != "/" && ch != "*" && ch != "+" && ch != "-" && ch != "."
                && ch != "(" && ch!= ")" && ch != "%" && ch!="**" && ch!="s" && ch!="q" && ch!="r" && ch!="t" && ch!=" ") {
                alert("invalid entry!"+ch)
                return false
                }
            }
        }
        return true
// }
}
function addChar(input, character) {
    if(input.value == null || input.value == "0")
        input.value = character
    else
        input.value += character
}

function reverseString(input){
    console.log("str: ",input.value)
    if(input.value!=null && input.value!="")
        console.log("str: ",input.value)
        input.value = input.value.split("").reverse().join("");
}

function toUpper(input){
    if(input.value!=null && input.value!="")
        input.value = input.value.toUpperCase();
}
function toLower(input){
    if(input.value!=null && input.value!="")
        input.value = input.value.toLowerCase();
}

function concatenate(input1,input2){
    input1.value+=input2.value;

}

function cos(form) {
    form.display.value = Math.cos(form.display.value);
}

function sin(form) {
    form.display.value = Math.sin(form.display.value);
}

function tan(form) {
    form.display.value = Math.tan(form.display.value);
}

function sqrt(form) {
    form.display.value = Math.sqrt(form.display.value);
}

function ln(form) {
    form.display.value = Math.log(form.display.value);
}

function exp(form) {
    form.display.value = Math.exp(form.display.value);
}

function deleteChar(input) {
    input.value = input.value.substring(0, input.value.length - 1)
}
var val = 0.0;
function percent(input) {
  val = input.value;
  input.value = input.value + "%";
}

function changeSign(input) {
    if(input.value.substring(0, 1) == "-")
        input.value = input.value.substring(1, input.value.length)
    else
        input.value = "-" + input.value
}

// function compute(form) {
//   //if (val !== 0.0) {
//    // var percent = form.display.value;  
//    // percent = pcent.substring(percent.indexOf("%")+1);
//    // form.display.value = parseFloat(percent)/100 * val;
//     //val = 0.0;
//  // } else 
//     form.display.value = eval(form.display.value);
//   }


function square(form) {
    form.display.value = eval(form.display.value) * eval(form.display.value)
}
