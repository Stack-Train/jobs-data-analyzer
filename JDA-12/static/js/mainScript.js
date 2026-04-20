// [<name>, <Title>, <Description>, <Thumbnail>]
var data = [];

function createTiles() {
    for (let i of data) {
        $("#contentList").append(
            `<div class='col-sm-4'><a href='javascript:selectDashboard("${i[0]}")' class='tile purple'>` +
            `<img src="${i[3]}"><h3 class='title'>${i[1]}</h3><p>${i[2]}</p></a></div>`
        );
    }
}

function selectDashboard(name) {
    window.location.href = 'dashboard?dashboardName=' + name;
}

function getCookie(cookie_name) {
    var name = cookie_name + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var cookie_array = decodedCookie.split(';');
    for (var i = 0; i < cookie_array.length; i++) {
        var c = cookie_array[i].trim();
        if (c.indexOf(name) === 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
