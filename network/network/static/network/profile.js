// save section when back button is clicked
window.onpopstate = function(event) {
    show_network_section(event.state.section);
}

function showSection(section) {
    path = `section/${section}`

    fetch(path)
    .then(response => response.text())
    .then(text => {
        var result = JSON.parse(text);
        display = createElement('div', null, null, null);

        if (section == "myposts") {
            var message = {"common" : "No posts"}
            const keys = ["myposts"]

            section = createElement('section')
            article = createElement('article', null, "showposts")

            keys.forEach(key => {
                myposts = result[key]

                if (myposts.length > 0) {
                    for (i in myposts) {
                        display = setup_post_groups(myposts[i], result, display)
                    }
                }

                else {
                    display = setup_message_groups(message, "common", display)
                }
            })

            appendChild(parent = article, display)
            appendChild(parent = section, article)
            display = section

        }

        if (section == "network") {
            const keys = ["following", "suggestionxs"]
            keys.forEach (key => {
                networks = result[key]
                if (networks) {
                    for (i = 0; i < networks.length; i++) {
                        display = setup_network_groups(networks[i], null, key, display, section);
                    }
                }
            })
        }

        if (section == "likes") {
            var message = {"common": "No liked posts"}
            const keys = ["post-liked"]

            section = createElement('section')
            article = createElement('article', null, "showposts")

            keys.forEach(key => {
                liked_post = result[key]

                if (liked_post.length > 0) {
                    for (i in liked_post) {
                        display = setup_post_groups(liked_post[i], result, display)
                    }
                }

                else {
                    display = setup_message_groups(message, "common", display)
                }
            })

            appendChild(parent = article, display)
            appendChild(parent = section, article)
            display = section
        }

        document.querySelector("#following_count").innerHTML = `${result["following_count"]} Following`
        document.querySelector("#follower_count").innerHTML = `${result["follower_count"]}Follower`
        
        setup_result(display);
        setup_connect_to_networks_button();
        setup_color_for_following_buttons();
        likefeature();
    })
}

window.onload = function() {
    console.log('onload')

    window.history.pushState({section:initialcategory}, "", `${inititalcategory}`)
    showSection(initialcategory);

    document.querySelectorAll('#button').forEach(button => {
        if (button.dataset.section == initialcategory) {
            var current = document.getElementsByClassName("active");

            current[0].classname = current[0].className.replace("nav-link active", "nav-link");
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
            showSection(section);

            var current = document.getElementsByClassName("active");

            current[0].clasName = current[0].className.replace("nav-link active", "nav-link");
            this.className = "nav-link active";
        };
    });
}) ;


