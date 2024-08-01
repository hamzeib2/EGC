

// Now you can send any text(even a form data) by calling sendMessage function.
// For example if you want to send the 'hello', you can call that function like this:

//sendMessage("hello");

// Bot token 5947359274:AAEw3xjBrSQdSnpK5nU40iiWKogqsLAY8zg
// chat id for me

// {
//    "update_id": 829776484,
//    "message": {
//        "message_id": 2234935,
//        "from": {
//            "id": 867971529,
//            "is_bot": false,
//            "first_name": "Hamze",
//            "last_name": "ibrahim",
//            "username": "hamzeib",
//            "language_code": "en"
//        },
//        "chat": {
//            "id": 867971529,
//            "first_name": "Hamze",
//            "last_name": "ibrahim",
//            "username": "hamzeib",
//            "type": "private"
//        },
//        "date": 1686039045,
//        "text": "/start",
//        "entities": [
//            {
//                "offset": 0,
//                "length": 6,
//                "type": "bot_command"
//            }
//        ]
//    }
// }



// AAAA-ABCDEF-ABCD
// AAAA-ABCDEF-ABCD
// AAAA-ABCDEF-ABC1
// AAAA-ABCDEF-ABC2
// AAAA-ABCDEF-ABC3
// AAAA-ABCDEF-ABC4
// AAAA-ABCDEF-ABC5
// AAAA-ABCDEF-ABC6
// AAAA-ABCDEF-ABC7
// AAAA-ABCDEF-ABC8
// AAAA-ABCDEF-ABC9
// AAAA-ABCDEF-AB10
// AAAA-ABCDEF-ABCD
// AAAA-ABCDEF-ABCD

function updateuserorder(prdid , cards ,value){
   console.log('Searching for data')

   var url = '/Process_cards/'

   fetch(url , {
       method:'POST',
       headers:{
           'Content_Type':'application/json',
           'X-CSRFToken': csrftoken,
       },
       body:JSON.stringify({'prdid':prdid,'cards':cards ,'value':value})
   })
   .then((response) => {
       return response.json()

   })

   .then((data) => {
       console.log('data:',data)
       location.reload()
       
   })
//    bot_send_message()

}


function reset_cards(user){
    var url = '/Reset_Draw_Cards/'

   fetch(url , {
       method:'POST',
       headers:{
           'Content_Type':'application/json',
           'X-CSRFToken': csrftoken,
       },
       body:JSON.stringify({'user':user})
   })
   .then((response) => {
       return response.json()

   })

   .then((data) => {
       console.log('data:',data)
       location.reload()
       
   })
}

function getuserinvoice(user){
    console.log('Searching for data')

   var url = '/getuserinvoice/'

   fetch(url , {
       method:'POST',
       headers:{
           'Content_Type':'application/json',
           'X-CSRFToken': csrftoken, 
       },
       body:JSON.stringify({'user':user })     
   })
   .then((response) => {  
       return response.json()

   })

   .then((data) => {  
       console.log('data:',data)
    //    location.reload()  
       
   })
}


function getsearchcode(code){
    console.log('Searching for data')

   var url = '/getsearchcode/'

   fetch(url , {
       method:'POST',
       headers:{
           'Content_Type':'application/json',
           'X-CSRFToken': csrftoken, 
       },
       body:JSON.stringify({'code':code })     
   })
   .then((response) => {  
       return response.json()

   })

   .then((data) => {  
       console.log('data:',data)
       location.reload()  
       
   })
}





function resetuserorder(prdid){
   console.log('Searching for data')

   var url = '/Reset_cards/'

   fetch(url , {
       method:'POST',
       headers:{
           'Content_Type':'application/json',
           'X-CSRFToken': csrftoken,
       },
       body:JSON.stringify({'prdid':prdid})
   })
   .then((response) => {
       return response.json()

   })

   .then((data) => {
       console.log('data:',data)
       location.reload()
       
   })
}


function resetuserbill(user){
    var url = '/Reset_bill/'

   fetch(url , {
       method:'POST',
       headers:{
           'Content_Type':'application/json',
           'X-CSRFToken': csrftoken,
       },
       body:JSON.stringify({'user':user})
   })
   .then((response) => {
       return response.json()

   })

   .then((data) => {
       console.log('data:',data)
       location.reload()
       
   })
}



var user = '{{request.user}}'
function getToken(name) {
let cookieValue = null;
if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
    }
}
return cookieValue;
}
const csrftoken = getToken('csrftoken');

/////////////////////////////////////////////////////////////////////////
//المهم بهاد التابع انو بيجيب الكوكيز يلي عنا بالمتصفح عن طريق اسما منمررو واذا مافي كوكيز بهاد الاسم بيرجع نول هاد الكود غير يل ذاكرو بالكورس يلي بالكورس بيضل يانشئ كوكيز جديدة
function getCookie(name) {
var nameEQ = name + "=";
var ca = document.cookie.split(';');
for (var i = 0; i < ca.length; i++) {
var c = ca[i];
while (c.charAt(0) == ' ') c = c.substring(1, c.length);
if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
}
return null;
}
var cart = JSON.parse(getCookie('cart'))//جبنا الكوكيز عن طريق اسمها وحطيناها بمتحول
console.log(cart)

if (cart == undefined){// اذا ماكان عنا كوكيز منحليها فاضية ومنبعتا للمتصفح بعد مانقصرها لسترينغ لان لازم تكون قيمة وحيدة مو اوبجكت
cart = {}
console.log('cart created')
document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
//هاي الطريقة لنبعت كوكيز للمتصفح فيك تشوفها هلق بالمتصفح من الابليكيشن واخر قيمة مشان نخلي الكوكيز للدومين تبع الموقع مشان مايضل يانشئ كوكيز جديدة بكل صفحة
}

console.log('cart:' , cart)