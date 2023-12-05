
var DEBUG = true
document.addEventListener('DOMContentLoaded',function(){
    
    // change_selected_plan()  
    var edit_app_popup_form_buttons = document.getElementsByClassName('delete_app_popup_form_button')
    for(let i=0;i<edit_app_popup_form_buttons.length;i++){
        edit_app_popup_form_buttons[i].onclick = function(){
            document.getElementById('app_edit_msg').innerHTML = '';
            var app_id = edit_app_popup_form_buttons[i].getAttribute('app_id')
            console.log(app_id);
            var edit_submit = document.getElementById('edit_submit')
            edit_submit.setAttribute('app_id',app_id)

        }
    }
 
    
})

function getCookie(name) {
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


async function create_app(){
    document.getElementById("create_app_button").onclick = function() {
        document.getElementById('app_created_msg').innerHTML = '';
    };
    
   const createsappUrl = '/dashboard/APIs/create_app'; 
        var scrf = getCookie("csrftoken")
        try {
            const response = await fetch(createsappUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',// Specify the content type (JSON in this example).
                    "X-CSRFToken":scrf, 
                    // Add any other headers you may need, such as authorization headers.
                },

                body: JSON.stringify({
                    'app_name':document.getElementById('new_app_name').value,
                    'app_description':document.getElementById('new_app_description').value,
                }), // Convert your data to JSON format.
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const result = await response.json(); // Parse the response JSON if the server sends a response.
            if (DEBUG === true){
            if (result['msg'] == "app is created")
            {
                document.getElementById('app_created_msg').innerHTML = 'App Created'
            console.log('app is created');
            }
            else console.log("app is not created",result)
            }
        } catch (error) {
            if (DEBUG === true)
            console.error('An error occurred while creating app:', error);
        }
}


async function update_app(){
    var app_id = document.getElementById('edit_submit').getAttribute('app_id')
    const updateappUrl = `/dashboard/APIs/update_app/${app_id}`; 
        var scrf = getCookie("csrftoken")
        try {
            const response = await fetch(updateappUrl, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',// Specify the content type (JSON in this example).
                    "X-CSRFToken":scrf, 
                    // Add any other headers you may need, such as authorization headers.
                },

                body: JSON.stringify({
                    'app_name':document.getElementById('updated_app_name').value,
                    'app_description':document.getElementById('updated_app_description').value,
                }), // Convert your data to JSON format.
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const result = await response.json(); // Parse the response JSON if the server sends a response.
            if (DEBUG === true){
            if (result['msg'] == "app is updated")
            {
                document.getElementById('app_edit_msg').innerHTML = 'App Updated'
            console.log('app is updated');
            }
            else console.log("app is not updated",result)
            }
        } catch (error) {
            if (DEBUG === true)
            console.error('An error occurred while updating app:', error);
        }
}

async function delete_app(id){
    
    app_card = document.getElementById('app_'+id)
    if (app_card) app_card.remove()
   const updateDataUrl = `/dashboard/APIs/delete_app/${id}`; 
        var scrf = getCookie("csrftoken")
        try {
            const response = await fetch(updateDataUrl, {
                method: 'Delete',
                headers: {
                    'Content-Type': 'application/json',// Specify the content type (JSON in this example).
                    "X-CSRFToken":scrf, 
                    // Add any other headers you may need, such as authorization headers.
                },
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const result = await response.json(); // Parse the response JSON if the server sends a response.
            if (DEBUG === true){
            if (result['msg'] == "app is deleted")
            {
            console.log('app is deleted');
            }
            else console.log("app is not deleted",result)
            }
        } catch (error) {
            if (DEBUG === true)
            console.error('An error occurred while deleting app:', error);
        }
}


async function change_selected_plan(app_id){
    var selectedOption = $(`#app_select_${app_id} :selected`);
    var selected_text = selectedOption.text();
    var selectedColor = selectedOption.data('color');
    
    $(`#app_select_${app_id}`).removeClass().addClass('form-select btn btn-' + selectedColor + ' mr-2 pl-2');
    
    // update in database using api
    console.log(`/dashboard/APIs/change_plan`);
    const updateDataUrl = `/dashboard/APIs/change_plan`; 
    var scrf = getCookie("csrftoken")
    try {
        const response = await fetch(updateDataUrl, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',// Specify the content type (JSON in this example).
                "X-CSRFToken":scrf, 
                // Add any other headers you may need, such as authorization headers.
            },

            body: JSON.stringify({
                'app_id':app_id,
                'selected_text':selected_text
            }), // Convert your data to JSON format.
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const result = await response.json(); // Parse the response JSON if the server sends a response.
        if (DEBUG === true){
        if (result['msg'] == "plan is changed")
        console.log('plan is changed:', result);
        else console.log("couldn't change app plan",result)
        }
    } catch (error) {
        if (DEBUG === true)
        console.error('An error occurred while changing status:', error);
    }
}