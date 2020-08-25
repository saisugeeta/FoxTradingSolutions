
// Function called on change of the dropdown(units) which will change the value from F to C and viceversa
function change_function(key)
{
    key=key.toString();
    var ch=key.concat("dropdown");



    if (document.getElementById(ch).value=="F")
    {
 
        document.getElementById(key).innerHTML=((document.getElementById(key).innerHTML*1.8)+32).toFixed(2);
    }
    if (document.getElementById(ch).value=="C")
    {
    document.getElementById(key).innerHTML=((document.getElementById(key).innerHTML-32)/1.8).toFixed(2);

    }
}
// Function triggered on change of the update dropdown

function onchange_function1(key)
{
    key=key.toString();
    
    var ch=key.concat("_update");
    var id_update=key.concat("_updatevalue");
    //alert("rr");
    document.getElementById(id_update).innerHTML=document.getElementById(ch).value;
    //alert(document.getElementById(id_value));
 


    // GET is the default method, so we don't need to set it
    fetch('/request_response')
        .then(function (response) {
            return response.text();
        }).then(function (text) {
            console.log('GET response text:');
            console.log(text); // Print the greeting as text
        });

    // Send the same request
    fetch('/request_response')
        .then(function (response) {
            return response.json(); // But parse it as JSON this time
        })
        .then(function (json) {
            console.log('GET response as JSON:');
            console.log(json); // Here’s our JSON object
        })
    fetch('/request_response', {

        // Specify the method
        method: 'POST',

        // A JSON payload
        body: JSON.stringify({
            "key": key,"value":document.getElementById(ch).value
        })
    }).then(function (response) { // At this point, Flask has printed our JSON
        return response.text();
    }).then(function (text) {

        console.log('POST response: ');

        // Should be 'OK' if everything was successful
        console.log(text);
    });




 

}



