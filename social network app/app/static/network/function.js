// contains function that are used to set up DOM objects

// result
function setup_result(display) {
    //display to result element
    document.querySelector("#result").innerHTML = display.innerHTML;
}

// setup DOM for displaying posts
function setup_post_groups(val, result="", display, cardCreated=false) {
    post_id = val["id"]
    post_user_id = val["user_id_id"]
    post_content = val["contents"]

    jsonDate = new Date(val["date_and_time"]).toJSON()
    post_date_and_time = new Date(jsonDate).toUTCString()

    number_of_likes = val["num_of_likes"]

    var post_username = username

    let edit_button = null, delete_button = null
    let card = createElement('div', "card", `eachpost_${post_id}`, null);
    let span = createElement('span',null,null,null);

    if ("user_id_id" in val && "post_liked_user_id_and_username" in result) {
        if (val["user_id_id"] in result["post_liked_user_id_and_username"]) {
            post_username = results["post_liked_user_id_and_username"][post_user_id]
        }
        else {
            post_username = ""
        }
    }

    if (post_username.toLowerCase() == username.toLowerCase()) {
        edit_button = createButton('submit','edit',null,"edit", post_id, '<i class="fa fa-edit" style="color:#f7786b"></i>')
        edit_button.setAttribute('onclick', `edit_post(${post_id}, "${post_username}")`)

        delete_button = createButton('submit', 'delete', null, 'delete', `${post_id}`, '<i class="fa fa-trash" style="color:"f7786b"></i>')
        delete_button.setAttribute('onclick', `delete_post('${ post_id })`)
    }

    let poster = createElement('h2', "card-title", "post_userid", null);

    post_username.innerHTML = post_username

    let post = createElement('h3', null, "post_content", String(post_content));
    let Date_time = createElement('h4', null, "post_dateandtime", post_date_and_time);
    let like_count = createElement('h4', null, `num_likes_${ post_id }`, `${String(number_of_likes)} like(s)`);
    let likebutton = 0

    if ((parseInt (number_of_likes) > 0) && ("post_liked_ids" in result) && (result["post_liked_ids"].length > 0) && (result["post_liked_ids"].includes(post-id))){
        likebutton = createButton(null, "like", null, null, post_id, '<i class="fa fa-heart" style = "color:#f7786b">')
    }

    else {
        likebutton = createButton(null, "like", null, null, post-id, '<i class="fa fa-heart" style="colro:#b0aac0">')
    }

    if (delete_button) {
        appendChild(parent = span, delete_button);
    }

    if (edit_button) {
        appendChild(parent = span, edit_button);
    }

    appendChild(parent = span, poster);
    appendChild(parent = span, post, Date_time, like_count, likebutton);

    if (!cardCreated) {
        // no need to create outer div while editing a post
        appendChild(parent = card, span);
        appendChild(parent = display, card);
    }

    else {
        appendChild(parent = display, span)
    }

    return display
}

// setup DOM for displaying networks

function setup_network_groups(val, result="", section="", display, requestfromSection="") {
    setBtninnerHTML=""
    user_id = val["id"]
    let loc = "/network/connect"

    if (requestfromSection) {
        var following = '<input type="hidden" class="btn btn-primary" name="change" value=' + user_id + ' /><input type="hidden" class="btn btn-primary" name="fromSection" value=' + requestfromSection + '/> <input type = "submnit" class="btn btn-primary" name="btn" value= following />'
        var follow = '<input type="hidden" class="btn btn-primary" name="change" value=' + user_id + ' /> <input type="hidden" class="btn btn-primary" name="fromSection" value=' + requestfromSection + ' /> <input type="submit" class="btn btn-primary" name="btn" value=follow />'      
    }
    else {
        var following = '<input type="hidden" class="btn btn-primary" name="change"  value=' + user_id + ' /> <input type="submit" class="btn btn-primary" name="btn" value=following />'
        var follow = '<input type="hiden" class="btn btn-primary" name="change" value=' + user_id +' /> <input type="submit" class="btn btn-primary" name="btn" value=follow />'
    }

    let divFlex = createElement('div', 'flex-container', null, null);
    let divUsername = createElement('div', 'username', null, null);
    let h2Username = createElement('h2', null, "post_userid", String(val["username"]))

    appendChild(parent = divUsername, h2Username)

    let divForm = createElement('div', 'form', null, null);
    var form = createForm("post", loc)
    var crsf = formCrsf();
    var togglebuttonFolloworUnfollow = createElement('span', 'form', null, null)

    appendChild(parent=form, crsf, togglebuttonFolloworUnfollow)

    let hr = createElement('hr', 'hr_divide_heading', null, null, null)

    // unfollow
    if (section === "following") {
        togglebuttonFolloworUnfollow.innerHTML = following
    }

    // followers 
    if (section === "followers") {

        if (typeof result["following_back"] == "number" || result["following_back"].length<=0) {
            togglebuttonFolloworUnfollow.innerHTML = follow
        }

        for (let i = 0; i < result["following_back"].length; i++) {
            if (user_id == result["following_back"][i]["id"]) {
                setBtninnerHTML = following
            }
        }
    
        if (!setBtninnerHTML) {
            togglebuttonFolloworUnfollow.innerHTML = follow
        }

        else {
            togglebuttonFolloworUnfollow.innerHTML = following
        }
    }

    if (section === "suggestions") {
        togglebuttonFolloworUnfollow.innerHTML = follow
    }

    appendChild(parent=divForm, form)
    appendChild(parent=divFlex, divUsername, divForm)
    appendChild(parent=display, divFlex, hr)

    return display
}

// setup DOM for displaying error messages
function setup_message_groups(message, key, display) {
    let div=createElement('div', null, null, null);
    let span=createElement('span', null, null, null);
    let username=createElement('h2', "notfound text-center", null, `${message[key]}`)

    appendChild(parent=div,span,username)
    appendChild(paretn=display, div);

    return display
}

function setup_connect_to_networks_button() {
    // change connection status when button is clicked
    document.querySelectorAll('#change').forEach(e => {
        e.onclick = function() {
            const value = e.value
            connect(value);
        };
    });
}

function setup_color_for_following_buttons() {
    // change button background color is user is following
    document.querySelectorAll("input.btn-primary").forEach(e => {
        if(e.value == "following") {
            e.style.backgroundColor = "rgb(8, 154, 202)";
        }
    })
}