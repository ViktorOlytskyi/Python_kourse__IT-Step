


function searchFilm() {
    document.getElementById("list_films").innerHTML = "";
    const selectElement = document.getElementById("movie_title");
    let filmName = selectElement.value;
    
    let request;
    if (window.XMLHttpRequest) {
        request = new XMLHttpRequest();
    }
    else {
        request = new ActiveXObject("Microsoft.XMLHTTP");
    }
    request.open("GET", `http://www.omdbapi.com/?s=${filmName}&type=${movie_type.value}&apikey=8a610735`);
    request.responseType = "json";
    request.onload = function () {
        if (request.status === 200) {
            document.getElementById("error_text").innerText = "";
            
            if (request.response.Response==="False") {
                document.getElementById("list_films").style.display = "none";
                document.getElementById("detail_film").style.display = "none";
                document.getElementById("error_text").innerText = `${movie_type.value.charAt(0).toUpperCase() + movie_type.value.slice(1)} not found!`;
                
                return;
            }
          
            for (let index = 0; index < request.response.Search.length; index++) {

                let imgSrc = request.response.Search[index].Poster;
                let divlemMain = document.createElement("div");
                let divlemtext = document.createElement("div");
                let divlemPict = document.createElement("div");
                
                let imgElem = document.createElement("img");
                let SpanElem = document.createElement("span");
                let bElem = document.createElement("b");
                let br = document.createElement("br");
                let pElem = document.createElement("p");
                let btnDetails = document.createElement("button");
                btnDetails.innerText = "details";
                btnDetails.className = "btnDetails"
                btnDetails.id = "DetailsBtn" + index;

                imgElem.src = imgSrc;
                imgElem.style.cssText = "width: 80px; height: 120px;"
                divlemMain.className = "list_item";
                divlemMain.id = "page"+index;

                divlemtext.className = "list_item_text";
                divlemPict.appendChild(imgElem);
                SpanElem.innerText = movie_type.value;
                divlemtext.appendChild(SpanElem);
                divlemtext.appendChild(br);
                bElem.innerHTML = request.response.Search[index].Title;
                divlemtext.appendChild(bElem);
                pElem.innerText = request.response.Search[index].Year;
                divlemtext.appendChild(pElem);
                divlemtext.appendChild(btnDetails);


                document.getElementById("list_films").style.display = "grid";
                
                document.getElementById("list_films").appendChild(divlemMain);
                document.getElementById("list_films").appendChild(divlemMain).appendChild(divlemPict);
                document.getElementById("list_films").appendChild(divlemMain).appendChild(divlemtext);
                


            }



        }
            


    }

    request.send();

}





document.onclick = e => {
    a = e.target.id;  // to get the element

    if (a.substring(0, a.length - 1) == "DetailsBtn") {


        filmName = document.getElementById(a).previousSibling.previousSibling.innerText;
        filmYear = document.getElementById(a).previousSibling.innerText;
       
        let request;
        if (window.XMLHttpRequest) {
            request = new XMLHttpRequest();
        }
        else {
            request = new ActiveXObject("Microsoft.XMLHTTP");
        }
        request.open("GET", `http://www.omdbapi.com/?t=${filmName}&y=${filmYear}&apikey=8a610735`);
        request.responseType = "json";
        request.onload = function () {
            if (request.status === 200) {

                let imgSrc = request.response.Poster;
                let divlemMain = document.createElement("div");
                let divlemtext = document.createElement("div");
                let divlemPict = document.createElement("div");
                let imgElem = document.createElement("img");

                imgElem.src = imgSrc;
                divlemMain.className = "film_detail";
                divlemtext.className = "detail_text";
                divlemPict.appendChild(imgElem);


                divlemtext.innerHTML = `<p><b>Title:</b><span class="about_text">${request.response.Title}</span></p>
                <p><b>Released:</b><span class="about_text">${request.response.Year}</span></p>
                <p><b>Genre:</b><span class="about_text">${request.response.Genre}</span></p>
                <p><b>Country:</b><span class="about_text">${request.response.Country}</span></p>
                <p><b>Director:</b><span class="about_text">${request.response.Director}</span></p>
                <p><b>Writer:</b><span class="about_text">${request.response.Writer}</span></p>
                <p><b>Actors:</b><span class="about_text">${request.response.Actors}</span></p>
                <p><b>Awards:</b><span class="about_text">${request.response.Awards}</span></p>
                `;

                // document.getElementById("detail_film").appendChild(divlemMain);
                document.getElementById("detail_film").innerHTML = "";
                document.getElementById("detail_film").style.display = "flex";
                document.getElementById("detail_film").appendChild(divlemPict);
                document.getElementById("detail_film").appendChild(divlemtext);

            }


        }


        request.send();
    }
    else {
        return;
    }
}







