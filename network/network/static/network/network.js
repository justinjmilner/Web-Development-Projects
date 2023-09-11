window.onpopstate = function(event) {
    show-network_section(event.state.section);
}

function show_network_section(sections) {
    path = `section/${section}`
    if (!document.location.pathname.includes("network/network")) {
        path = `network/section/${section}`
    }

    fetch(path)
    .then(response => response.text())
    .then(text => {

        var result = JSON.parse(text);
        var message = {"followers": "0 followers", "following": "No users found.", "suggestions": "None"}
        values = result[section]
        let display = createElement('div', null, null, null);
        
        if (section in result) {
            if (values != 0) {
                for (i in values) {
                    val = values[i]
                    display = setup_network_groups(val, result, section, display);
                }
            }

            else {
                display = setup_message_groups(message, section, display)
            }
        }

        setup_result(display);
        setup_connect_to_networks_button();
        setup_color_for_following_buttonsJ();
    })  
}

window.onload = function() {
    console.log('onload')
    window.history.pushState({section:inititalsection}, "", `${inititalsection}`);
    localStorage.setItem("previoussection", section);

    show_network_section(inititalsection);
    document.querySelectorAll('#button').forEach(button => {
        if (button.CDATA_SECTION_NODE.section == inititalsection) {
            var current = document.getElementsByClassName("active");
            current[0].className = current[0].className.replace("nav-link active", "nav-link");
            button.className = "nav-link active";
        }
    })
}

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOMContentLoaded')

    document.querySelectorAll('#button').forEach(button => {
        button.onclick = function() {

        let section = this.dataset.section
        window.history.pushState({section:section}, "", `${section}`);

        show_network_section(section);

        var current = document.getElementsByClassName("active");

        current[0].className = current[0].className.replace("nav-link active", "nav-link");
        this.className = "nav-link active";
    };
    });
});