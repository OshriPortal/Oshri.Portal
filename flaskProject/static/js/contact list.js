fetch('https://reqres.in/api/users?page=2').then(
    response => response.json()
)
    .then(
        responseJSON => createUsersList(responseJSON.data)
    )
    .catch(
        err => console.log(err)
    )

function createUsersList(users) {
    const curr_main = document.querySelector("main");
    for (let user of users) {
        const section = document.createElement('section');
        section.innerHTML = `
        <hr style="height:2px;border-width:0;color:gray;background-color:#02131c">
        <br><img src="${user.avatar}" alt="Profile Picture"/>
        <div>
        <span>${user.first_name} ${user.last_name}</span>
        <br>
        <a href="mailto:${user.email}">Send Email</a>
        </div>
        <br>
        `;
        curr_main.appendChild(section);
    }
}
